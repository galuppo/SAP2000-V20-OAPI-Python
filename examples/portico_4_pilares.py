"""Exemplo de uso da sap2000_oapi: modela um pórtico de 2 pavimentos com
4 pilares, vigas e lajes em cada nível, aplica carga de escritório
(NBR 6120) e uma carga horizontal de vento simplificada, processa a
análise e exporta os esforços principais nas barras e as reações de
apoio para dois arquivos CSV.

Geometria (planta retangular, em metros):
    (0,5) P4 -------- V -------- P3 (6,5)
      |                            |
      V                            V
      |                            |
    (0,0) P1 -------- V -------- P2 (6,0)

2 níveis: Z = 3.0 m (piso 1) e Z = 6.0 m (cobertura), pé-direito 3.0 m.
Pilares e vigas: concreto C30 (agregado basalto), NBR 6118.

IMPORTANTE: a carga de vento aplicada aqui é ilustrativa (valores fixos
por nó, crescendo com a altura) — não substitui o cálculo de ações de
vento pela NBR 6123 (Vo, S1, S2, S3, Ca, área de influência real por
pavimento). Para um projeto real, substitua VENTO_NIVEL1_KGF/
VENTO_NIVEL2_KGF pelo resultado desse cálculo.
"""

from __future__ import annotations

import csv
from pathlib import Path

from sap2000_oapi.src.sap2000_oapi.connection import Sap2000Connection
from sap2000_oapi.src.sap2000_oapi.enums import eMatType, eUnits

# ---------------------------------------------------------------------------
# Parâmetros do modelo
# ---------------------------------------------------------------------------

LX = 6.0  # dimensão em X da planta [m]
LY = 5.0  # dimensão em Y da planta [m]
PE_DIREITO = 3.0  # altura de cada pavimento [m]
NIVEIS = [PE_DIREITO, 2 * PE_DIREITO]  # Z dos pisos: 3.0 e 6.0 m

FCK_MPA = 30.0
AGREGADO_ALPHA_E = 1.2  # basalto, NBR 6118 item 8.2.8

PILAR_LARGURA_CM = 30.0
PILAR_ALTURA_CM = 30.0
VIGA_LARGURA_CM = 20.0
VIGA_ALTURA_CM = 50.0
LAJE_ESPESSURA_M = 0.12

PESO_ESPECIFICO_CONCRETO_KGF_M3 = 2500.0
CARGA_PERMANENTE_KGF_M2 = 100.0  # acabamento/revestimento, ilustrativo
CARGA_SOBRECARGA_KGF_M2 = 200.0  # escritório, NBR 6120 (2,0 kN/m²)

# Vento simplificado/ilustrativo — ver aviso no docstring do módulo.
VENTO_NIVEL1_KGF = 250.0  # por nó de topo do pavimento 1
VENTO_NIVEL2_KGF = 400.0  # por nó de topo da cobertura

GAMMA_G = 1.4
GAMMA_Q = 1.4
PSI0_SOBRECARGA = 0.5  # NBR 6118 Tabela 11.2 — escritórios
PSI0_VENTO = 0.6  # NBR 6118 Tabela 11.2 — vento

NOME_MODELO = "Portico 4 Pilares"
SAIDA_ESFORCOS = Path("output/esforcos_barras.csv")
SAIDA_REACOES = Path("output/reacoes_base.csv")


def eci_mpa(fck_mpa: float, alpha_e: float) -> float:
    """Módulo de elasticidade inicial do concreto, NBR 6118 eq. 8.1/8.2."""
    if fck_mpa <= 50:
        return alpha_e * 5600 * fck_mpa**0.5
    return 21.5e3 * alpha_e * (fck_mpa / 10 + 1.25) ** (1 / 3)


