"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PropSolid:
    """Wrapper para SapModel.PropSolid."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing solid property. The function returns zero if
        the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined solid property.
        NewName (input): The new name for the solid property.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropSolid.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns the total number of defined solid properties in the model.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified solid property. The function returns zero if the property
        is successfully deleted; otherwise it returns a nonzero value. It returns an error
        if the specified property can not be deleted, for example, if it is assigned to an
        existing object.
    
        Name (input): The name of an existing solid property.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropSolid.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetNameList(self):
        """This function retrieves the names of all defined solid properties in the model. The function
        returns zero if the names are successfully retrieved; otherwise it returns nonzero.
    
        NumberNames (output): The number of solid property names retrieved by the program.
        MyName (output): This is a one-dimensional array of solid property names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames - 1) inside the SAP2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropSolid.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetProp(self, Name: str, MatProp: str, Incompatible: bool, Color: int, Notes: str, GUID: str):
        """This function retrieves solid property definition data. The function returns zero if the
        property data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid property.
        MatProp (input): The name of the material property assigned to the solid property.
        a (output): The material angle A. [deg]
        c (output): The material angle C. [deg]
        Incompatible (input): If this item is True, incompatible bending modes are included
            in the stiffness formulation. In general, incompatible modes significantly
            improve the bending behavior of the object.
        Color (input): The display color assigned to the property.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetProp(Name, MatProp, 0.0, 0.0, 0.0, Incompatible, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropSolid.GetProp falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetProp(self, Name: str, MatProp: str, a: float, B: float, c: float, Incompatible: bool, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function defines a solid property. The function returns zero if the property is
        successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new solid property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        MatProp (input): The name of the material property assigned to the solid property.
        a (input): The material angle A. [deg]
        c (input): The material angle C. [deg]
        Incompatible (input): If this item is True, incompatible bending modes are included
            in the stiffness formulation. In general, incompatible modes significantly
            improve the bending behavior of the object.
        Color (input): The display color assigned to the property. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetProp(Name, MatProp, a, B, c, Incompatible, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropSolid.SetProp falhou (ret={_r})".format(_r=_r))
        return None


