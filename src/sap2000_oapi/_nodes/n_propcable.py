"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PropCable:
    """Wrapper para SapModel.PropCable."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing cable property. The function returns zero if
        the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined cable property.
        NewName (input): The new name for the cable property.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropCable.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns the total number of defined cable properties in the model.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified cable property. The function returns zero if the property
        is successfully deleted; otherwise it returns a nonzero value. It returns an error
        if the specified property can not be deleted, for example, if it is assigned to an
        existing object.
    
        Name (input): The name of an existing cable property.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropCable.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetModifiers(self, Name: str):
        """This function retrieves the modifier assignments for a cable property. The default value for
        all modifiers is one. The function returns zero if the modifier assignments are
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable property.
        Value (output): This is an array of three unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Mass modifier Value(2) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropCable.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined cable properties in the model. The function
        returns zero if the names are successfully retrieved; otherwise it returns nonzero.
    
        NumberNames (output): The number of cable property names retrieved by the program.
        MyName (output): This is a one-dimensional array of cable property names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames - 1) inside the SAP2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropCable.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetProp(self, Name: str, MatProp: str, Color: int, Notes: str, GUID: str):
        """This function retrieves cable property definition data. The function returns zero if the
        property data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable property.
        MatProp (input): The name of the material property assigned to the cable property.
        Area (output): The cross-sectional area of the cable. [L 2 ]
        Color (input): The display color assigned to the property.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetProp(Name, MatProp, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropCable.GetProp falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetModifiers(self, Name: str, Value: list[float]):
        """This function assigns property modifiers to a cable property. The default value for all
        modifiers is one. The function returns zero if the modifiers are successfully
        assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable property.
        Value (input): This is an array of 3 unitless modifiers. Value(0) = Cross sectional
            area modifier Value(1) = Mass modifier Value(2) = Weight modifier
        """
        _r = self._raw.SetModifiers(Name, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropCable.SetModifiers falhou (ret={_r})".format(_r=_r))
        return None

    def SetProp(self, Name: str, MatProp: str, Area: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function defines a cable property. The function returns zero if the property is
        successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new cable property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        MatProp (input): The name of the material property assigned to the cable property.
        Area (input): The cross-sectional area of the cable. [L 2 ]
        Color (input): The display color assigned to the property. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetProp(Name, MatProp, Area, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropCable.SetProp falhou (ret={_r})".format(_r=_r))
        return None


