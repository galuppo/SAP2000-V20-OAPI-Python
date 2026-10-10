"""Extrai, de cada página .htm do CHM da OAPI, uma estrutura de dados com:
sintaxe (caminho do objeto), assinatura VB6, parâmetros (nome + descrição)
e remarks. Usa as classes CSS consistentes do RoboHelp (h2 de seção,
p.ParameterName / p.Comment) em vez de regex sobre texto solto.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path

from bs4 import BeautifulSoup

CHM_ROOT = Path("/home/claude/chm_extract/SAP2000_API_Fuctions")
EXCLUDE_DIRS = {"Obsolete_Functions"}


@dataclass
class ParamInfo:
    name: str
    description: str = ""


@dataclass
class FunctionInfo:
    file: str
    title: str
    syntax_path: str = ""          # ex.: SapModel.PropMaterial.SetMaterial
    proc_kind: str = ""            # "Function" ou "Sub"
    func_name: str = ""            # nome real, extraído da assinatura VB6
    return_type: str = ""          # "Long", "String", "Double", "" (Sub)
    signature_params: list = field(default_factory=list)  # [(byref, name, type, is_array, optional, default)]
    param_docs: dict = field(default_factory=dict)        # nome -> descrição concatenada
    remarks: str = ""


def _section_text_blocks(soup: BeautifulSoup) -> dict:
    """Divide o corpo em blocos por cabeçalho h2, preservando os <p> de cada um."""
    body = soup.body
    if body is None:
        return {}
    sections: dict[str, list] = {}
    current = None
    for el in body.find_all(["h2", "p"], recursive=False):
        if el.name == "h2":
            current = el.get_text(strip=True)
            sections[current] = []
        elif current is not None:
            sections[current].append(el)
    return sections


def parse_file(path: Path) -> FunctionInfo | None:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(raw, "html.parser")

    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else path.stem

    sections = _section_text_blocks(soup)
    if "Syntax" not in sections or "VB6 Procedure" not in sections:
        return None  # página que não documenta uma função (índice, etc.)

    syntax_text = " ".join(p.get_text(" ", strip=True) for p in sections["Syntax"])
    proc_text = " ".join(p.get_text(" ", strip=True) for p in sections["VB6 Procedure"])
    proc_text = re.sub(r"\s+", " ", proc_text).strip()

    m = re.search(r"(Function|Sub)\s+(\w+)\s*\((.*?)\)(?:\s*As\s*([\w.]+))?\s*$", proc_text)
    if not m:
        return None
    proc_kind, func_name, params_raw, return_type = m.groups()
    return_type = return_type or ""

    signature_params = _parse_param_list(params_raw)

    # Parâmetros documentados: sequência ParameterName -> (Comment/ParameterDescription)*
    param_docs: dict[str, str] = {}
    if "Parameters" in sections:
        current_name = None
        buf: list[str] = []
        for p in sections["Parameters"]:
            classes = p.get("class") or []
            txt = p.get_text(" ", strip=True)
            if "ParameterName" in classes:
                if current_name is not None:
                    param_docs[current_name] = " ".join(buf).strip()
                current_name = txt
                buf = []
            else:
                if txt:
                    buf.append(txt)
        if current_name is not None:
            param_docs[current_name] = " ".join(buf).strip()
    param_docs = {k: re.sub(r"\s+", " ", v).strip() for k, v in param_docs.items()}

    remarks = ""
    if "Remarks" in sections:
        remarks = " ".join(p.get_text(" ", strip=True) for p in sections["Remarks"])
    remarks = re.sub(r"\s+", " ", remarks).strip()

    return FunctionInfo(
        file=str(path),
        title=title,
        syntax_path=syntax_text,
        proc_kind=proc_kind,
        func_name=func_name,
        return_type=return_type,
        signature_params=signature_params,
        param_docs=param_docs,
        remarks=remarks,
    )


_PARAM_RE = re.compile(
    r"(?:(?P<optional>Optional)\s+)?"
    r"(?P<byref>ByVal|ByRef)\s*"
    r"(?P<name>\w+)(?P<array>\s*\(\s*\))?\s+As\s+(?P<type>[\w.]+)"
    r"(?:\s*=\s*(?P<default>-?\"[^\"]*\"|-?[\w.]+))?",
    re.IGNORECASE,
)

# Fallback para parâmetros sem o prefixo ByVal/ByRef explícito (a doc às
# vezes omite a repetição do modificador em parâmetros consecutivos do
# mesmo tipo). O padrão VB6 nesse caso é ByRef por default.
_PARAM_RE_NO_MODIFIER = re.compile(
    r"(?:(?P<optional>Optional)\s+)?"
    r"(?P<name>\w+)(?P<array>\s*\(\s*\))?\s+As\s+(?P<type>[\w.]+)"
    r"(?:\s*=\s*(?P<default>-?\"[^\"]*\"|-?[\w.]+))?",
    re.IGNORECASE,
)


def _split_top_level_commas(s: str) -> list:
    """Divide por vírgulas de nível 0, ignorando vírgulas dentro de strings entre aspas."""
    parts, buf, in_str = [], [], False
    for ch in s:
        if ch == '"':
            in_str = not in_str
        if ch == "," and not in_str:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if buf:
        parts.append("".join(buf))
    return [p.strip() for p in parts if p.strip()]


def _parse_param_list(params_raw: str) -> list:
    result = []
    for chunk in _split_top_level_commas(params_raw):
        m = _PARAM_RE.search(chunk)
        if m:
            result.append({
                "optional": bool(m.group("optional")),
                "byref": m.group("byref").lower() == "byref",
                "name": m.group("name"),
                "type": m.group("type"),
                "is_array": bool(m.group("array")),
                "default": m.group("default"),
            })
            continue
        # Fallback: parâmetro sem ByVal/ByRef explícito -> ByRef por default (VB6).
        m2 = _PARAM_RE_NO_MODIFIER.search(chunk)
        if m2:
            result.append({
                "optional": bool(m2.group("optional")),
                "byref": True,
                "name": m2.group("name"),
                "type": m2.group("type"),
                "is_array": bool(m2.group("array")),
                "default": m2.group("default"),
                "modifier_inferred": True,
            })
    return result


def main():
    files = [
        p for p in CHM_ROOT.rglob("*.htm")
        if not any(part in EXCLUDE_DIRS for part in p.parts)
    ]
    print(f"Total de arquivos candidatos: {len(files)}")

    functions = []
    skipped = []
    for p in sorted(files):
        try:
            info = parse_file(p)
        except Exception as exc:  # noqa: BLE001
            skipped.append((str(p), f"exception: {exc}"))
            continue
        if info is None:
            skipped.append((str(p), "sem Syntax/VB6 Procedure"))
            continue
        functions.append(info)

    print(f"Funções extraídas: {len(functions)}")
    print(f"Páginas ignoradas: {len(skipped)}")

    out = Path("/home/claude/sap2000_oapi_build/parsed_functions.json")
    out.write_text(
        json.dumps([asdict(f) for f in functions], ensure_ascii=False, indent=1),
        encoding="utf-8",
    )

    skipped_out = Path("/home/claude/sap2000_oapi_build/skipped_pages.json")
    skipped_out.write_text(json.dumps(skipped, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"Gravado em {out}")


if __name__ == "__main__":
    main()
