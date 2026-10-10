"""sap2000_oapi — wrapper Python tipado para a OAPI do SAP2000 v20,
gerado automaticamente a partir de CSI_OAPI_Documentation.chm.

Uso básico:

    from sap2000_oapi import Sap2000Connection
    from sap2000_oapi.enums import eMatType

    with Sap2000Connection(visible=True) as sap:
        sap.PropMaterial.SetMaterial("C30", eMatType.MATERIAL_CONCRETE)

Veja reports/revisao_necessaria.md para os pontos gerados por heurística
que merecem checagem manual antes de uso em produção.

Nota: `Sap2000Connection` depende de `comtypes`, que só funciona no
Windows. O resto do pacote (model, enums, errors, a árvore de nós) não
depende de COM e pode ser importado/testado em qualquer SO — por isso o
import de Sap2000Connection é preguiçoso (só falha se você realmente usá-la
fora do Windows).
"""

from .errors import Sap2000ApiError
from .model import SapModelWrapper

__all__ = ["Sap2000Connection", "Sap2000ApiError", "SapModelWrapper"]
__version__ = "0.1.0"


def __getattr__(name):
    if name == "Sap2000Connection":
        from .connection import Sap2000Connection

        return Sap2000Connection
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
