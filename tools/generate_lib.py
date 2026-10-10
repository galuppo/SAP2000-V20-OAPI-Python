"""Gera a biblioteca `sap2000_oapi` a partir de parsed_functions.json.

Lógica central (ver classify.py para as heurísticas):
- ByVal sempre vira parâmetro de entrada em Python.
- ByRef é classificado como entrada ou saída a partir do texto da doc.
- Parâmetros de saída não entram na assinatura Python: o wrapper passa um
  placeholder (0 / "" / False / []) para a chamada COM crua e devolve os
  valores de saída no retorno.
- Convenção de retorno "status" (Long, 0 = sucesso, documentado
  explicitamente) dispara exceção em caso de erro; convenção "data"
  (ex.: Count()) devolve o valor como dado.
"""

from __future__ import annotations

import json
import keyword
import re
from collections import defaultdict
from pathlib import Path

from classify import (
    classify_param_direction,
    extract_enum_mentions,
    status_return_kind,
    vb_type_to_py,
)

BUILD_DIR = Path("/home/claude/sap2000_oapi_build")
OUT_ROOT = Path("/home/claude/sap2000_oapi/src/sap2000_oapi")
REPORT_DIR = Path("/home/claude/sap2000_oapi/reports")

PLACEHOLDER_BY_TYPE = {
    "string": '""',
    "double": "0.0",
    "long": "0",
    "boolean": "False",
}


def normalize_path(syntax_path: str) -> list:
    p = syntax_path.strip()
    if p.startswith("SapObject."):
        p = p[len("SapObject."):]
    if p.startswith("Sap2000."):
        p = "SapModel." + p[len("Sap2000."):]
    if not p.startswith("SapModel"):
        p = "SapModel." + p
    return p.split(".")


def py_identifier(name: str) -> str:
    if keyword.iskeyword(name):
        return name + "_"
    if not name.isidentifier():
        name = re.sub(r"\W", "_", name)
        if not name or name[0].isdigit():
            name = "_" + name
    return name


def raw_attr_name(seg: str, report_list: list) -> str:
    """Nome do segmento tal como deve aparecer em `self._raw.<seg>`.

    Alguns segmentos de path na doc têm caracteres inválidos (provável erro
    de digitação da própria documentação, ex.: 'Indian_IS:800_1998' ao invés
    de 'Indian_IS_800_1998'). Sanitiza e registra para revisão manual.
    """
    cleaned = seg.strip()
    if cleaned.isidentifier():
        return cleaned
    sanitized = re.sub(r"\W", "_", cleaned)
    if sanitized and sanitized[0].isdigit():
        sanitized = "_" + sanitized
    report_list.append((seg, sanitized))
    return sanitized


def resolve_vb_default(default_raw: str, enums: dict):
    """Converte o literal de default VB6 para um literal Python, quando possível.

    Retorna (python_literal_str, resolved: bool).
    """
    if default_raw is None:
        return "None", True
    s = default_raw.strip()
    if s.startswith('"') and s.endswith('"'):
        return repr(s[1:-1]), True
    if re.fullmatch(r"-?\d+", s):
        return s, True
    if re.fullmatch(r"-?\d+\.\d+", s):
        return s, True
    if s.lower() == "true":
        return "True", True
    if s.lower() == "false":
        return "False", True
    # Identificador solto (provável membro de enum, ex.: "Element", "Object").
    for enum_name, members in enums.items():
        if s in members:
            return str(members[s]), True
    # Não resolvido: melhor esforço - trata como string literal.
    return repr(s), False


def build_enum_registry(data: list) -> dict:
    enums: dict = {}
    for d in data:
        for ptext in d["param_docs"].values():
            for enum_name, members in extract_enum_mentions(ptext):
                enums.setdefault(enum_name, {}).update(members)
    return enums


