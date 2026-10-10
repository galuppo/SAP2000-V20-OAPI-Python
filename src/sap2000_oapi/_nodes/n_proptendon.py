"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PropTendon:
    """Wrapper para SapModel.PropTendon."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing tendon property. The function returns zero if
        the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined tendon property.
        NewName (input): The new name for the tendon property.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropTendon.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns the total number of defined tendon properties in the model.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified tendon property. The function returns zero if the property
        is successfully deleted; otherwise it returns a nonzero value. It returns an error
        if the specified property can not be deleted, for example, if it is assigned to an
        existing object.
    
        Name (input): The name of an existing tendon property.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropTendon.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetNameList(self):
        """This function retrieves the names of all defined tendon properties in the model. The
        function returns zero if the names are successfully retrieved; otherwise it returns
        nonzero.
    
        NumberNames (output): The number of tendon property names retrieved by the program.
        MyName (output): This is a one-dimensional array of tendon property names. The
            MyName array is created as a dynamic, zero-based, array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames - 1) inside the
            SAP2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropTendon.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetProp(self, Name: str, MatProp: str, Color: int, Notes: str, GUID: str):
        """This function retrieves tendon property definition data. The function returns zero if the
        property data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon property.
        MatProp (input): The name of the material property assigned to the tendon property.
        ModelingOption (output): This is either 1 or 2, indicating the tendon modeling
            option. 1 = Model tendon as loads 2 = Model tendon as elements
        Area (output): The cross-sectional area of the tendon. [L 2 ]
        Color (input): The display color assigned to the property.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetProp(Name, MatProp, 0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropTendon.GetProp falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetProp(self, Name: str, MatProp: str, ModelingOption: int, Area: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function defines a tendon property. The function returns zero if the property is
        successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new tendon property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        MatProp (input): The name of the material property assigned to the tendon property.
        ModelingOption (input): This is either 1 or 2, indicating the tendon modeling
            option. 1 = Model tendon as loads 2 = Model tendon as elements
        Area (input): The cross-sectional area of the tendon. [L 2 ]
        Color (input): The display color assigned to the property. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetProp(Name, MatProp, ModelingOption, Area, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropTendon.SetProp falhou (ret={_r})".format(_r=_r))
        return None


