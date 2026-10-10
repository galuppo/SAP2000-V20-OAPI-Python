"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_RespCombo:
    """Wrapper para SapModel.RespCombo."""

    def __init__(self, raw):
        self._raw = raw

    def AddDesignDefaultCombos(self, DesignSteel: bool, DesignConcrete: bool, DesignAluminum: bool, DesignColdFormed: bool):
        """This function adds a new default design load combinations to the model. The function returns
        zero if the load combinations are successfully added, otherwise it returns a nonzero
        value.
    
        DesignSteel (input): If this item is True, default steel design combinations are to
            be added to the model.
        DesignConcrete (input): If this item is True, default concrete design combinations
            are to be added to the model.
        DesignAluminum (input): If this item is True, default aluminum design combinations
            are to be added to the model.
        DesignColdFormed (input): If this item is True, default cold formed design
            combinations are to be added to the model.
        """
        _r = self._raw.AddDesignDefaultCombos(DesignSteel, DesignConcrete, DesignAluminum, DesignColdFormed)
        if _r != 0:
            raise Sap2000ApiError("SapModel.RespCombo.AddDesignDefaultCombos falhou (ret={_r})".format(_r=_r))
        return None

    def Add(self, Name: str, ComboType: int):
        """This function adds a new load combination. The function returns zero if the load combination
        is successfully added, otherwise it returns a nonzero value. The new load
        combination must have a different name from all other load combinations and all load
        cases. If the name is not unique, an error will be returned.
    
        Name (input): The name of a new load combination.
        ComboType (input): This is 0, 1, 2, 3 or 4 indicating the load combination type. 0 =
            Linear Additive 1 = Envelope 2 = Absolute Additive 3 = SRSS 4 = Range Additive
        """
        _r = self._raw.Add(Name, ComboType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.RespCombo.Add falhou (ret={_r})".format(_r=_r))
        return None

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value. The new load combination name must be different from all other load
        combinations and all load cases. If the name is not unique, an error will be
        returned.
    
        Name (input): The existing name of a defined load combination.
        NewName (input): The new name for the combination.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.RespCombo.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def CountCase(self, Name: str):
        """This function retrieves the total number of load case and/or combinations included in a
        specified load combination. The function returns zero if the count is successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        Count (output): The number of load case and/or combinations included in the
            specified combination.
        """
        _r = self._raw.CountCase(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.RespCombo.CountCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def Count(self):
        """This function returns the total number of load combinations defined in the model.
        """
        _r = self._raw.Count()
        return _r

    def DeleteCase(self, Name: str, CType: int, CName: str):
        """This function deletes one load case or load combination from the list of cases included in
        the specified load combination. The function returns zero if the item is
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        CType (input): This is one of the following items in the eCNameType enumeration:
            LoadCase = 0 LoadCombo = 1 This item indicates whether the CName item is an
            analysis case (LoadCase) or a load combination (LoadCombo).
        CName (input): The name of the load case or load combination to be deleted from the
            specified combination.
        """
        _r = self._raw.DeleteCase(Name, CType, CName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.RespCombo.DeleteCase falhou (ret={_r})".format(_r=_r))
        return None

    def Delete(self, Name: str):
        """This function deletes the specified load combination. The function returns zero if the
        combination is successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.RespCombo.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetCaseList(self, Name: str):
        """This function returns all load cases and response combinations included in the load
        combination specified by the Name item. The function returns zero if the data is
        successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        NumberItems (output): The total number of load cases and load combinations included
            in the load combination specified by the Name item.
        CType (output): This is an array of one of the following items in the eCNameType
            enumeration: LoadCase = 0 LoadCombo = 1 This item indicates if the associated
            CName item is an load case (LoadCase) or a load combination (LoadCombo).
        CName (output): This is an array of the names of the load cases or load combinations
            included in the load combination specified by the Name item.
        SF (output): The scale factor multiplying the case or combination indicated by the
            CName item.
        """
        _r = self._raw.GetCaseList(Name, 0, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.RespCombo.GetCaseList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNameList(self):
        """This function retrieves the names of all defined response combinations. The function returns
        zero if the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of load combination names retrieved by the program.
        MyName (output): This is a one-dimensional array of load combination names. The
            MyName array is created as a dynamic, zero-based, array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames 1) inside the
            Sap2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.RespCombo.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNote(self, Name: str):
        """This function retrieves the user note for specified response combination. The note may be
        blank. The function returns zero if the note is successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        Note (output): The user note, if any, included with the specified combination.
        """
        _r = self._raw.GetNote(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.RespCombo.GetNote falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetTypeOAPI(self, Name: str):
        """This function retrieves the combination type for specified load combination. The function
        returns zero if the type is successfully retrieved, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing load combination.
        ComboType (output): This is 0, 1, 2, 3 or 4 indicating the load combination type. 0
            = Linear Additive 1 = Envelope 2 = Absolute Additive 3 = SRSS 4 = Range Additive
        """
        _r = self._raw.GetTypeOAPI(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.RespCombo.GetTypeOAPI falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetCaseList(self, Name: str, CNameType: int, CName: str, SF: float):
        """This function adds or modifies one load case or response combination in the list of cases
        included in the load combination specified by the Name item. The function returns
        zero if the item is successfully added or modified, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing load combination.
        CNameType (input): This is one of the following items in the eCNameType enumeration:
            LoadCase = 0 LoadCombo = 1 This item indicates if the CName item is an load case
            (LoadCase) or a load combination (LoadCombo).
        CName (input): The name of the load case or load combination to be added to or
            modified in the combination specified by the Name item. If the load case or
            combination already exists in the combination specified by the Name item, the
            scale factor is modified as indicated by the SF item for that load case or
            combination. If the analysis case or combination does not exist in the
            combination specified by the Name item, it is added.
        SF (input): The scale factor multiplying the case or combination indicated by the
            CName item.
        """
        _r = self._raw.SetCaseList(Name, CNameType, CName, SF)[1]
        if _r != 0:
            raise Sap2000ApiError("SapModel.RespCombo.SetCaseList falhou (ret={_r})".format(_r=_r))
        return None

    def SetNote(self, Name: str, Note: str):
        """This function sets the user note for specified response combination. The note may be blank.
        The function returns zero if the note is successfully set, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing load combination.
        Note (input): The user note included with the specified combination. It may be a
            blank string.
        """
        _r = self._raw.SetNote(Name, Note)
        if _r != 0:
            raise Sap2000ApiError("SapModel.RespCombo.SetNote falhou (ret={_r})".format(_r=_r))
        return None

    def SetTypeOAPI(self, Name: str, ComboType: int):
        """This function sets the combination type for specified load combination. The function returns
        zero if the type is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        ComboType (input): This is 0, 1, 2, 3 or 4 indicating the load combination type. 0 =
            Linear Additive 1 = Envelope 2 = Absolute Additive 3 = SRSS 4 = Range Additive
        """
        _r = self._raw.SetTypeOAPI(Name, ComboType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.RespCombo.SetTypeOAPI falhou (ret={_r})".format(_r=_r))
        return None


