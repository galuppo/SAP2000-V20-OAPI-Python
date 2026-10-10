"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_GDispl:
    """Wrapper para SapModel.GDispl."""

    def __init__(self, raw):
        self._raw = raw

    def Add(self, Name: str, MyType: int):
        """This function adds a new generalized displacement with the specified name and type. The
        function returns zero if the generalized displacement is successfully added,
        otherwise it returns a nonzero value. The new generalized displacement must have a
        different name from all other generalized displacements. If the name is not unique,
        an error will be returned.
    
        Name (input): The name of a new generalized displacement.
        MyType (input): This is 1 or 2 indicating the generalized displacement type. 1 =
            Translational 2 = Rotational
        """
        _r = self._raw.Add(Name, MyType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GDispl.Add falhou (ret={_r})".format(_r=_r))
        return None

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value. The new generalized displacement name must be different from all
        other generalized displacement names. If the name is not unique, an error will be
        returned.
    
        Name (input): The existing name of a defined generalized displacement.
        NewName (input): The new name for the generalized displacement.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GDispl.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def CountPoint(self, Name: str):
        """This function retrieves the total number of point objects included in a specified
        generalized displacement. The function returns zero if the count is successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing generalized displacement.
        Count (output): The number of point objects included in the specified generalized
            displacement.
        """
        _r = self._raw.CountPoint(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GDispl.CountPoint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def Count(self):
        """This function returns the total number of generalized displacements defined in the model.
        """
        _r = self._raw.Count()
        return _r

    def DeletePoint(self, Name: str, PointName: str):
        """This function deletes one point object from a generalized displacement definition. The
        function returns zero if the point is successfully deleted from the generalized
        displacement definition, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing generalized displacement.
        PointName (input): The name of a point object included in the generalized
            displacement that is to be deleted.
        """
        _r = self._raw.DeletePoint(Name, PointName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GDispl.DeletePoint falhou (ret={_r})".format(_r=_r))
        return None

    def Delete(self, Name: str):
        """This function deletes the specified generalized displacement. The function returns zero if
        the generalized displacement is successfully deleted, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing generalized displacement.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GDispl.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetNameList(self):
        """This function retrieves the names of all defined generalized displacements. The function
        returns zero if the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of generalized displacement names retrieved by the
            program.
        MyName (output): This is a one-dimensional array of generalized displacement names.
            The MyName array is created as a dynamic, zero-based, array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames 1) inside the
            Sap2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GDispl.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoint(self, Name: str):
        """This function retrieves the point objects and their scale factors from a generalized
        displacement definition. The function returns zero if the data is successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing generalized displacement.
        NumberItems (output): The number of point objects included in the generalized
            displacement definition.
        PointName (output): This is an array that includes the name of the point objects
            included in the generalized displacement definition.
        """
        _r = self._raw.GetPoint(Name, 0, [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GDispl.GetPoint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTypeOAPI(self, Name: str):
        """This function retrieves the generalized displacement type. The function returns zero if the
        type is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing generalized displacement.
        MyType (output): This is 1 or 2, indicating the generalized displacement type. 1 =
            Translational 2 = Rotational
        """
        _r = self._raw.GetTypeOAPI(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GDispl.GetTypeOAPI falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetPoint(self, Name: str, PointName: str, SF: list[float]):
        """This function adds a point object and its scale factors to a generalized displacement
        definition, or, if the point object already exists in the generalized displacement
        definition, it modifies the scale factors. The function returns zero if the data is
        successfully added or modified, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing generalized displacement.
        PointName (input): The name of a point object to be included in the generalized
            displacement definition.
        SF (input): This is an array of six unitless scale factors for the point object
            displacement degrees of freedom. SF(0) = U1 scale factor SF(1) = U2 scale factor
            SF(2) = U3 scale factor SF(3) = R1 scale factor SF(4) = R2 scale factor SF(5) =
            R3 scale factor
        """
        _r = self._raw.SetPoint(Name, PointName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GDispl.SetPoint falhou (ret={_r})".format(_r=_r))
        return None

    def SetTypeOAPI(self, Name: str, MyType: int):
        """This function sets the generalized displacement type. The function returns zero if the type
        is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing generalized displacement.
        MyType (input): This is 1 or 2, indicating the generalized displacement type. 1 =
            Translational 2 = Rotational
        """
        _r = self._raw.SetTypeOAPI(Name, MyType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GDispl.SetTypeOAPI falhou (ret={_r})".format(_r=_r))
        return None


