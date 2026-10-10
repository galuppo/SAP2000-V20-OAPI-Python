"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_LinkElm:
    """Wrapper para SapModel.LinkElm."""

    def __init__(self, raw):
        self._raw = raw

    def Count(self):
        """This function returns the total number of link elements in the analysis model.
        """
        _r = self._raw.Count()
        return _r

    def GetLoadDeformation(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the deformation load assignments to link elements. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing link object, link element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified link elements.
        LinkName (output): This is an array that includes the name of the link element
            associated with each deformation load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each deformation load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the link elements
            corresponding to the link object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the link element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the link elements corresponding to all link objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for link elements corresponding to all selected link objects, and
            the Name item is ignored.
        """
        _r = self._raw.GetLoadDeformation(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetLoadDeformation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadGravity(self, Name: str, ItemType: int = 0):
        """This function retrieves the gravity load assignments to link elements. The function returns
        zero if the load assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing link object, link element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            link elements.
        LinkName (output): This is an array that includes the name of the link element
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTargetForce(self, Name: str, ItemType: int = 0):
        """This function retrieves the target force assignments to link elements. The function returns
        zero if the target force assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing link object, link element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified link elements.
        LinkName (output): This is an array that includes the name of the link element
            associated with each target force.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each target force.
        """
        _r = self._raw.GetLoadTargetForce(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetLoadTargetForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str):
        """This function retrieves the local axis angle assignment for link elements. The function
        returns zero if the assignment is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing link element.
        Ang (output): This is the angle that the local 2 and 3 axes are rotated about the
            positive local 1 axis, from the default orientation. The rotation for a positive
            angle appears counter clockwise when the local +1 axis is pointing toward you.
            [deg]
        """
        _r = self._raw.GetLocalAxes(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined link elements. The function returns zero if
        the names are successfully retrieved; otherwise it returns nonzero.
    
        NumberNames (output): The number of link element names retrieved by the program.
        MyName (output): This is a one-dimensional array of link element names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames 1) inside the SAP2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetObj(self, Name: str):
        """This function retrieves the object associated with a specified link element. The function
        returns zero if the object is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing link element.
        Obj (output): The name of the object associated with the specified link element. The
            type of object or item is determined from the ObjType variable.
        ObjType (output): A number indicating the type of object that is associated with the
            point element. 2 Obj is a line object that is has a line spring assignment. The
            springs are modeled using link elements. 3 Obj is a area object that is has an
            area spring assignment. The springs are modeled using link elements. 6 Obj is a
            solid object that is has a surface spring assignment. The springs are modeled
            using link elements. 9 Obj is a point object that has a panel zone assignment.
            The specified link element is internally added by the program at the point
            object (panel zone) location to model the panel zone.
        """
        _r = self._raw.GetObj(Name, "", 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetObj falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoints(self, Name: str):
        """This function retrieves the names of the point elements at each end of a specified link
        element. The points at each end have the same name if the link element is a one-
        joint element. The function returns zero if the point names are successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a defined link element.
        Point1 (output): The name of the point element at the I-End of the specified link
            element.
        Point2 (output): The name of the point element at the J-End of the specified link
            element.
        """
        _r = self._raw.GetPoints(Name, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPropertyFD(self, Name: str, PropName: str):
        """This function retrieves the frequency dependent property assignment to a link element. If no
        frequency dependent property is assigned to the link, the PropName is returned as
        None. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link element.
        PropName (input): The name of the frequency dependent link property assigned to the
            link element.
        """
        _r = self._raw.GetPropertyFD(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetPropertyFD falhou (ret={_r})".format(_r=_r))
        return None

    def GetProperty(self, Name: str, PropName: str):
        """This function retrieves the property assignment to a link element. The function returns zero
        if the property data is successfully retrieved; otherwise it returns a nonzero
        value. The sVarTotalLength and sVarRelStartLoc items apply only when the Var item is
        True.
    
        Name (input): The name of an existing link element.
        PropName (input): The name of the link property assigned to the link element.
        """
        _r = self._raw.GetProperty(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def GetTransformationMatrix(self, Name: str):
        """The function returns zero if the transformation matrix is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing link element.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the link element local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array, (Local1, Local2, Local3)
            are an item (such as a load) in the element local coordinate system, and
            (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkElm.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