def main():
    data = json.loads((BUILD_DIR / "parsed_functions.json").read_text(encoding="utf-8"))
    enums = build_enum_registry(data)

    # ---- Monta a árvore de "nós" (object paths) ------------------------
    functions_by_tail = defaultdict(list)
    low_confidence = []  # (func_display, param_name, direction, motivo)
    unresolved_defaults = []
    parse_problems = []
    sanitized_path_segments = []
    duplicate_params = []

    for d in data:
        segs = normalize_path(d["syntax_path"])
        tail = tuple(segs[1:-1])
        func_display = ".".join(segs)

        ordered_params = []
        seen_names = {}
        for p in d["signature_params"]:
            direction, confidence = classify_param_direction(
                p, d["param_docs"].get(p["name"], ""), d["func_name"]
            )
            if confidence == "low":
                low_confidence.append((func_display, p["name"], direction))
            name = p["name"]
            if name in seen_names:
                seen_names[name] += 1
                new_name = f"{name}_{seen_names[name]}"
                duplicate_params.append((func_display, name, new_name))
                p = {**p, "name": new_name}
            else:
                seen_names[name] = 1
            ordered_params.append({**p, "direction": direction})

        return_kind = status_return_kind(d["return_type"], d["remarks"])

        functions_by_tail[tail].append({
            "info": d,
            "func_display": func_display,
            "ordered_params": ordered_params,
            "return_kind": return_kind,
        })

    # Fecho de prefixos: garante nó-contêiner para todo prefixo de todo tail.
    all_tails = set(functions_by_tail.keys())
    closure = set(all_tails)
    for t in all_tails:
        for i in range(len(t)):
            closure.add(t[:i])
    closure.add(())

    print(f"Nós totais (com fechamento de prefixos): {len(closure)}")
    print(f"Funções: {sum(len(v) for v in functions_by_tail.values())}")
    print(f"Parâmetros com classificação de baixa confiança: {len(low_confidence)}")

    # ---- Gera código -----------------------------------------------------
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / "_nodes").mkdir(exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    root_children = sorted({t[0] for t in closure if len(t) >= 1})
    children_of = defaultdict(list)
    for t in closure:
        if len(t) >= 1:
            children_of[t[:-1]].append(t)

    def node_class_name(tail: tuple) -> str:
        if not tail:
            return "RootMethods"
        return "N_" + "_".join(py_identifier(seg) for seg in tail)

    def gen_function_code(func_entry: dict, indent: str = "    ") -> str:
        info = func_entry["info"]
        params = func_entry["ordered_params"]
        return_kind = func_entry["return_kind"]
        func_name = info["func_name"]
        py_name = py_identifier(func_name)

        input_params = [p for p in params if p["direction"] == "input"]
        output_params = [p for p in params if p["direction"] == "output"]

        # --- assinatura python ---
        sig_parts = ["self"]
        call_args_by_orig = {}
        seen_optional = False
        for p in input_params:
            pyname = py_identifier(p["name"])
            pytype = vb_type_to_py(p["type"], p["is_array"], set(enums))
            if p["optional"]:
                seen_optional = True
                default_literal, resolved = resolve_vb_default(p["default"], enums)
                if not resolved:
                    unresolved_defaults.append((func_entry["func_display"], p["name"], p["default"]))
                sig_parts.append(f"{pyname}: {pytype} = {default_literal}")
            else:
                if seen_optional:
                    # VB6 permite obrigatório após opcional em posições raras;
                    # em Python isso é inválido - força default None e valida no corpo.
                    sig_parts.append(f"{pyname}: {pytype} = None")
                else:
                    sig_parts.append(f"{pyname}: {pytype}")
            call_args_by_orig[p["name"]] = pyname

        # --- placeholders para params de saída, na chamada crua ---
        for p in output_params:
            t = p["type"].lower()
            base_placeholder = PLACEHOLDER_BY_TYPE.get(t, "None")
            call_args_by_orig[p["name"]] = "[]" if p["is_array"] else base_placeholder

        raw_call_args = ", ".join(call_args_by_orig[p["name"]] for p in params)

        lines = []
        sig = f"{indent}def {py_name}({', '.join(sig_parts)}):"
        lines.append(sig)

        doc = info["remarks"].strip()
        param_doc_lines = []
        for p in params:
            desc = info["param_docs"].get(p["name"], "").strip()
            if desc:
                desc = re.sub(r"\s+", " ", desc)
                if len(desc) > 300:
                    desc = desc[:300] + "..."
                param_doc_lines.append(f"{indent}    {p['name']} ({p['direction']}): {desc}")
        docstring_body = doc
        if len(docstring_body) > 500:
            docstring_body = docstring_body[:500] + "..."
        lines.append(f'{indent}    """{docstring_body}')
        if param_doc_lines:
            lines.append(f"{indent}")
            lines.extend(param_doc_lines)
        lines.append(f'{indent}    """')

        if raw_call_args:
            lines.append(f"{indent}    _r = self._raw.{func_name}({raw_call_args})")
        else:
            lines.append(f"{indent}    _r = self._raw.{func_name}()")

        if not output_params:
            if return_kind == "status":
                lines.append(f"{indent}    if _r != 0:")
                lines.append(
                    f'{indent}        raise Sap2000ApiError('
                    f'"{func_entry["func_display"]} falhou (ret={{_r}})".format(_r=_r))'
                )
                lines.append(f"{indent}    return None")
            elif return_kind == "data":
                lines.append(f"{indent}    return _r")
            else:
                lines.append(f"{indent}    return None")
        else:
            lines.append(f"{indent}    *_outs, _ret = _r")
            if return_kind == "status":
                lines.append(f"{indent}    if _ret != 0:")
                lines.append(
                    f'{indent}        raise Sap2000ApiError('
                    f'"{func_entry["func_display"]} falhou (ret={{_ret}})".format(_ret=_ret))'
                )
                if len(output_params) == 1:
                    lines.append(f"{indent}    return _outs[0]")
                else:
                    lines.append(f"{indent}    return tuple(_outs)")
            else:
                if len(output_params) == 1:
                    lines.append(f"{indent}    return _outs[0]")
                else:
                    lines.append(f"{indent}    return (*_outs, _ret)")

        return "\n".join(lines) + "\n\n"

    # ---- Emite um arquivo por "root_child" (primeiro segmento do tail) --
    file_headers = (
        '"""Módulo gerado automaticamente a partir da documentação da OAPI\n'
        'do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -\n'
        "reexecute tools/generate.py se precisar regenerar.\n"
        '"""\n\n'
        "from __future__ import annotations\n\n"
        "from functools import cached_property\n\n"
        "from ..errors import Sap2000ApiError\n\n\n"
    )

    nodes_by_root_child = defaultdict(list)
    for t in closure:
        if len(t) >= 1:
            nodes_by_root_child[t[0]].append(t)
    root_direct_functions = functions_by_tail.get((), [])

    generated_index = {}  # tail -> (module_name, class_name)

    for root_child in root_children:
        module_name = "n_" + py_identifier(root_child).lower()
        tails_here = sorted(nodes_by_root_child[root_child], key=len)
        src = [file_headers]
        for t in tails_here:
            cls_name = node_class_name(t)
            generated_index[t] = (module_name, cls_name)
            src.append(f"class {cls_name}:\n")
            src.append(f'    """Wrapper para SapModel.{".".join(t)}."""\n\n')
            src.append("    def __init__(self, raw):\n        self._raw = raw\n\n")
            for func_entry in functions_by_tail.get(t, []):
                src.append(gen_function_code(func_entry))
            for child_tail in sorted(children_of.get(t, [])):
                child_attr = py_identifier(child_tail[-1])
                child_cls = node_class_name(child_tail)
                raw_seg = raw_attr_name(child_tail[-1], sanitized_path_segments)
                src.append(f"    @cached_property\n")
                src.append(f"    def {child_attr}(self):\n")
                src.append(f"        return {child_cls}(self._raw.{raw_seg})\n\n")
            src.append("\n")
        (OUT_ROOT / "_nodes" / f"{module_name}.py").write_text("".join(src), encoding="utf-8")

    # ---- Módulo raiz: funções direto em SapModel -------------------------
    root_src = [file_headers]
    root_src.append("class RootMethods:\n")
    root_src.append('    """Funções chamadas diretamente em SapModel (sem sub-objeto)."""\n\n')
    root_src.append("    def __init__(self, raw):\n        self._raw = raw\n\n")
    for func_entry in root_direct_functions:
        root_src.append(gen_function_code(func_entry))
    (OUT_ROOT / "_nodes" / "n__root.py").write_text("".join(root_src), encoding="utf-8")

    # ---- model.py: monta a árvore inteira ---------------------------------
    model_lines = [
        '"""Monta a árvore SapModel completa a partir dos nós gerados."""\n\n',
        "from __future__ import annotations\n\n",
        "from functools import cached_property\n\n",
        "from ._nodes.n__root import RootMethods\n",
    ]
    imported_modules = sorted({mod for mod, _ in generated_index.values()})
    for mod in imported_modules:
        classes_in_mod = sorted({cls for (m, cls) in generated_index.values() if m == mod})
        model_lines.append(f"from ._nodes.{mod} import {', '.join(classes_in_mod)}\n")
    model_lines.append("\n\n")
    model_lines.append("class SapModelWrapper(RootMethods):\n")
    model_lines.append(
        '    """Wrapper tipado para SapModel. Espelha a árvore de objetos da OAPI:\n'
        "    sap.PropMaterial.SetMaterial(...), sap.LoadPatterns.AutoSeismic.GetNBCC95(...), etc.\n"
        '    """\n\n'
    )
    model_lines.append("    def __init__(self, raw):\n        self._raw = raw\n\n")
    for t in sorted(t for t in closure if len(t) == 1):
        attr = py_identifier(t[0])
        _, cls_name = generated_index[t]
        raw_seg = raw_attr_name(t[0], sanitized_path_segments)
        model_lines.append("    @cached_property\n")
        model_lines.append(f"    def {attr}(self):\n")
        model_lines.append(f"        return {cls_name}(self._raw.{raw_seg})\n\n")
    (OUT_ROOT / "model.py").write_text("".join(model_lines), encoding="utf-8")

    (OUT_ROOT / "_nodes" / "__init__.py").write_text("", encoding="utf-8")

    # ---- enums.py ----------------------------------------------------------
    enum_lines = [
        '"""Enumerações eXxx extraídas da documentação da OAPI (SAP2000 v20)."""\n\n',
        "from __future__ import annotations\n\n",
        "from enum import IntEnum\n\n\n",
    ]
    for enum_name in sorted(enums):
        members = enums[enum_name]
        enum_lines.append(f"class {enum_name}(IntEnum):\n")
        for member_name, value in members.items():
            safe_member = py_identifier(member_name)
            if keyword.iskeyword(safe_member) or not safe_member.isidentifier():
                continue
            enum_lines.append(f"    {safe_member} = {value}\n")
        enum_lines.append("\n\n")
    (OUT_ROOT / "enums.py").write_text("".join(enum_lines), encoding="utf-8")

    # ---- errors.py -----------------------------------------------------
    (OUT_ROOT / "errors.py").write_text(
        '"""Exceções da biblioteca."""\n\n\n'
        "class Sap2000ApiError(RuntimeError):\n"
        '    """Uma chamada da OAPI retornou código de erro (ret != 0)."""\n'
        "\n",
        encoding="utf-8",
    )

    # ---- relatório de revisão -------------------------------------------
    report = ["# Itens para revisão manual\n\n"]
    report.append(f"Gerado a partir de {len(data)} funções extraídas do CHM.\n\n")
    report.append("## Páginas que não puderam ser parseadas automaticamente\n\n")
    report.append(
        "Ver `skipped_pages.json` no diretório de build - a maioria são páginas "
        "descritivas (não são de fato uma função) ou têm formatação irregular na doc.\n\n"
    )
    report.append(f"## Parâmetros ByRef com direção inferida por heurística de baixa confiança ({len(low_confidence)})\n\n")
    report.append(
        "Nestes casos o texto da descrição não continha um sinal claro de entrada/saída; "
        "a direção foi inferida pelo prefixo do nome da função (Get/Count -> saída, "
        "Set/Add/Delete -> entrada). Confira manualmente antes de usar em produção.\n\n"
    )
    for func_display, param_name, direction in low_confidence:
        report.append(f"- `{func_display}` — parâmetro `{param_name}` classificado como **{direction}**\n")
    report.append(f"\n## Valores default (VB6) não resolvidos para literal Python ({len(unresolved_defaults)})\n\n")
    for func_display, param_name, default_raw in unresolved_defaults:
        report.append(f"- `{func_display}` — parâmetro `{param_name}`, default original `{default_raw}` (usado como string; confira)\n")
    report.append(f"\n## Segmentos de path com caractere inválido, sanitizados ({len(sanitized_path_segments)})\n\n")
    report.append(
        "Prováveis erros de digitação na própria documentação (ex.: falta um "
        "underscore). O nome sanitizado foi usado como aposta no atributo COM "
        "real - confira contra o SAP2000 antes de usar essa parte da árvore.\n\n"
    )
    for original, sanitized in sanitized_path_segments:
        report.append(f"- `{original}` -> usado como `{sanitized}`\n")
    report.append(f"\n## Parâmetros duplicados na assinatura (erro na doc original), renomeados ({len(duplicate_params)})\n\n")
    report.append(
        "A própria documentação da CSI declara o mesmo nome de parâmetro duas "
        "vezes na mesma função (ex.: `Fx` duas vezes, provavelmente deveria ser "
        "`Fx`/`Fy`). Renomeei a segunda ocorrência para não quebrar a assinatura "
        "Python - confira o nome real antes de usar essa função.\n\n"
    )
    for func_display, original, renamed in duplicate_params:
        report.append(f"- `{func_display}` — `{original}` duplicado, segunda ocorrência renomeada para `{renamed}`\n")
    (REPORT_DIR / "revisao_necessaria.md").write_text("".join(report), encoding="utf-8")

    print("Geração concluída.")


if __name__ == "__main__":
    main()
