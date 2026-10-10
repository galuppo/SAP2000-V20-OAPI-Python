"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_EditGeneral:
    """Wrapper para SapModel.EditGeneral."""

    def __init__(self, raw):
        self._raw = raw

    def Move(self, dx: float, dy: float, dz: float):
        """This function moves selected point, frame, cable, tendon, area, solid and link objects. The
        function returns zero if the move is successful; otherwise it returns a nonzero
        value.
        """
        _r = self._raw.Move(dx, dy, dz)
        if _r != 0:
            raise Sap2000ApiError("SapModel.EditGeneral.Move falhou (ret={_r})".format(_r=_r))
        return None


