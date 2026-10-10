"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_CableObj:
    """Wrapper para SapModel.CableObj."""

    def __init__(self, raw):
        self._raw = raw

    def AddByCoord(self, xi: float, yi: float, zi: float, xj: float, yj: float, zj: float, PropName: str = 'Default', UserName: str = '', CSys: str = 'Global'):
        """This function adds a new cable object whose end points are at the specified coordinates. The
        function returns zero if the cable object is successfully added, otherwise it
        returns a nonzero value.
    
        Name (output): This is the name that the program ultimately assigns for the cable
            object. If no UserName is specified,n the program assigns a default name to the
            cable object. If a UserName is specified and that name is not used for another
            frame, cable or tendon object, the UserName is assigned to the cable object;
            otherwise a default name is assigned to the cable object.
        PropName (input): This is Default or the name of a defined cable property. If it is
            Default, the program assigns a default cable property to the cable object. If it
            is the name of a defined cable property, that property is assigned to the cable
            object.
        UserName (input): This is an optional user specified name for the cable object. If a
            UserName is specified and that name is already used for another cable object,
            the program ignores the UserName.
        CSys (input): The name of the coordinate system in which the cable object end point
            coordinates are defined.
        """
        _r = self._raw.AddByCoord(xi, yi, zi, xj, yj, zj, "", PropName, UserName, CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.AddByCoord falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def AddByPoint(self, Point1: str, Point2: str, PropName: str = 'Default', UserName: str = ''):
        """This function adds a new cable object whose end points are specified by name. The function
        returns zero if the cable object is successfully added, otherwise it returns a
        nonzero value.
    
        Point1 (input): The name of a defined point object at the I-End of the added cable
            object.
        Point2 (input): The name of a defined point object at the J-End of the added cable
            object.
        Name (output): This is the name that the program ultimately assigns for the cable
            object. If no UserName is specified, the program assigns a default name to the
            cable object. If a UserName is specified and that name is not used for another
            frame, cable or tendon object, the UserName is assigned to the cable object;
            otherwise a default name is assigned to the cable object.
        PropName (input): This is Default or the name of a defined cable property. If it is
            Default, the program assigns a default cable property to the cable object. If it
            is the name of a defined cable property, that property is assigned to the cable
            object.
        UserName (input): This is an optional user specified name for the cable object. If a
            UserName is specified and that name is already used for another cable object,
            the program ignores the UserName.
        """
        _r = self._raw.AddByPoint(Point1, Point2, "", PropName, UserName)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.AddByPoint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value.
    
        Name (input): The existing name of a defined cable object.
        NewName (input): The new name for the cable object.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns a count of the cable objects in the model.
        """
        _r = self._raw.Count()
        return _r

    def DeleteLoadDeformation(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the deformation load assignments to the specified cable objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the cable object specified by the Name item. If this
            item is Group, the load assignments are deleted for all cable objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected cable objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadDeformation(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.DeleteLoadDeformation falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadDistributedWithGUID(self, Name: str, GUID: str):
        """This function deletes the distributed load assignment with the specified global unique ID
        for the specified cable object. The function returns zero if the load assignment is
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object.
        GUID (input): The global unique ID of one of the distributed loads on that cable
            object.
        """
        _r = self._raw.DeleteLoadDistributedWithGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.DeleteLoadDistributedWithGUID falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadDistributed(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the distributed load assignments to the specified cable objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the cable object specified by the Name item. If this
            item is Group, the load assignments are deleted for all cable objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected cable objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadDistributed(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.DeleteLoadDistributed falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadGravity(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the gravity load assignments to the specified cable objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the cable object specified by the Name item. If this
            item is Group, the load assignments are deleted for all cable objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected cable objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadGravity(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.DeleteLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadStrain(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the strain load assignments to the specified cable objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the cable object specified by the Name item. If this
            item is Group, the load assignments are deleted for all cable objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected cable objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadStrain(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.DeleteLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadTargetForce(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the target force assignments to the specified cable objects for the
        specified load pattern. The function returns zero if the target force assignments
        are successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the cable object specified by the Name item. If this
            item is Group, the load assignments are deleted for all cable objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected cable objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadTargetForce(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.DeleteLoadTargetForce falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadTemperature(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the temperature load assignments to the specified cable objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the cable object specified by the Name item. If this
            item is Group, the load assignments are deleted for all cable objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected cable objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadTemperature(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.DeleteLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteMass(self, Name: str, ItemType: int = 0):
        """This function deletes the cable mass assignments for cable objects. The function returns
        zero if the mass assignments are successfully deleted, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the cable mass
            assignments are deleted for the cable object specified by the Name item. If this
            item is Group, the cable mass assignments are deleted for all cable objects in
            the group specified by the Name item. If this item is SelectedObjects, the cable
            mass assignments are deleted for all selected cable objects, and the Name item
            is ignored.
        """
        _r = self._raw.DeleteMass(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.DeleteMass falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteModifiers(self, Name: str, ItemType: int = 0):
        """This function deletes the cable modifier assignments for cable objects. The function returns
        zero if the modifier assignments are successfully deleted, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the cable
            modifier assignments are deleted for the cable object specified by the Name
            item. If this item is Group, the cable modifier assignments are deleted for all
            cable objects in the group specified by the Name item. If this item is
            SelectedObjects, the cable modifier assignments are deleted for all selected
            cable objects, and the Name item is ignored.
        """
        _r = self._raw.DeleteModifiers(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.DeleteModifiers falhou (ret={_r})".format(_r=_r))
        return None

    def Delete(self, Name: str, ItemType: int = 0):
        """The function deletes cable objects. The function returns zero if the cable objects are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the cable
            object specified by the Name item is deleted. If this item is Group, the all
            cable objects in the group specified by the Name item are deleted. If this item
            is SelectedObjects, all selected cable objects are deleted, and the Name item is
            ignored.
        """
        _r = self._raw.Delete(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetCableData(self, UseDeformedGeom: bool, ModelUsingFrames: bool):
        """This function retrieves definition data for a specified cable object. The function returns
        zero if the data is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (output): The name of a defined cable object.
        CableType (output): This is 1, 2, 3, 4, 5, 6, 7, 8, or 9, indicating the cable
            definition parameter. 1 = Minimum tension at I-End 2 = Minimum tension at J-End
            3 = Tension at I-End 4 = Tension at J-End 5 = Horizontal tension component 6 =
            Maximum vertical sag 7 = Low-point vertical sag 8 = Undeformed length 9 =
            Relative undeformed length
        NumSegs (output): This is the number of segments into which the program internally
            divides the cable.
        Weight (output): The added weight per unit length used when calculating the cable
            shape. [F/L]
        ProjectedLoad (output): The projected uniform gravity load used when calculating the
            cable shape. [F/L]
        UseDeformedGeom (input): If this item is True, the program uses the deformed
            geometry for the cable object; otherwise it uses the undeformed geometry.
        ModelUsingFrames (input): If this item is True, the analysis model uses frame
            elements to model the cable instead of using cable elements.
        Parameter (output): This is an array of parameters related to the cable shape. The
            array is dimensioned by Sap2000. Parameter(0) = Tension at I-End [F]
            Parameter(1) = Tension at J-End [F] Parameter(2) = Horizontal tension component
            [F] Parameter(3) = Maximum deformed vertical sag [L] Parameter(4) = Deformed
            low-point vertical sag [L] Parameter(5) = Deformed length [L] Parameter(6) =
            Deformed relative length Parameter(7) = Maximum undeformed vertical sag [L]
            Parameter(8) = Undeformed low-point vertical sag [L] Parameter(9) = Undeformed
            length [L] Parameter(10) = Undeformed relative length
        """
        _r = self._raw.GetCableData("", 0, 0, 0.0, 0.0, UseDeformedGeom, ModelUsingFrames, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetCableData falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCableGeometry(self, CSys: str = 'Global'):
        """This function retrieves geometric data for a specified cable object. The function returns
        zero if the data is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (output): The name of a defined cable object.
        NumberPoints (output): The number of points defining the cable geometry.
        Sag (output): The cable vertical sag, measured from the chord, at the considered
            point. [L]
        RD (output): The relative distance along the cable, measured from the cable I-End,
            to the considered point.
        CSys (input): The name of the coordinate system in which the x, y and z coordinates
            are to be reported.
        """
        _r = self._raw.GetCableGeometry("", 0, [], [], [], [], [], [], CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetCableGeometry falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetElm(self, Name: str):
        """This function retrieves the names of the line elements (analysis model lines) associated
        with a specified cable object in the object-based model. It also retrieves
        information about the location of the line elements along the cable object. This
        function returns zero if the line element information is successfully returned;
        otherwise it returns nonzero. An error occurs if the analysis model does not
        currently exist.
    
        Name (input): The name of an existing cable object.
        nelm (output): The number of line elements created from the specified cable object.
        Elm (output): An array that includes the name of a line element created from the
            specified cable object.
        RDI (output): An array that includes the relative distance along the cable object to
            the I-End of the line element.
        RDJ (output): An array that includes the relative distance along the cable object to
            the J-End of the line element.
        """
        _r = self._raw.GetElm(Name, 0, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetElm falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetGUID(self, name: str):
        """This function retrieves the GUID for the specified cable object. This function returns zero
        if the cable object GUID is successfully retrieved; otherwise it returns nonzero.
    
        GUID (output): The GUID (Global Unique ID) for the specified cable object.
        """
        _r = self._raw.GetGUID(name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetGUID falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGroupAssign(self, Name: str):
        """This function retrieves the names of the groups to which a specified cable object is
        assigned. The function returns zero if the group assignments are successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object.
        NumberGroups (output): The number of group names retrieved.
        Groups (output): The names of the groups to which the cable object is assigned.
        """
        _r = self._raw.GetGroupAssign(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetGroupAssign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDeformation(self, Name: str, ItemType: int = 0):
        """This function retrieves the deformation load assignments to cable objects. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified cable objects.
        CableName (output): This is an array that includes the name of the cable object
            associated with each deformation load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each deformation load.
        U1 (output): This is an array of axial deformation load values. [L]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the cable object specified by the Name item. If this item is
            Group, the assignments are retrieved for all cable objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected cable objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadDeformation(Name, 0, [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetLoadDeformation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDistributed(self, Name: str, ItemType: int = 0):
        """This function retrieves the distributed load assignments to cable objects. The loads are
        uniformly distributed over the full length of cable objects. The function returns
        zero if the load assignments are successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of distributed loads retrieved for the
            specified cable objects.
        CableName (output): This is an array that includes the name of the cable object
            associated with each distributed load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the distributed loads are specified.
        MyType (output): This is an array that includes 1 or 2, indicating the type of
            distributed load. 1 = Force 2 = Moment
        CSys (output): This is an array that includes the name of the coordinate system in
            which each distributed load is defined. It may be Local or the name of a defined
            coordinate system.
        Dir (output): This is 1, 2, 3, 4, 5, 6 or 10, indicating the direction of the load.
            1 = Local 1 axis (only applies when CSys is Local) 2 = Local 2 axis (only
            applies when CSys is Local) 3 = Local 3 axis (only applies when CSys is Local) 4
            = X direction (does not apply when CSys is Local) 5 = Y direction (does not
            apply when CSys is Local) 6 = Z direction (does not apply when CSys is Local) 10
            = Gravity direction (only applies when CSys is Global) The positive gravity
            direction (see Dir = 10) is in the negative Global Z direction.
        Value (output): This is the load value of the distributed load. The distributed load
            is applied over the full length of the cable. [F/L] when MyType is 1 and [FL/L]
            when MyType is 2
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the cable object specified by the Name item. If this item is
            Group, the assignments are retrieved for all cable objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected cable objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadDistributed(Name, 0, [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetLoadDistributed falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadGravity(self, Name: str, ItemType: int = 0):
        """This function retrieves the gravity load assignments to cable objects. The function returns
        zero if the load assignments are successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            cable objects.
        CableName (output): This is an array that includes the name of the cable object
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the cable object specified by the Name item. If this item is
            Group, the assignments are retrieved for all cable objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected cable objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadStrain(self, Name: str, ItemType: int = 0):
        """This function retrieves the strain load assignments to cable objects. The function returns
        zero if the strain load assignments are successfully retrieved, otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of strain loads retrieved for the specified
            cable objects.
        CableName (output): This is an array that includes the name of the cable object
            associated with each strain load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each strain load.
        Strain (output): This is an array that includes the axial strain value. [L/L]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the strain load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the cable object specified by the Name item. If this item is
            Group, the assignments are retrieved for all cable objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected cable objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadStrain(Name, 0, [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetLoadStrain falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTargetForce(self, Name: str, ItemType: int = 0):
        """This function retrieves the target force assignments to cable objects. The function returns
        zero if the target force assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified cable objects.
        CableName (output): This is an array that includes the name of the cable object
            associated with each target force.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each target force.
        P (output): This is an array of axial target force values. [F]
        RD (output): This is an array of the relative distances along the cable objects
            where the axial target force values apply.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the cable object specified by the Name item. If this item is
            Group, the assignments are retrieved for all cable objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected cable objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadTargetForce(Name, 0, [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetLoadTargetForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTemperature(self, Name: str, ItemType: int = 0):
        """This function retrieves the temperature load assignments to cable objects. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of temperature loads retrieved for the
            specified cable objects.
        CableName (output): This is an array that includes the name of the cable object
            associated with each temperature load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each temperature load.
        Val (output): This is an array that includes the temperature load value. [T]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the temperature load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the cable object specified by the Name item. If this item is
            Group, the assignments are retrieved for all cable objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected cable objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadTemperature(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetLoadTemperature falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMass(self, Name: str, MassOverL: float):
        """This function retrieves the mass per unit length assignment for cable objects. The function
        returns zero if the mass assignment is successfully retrieved, otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing cable object.
        MassOverL (input): The mass per unit length assigned to the cable object. [M/L]
        """
        _r = self._raw.GetMass(Name, MassOverL)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetMass falhou (ret={_r})".format(_r=_r))
        return None

    def GetMatTemp(self, Name: str, Temp: float):
        """This function retrieves the material temperature assignments to cable objects. The function
        returns zero if the material temperature assignments are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object.
        Temp (input): This is the material temperature value assigned to the cable object.
            [T]
        PatternName (output): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the cable object is uniform along the object
            at the value specified by Temp. If PatternName is the name of a defined joint
            pattern, the material temperature for the cable object may vary from one end to
            the other. The material temperature at each end of the object is equal to the
            specified temperature multiplied by the pattern value at the joint at the end of
            the cable object.
        """
        _r = self._raw.GetMatTemp(Name, Temp, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetMatTemp falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMaterialOverwrite(self, Name: str):
        """This function retrieves the material overwrite assigned to a cable object, if any. It
        returns None if there is no material overwrite assignment. The function returns zero
        if the material overwrite assignment is successfully retrieved, otherwise it returns
        a nonzero value.
    
        Name (input): The name of a defined cable object.
        PropName (output): This is None, indicating that no material overwrite exists for
            the specified cable object, or it is the name of an existing material property.
        """
        _r = self._raw.GetMaterialOverwrite(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetMaterialOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetModifiers(self, Name: str):
        """This function retrieves the cable modifier assignment for cable objects. The default value
        for all modifiers is one. The function returns zero if the modifier assignments are
        successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object.
        Value (output): This is an array of three unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Mass modifier Value(2) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined cable objects. The function returns zero if
        the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of cable object names retrieved by the program.
        MyName (output): This is a one-dimensional array of cable object names. The MyName
            array is created as a dynamic, zero-based, array by the APIuser: Dim MyName() as
            String The array is dimensioned to (NumberNames 1) inside the Sap2000 program,
            filled with the names, and returned to the APIuser.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOutputStations(self, Name: str, NoOutPutAndDesignAtElementEnds: bool, NoOutPutAndDesignAtPointLoads: bool):
        """This function retrieves cable object output station data. The function returns zero if the
        data is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object.
        MyType (output): This is 1 or 2, indicating how the output stations are specified. 1
            = maximum segment size, that is, maximum station spacing 2 = minimum number of
            stations
        MaxSegSize (output): The maximum segment size, that is, the maximum station spacing.
            This item applies only when MyType = 1. [L]
        MinSections (output): The minimum number of stations. This item applies only when
            MyType = 2.
        NoOutPutAndDesignAtElementEnds (input): If this item is True, no additional output
            stations are added at the ends of line elements when the cable object is
            internally meshed.
        NoOutPutAndDesignAtPointLoads (input): If this item is True, no additional output
            stations are added at point load locations.
        """
        _r = self._raw.GetOutputStations(Name, 0, 0.0, 0, NoOutPutAndDesignAtElementEnds, NoOutPutAndDesignAtPointLoads)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetOutputStations falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoints(self, Name: str):
        """This function retrieves the names of the point objects at each end of a specified cable
        object. The function returns zero if the point names are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of a defined cable object.
        Point1 (output): The name of the point object at the I-End of the specified cable
            object.
        Point2 (output): The name of the point object at the J-End of the specified cable
            object.
        """
        _r = self._raw.GetPoints(Name, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetProperty(self, Name: str, PropName: str):
        """This function retrieves the cable property assigned to a cable object. The function returns
        zero if the cable object property is successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of a defined cable object.
        PropName (input): The name of the cable property assigned to the cable object.
        """
        _r = self._raw.GetProperty(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def GetSelected(self, Name: str):
        """This function retrieves the selected status for a cable object. The function returns zero if
        the selected status is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object.
        Selected (output): This item returns True if the specified cable object is selected,
            otherwise it returns False.
        """
        _r = self._raw.GetSelected(Name, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetSelected falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetTransformationMatrix(self, Name: str, IsGlobal: bool = True):
        """The function returns zero if the cable object transformation matrix is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the cable object local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array, (Local1, Local2, Local3)
            are an item (such as a load) in the object local coordinate system, and
            (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.
            The transformation from the local coordinate system to the present coordinate
            system is the same as that shown above for the global system if you substitute
            the present system for the global system.
        IsGlobal (input): If this item is True, the transformation matrix is between the
            Global coordinate system and the cable object local coordinate system. If this
            item is False, the transformation matrix is between the present coordinate
            system and the cable object local coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [], IsGlobal)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CableObj.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetCableData(self, Name: str, CableType: int, NumSegs: int, Weight: float, ProjectedLoad: float, Value: float, UseDeformedGeom: bool = False, ModelUsingFrames: bool = False):
        """This function assigns the cable definition parameters to a cable object. The function
        returns zero if the cable object is successfully defined; otherwise it returns a
        nonzero value. If the cable object is not successfully defined, it may be deleted.
    
        Name (input): The name of a defined cable object.
        CableType (input): This is 1, 2, 3, 4, 5, 6, 7, 8, or 9, indicating the cable
            definition parameter. 1 = Minimum tension at I-End 2 = Minimum tension at J-End
            3 = Tension at I-End 4 = Tension at J-End 5 = Horizontal tension component 6 =
            Maximum vertical sag 7 = Low-point vertical sag 8 = Undeformed length 9 =
            Relative undeformed length
        NumSegs (input): This is the number of segments into which the program internally
            divides the cable.
        Weight (input): The added weight per unit length used when calculating the cable
            shape. [F/L]
        ProjectedLoad (input): The projected uniform gravity load used when calculating the
            cable shape. [F/L]
        Value (input): This is the value of the parameter used to define the cable shape.
            The item that Value represents depends on the CableType item. CableType = 1: Not
            Used CableType = 2: Not Used CableType = 3: Tension at I-End [F] CableType = 4:
            Tension at J-End [F] CableType = 5: Horizontal tension component [F] CableType =
            6: Maximum vertical sag [L] CableType = 7: Low-point vertical sag [L] CableType
            = 8: Undeformed length [L] CableType = 9: Relative undeformed length
        UseDeformedGeom (input): If this item is True, the program uses the deformed
            geometry for the cable object; otherwise it uses the undeformed geometry.
        ModelUsingFrames (input): If this item is True, the analysis model uses frame
            elements to model the cable instead of using cable elements.
        """
        _r = self._raw.SetCableData(Name, CableType, NumSegs, Weight, ProjectedLoad, Value, UseDeformedGeom, ModelUsingFrames)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetCableData falhou (ret={_r})".format(_r=_r))
        return None

    def SetGUID(self, Name: str, GUID: str = ''):
        """This function sets the GUID for the specified cable object. If the GUID is passed in as a
        blank string, the program automatically creates a GUID for the object. This function
        returns zero if the cable object GUID is successfully set; otherwise it returns
        nonzero.
    
        Name (input): The name of an existing cable object.
        GUID (input): The GUID (Global Unique ID) for the specified cable object.
        """
        _r = self._raw.SetGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetGUID falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroupAssign(self, Name: str, GroupName: str, Remove: bool, ItemType: int = 0):
        """This function adds or removes cable objects from a specified group. The function returns
        zero if the group assignment is successful, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        GroupName (input): The name of an existing group to which the assignment is made.
        Remove (input): If this item is False, the specified cable objects are added to the
            group specified by the GroupName item. If it is True, the cable objects are
            removed from the group.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the cable
            object specified by the Name item is added or removed from the group specified
            by the GroupName item. If this item is Group, all cable objects in the group
            specified by the Name item are added or removed from the group specified by the
            GroupName item. If this item is SelectedObjects, all selected cable objects are
            added or removed from the group specified by the GroupName item, and the Name
            item is ignored.
        """
        _r = self._raw.SetGroupAssign(Name, GroupName, Remove, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetGroupAssign falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadDeformation(self, Name: str, LoadPat: str, d: float, ItemType: int = 0):
        """This function assigns deformation loads to cable objects. The function returns zero if the
        loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        d (input): This is the axial deformation load value. [L]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadDeformation(Name, LoadPat, d, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetLoadDeformation falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadDistributed(self, Name: str, LoadPat: str, MyType: int, Dir: int, Value: float, CSys: str = 'Global', Replace: bool = True, ItemType: int = 0):
        """This function assigns uniform distributed loads over the full length of cable objects. The
        function returns zero if the loads are successfully assigned, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        MyType (input): This is 1 or 2, indicating the type of distributed load. 1 = Force
            per unit length 2 = Moment per unit length
        Dir (input): This is 1, 2, 3, 4, 5, 6 or 10, indicating the direction of the load. 1
            = Local 1 axis (only applies when CSys is Local) 2 = Local 2 axis (only applies
            when CSys is Local) 3 = Local 3 axis (only applies when CSys is Local) 4 = X
            direction (does not apply when CSys is Local) 5 = Y direction (does not apply
            when CSys is Local) 6 = Z direction (does not apply when CSys is Local) 10 =
            Gravity direction (only applies when CSys is Global) The positive gravity
            direction (see Dir = 10) is in the negative Global Z direction.
        Value (input): This is the load value of the distributed load. The distributed load
            is applied over the full length of the cable. [F/L] when MyType is 1 and [FL/L]
            when MyType is 2
        CSys (input): This is Local or the name of a defined coordinate system. It is the
            coordinate system in which the loads are specified.
        Replace (input): If this item is True, all previous loads, if any, assigned to the
            specified cable object(s), in the specified load pattern, are deleted before
            making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadDistributed(Name, LoadPat, MyType, Dir, Value, CSys, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetLoadDistributed falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadGravity(self, Name: str, LoadPat: str, x: float, y: float, z: float, Replace: bool = True, CSys: str = 'Global', ItemType: int = 0):
        """This function assigns gravity load multipliers to cable objects. The function returns zero
        if the loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Replace (input): If this item is True, all previous gravity loads, if any, assigned
            to the specified cable object(s), in the specified load pattern, are deleted
            before making the new assignment.
        CSys (input): The coordinate system in which the x, y and z multipliers are
            specified.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadGravity(Name, LoadPat, x, y, z, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadStrain(self, Name: str, LoadPat: str, Strain: float, Replace: bool = True, PatternName: str = '', ItemType: int = 0):
        """This function assigns strain loads to cable objects. The function returns zero if the loads
        are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Strain (input): This is the axial strain load value. [L/L]
        Replace (input): If this item is True, all previous strain loads, if any, assigned
            to the specified cable object(s), in the specified load pattern, are deleted
            before making the new assignment.
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the strain load for the cable object is uniform along the object at the
            value specified by Strain. If PatternName is the name of a defined joint
            pattern, the strain load for the cable object is based on the specified strain
            value multiplied by the pattern value at the joints at each end of the cable
            object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadStrain(Name, LoadPat, Strain, Replace, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadTargetForce(self, Name: str, LoadPat: str, P: float, RD: float, ItemType: int = 0):
        """This function assigns target forces to cable objects. The function returns zero if the
        target forces are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        P (input): This is the axial target force value. [F]
        RD (input): This is the relative distance along the cable object to the location
            where the target force value applies. The relative distance must be between 0
            and 1, 0 <= RD <=1.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadTargetForce(Name, LoadPat, P, RD, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetLoadTargetForce falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadTemperature(self, Name: str, LoadPat: str, Val: float, PatternName: str = '', Replace: bool = True, ItemType: int = 0):
        """This function assigns temperature loads to cable objects. The function returns zero if the
        loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Val (input): This is the temperature change value. [T]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the temperature load for the cable object is uniform along the object at
            the value specified by Val. If PatternName is the name of a defined joint
            pattern, the temperature load for the cable object is based on the specified
            temperature value multiplied by the pattern value at the joints at each end of
            the cable object.
        Replace (input): If this item is True, all previous temperature loads, if any,
            assigned to the specified cable object(s), in the specified load case, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadTemperature(Name, LoadPat, Val, PatternName, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def SetMass(self, Name: str, MassOverL: float, Replace: bool = False, ItemType: int = 0):
        """This function assigns mass per unit length to cable objects. The function returns zero if
        the mass is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        MassOverL (input): The mass per unit length assigned to the cable object. [M/L]
        Replace (input): If this item is True, all existing mass assignments to the cable
            object are removed before assigning the specified mas. If it is False, the
            specified mass is added to any mass already assigned to the cable object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetMass(Name, MassOverL, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetMass falhou (ret={_r})".format(_r=_r))
        return None

    def SetMatTemp(self, Name: str, Temp: float, PatternName: str = '', ItemType: int = 0):
        """This function assigns material temperatures to cable objects. The function returns zero if
        the material temperatures are successfully assigned, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        Temp (input): This is the material temperature value assigned to the cable object.
            [T]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the cable object is uniform along the object
            at the value specified by Temp. If PatternName is the name of a defined joint
            pattern, the material temperature for the cable object may vary from one end to
            the other. The material temperature at each end of the object is equal to the
            specified temperature multiplied by the pattern value at the joint at the end of
            the cable object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetMatTemp(Name, Temp, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetMatTemp falhou (ret={_r})".format(_r=_r))
        return None

    def SetMaterialOverwrite(self, Name: str, PropName: str, ItemType: int = 0):
        """This function sets the material overwrite assignment for cable objects. The function returns
        zero if the material overwrite assignment is successfully assigned, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        PropName (input): This is None or a blank string, indicating that any existing
            material overwrites assigned to the specified cable objects are to be removed,
            or it is the name of an existing material property.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetMaterialOverwrite(Name, PropName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetMaterialOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetModifiers(self, Name: str, Value: list[float], ItemType: int = 0):
        """This function sets the cable modifier assignment for cable objects. The default value for
        all modifiers is one. The function returns zero if the modifier assignments are
        successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        Value (input): This is an array of three unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Mass modifier Value(2) = Weight modifier
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetModifiers(Name, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetModifiers falhou (ret={_r})".format(_r=_r))
        return None

    def SetOutputStations(self, Name: str, MyType: int, MaxSegSize: float, MinSections: int, NoOutPutAndDesignAtElementEnds: bool = None, NoOutPutAndDesignAtPointLoads: bool = None, ItemType: int = 0):
        """This function assigns cable object output station data. The function returns zero if the
        data is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        MyType (input): This is 1 or 2, indicating how the output stations are specified. 1
            = maximum segment size, that is, maximum station spacing 2 = minimum number of
            stations
        MaxSegSize (input): The maximum segment size, that is, the maximum station spacing.
            This item applies only when MyType = 1. [L]
        MinSections (input): The minimum number of stations. This item applies only when
            MyType = 2.
        NoOutPutAndDesignAtElementEnds (input): If this item is True, no additional output
            stations are added at the ends of line elements when the cable object is
            internally meshed.
        NoOutPutAndDesignAtPointLoads (input): If this item is True, no additional output
            stations are added at point load locations.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOutputStations(Name, MyType, MaxSegSize, MinSections, NoOutPutAndDesignAtElementEnds, NoOutPutAndDesignAtPointLoads, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetOutputStations falhou (ret={_r})".format(_r=_r))
        return None

    def SetProperty(self, name: str, PropName: str, ItemType: int = 0):
        """This function assigns a cable property to a cable object. The function returns zero if the
        cable property is successfully assigned, otherwise it returns a nonzero value.
    
        PropName (input): The name of a cable property to be assigned to the specified cable
            object(s).
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the cable object specified by the Name item. If this item is Group,
            the assignment is made to all cable objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected cable
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetProperty(name, PropName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def SetSelected(self, Name: str, Selected: bool, ItemType: int = 0):
        """This function sets the selected status for a cable object. The function returns zero if the
        selected status is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cable object or group, depending on the value
            of the ItemType item.
        Selected (input): This item is True if the specified cable object is selected,
            otherwise it is False.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the selected
            status is set for the cable object specified by the Name item. If this item is
            Group, the selected status is set for all cable objects in the group specified
            by the Name item. If this item is SelectedObjects, the selected status is set
            for all selected cable objects, and the Name item is ignored.
        """
        _r = self._raw.SetSelected(Name, Selected, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CableObj.SetSelected falhou (ret={_r})".format(_r=_r))
        return None


