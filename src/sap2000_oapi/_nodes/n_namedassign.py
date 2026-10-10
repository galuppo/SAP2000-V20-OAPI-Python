"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_NamedAssign:
    """Wrapper para SapModel.NamedAssign."""

    def __init__(self, raw):
        self._raw = raw

    @cached_property
    def ModifierArea(self):
        return N_NamedAssign_ModifierArea(self._raw.ModifierArea)

    @cached_property
    def ModifierCable(self):
        return N_NamedAssign_ModifierCable(self._raw.ModifierCable)

    @cached_property
    def ModifierFrame(self):
        return N_NamedAssign_ModifierFrame(self._raw.ModifierFrame)

    @cached_property
    def ReleaseFrame(self):
        return N_NamedAssign_ReleaseFrame(self._raw.ReleaseFrame)


class N_NamedAssign_ModifierFrame:
    """Wrapper para SapModel.NamedAssign.ModifierFrame."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing frame property modifier. The function returns
        zero if the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined frame property modifier.
        NewName (input): The new name for the frame property modifier.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierFrame.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns the total number of defined frame property modifiers in the model.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified frame property modifier. The function returns zero if the
        modifier is successfully deleted; otherwise it returns a nonzero value. It returns
        an error if the specified modifier can not be deleted; for example, if it is
        currently used by a staged construction load case.
    
        Name (input): The name of an existing frame property modifier.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierFrame.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetModifiers(self, Name: str):
        """This function retrieves the modifier assignments for a frame property modifier. The default
        value for all modifier values is one. The function returns zero if the modifier
        assignments are successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame property modifier.
        Value (output): This is an array of eight unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Shear area in local 2 direction modifier
            Value(2) = Shear area in local 3 direction modifier Value(3) = Torsional
            constant modifier Value(4) = Moment of inertia about local 2 axis modifier
            Value(5) = Moment of inertia about local 3 axis modifier Value(6) = Mass
            modifier Value(7) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierFrame.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined frame property modifiers. The function
        returns zero if the names are successfully retrieved; otherwise it returns nonzero.
    
        NumberNames (output): The number of frame property modifier names retrieved by the
            program.
        MyName (output): This is a one-dimensional array of frame property modifier names.
            The MyName array is created as a dynamic, zero-based, array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames - 1) inside the
            SAP2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierFrame.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetModifiers(self, Name: str, Value: list[float]):
        """This function defines a named frame property modifier. The default value for all modifier
        values is one. The function returns zero if the modifier is successfully defined;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a new or existing frame property modifier.
        Value (input): This is an array of eight unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Shear area in local 2 direction modifier
            Value(2) = Shear area in local 3 direction modifier Value(3) = Torsional
            constant modifier Value(4) = Moment of inertia about local 2 axis modifier
            Value(5) = Moment of inertia about local 3 axis modifier Value(6) = Mass
            modifier Value(7) = Weight modifier
        """
        _r = self._raw.SetModifiers(Name, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierFrame.SetModifiers falhou (ret={_r})".format(_r=_r))
        return None


class N_NamedAssign_ModifierArea:
    """Wrapper para SapModel.NamedAssign.ModifierArea."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing area stiffness modifier. The function returns
        zero if the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined area stiffness modifier.
        NewName (input): The new name for the area stiffness modifier.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierArea.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns the total number of defined area stiffness modifiers in the model.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified area stiffness modifier. The function returns zero if the
        modifier is successfully deleted; otherwise it returns a nonzero value. It returns
        an error if the specified modifier can not be deleted; for example, if it is
        currently used by a staged construction load case.
    
        Name (input): The name of an existing area stiffness modifier.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierArea.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetModifiers(self, Name: str):
        """This function retrieves the modifier assignments for an area stiffness modifier. The default
        value for all modifier values is one. The function returns zero if the modifier
        assignments are successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area stiffness modifier.
        Value (output): This is an array of ten unitless modifiers. Value(0) = Membrane f11
            modifier Value(1) = Membrane f22 modifier Value(2) = Membrane f12 modifier
            Value(3) = Bending m11 modifier Value(4) = Bending m22 modifier Value(5) =
            Bending m12 modifier Value(6) = Shear v13 modifier Value(7) = Shear v23 modifier
            Value(8) = Mass modifier Value(9) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierArea.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined area stiffness modifiers. The function
        returns zero if the names are successfully retrieved; otherwise it returns nonzero
        values.
    
        NumberNames (output): The number of area stiffness modifier names retrieved by the
            program.
        MyName (output): This is a one-dimensional array of area stiffness modifier names.
            The MyName array is created as a dynamic, zero-based array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames - 1) inside the
            SAP2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierArea.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetModifiers(self, Name: str, Value: list[float]):
        """This function defines a named area stiffness modifier. The default value for all modifier
        values is one. The function returns zero if the modifier is successfully defined;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a new or existing area stiffness modifier.
        Value (input): This is an array of ten unitless modifiers. Value(0) = Membrane f11
            modifier Value(1) = Membrane f22 modifier Value(2) = Membrane f12 modifier
            Value(3) = Bending m11 modifier Value(4) = Bending m22 modifier Value(5) =
            Bending m12 modifier Value(6) = Shear v13 modifier Value(7) = Shear v23 modifier
            Value(8) = Mass modifier Value(9) = Weight modifier
        """
        _r = self._raw.SetModifiers(Name, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierArea.SetModifiers falhou (ret={_r})".format(_r=_r))
        return None


class N_NamedAssign_ReleaseFrame:
    """Wrapper para SapModel.NamedAssign.ReleaseFrame."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing frame end release. The function returns zero
        if the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined frame end release.
        NewName (input): The new name for the frame end release.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ReleaseFrame.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns the total number of defined frame end releases in the model.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified frame end release. The function returns zero if the end
        release is successfully deleted; otherwise it returns a nonzero value. It returns an
        error if the specified end release can not be deleted; for example, if it is
        currently used by a staged construction load case.
    
        Name (input): The name of an existing frame end release.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ReleaseFrame.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetNameList(self):
        """This function retrieves the names of all defined frame end releases. The function returns
        zero if the names are successfully retrieved; otherwise it returns nonzero values.
    
        NumberNames (output): The number of frame end release names retrieved by the
            program.
        MyName (output): This is a one-dimensional array of frame end release names. The
            MyName array is created as a dynamic, zero-based array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames - 1) inside the
            SAP2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ReleaseFrame.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetReleases(self, Name: str):
        """This function retrieves the release assignments for a frame end release. The function
        returns zero if the release assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame end release.
        """
        _r = self._raw.GetReleases(Name, [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ReleaseFrame.GetReleases falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetReleases(self, Name: str, ii: list[bool], jj: list[bool], StartValue: list[float], EndValue: list[float]):
        """This function defines a named frame end release. The function returns zero if the release is
        successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of a new or existing frame end release.
        """
        _r = self._raw.SetReleases(Name, ii, jj, StartValue, EndValue)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ReleaseFrame.SetReleases falhou (ret={_r})".format(_r=_r))
        return None


class N_NamedAssign_ModifierCable:
    """Wrapper para SapModel.NamedAssign.ModifierCable."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing cable property modifier. The function returns
        zero if the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined cable property modifier.
        NewName (input): The new name for the cable property modifier.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierCable.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns the total number of defined cable property modifiers in the model.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified cable property modifier. The function returns zero if the
        modifier is successfully deleted; otherwise it returns a nonzero value. It returns
        an error if the specified modifier can not be deleted, for example, if it is
        currently used by a staged construction load case.
    
        Name (input): The name of an existing cable property modifier.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierCable.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetModifiers(self, Name: str):
        """This function retrieves the modifier assignments for a cable property modifier. The default
        value for all modifier values is one. The function returns zero if the modifier
        assignments are successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable property modifier.
        Value (output): This is an array of three unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Mass modifier Value(2) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierCable.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined cable property modifiers. The function
        returns zero if the names are successfully retrieved; otherwise it returns nonzero.
    
        NumberNames (output): The number of cable property modifier names retrieved by the
            program.
        MyName (output): This is a one-dimensional array of cable property modifier names.
            The MyName array is created as a dynamic, zero-based array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames - 1) inside the
            SAP2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierCable.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetModifiers(self, Name: str, Value: list[float]):
        """This function defines a named cable property modifier. The default value for all modifier
        values is one. The function returns zero if the modifier is successfully defined;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a new or existing cable property modifier.
        Value (input): This is an array of three unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Mass modifier Value(2) = Weight modifier
        """
        _r = self._raw.SetModifiers(Name, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedAssign.ModifierCable.SetModifiers falhou (ret={_r})".format(_r=_r))
        return None


