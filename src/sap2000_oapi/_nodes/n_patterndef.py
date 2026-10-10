"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PatternDef:
    """Wrapper para SapModel.PatternDef."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value.
    
        Name (input): The existing name of a defined joint pattern.
        NewName (input): The new name for the joint pattern.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PatternDef.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """The function returns the number of defined joint patterns.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes the specified joint pattern. At least one joint pattern must be
        defined. The function will return an error if an attempt is made to delete the last
        joint pattern. The function returns zero if the joint pattern is successfully
        deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing joint pattern.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PatternDef.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetNameList(self):
        """This function retrieves the names of all defined joint patterns. The function returns zero
        if the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of joint pattern names retrieved by the program.
        MyName (output): This is a one-dimensional array of joint pattern names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames 1) inside the Sap2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PatternDef.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetPattern(self, Name: str):
        """The function defines a new joint pattern. It returns an error if the specified joint pattern
        name is already in use. The function returns zero if the new joint pattern is
        successfully defined, otherwise it returns a nonzero value.
    
        Name (input): The name of a new joint pattern.
        """
        _r = self._raw.SetPattern(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PatternDef.SetPattern falhou (ret={_r})".format(_r=_r))
        return None


