# sap2000_oapi

Wrapper Python **tipado** para a OAPI completa do SAP2000 v20, gerado
automaticamente a partir de `CSI_OAPI_Documentation.chm`.

```python
from sap2000_oapi import Sap2000Connection
from sap2000_oapi.enums import eMatType

with Sap2000Connection(visible=True) as sap:
    sap.PropMaterial.SetMaterial("C30", eMatType.MATERIAL_CONCRETE)
    sap.PropFrame.SetRectangle("RET_20x40", "C30", 0.40, 0.20)
    nome = sap.FrameObj.AddByCoord(0, 0, 0, 0, 0, 6, PropName="RET_20x40")
    sap.FrameObj.GetPoints(nome)
```

A árvore de objetos (`sap.PropMaterial`, `sap.LoadPatterns.AutoSeismic`,
`sap.Results.Setup`, ...) espelha exatamente a documentação da OAPI — se
você já usou a API em VBA/VB.NET, o caminho é o mesmo, só que com métodos
tipados, docstrings extraídas da doc e exceções em vez de código de
retorno.

## Números

- **1795** funções da OAPI extraídas de **1813** páginas do CHM (99%).
- **156** nós na árvore de objetos (classes geradas).
- **13** enumerações (`eMatType`, `eUnits`, `eLoadPatternType`, ...) em `enums.py`.

## Como funciona cada método gerado

- Parâmetros `ByVal` da assinatura VB6 viram argumentos Python normais.
- Parâmetros `ByRef` são classificados como **entrada** ou **saída** a
  partir do texto da documentação (ByRef é usado nos dois sentidos em
  VB6, a doc não expõe o atributo COM in/out real). Parâmetros de saída
  **não entram** na assinatura Python — eles voltam no retorno.
- Função cuja doc diz "retorna zero em caso de sucesso" (a maioria):
  levanta `Sap2000ApiError` se o código de retorno for diferente de zero.
- Função tipo `Count()`, que devolve um dado de verdade (não um código de
  status): o valor é devolvido diretamente.
- 1 parâmetro de saída → retorno direto do valor. 2+ → tupla.

```python
# GetPoints tem 2 saídas (Point1, Point2) -> tupla
p1, p2 = sap.FrameObj.GetPoints("P1")

# AddByCoord tem 1 saída (o Name que o programa atribui) -> valor direto
nome = sap.FrameObj.AddByCoord(0, 0, 0, 0, 0, 6)

# SetMaterial não tem saída, só status -> levanta exceção se falhar
sap.PropMaterial.SetMaterial("C30", 2)
```

## Limitações conhecidas — leia antes de usar em produção

Isso foi gerado por um parser + heurísticas de classificação de texto
contra ~1800 páginas de documentação, não revisado função por função à
mão (diferente do projeto `pilar_sap2000`, onde cada chamada usada foi
conferida manualmente). Antes de usar uma função em produção:

1. **Confira `reports/revisao_necessaria.md`** — lista, por função:
   - Parâmetros `ByRef` cuja direção (entrada/saída) foi inferida com
     baixa confiança (o texto da doc não continha um sinal claro).
   - Valores default do VB6 que não foram resolvidos para um literal
     Python (foram tratados como string; confira).
   - Segmentos de path com caractere inválido, sanitizados (prováveis
     erros de digitação na própria doc da CSI).
   - Parâmetros duplicados na mesma assinatura (erro na doc original).
   - Colisões de nome dentro da mesma classe, resolvidas via nome de
     arquivo ou realocação de nó.
2. A CSI tem **erros de copiar-colar na própria documentação** — em pelo
   menos 25 funções o nome na assinatura VB6 não bate com o nome real
   (Syntax path), e em pelo menos 7 casos é o Syntax path que foi copiado
   de uma página vizinha. Usei o nome de arquivo como critério de
   desempate quando isso gerava colisão, mas vale conferir a função
   específica que você for usar contra o SAP2000 real antes de confiar
   cegamente.
3. **18 páginas não puderam ser parseadas** automaticamente (algumas nem
   são de fato uma função — são texto descritivo; outras têm formatação
   irregular). Não estão na biblioteca. Ver `skipped_pages.json` em
   `tools/` (gerado ao rodar `parse_chm.py`).
4. Funções com parâmetros `ByRef` de **entrada** (arrays que você
   preenche antes de chamar, não resultado) dependem inteiramente da
   heurística de texto ter identificado a direção certa — essas são as
   que mais valem uma conferência manual antes de usar, já que passar um
   array de saída como se fosse entrada (ou vice-versa) quebra em
   runtime, não silenciosamente.

O padrão de chamada em si (como o comtypes espera os parâmetros de saída
como placeholders e devolve tudo numa tupla) foi conferido manualmente
contra a doc para várias funções representativas (`SetMaterial`,
`AddByCoord`, `GetPoints`, `FrameForce`, `JointReact`, `LoadPatterns.Add`,
`SetLoadDistributed`) antes de generalizar — esse mecanismo central tem
alta confiança. A parte que exige mais cautela é a classificação de
direção **por função individual**, não o mecanismo de geração em si.

## Reproduzir / regenerar

Os scripts que geraram a biblioteca estão em `tools/`:

```bash
python tools/parse_chm.py     # extrai parsed_functions.json do CHM
python tools/generate_lib.py  # gera src/sap2000_oapi/ a partir do JSON
```

Ambos têm caminhos configurados como constantes no topo do arquivo
(`CHM_ROOT`, `OUT_ROOT` etc.) — ajuste se for rodar em outra máquina.
Regenere se a CSI atualizar a documentação (ex.: nova versão do SAP2000).

## Requisitos

- SAP2000 v20 instalado e licenciado (Windows) para `Sap2000Connection`.
- O resto do pacote (`model`, `enums`, `errors`, a árvore de nós) **não**
  depende de COM/Windows e pode ser importado e testado em qualquer SO
  (é assim que os testes em `tests/` rodam).