def main() -> None:
    program_path = r'"C:\Program Files\Computers and Structures\SAP2000 20\RunAsDate.exe" /movetime 06\08\2018 00:00:00 "C:\Program Files\Computers and Structures\SAP2000 20\SAP2000.exe"'
    with Sap2000Connection(program_path=program_path, visible=True, units=eUnits.kgf_m_C) as sap:
        # --- Material -----------------------------------------------------
        nome_material = "C30_BASALTO"
        sap.PropMaterial.SetMaterial(nome_material, eMatType.MATERIAL_CONCRETE)
        sap.PropMaterial.SetWeightAndMass(nome_material, 1, PESO_ESPECIFICO_CONCRETO_KGF_M3)
        e_kgf_m2 = eci_mpa(FCK_MPA, AGREGADO_ALPHA_E) * 101_971.6  # MPa -> kgf/m2
        sap.PropMaterial.SetMPIsotropic(nome_material, e_kgf_m2, 0.2, 1.0e-5)

        # --- Seções ---------------------------------------------------------
        nome_pilar = "P30x30"
        sap.PropFrame.SetRectangle(
            nome_pilar, nome_material, PILAR_ALTURA_CM / 100, PILAR_LARGURA_CM / 100
        )
        nome_viga = "V20x50"
        sap.PropFrame.SetRectangle(
            nome_viga, nome_material, VIGA_ALTURA_CM / 100, VIGA_LARGURA_CM / 100
        )
        nome_laje = "LAJE_12CM"
        sap.PropArea.SetShell_1(
            nome_laje,
            1,  # ShellType = 1 (Shell - thin)
            True,  # IncludeDrillingDOF
            nome_material,
            0.0,  # MatAng
            LAJE_ESPESSURA_M,  # Thickness (membrana)
            LAJE_ESPESSURA_M,  # Bending
        )

        # --- Geometria: pontos da grade (4 cantos x 3 cotas) -----------------
        cantos_xy = [(0.0, 0.0), (LX, 0.0), (LX, LY), (0.0, LY)]
        cotas_z = [0.0, *NIVEIS]

        pontos = {}  # (canto_idx, nivel_idx) -> nome do ponto no SAP2000
        for i, (x, y) in enumerate(cantos_xy):
            for k, z in enumerate(cotas_z):
                pontos[(i, k)] = sap.PointObj.AddCartesian(x, y, z)

        # --- Pilares: um por canto, por trecho entre níveis -------------------
        nomes_pilares = []
        for i in range(4):
            for k in range(len(cotas_z) - 1):
                nome = sap.FrameObj.AddByPoint(
                    pontos[(i, k)], pontos[(i, k + 1)], nome_pilar, f"P{i + 1}_N{k + 1}"
                )
                nomes_pilares.append(nome)

        # --- Vigas: perímetro fechado em cada nível (não conta a base) -------
        nomes_vigas = []
        for k in range(1, len(cotas_z)):  # níveis 1 e 2 (ignora a base, k=0)
            for i in range(4):
                j = (i + 1) % 4
                nome = sap.FrameObj.AddByPoint(
                    pontos[(i, k)], pontos[(j, k)], nome_viga, f"V_N{k}_{i + 1}{j + 1}"
                )
                nomes_vigas.append(nome)

        # --- Lajes: uma por nível ---------------------------------------------
        nomes_lajes = []
        for k in range(1, len(cotas_z)):
            pontos_do_nivel = [pontos[(i, k)] for i in range(4)]
            nome = sap.AreaObj.AddByPoint(4, pontos_do_nivel, nome_laje, f"LAJE_N{k}")
            nomes_lajes.append(nome)

        # --- Restrições: engaste na base (4 pontos em Z=0) --------------------
        engaste = [True, True, True, True, True, True]
        pontos_base = [pontos[(i, 0)] for i in range(4)]
        for p in pontos_base:
            sap.PointObj.SetRestraint(p, engaste)

        # --- Casos de carga -----------------------------------------------
        LTYPE_DEAD, LTYPE_SUPERDEAD, LTYPE_LIVE, LTYPE_WIND = 1, 2, 3, 6
        sap.LoadPatterns.Add("PP", LTYPE_DEAD, 1.0)
        sap.LoadPatterns.Add("PERM", LTYPE_SUPERDEAD, 0.0)
        sap.LoadPatterns.Add("SC", LTYPE_LIVE, 0.0)
        sap.LoadPatterns.Add("VENTO", LTYPE_WIND, 0.0)

        # --- Cargas de área: permanente e sobrecarga nas lajes -----------------
        DIR_GRAVIDADE = 10  # SetLoadUniform: 10 = direção da gravidade (-Z global)
        for laje in nomes_lajes:
            sap.AreaObj.SetLoadUniform(laje, "PERM", CARGA_PERMANENTE_KGF_M2, DIR_GRAVIDADE)
            sap.AreaObj.SetLoadUniform(laje, "SC", CARGA_SOBRECARGA_KGF_M2, DIR_GRAVIDADE)

        # --- Carga de vento: pontual em X nos nós de topo de cada nível --------
        valores_vento = {1: VENTO_NIVEL1_KGF, 2: VENTO_NIVEL2_KGF}
        for k, valor_kgf in valores_vento.items():
            valores = [valor_kgf, 0.0, 0.0, 0.0, 0.0, 0.0]  # Fx, Fy, Fz, Mx, My, Mz
            for i in range(4):
                sap.PointObj.SetLoadForce(pontos[(i, k)], "VENTO", valores)

        # --- Combinações ELU (NBR 6118) --------------------------------------
        def montar_combinacao(nome: str, casos_fatores: list[tuple[str, float]]) -> None:
            sap.RespCombo.Add(nome, 0)  # 0 = linear aditiva
            for caso, fator in casos_fatores:
                sap.RespCombo.SetCaseList(nome, 0, caso, fator)

        montar_combinacao(
            "ELU_SC_PRINCIPAL",
            [
                ("PP", GAMMA_G),
                ("PERM", GAMMA_G),
                ("SC", GAMMA_Q),
                ("VENTO", GAMMA_Q * PSI0_VENTO),
            ],
        )
        montar_combinacao(
            "ELU_VENTO_PRINCIPAL",
            [
                ("PP", GAMMA_G),
                ("PERM", GAMMA_G),
                ("VENTO", GAMMA_Q),
                ("SC", GAMMA_Q * PSI0_SOBRECARGA),
            ],
        )

        # --- Salva, processa -----------------------------------------------
        sap.File.Save(str(Path(f"{NOME_MODELO}.sdb").resolve()))
        sap.Analyze.RunAnalysis()

        # --- Extrai esforços nas barras (pilares + vigas) ----------------------
        sap.Results.Setup.DeselectAllCasesAndCombosForOutput()
        sap.Results.Setup.SetComboSelectedForOutput("ELU_SC_PRINCIPAL")
        sap.Results.Setup.SetComboSelectedForOutput("ELU_VENTO_PRINCIPAL")

        registros_esforcos = []
        for nome_barra in [*nomes_pilares, *nomes_vigas]:
            resultado = sap.Results.FrameForce(nome_barra, 0)
            (_num, obj, obj_sta, elm, elm_sta, load_case, step_type, step_num,
             p, v2, v3, t, m2, m3) = resultado
            for idx in range(len(obj)):
                registros_esforcos.append({
                    "barra": obj[idx],
                    "posicao_m": obj_sta[idx],
                    "combinacao": load_case[idx],
                    "N_kgf": p[idx],
                    "V2_kgf": v2[idx],
                    "V3_kgf": v3[idx],
                    "T_kgfm": t[idx],
                    "M2_kgfm": m2[idx],
                    "M3_kgfm": m3[idx],
                })

        SAIDA_ESFORCOS.parent.mkdir(parents=True, exist_ok=True)
        with SAIDA_ESFORCOS.open("w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=list(registros_esforcos[0].keys()))
            escritor.writeheader()
            escritor.writerows(registros_esforcos)

        # --- Extrai reações nas bases dos pilares ------------------------------
        registros_reacoes = []
        for ponto in pontos_base:
            resultado = sap.Results.JointReact(ponto, 0)
            _num, obj, elm, load_case, step_type, step_num, f1, f2, f3, m1, m2, m3 = resultado
            for idx in range(len(obj)):
                registros_reacoes.append({
                    "ponto": obj[idx],
                    "combinacao": load_case[idx],
                    "Fx_kgf": f1[idx],
                    "Fy_kgf": f2[idx],
                    "Fz_kgf": f3[idx],
                    "Mx_kgfm": m1[idx],
                    "My_kgfm": m2[idx],
                    "Mz_kgfm": m3[idx],
                })

        SAIDA_REACOES.parent.mkdir(parents=True, exist_ok=True)
        with SAIDA_REACOES.open("w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=list(registros_reacoes[0].keys()))
            escritor.writeheader()
            escritor.writerows(registros_reacoes)

        print(f"Esforços salvos em {SAIDA_ESFORCOS}")
        print(f"Reações salvas em {SAIDA_REACOES}")


if __name__ == "__main__":
    main()
