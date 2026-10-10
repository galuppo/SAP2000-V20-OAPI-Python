"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_SapMoel:
    """Wrapper para SapModel.SapMoel."""

    def __init__(self, raw):
        self._raw = raw

    @cached_property
    def SelectObj(self):
        return N_SapMoel_SelectObj(self._raw.SelectObj)


class N_SapMoel_SelectObj:
    """Wrapper para SapModel.SapMoel.SelectObj."""

    def __init__(self, raw):
        self._raw = raw

    def LinesParallelToLine(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all line objects that are parallel to a specified line
        object. The function returns zero if the selection is successfully completed,
        otherwise it returns nonzero.
    
        Name (input): The name of a line object.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.LinesParallelToLine(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SapMoel.SelectObj.LinesParallelToLine falhou (ret={_r})".format(_r=_r))
        return None


