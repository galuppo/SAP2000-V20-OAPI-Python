"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_LinkObj:
    """Wrapper para SapModel.LinkObj."""

    def __init__(self, raw):
        self._raw = raw

    def AddByCoord(self, xi: float, yi: float, zi: float, xj: float, yj: float, zj: float, IsSingleJoint: bool = False, PropName: str = 'Default', UserName: str = '', CSys: str = 'Global'):
        """This function adds a new link object whose end points are at the specified coordinates. The
        function returns zero if the link object is successfully added; otherwise it returns
        a nonzero value.
    
        Name (output): This is the name that the program ultimately assigns for the link
            object. If no UserName is specified, the program assigns a default name to the
            link object. If a UserName is specified and that name is not used for another
            link object, the UserName is assigned to the link object; otherwise a default
            name is assigned to the link object.
        IsSingleJoint (input): This item is True if a one-joint link is added and False if a
            two-joint link is added.
        PropName (input): This is either Default or the name of a defined link property. If
            it is Default the program assigns a default link property to the link object. If
            it is the name of a defined link property, that property is assigned to the link
            object.
        UserName (input): This is an optional user specified name for the link object. If a
            UserName is specified and that name is already used for another link object, the
            program ignores the UserName.
        CSys (input): The name of the coordinate system in which the link object end point
            coordinates are defined.
        """
        _r = self._raw.AddByCoord(xi, yi, zi, xj, yj, zj, "", IsSingleJoint, PropName, UserName, CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.AddByCoord falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def AddByPoint(self, Point1: str, Point2: str, IsSingleJoint: bool = False, PropName: str = 'Default', UserName: str = ''):
        """This function adds a new link object whose end points are specified by name. The function
        returns zero if the link object is successfully added; otherwise it returns a
        nonzero value.
    
        Point1 (input): The name of a defined point object at the I-End of the added link
            object.
        Point2 (input): The name of a defined point object at the J-End of the added link
            object. This item is ignored if the IsSingleJoint item is True.
        Name (output): This is the name that the program ultimately assigns for the link
            object. If no UserName is specified, the program assigns a default name to the
            link object. If a UserName is specified and that name is not used for another
            link object, the UserName is assigned to the link object; otherwise a default
            name is assigned to the link object.
        IsSingleJoint (input): This item is True if a one-joint link is added and False if a
            two-joint link is added.
        PropName (input): This is either Default or the name of a defined link property. If
            it is Default the program assigns a default link property to the link object. If
            it is the name of a defined link property, that property is assigned to the link
            object.
        UserName (input): This is an optional user specified name for the link object. If a
            UserName is specified and that name is already used for another link object, the
            program ignores the UserName.
        """
        _r = self._raw.AddByPoint(Point1, Point2, "", IsSingleJoint, PropName, UserName)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.AddByPoint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ChangeName(self, Name: str, NewName: str):
        """This function applies a new name to an link object. The function returns zero if the new
        name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined link object.
        NewName (input): The new name for the link object.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns a count of the link objects in the model.
        """
        _r = self._raw.Count()
        return _r

    def DeleteLoadDeformation(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the deformation load assignments to the specified link objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the link object specified by the Name item. If this
            item is Group, the load assignments are deleted for all link objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected link objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadDeformation(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.DeleteLoadDeformation falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadGravity(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the gravity load assignments to the specified link objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the link object specified by the Name item. If this
            item is Group, the load assignments are deleted for all link objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected link objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadGravity(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.DeleteLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadTargetForce(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the target force assignments to the specified link objects for the
        specified load pattern. The function returns zero if the target force assignments
        are successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the link object specified by the Name item. If this
            item is Group, the load assignments are deleted for all link objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected link objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadTargetForce(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.DeleteLoadTargetForce falhou (ret={_r})".format(_r=_r))
        return None

    def Delete(self, Name: str, ItemType: int = 0):
        """The function deletes link objects. The function returns zero if the link objects are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the link object
            specified by the Name item is deleted. If this item is Group, the all link
            objects in the group specified by the Name item are deleted. If this item is
            SelectedObjects, all selected link objects are deleted, and the Name item is
            ignored.
        """
        _r = self._raw.Delete(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetElm(self, Name: str):
        """This function retrieves the name of the link element (analysis model link) associated with a
        specified link object in the object-based model. This function returns zero if the
        link element name is successfully retrieved; otherwise it returns nonzero. An error
        occurs if the analysis model does not exist.
    
        Name (input): The name of an existing link object.
        Elm (output): The name of the link element created from the specified link object.
        """
        _r = self._raw.GetElm(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetElm falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGUID(self, name: str):
        """This function retrieves the GUID for the specified link object. This function returns zero
        if the link object GUID is successfully retrieved; otherwise it returns nonzero.
    
        GUID (output): The GUID (Global Unique ID) for the specified link object.
        """
        _r = self._raw.GetGUID(name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetGUID falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGroupAssign(self, Name: str):
        """This function retrieves the names of the groups to which a specified link object is
        assigned. The function returns zero if the group assignments are successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object.
        NumberGroups (output): The number of group names retrieved.
        Groups (output): The names of the groups to which the link object is assigned.
        """
        _r = self._raw.GetGroupAssign(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetGroupAssign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDeformation(self, Name: str, ItemType: int = 0):
        """This function retrieves the deformation load assignments to link objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified link objects.
        LinkName (output): This is an array that includes the name of the link object
            associated with each deformation load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each deformation load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the link object specified by the Name item. If this item is
            Group, the assignments are retrieved for all link objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected link objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadDeformation(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetLoadDeformation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadGravity(self, Name: str, ItemType: int = 0):
        """This function retrieves the gravity load assignments to link objects. The function returns
        zero if the load assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            link objects.
        LinkName (output): This is an array that includes the name of the link object
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the link object specified by the Name item. If this item is
            Group, the assignments are retrieved for all link objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected link objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTargetForce(self, Name: str, ItemType: int = 0):
        """This function retrieves the target force assignments to link objects. The function returns
        zero if the target force assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified link objects.
        LinkName (output): This is an array that includes the name of the link object
            associated with each target force.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each target force.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the link object specified by the Name item. If this item is
            Group, the assignments are retrieved for all link objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected link objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadTargetForce(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetLoadTargetForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxesAdvanced(self, Name: str):
        """This function assigns advanced local axes to link objects. The function returns zero if the
        advanced local axes assignments are assigned successfully; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing link object.
        Active (output): This is True if advanced local axes exist.
        Plane2 (output): This is 12 or 13, indicating that the local plane determined by the
            plane reference vector is the 1-2 or 1-3 plane. This item applies only when the
            Active item is True.
        """
        _r = self._raw.GetLocalAxesAdvanced(Name, False, 0, "", [], [], [], 0, 0, "", [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetLocalAxesAdvanced falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str, Advanced: bool):
        """This function retrieves the local axis angle assignment for link objects. The function
        returns zero if the assignment is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing link object.
        Ang (output): This is the angle that the local 2 and 3 axes are rotated about the
            positive local 1 axis, from the default orientation or, if the Advanced item is
            True, from the orientation determined by the plane reference vector. The
            rotation for a positive angle appears counter clockwise when the local +1 axis
            is pointing toward you. [deg]
        Advanced (input): This item is True if the link object local axes orientation was
            obtained using advanced local axes parameters.
        """
        _r = self._raw.GetLocalAxes(Name, 0.0, Advanced)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined link objects. The function returns zero if
        the names are successfully retrieved; otherwise it returns nonzero.
    
        NumberNames (output): The number of link object names retrieved by the program.
        MyName (output): This is a one-dimensional array of link object names. The MyName
            array is created as a dynamic, zero-based, array by the APIuser: Dim MyName() as
            String The array is dimensioned to (NumberNames 1) inside the SAP2000 program,
            filled with the names, and returned to the APIuser.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoints(self, Name: str):
        """This function retrieves the names of the point objects at each end of a specified link
        object. If names of the two point objects are the same, the specified link object is
        a one-joint link object. The function returns zero if the point names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a defined link object.
        Point1 (output): The name of the point object at the I-End of the specified link
            object.
        Point2 (output): The name of the point object at the J-End of the specified link
            object.
        """
        _r = self._raw.GetPoints(Name, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPropertyFD(self, Name: str, PropName: str):
        """This function retrieves the frequency dependent link property assigned to a link object. The
        function returns zero if the property is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a defined link object.
        PropName (input): The name of the frequency dependent link property assigned to the
            link object. This item is None if there is no frequency dependent link property
            assigned to the link object.
        """
        _r = self._raw.GetPropertyFD(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetPropertyFD falhou (ret={_r})".format(_r=_r))
        return None

    def GetProperty(self, Name: str, PropName: str):
        """This function retrieves the link property assigned to a link object. The function returns
        zero if the property is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of a defined link object.
        PropName (input): The name of the link property assigned to the link object.
        """
        _r = self._raw.GetProperty(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def GetSelected(self, Name: str, Selected: bool):
        """This function retrieves the selected status for a link object. The function returns zero if
        the selected status is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object.
        Selected (input): This item is True if the specified link object is selected;
            otherwise it is False.
        """
        _r = self._raw.GetSelected(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetSelected falhou (ret={_r})".format(_r=_r))
        return None

    def GetTransformationMatrix(self, Name: str, IsGlobal: bool = True):
        """The function returns zero if the link object transformation matrix is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the link object local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array, (Local1, Local2, Local3)
            are an item (such as a load) in the object local coordinate system, and
            (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.
            The transformation from the local coordinate system to the present coordinate
            system is the same as that shown above for the global system if you substitute
            the present system for the global system.
        IsGlobal (input): If this item is True, the transformation matrix is between the
            Global coordinate system and the link object local coordinate system. If this
            item is False, the transformation matrix is between the present coordinate
            system, and the link object local coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [], IsGlobal)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LinkObj.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetGUID(self, Name: str, GUID: str = ''):
        """This function sets the GUID for the specified link object. If the GUID is passed in as a
        blank string, the program automatically creates a GUID for the object. This function
        returns zero if the link object GUID is successfully set; otherwise it returns
        nonzero.
    
        Name (input): The name of an existing link object.
        GUID (input): The GUID (Global Unique ID) for the specified link object.
        """
        _r = self._raw.SetGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetGUID falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroupAssign(self, Name: str, GroupName: str, Remove: bool, ItemType: int = 0):
        """This function adds or removes link objects from a specified group. The function returns zero
        if the group assignment is successful; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        GroupName (input): The name of an existing group to which the assignment is made.
        Remove (input): If this item is False, the specified link objects are added to the
            group specified by the GroupName item. If it is True, the link objects are
            removed from the group.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the link object
            specified by the Name item is added or removed from the group specified by the
            GroupName item. If this item is Group, all link objects in the group specified
            by the Name item are added or removed from the group specified by the GroupName
            item. If this item is SelectedObjects, all selected link objects are added or
            removed from the group specified by the GroupName item, and the Name item is
            ignored.
        """
        _r = self._raw.SetGroupAssign(Name, GroupName, Remove, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetGroupAssign falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadDeformation(self, Name: str, LoadPat: str, DOF: list[bool], d: list[float], ItemType: int = 0):
        """This function assigns deformation loads to link objects. The function returns zero if the
        loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        DOF (input): This is a array of boolean values indicating if the considered degree
            of freedom has a deformation load. DOF(1) = U1 DOF(2) = U2 DOF(3) = U3 DOF(4) =
            R1 DOF(5) = R2 DOF(6) = R3
        d (input): This is a array of deformation load values. The deformations specified
            for a given degree of freedom are applied only if the corresponding DOF item for
            that degree of freedom is True. d(1) = U1 deformation [L] d(2) = U2 deformation
            [L] d(3) = U3 deformation [L] d(4) = R1 deformation [rad] d(5) = R2 deformation
            [rad] d(6) = R3 deformation [rad]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the link object specified by the Name item. If this item is Group,
            the assignment is made to all link objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected link
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadDeformation(Name, LoadPat, DOF, d, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetLoadDeformation falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadGravity(self, Name: str, LoadPat: str, x: float, y: float, z: float, Replace: bool = True, CSys: str = 'Global', ItemType: int = 0):
        """This function assigns gravity load multipliers to link objects. The function returns zero if
        the loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Replace (input): If this item is True, all previous gravity loads, if any, assigned
            to the specified link object(s), in the specified load pattern, are deleted
            before making the new assignment.
        CSys (input): The coordinate system in which the x, y and z multipliers are
            specified.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the link object specified by the Name item. If this item is Group,
            the assignment is made to all link objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected link
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadGravity(Name, LoadPat, x, y, z, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadTargetForce(self, Name: str, LoadPat: str, DOF: list[bool], f: list[float], RD: list[float], ItemType: int = 0):
        """This function assigns target forces to frame objects. The function returns zero if the
        target forces are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        DOF (input): This is a array of boolean values indicating if the considered degree
            of freedom has a target force. DOF(1) = P DOF(2) = V2 DOF(3) = V3 DOF(4) = T
            DOF(5) = M2 DOF(6) = M3
        f (input): This is a array of target force values. The target forces specified for a
            given degree of freedom are applied only if the corresponding DOF item for that
            degree of freedom is True. f(1) = P [F] f(2) = V2 [F] f(3) = V3 [F] f(4) = T
            [FL] f(5) = M2 [FL] f(6) = M3 [FL]
        RD (input): This is a array of relative distances along the link objects where the
            target force values apply. The relative distances specified for a given degree
            of freedom are applicable only if the corresponding DOF item for that degree of
            freedom is True. The relative distance must be between 0 and 1, 0 <= RD <=1.
            RD(1) = relative location for P target force RD(2) = relative location for V2
            target force RD(3) = relative location for V3 target force RD(4) = relative
            location for T target force RD(5) = relative location for M2 target force RD(6)
            = relative location for M3 target force
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the link object specified by the Name item. If this item is Group,
            the assignment is made to all link objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected link
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadTargetForce(Name, LoadPat, DOF, f, RD, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetLoadTargetForce falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxesAdvanced(self, Name: str, Active: bool, AxVectOpt: int, AxCSys: str, AxDir: list[int], AxPt: list[str], AxVect: list[float], Plane2: int, PlVectOpt: int, PlCSys: str, PlDir: list[int], PlPt: list[str], PlVect: list[float], ItemType: int = 0):
        """This function assigns advanced local axes to link objects. The function returns zero if the
        advanced local axes assignments are assigned successfully; otherwise, it returns a
        nonzero value.
    
        Name (input): The name of an existing link object or group depending on the value of
            the ItemType item.
        Active (input): This is True if advanced local axes exist.
        Plane2 (input): This is 12 or 13, indicating that the local plane determined by the
            plane reference vector is the 1-2 or 1-3 plane. This item applies only when the
            Active item is True.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 Selection = 2 If this item is Object, the assignment is
            made to the link object specified by the Name item. If this item is Group, the
            assignment is made to all link objects in the group specified by the Name item.
            If this item is Selection, assignment is made to all selected link objects and
            the Name item is ignored.
        """
        _r = self._raw.SetLocalAxesAdvanced(Name, Active, AxVectOpt, AxCSys, AxDir, AxPt, AxVect, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetLocalAxesAdvanced falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxes(self, Name: str, Ang: float, ItemType: int = 0):
        """This function assigns a local axis angle to link objects. The function returns zero if the
        local axis angle is successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        Ang (input): This is the angle that the local 2 and 3 axes are rotated about the
            positive local 1 axis, from the default orientation or, if the Advanced item is
            True, from the orientation determined by the plane reference vector. The
            rotation for a positive angle appears counter clockwise when the local +1 axis
            is pointing toward you. [deg]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the link object specified by the Name item. If this item is Group,
            the assignment is made to all link objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected link
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLocalAxes(Name, Ang, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetLocalAxes falhou (ret={_r})".format(_r=_r))
        return None

    def SetPropertyFD(self, name: str, PropName: str, ItemType: int = 0):
        """This function assigns a frequency dependent link property to link objects. The function
        returns zero if the property is successfully assigned; otherwise it returns a
        nonzero value.
    
        PropName (input): This is either None or the name of a frequency dependent link
            property to be assigned to the specified link object(s). None means that no
            frequency dependent link property is assigned to the link object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the link object specified by the Name item. If this item is Group,
            the assignment is made to all link objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected link
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetPropertyFD(name, PropName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetPropertyFD falhou (ret={_r})".format(_r=_r))
        return None

    def SetProperty(self, name: str, PropName: str, ItemType: int = 0):
        """This function assigns a link property to link objects. The function returns zero if the
        property is successfully assigned; otherwise it returns a nonzero value.
    
        PropName (input): This is the name of a link property to be assigned to the
            specified link object(s).
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the link object specified by the Name item. If this item is Group,
            the assignment is made to all link objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected link
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetProperty(name, PropName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def SetSelected(self, Name: str, Selected: bool, ItemType: int = 0):
        """This function sets the selected status for link objects. The function returns zero if the
        selected status is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link object or group, depending on the value
            of the ItemType item.
        Selected (input): This item is True if the specified link object is selected;
            otherwise it is False.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the selected
            status is set for the link object specified by the Name item. If this item is
            Group, the selected status is set for all link objects in the group specified by
            the Name item. If this item is SelectedObjects, the selected status is set for
            all selected link objects, and the Name item is ignored.
        """
        _r = self._raw.SetSelected(Name, Selected, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LinkObj.SetSelected falhou (ret={_r})".format(_r=_r))
        return None


