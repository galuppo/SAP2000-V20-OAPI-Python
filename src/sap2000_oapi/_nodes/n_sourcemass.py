"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_SourceMass:
    """Wrapper para SapModel.SourceMass."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing mass source. The function returns zero if the
        mass source is successfully changed, otherwise it returns a nonzero value. If the
        new name already exists, a nonzero value is returned and the mass source name is not
        changed.
    
        Name (input): The name of an existing mass source.
        NewName (input): The new name for the mass source.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SourceMass.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns the number of defined mass sources.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """This function deletes an existing mass source. The function returns zero if the mass source
        is successfully deleted; otherwise it returns a nonzero value. If the mass source to
        be deleted is the default mass source, a nonzero value is returned and th mass
        source is not deleted.
    
        Name (input): The name of the mass source to be deleted.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SourceMass.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetDefault(self):
        """This function retrieves the default mass source. The function returns zero if the default
        mass source is successfully retrieved, otherwise it returns nonzero.
    
        Name (output): The name of the default mass source.
        """
        _r = self._raw.GetDefault("")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SourceMass.GetDefault falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMassSource(self, Name: str, MassFromElements: bool, MassFromMasses: bool, MassFromLoads: bool, IsDefault: bool):
        """This function gets the mass source data for an existing mass source. The function returns
        zero if the mass source data is successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The mass source name.
        MassFromElements (input): If this item is True then element self mass is included in
            the mass.
        MassFromMasses (input): If this item is True then assigned masses are included in
            the mass.
        MassFromLoads (input): If this item is True then specified load patterns are
            included in the mass.
        IsDefault (input): If this item is True then the mass source is the default mass
            source.
        NumberLoads (output): The number of load patterns specified for the mass source.
            This item is only applicable when the MassFromLoads item is True.
        LoadPat (output): This is an array of load pattern names specified for the mass
            source.
        SF (output): This is an array of load pattern multipliers specified for the mass
            source.
        """
        _r = self._raw.GetMassSource(Name, MassFromElements, MassFromMasses, MassFromLoads, IsDefault, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SourceMass.GetMassSource falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNameList(self):
        """This function retrieves the names of all defined mass sources. The function returns zero if
        the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of mass source names retrieved by the program.
        MyName (output): This is a one-dimensional array of mass source names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames 1) inside the Sap2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SourceMass.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetDefault(self, Name: str):
        """This function sets the default mass source. The function returns zero if the mass source is
        successfully flagged as default, otherwise it returns nonzero. Only one mass source
        can be the default mass source so when this assignment is set all other mass sources
        are automatically set to have their IsDefault flag False.
    
        Name (input): The name of the mass source to be flagged as the default mass source.
        """
        _r = self._raw.SetDefault(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SourceMass.SetDefault falhou (ret={_r})".format(_r=_r))
        return None

    def SetMassSource(self, Name: str, MassFromElements: bool, MassFromMasses: bool, MassFromLoads: bool, IsDefault: bool, NumberLoads: int, LoadPat: list[str], SF: list[float]):
        """This function adds a new mass source to the model or reinitializes an existing mass source.
        The function returns zero if the mass source is successfully added or initialized,
        otherwise it returns a nonzero value.
    
        Name (input): The mass source name. If a mass source with this name already exists
            then the mass source is reinitialized with the new data. All previous data
            assigned to the mass source is lost. If a mass source with this name does not
            exist then a new mass source is added.
        MassFromElements (input): If this item is True then element self mass is included in
            the mass.
        MassFromMasses (input): If this item is True then assigned masses are included in
            the mass.
        MassFromLoads (input): If this item is True then specified load patterns are
            included in the mass.
        IsDefault (input): If this item is True then the mass source is the default mass
            source. Only one mass source can be the default mass source so when this
            assignment is True all other mass sources are automatically set to have the
            IsDefault flag False.
        NumberLoads (input): The number of load patterns specified for the mass source. This
            item is only applicable when the MassFromLoads item is True.
        LoadPat (input): This is an array of load pattern names specified for the mass
            source.
        SF (input): This is an array of load pattern multipliers specified for the mass
            source.
        """
        _r = self._raw.SetMassSource(Name, MassFromElements, MassFromMasses, MassFromLoads, IsDefault, NumberLoads, LoadPat, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SourceMass.SetMassSource falhou (ret={_r})".format(_r=_r))
        return None


