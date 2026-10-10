"""Heurísticas de classificação usadas pelo gerador:

1. Direção de cada parâmetro ByRef (entrada vs. saída) — a partir do texto
   da descrição na doc, já que VB6 usa ByRef tanto para arrays de entrada
   quanto de saída (a doc não expõe o atributo COM in/out/inout real).
2. Convenção de retorno da função — "status code" (0 = sucesso, convenção
   documentada explicitamente) vs. "valor de dado" (ex.: Count()).
3. Extração de enumerações (eXxx) citadas nas descrições de parâmetro.
"""

from __future__ import annotations

import re

OUTPUT_SIGNALS = re.compile(
    r"returned by the (program|application)"
    r"|retriev(ed|es|al)"
    r"|recovered"
    r"|this function (reports|retrieves|recovers)"
    r"|the program (assigns|calculates|computes|reports)"
    r"|ultimately assign"
    r"|associated with each result"
    r"|the total number of"
    r"|the name that the program",
    re.IGNORECASE,
)

INPUT_SIGNALS = re.compile(
    r"specified by (the )?(caller|user)"
    r"|to be assigned"
    r"|is (defined|specified) by"
    r"|assign(ed)? to"
    r"|input by"
    r"|the value(s)? (used|applied)"
    r"|if this item is"  # geralmente flags/enums de entrada
    r"|this item is (true|false|either|one of|any)",
    re.IGNORECASE,
)

STATUS_RETURN_SIGNAL = re.compile(
    r"returns? (a )?(zero|0)\b.{0,40}success"
    r"|returns? (nonzero|non-zero)\b.{0,60}(not|fail)"
    r"|successfully",
    re.IGNORECASE,
)


def classify_param_direction(param: dict, description: str, func_name: str) -> tuple:
    """Retorna (direction, confidence) onde direction é 'input' ou 'output'.

    confidence é 'high' quando um sinal textual explícito bateu OU quando o
    prefixo do nome da função (Get/Count/Is -> saída; Set/Delete -> entrada)
    é, por convenção observada nesta API, confiável por si só. 'low' fica
    reservado para os casos genuinamente ambíguos (ex.: prefixo Add, onde
    o padrão varia: 'Name' costuma ser saída, o resto costuma ser entrada).
    """
    if not param["byref"]:
        return "input", "high"  # ByVal nunca é ambíguo

    text = description or ""
    has_output_signal = bool(OUTPUT_SIGNALS.search(text))
    has_input_signal = bool(INPUT_SIGNALS.search(text))

    if has_output_signal and not has_input_signal:
        return "output", "high"
    if has_input_signal and not has_output_signal:
        return "input", "high"

    name_lower = func_name.lower()
    if name_lower.startswith("get") or name_lower.startswith("count") or name_lower.startswith("is"):
        return "output", "high"
    if name_lower.startswith("set") or name_lower.startswith("delete"):
        return "input", "high"
    if name_lower.startswith("add"):
        # Padrão observado: o parâmetro "Name" em funções Add* é o nome que
        # o programa atribui (saída); os demais costumam ser dados de entrada.
        if param["name"].lower() == "name":
            return "output", "medium"
        return "input", "low"

    return "output", "low"


ENUM_MENTION_RE = re.compile(
    r"(?:in|from) the (?P<enum>e[A-Za-z0-9][A-Za-z0-9_]*) enumeration",
    re.IGNORECASE,
)
ENUM_ITEM_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(-?\d+)")


def extract_enum_mentions(text: str) -> list:
    """Retorna [(nome_enum, {membro: valor, ...}), ...] achados no texto."""
    results = []
    for m in ENUM_MENTION_RE.finditer(text):
        enum_name = m.group("enum")
        tail = text[m.end():m.end() + 400]
        items = ENUM_ITEM_RE.findall(tail)
        if items:
            members = {}
            for name, value in items:
                # Para de coletar se o padrão name=value some por um trecho
                # longo de prosa (heurística simples: só aceita até achar
                # uma quebra clara, aqui já limitada pelo corte de 400 chars).
                members[name] = int(value)
            results.append((enum_name, members))
    return results


def status_return_kind(return_type: str, remarks: str) -> str:
    """Retorna 'status' (Long convencional 0=sucesso) ou 'data' (valor real)."""
    if return_type.lower() != "long":
        return "data" if return_type else "none"
    if STATUS_RETURN_SIGNAL.search(remarks or ""):
        return "status"
    return "data"


VB_TO_PY_TYPE = {
    "string": "str",
    "double": "float",
    "long": "int",
    "boolean": "bool",
    "variant": "object",
    "object": "object",
}


def vb_type_to_py(vb_type: str, is_array: bool, known_enums: set) -> str:
    base = VB_TO_PY_TYPE.get(vb_type.lower())
    if base is None:
        if vb_type in known_enums:
            base = "int"
        elif vb_type.lower().startswith("e"):
            base = "int"
        else:
            base = "object"
    if is_array:
        return f"list[{base}]"
    return base
