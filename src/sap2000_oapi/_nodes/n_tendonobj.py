"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_TendonObj:
    """Wrapper para SapModel.TendonObj."""

    def __init__(self, raw):
        self._raw = raw

    def AddByCoord(self, xi: float, yi: float, zi: float, xj: float, yj: float, zj: float, PropName: str = 'Default', UserName: str = '', CSys: str = 'Global'):
        """This function adds a new tendon object whose end points are at the specified coordinates.
        The function returns zero if the tendon object is successfully added, otherwise it
        returns a nonzero value.
    
        Name (output): This is the name that the program ultimately assigns for the tendon
            object. If no UserName is specified, the program assigns a default name to the
            tendon object. If a UserName is specified and that name is not used for another
            frame, cable or tendon object, the UserName is assigned to the tendon object;
            otherwise a default name is assigned to the tendon object.
        PropName (input): This is Default, None or the name of a defined tendon property. If
            it is Default, the program assigns a default tendon property to the tendon
            object. If it is None, no tendon property is assigned to the tendon object. If
            it is the name of a defined tendon property, that property is assigned to the
            tendon object.
        UserName (input): This is an optional user specified name for the tendon object. If
            a UserName is specified and that name is already used for another tendon object,
            the program ignores the UserName.
        CSys (input): The name of the coordinate system in which the tendon object end point
            coordinates are defined.
        """
        _r = self._raw.AddByCoord(xi, yi, zi, xj, yj, zj, "", PropName, UserName, CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.AddByCoord falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def AddByPoint(self, Point1: str, Point2: str, PropName: str = 'Default', UserName: str = ''):
        """This function adds a new tendon object whose end points are specified by name. The function
        returns zero if the tendon object is successfully added, otherwise it returns a
        nonzero value.
    
        Point1 (input): The name of a defined point object at the I-End of the added tendon
            object.
        Point2 (input): The name of a defined point object at the J-End of the added tendon
            object.
        Name (output): This is the name that the program ultimately assigns for the tendon
            object. If no UserName is specified, the program assigns a default name to the
            tendon object. If a UserName is specified and that name is not used for another
            frame, cable or tendon object, the UserName is assigned to the tendon object;
            otherwise a default name is assigned to the tendon object.
        PropName (input): This is Default, None or the name of a defined tendon property. If
            it is Default, the program assigns a default tendon property to the tendon
            object. If it is None, no tendon property is assigned to the tendon object. If
            it is the name of a defined tendon property, that property is assigned to the
            tendon object.
        UserName (input): This is an optional user specified name for the tendon object. If
            a UserName is specified and that name is already used for another tendon object,
            the program ignores the UserName.
        """
        _r = self._raw.AddByPoint(Point1, Point2, "", PropName, UserName)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.AddByPoint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value.
    
        Name (input): The existing name of a defined tendon object.
        NewName (input): The new name for the tendon object.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns a count of the tendon objects in the model.
        """
        _r = self._raw.Count()
        return _r

    def DeleteLoadDeformation(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the deformation load assignments to the specified tendon objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the tendon object specified by the Name item. If
            this item is Group, the load assignments are deleted for all tendon objects in
            the group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected tendon objects and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadDeformation(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.DeleteLoadDeformation falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadForceStress(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the tendon force/stress load assignments to the specified tendon
        objects for the specified load pattern. The function returns zero if the load
        assignments are successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the tendon object specified by the Name item. If
            this item is Group, the load assignments are deleted for all tendon objects in
            the group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected tendon objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadForceStress(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.DeleteLoadForceStress falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadGravity(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the gravity load assignments to the specified tendon objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the tendon object specified by the Name item. If
            this item is Group, the load assignments are deleted for all tendon objects in
            the group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected tendon objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadGravity(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.DeleteLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadStrain(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the strain load assignments to the specified tendon objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the tendon object specified by the Name item. If
            this item is Group, the load assignments are deleted for all tendon objects in
            the group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected tendon objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadStrain(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.DeleteLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadTemperature(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the temperature load assignments to the specified tendon objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the tendon object specified by the Name item. If
            this item is Group, the load assignments are deleted for all tendon objects in
            the group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected tendon objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadTemperature(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.DeleteLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def Delete(self, Name: str, ItemType: int = 0):
        """The function deletes tendon objects. The function returns zero if the tendon objects are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the tendon
            object specified by the Name item is deleted. If this item is Group, all of the
            tendon objects in the group specified by the Name item are deleted. If this item
            is SelectedObjects, all selected tendon objects are deleted, and the Name item
            is ignored.
        """
        _r = self._raw.Delete(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetDiscretization(self, Name: str):
        """This function retrieves the maximum discretization length assignment for tendon objects. The
        function returns zero if the assignment is successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing tendon object.
        Value (output): The maximum discretization length for the tendon. [L]
        """
        _r = self._raw.GetDiscretization(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetDiscretization falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetElm(self, Name: str):
        """This function retrieves the names of the line elements (analysis model lines) associated
        with a specified tendon object in the object-based model. It also retrieves
        information about the location of the line elements along the tendon object. This
        function returns zero if the line element information is successfully returned;
        otherwise it returns nonzero. An error occurs if the analysis model does not
        currently exist.
    
        Name (input): The name of an existing tendon object.
        nelm (output): The number of line elements created from the specified tendon object.
        Elm (output): An array that includes the name of a line element created from the
            specified tendon object.
        RDI (output): An array that includes the relative distance along the tendon object
            to the I-End of the line element.
        RDJ (output): An array that includes the relative distance along the tendon object
            to the J-End of the line element.
        """
        _r = self._raw.GetElm(Name, 0, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetElm falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetGUID(self, name: str):
        """This function retrieves the GUID for the specified tendon object. This function returns zero
        if the tendon object GUID is successfully retrieved; otherwise it returns nonzero.
    
        GUID (output): The GUID (Global Unique ID) for the specified tendon object.
        """
        _r = self._raw.GetGUID(name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetGUID falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGroupAssign(self, Name: str):
        """This function retrieves the names of the groups to which a specified tendon object is
        assigned. The function returns zero if the group assignments are successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object.
        NumberGroups (output): The number of group names retrieved.
        Groups (output): The names of the groups to which the tendon object is assigned.
        """
        _r = self._raw.GetGroupAssign(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetGroupAssign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDeformation(self, Name: str, ItemType: int = 0):
        """This function retrieves the deformation load assignments to tendon objects. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified tendon objects.
        TendonName (output): This is an array that includes the name of the tendon object
            associated with each deformation load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each deformation load.
        U1 (output): This is an array of axial deformation load values. [L]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the tendon object specified by the Name item. If this item is
            Group, the assignments are retrieved for all tendon objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected tendon objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadDeformation(Name, 0, [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetLoadDeformation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadForceStress(self, Name: str, ItemType: int = 0):
        """This function retrieves the force/stress load assignments to tendon objects. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of temperature loads retrieved for the
            specified tendon objects.
        TendonName (output): This is an array that includes the name of the tendon object
            associated with each temperature load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each temperature load.
        JackFrom (output): This is an array that includes 1, 2 or 3, indicating how the
            tendon is jacked. 1 = Tendon jacked from I-End 2 = Tendon jacked from J-End 3 =
            Tendon jacked from both ends
        LoadType (output): This is an array that includes either 0 or 1, indicating how the
            type of load. 0 = Force 1 = Stress
        Value (output): This is an array that includes the load value. [F] when LoadType is
            0, and [F/L 2 ] when Loadtype is 1
        CurvatureCoeff (output): This is an array that includes the curvature coefficient
            used when calculating friction losses.
        WobbleCoeff (output): This is an array that includes the wobble coefficient used
            when calculating friction losses. [1/L]
        LossAnchorage (output): This is an array that includes the anchorage set slip. [L]
        LossShortening (output): This is an array that includes the tendon stress loss due
            to elastic shortening. [F/L 2 ]
        LossCreep (output): This is an array that includes the tendon stress loss due to
            creep. [F/L 2 ]
        LossShrinkage (output): This is an array that includes the tendon stress loss due to
            shrinkage. [F/L 2 ]
        LossSteelRelax (output): This is an array that includes the tendon stress loss due
            to tendon steel relaxation. [F/L 2 ]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the tendon object specified by the Name item. If this item is
            Group, the assignments are retrieved for all tendon objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected tendon objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadForceStress(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetLoadForceStress falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadGravity(self, Name: str, ItemType: int = 0):
        """This function retrieves the gravity load assignments to tendon objects. The function returns
        zero if the load assignments are successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            tendon objects.
        TendonName (output): This is an array that includes the name of the tendon object
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the tendon object specified by the Name item. If this item is
            Group, the assignments are retrieved for all tendon objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected tendon objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadStrain(self, Name: str, ItemType: int = 0):
        """This function retrieves the strain load assignments to tendon objects. The function returns
        zero if the strain load assignments are successfully retrieved, otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of strain loads retrieved for the specified
            tendon objects.
        TendonName (output): This is an array that includes the name of the tendon object
            associated with each strain load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each strain load.
        Strain (output): This is an array that includes the axial strain value. [L/L]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the strain load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the tendon object specified by the Name item. If this item is
            Group, the assignments are retrieved for all tendon objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected tendon objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadStrain(Name, 0, [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetLoadStrain falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTemperature(self, Name: str, ItemType: int = 0):
        """This function retrieves the temperature load assignments to tendon objects. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of temperature loads retrieved for the
            specified tendon objects.
        TendonName (output): This is an array that includes the name of the tendon object
            associated with each temperature load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each temperature load.
        Val (output): This is an array that includes the temperature load value. [T]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the temperature load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the tendon object specified by the Name item. If this item is
            Group, the assignments are retrieved for all tendon objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected tendon objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadTemperature(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetLoadTemperature falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadedGroup(self, Name: str):
        """This function retrieves the loaded group for tendon objects. A tendon object transfers its
        load to any object that is in the specified group. The function returns zero if the
        assignment is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object.
        GroupName (output): This is the name of an existing group. All objects in the
            specified group can be loaded by the tendon.
        """
        _r = self._raw.GetLoadedGroup(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetLoadedGroup falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLocalAxes(self, Name: str):
        """This function retrieves the tendon local axis angle assignment for tendon objects. The
        function returns zero if the assignment is successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing tendon object.
        Ang (output): This is the angle that the local 2 and 3 axes are rotated about the
            positive local 1 axis, from the default orientation. The rotation for a positive
            angle appears counter clockwise when the local +1 axis is pointing toward you.
            [deg]
        """
        _r = self._raw.GetLocalAxes(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMatTemp(self, Name: str, Temp: float):
        """This function retrieves the material temperature assignments to tendon objects. The function
        returns zero if the material temperature assignments are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object.
        Temp (input): This is the material temperature value assigned to the tendon object.
            [T]
        PatternName (output): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the tendon object is uniform along the
            object at the value specified by Temp. If PatternName is the name of a defined
            joint pattern, the material temperature for the tendon object may vary from one
            end to the other. The material temperature at each end of the object is equal to
            the specified temperature multiplied by the pattern value at the joint at the
            end of the tendon object.
        """
        _r = self._raw.GetMatTemp(Name, Temp, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetMatTemp falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined tendon objects. The function returns zero
        if the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of tendon object names retrieved by the program.
        MyName (output): This is a one-dimensional array of tendon object names. The MyName
            array is created as a dynamic, zero-based, array by the APIuser: Dim MyName() as
            String The array is dimensioned to (NumberNames 1) inside the Sap2000 program,
            filled with the names, and returned to the APIuser.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoints(self, Name: str):
        """This function retrieves the names of the point objects at each end of a specified tendon
        object. The function returns zero if the point names are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of a defined tendon object.
        Point1 (output): The name of the point object at the I-End of the specified tendon
            object.
        Point2 (output): The name of the point object at the J-End of the specified tendon
            object.
        """
        _r = self._raw.GetPoints(Name, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetProperty(self, Name: str, PropName: str):
        """This function retrieves the tendon property assigned to a tendon object. The function
        returns zero if the tendon object property is successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of a defined tendon object.
        PropName (input): The name of the tendon property assigned to the tendon object.
        """
        _r = self._raw.GetProperty(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def GetSelected(self, Name: str):
        """This function retrieves the selected status for a tendon object. The function returns zero
        if the selected status is successfully retrieved, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing tendon object.
        Selected (output): This item returns True if the specified tendon object is
            selected, otherwise it returns False.
        """
        _r = self._raw.GetSelected(Name, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetSelected falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetTCLimits(self, Name: str, LimitCompressionExists: bool, LimitTensionExists: bool):
        """This function retrieves the tension/compression force limit assignments to tendon objects.
        The function returns zero if the assignments are successfully retrieved, otherwise
        it returns a nonzero value. Note that the tension and compression limits are used in
        nonlinear analyses only.
    
        Name (input): The name of an existing tendon object.
        LimitCompressionExists (input): This item is True if a compression force limit
            exists for the tendon object.
        LimitCompression (output): The compression force limit for the tendon object. [F]
        LimitTensionExists (input): This item is True if a tension force limit exists for
            the tendon object.
        LimitTension (output): The tension force limit for the tendon object. [F]
        """
        _r = self._raw.GetTCLimits(Name, LimitCompressionExists, 0.0, LimitTensionExists, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetTCLimits falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTendonData(self, Name: str, CSys: str = 'Global'):
        """This function retrieves the tendon geometric definition parameters for a tendon object. The
        function returns zero if the tendon object parameters are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of a defined tendon object.
        NumberPoints (output): The number of items used to define the tendon geometry.
        MyType (output): This is an array of values that are 1, 3, 6, 7, 8, or 9, indicating
            the tendon geometry definition parameter for the specified point. 1 = Start of
            tendon 2 = The segment preceding the point is linear 6 = The specified point is
            the end of a parabola 7 = The specified point is an intermediate point on a
            parabola 8 = The specified point is the end of a circle 9 = The specified point
            is an intermediate point on a parabola The first point always has a MyType value
            of 1. MyType of 6 through 9 is based on using three points to calculate a
            parabolic or circular arc. MyType 6 and 8 use the specified point and the two
            previous points as the three points. MyType 7 and 9 use the specified point and
            the points just before and after the specified point as the three points.
        x (output): This is an array of the X (or local 1) coordinate of each point in the
            coordinate system specified by CSys. [L]
        y (output): This is an array of the Y (or local 2) coordinate of each point in the
            coordinate system specified by CSys. [L]
        z (output): This is an array of the Z (or local 3) coordinate of each point in the
            coordinate system specified by CSys. [L]
        CSys (input): This is the coordinate system in which the x, y and z coordinate
            parameters are defined. It is Local or the name of a defined coordinate system.
            Local means that the point coordinates are in the local system of the specified
            tendon object with the origin assumed to be at the I-End of the tendon.
        """
        _r = self._raw.GetTendonData(Name, 0, [], [], [], [], CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetTendonData falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTendonGeometry(self, Name: str, CSys: str = 'Global'):
        """This function retrieves tendon object discretized geometry, that is, it retrieves the
        coordinates of the points along the discretized tendon. The function returns zero if
        the tendon object discretized geometry is successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of a defined tendon object.
        NumberPoints (output): The number of items used to define the discretized tendon
            geometry.
        x (output): This is an array of the X (or local 1) coordinate of each point in the
            coordinate system specified by CSys. [L]
        y (output): This is an array of the Y (or local 2) coordinate of each point in the
            coordinate system specified by CSys. [L]
        z (output): This is an array of the Z (or local 3) coordinate of each point in the
            coordinate system specified by CSys. [L]
        CSys (input): This is the coordinate system in which the x, y and z coordinate
            parameters are defined. It is Local or the name of a defined coordinate system.
            Local means that the point coordinates are in the local system of the specified
            tendon object with the origin assumed to be at the I-End of the tendon.
        """
        _r = self._raw.GetTendonGeometry(Name, 0, [], [], [], CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetTendonGeometry falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTransformationMatrix(self, Name: str, IsGlobal: bool = True):
        """The function returns zero if the tendon object transformation matrix is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the tendon object local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array, (Local1, Local2, Local3)
            are an item (such as a load) in the object local coordinate system, and
            (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.
            The transformation from the local coordinate system to the present coordinate
            system is the same as that shown above for the global system if you substitute
            the present system for the global system.
        IsGlobal (input): If this item is True, the transformation matrix is between the
            Global coordinate system and the tendon object local coordinate system. If this
            item is False, the transformation matrix is between the present coordinate
            system and the tendon object local coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [], IsGlobal)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.TendonObj.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetDiscretization(self, Name: str, Ang: float, ItemType: int = 0):
        """This function assigns a maximum discretization length to tendon objects. The function
        returns zero if the discretization length is successfully assigned, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetDiscretization(Name, Ang, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetDiscretization falhou (ret={_r})".format(_r=_r))
        return None

    def SetGUID(self, Name: str, GUID: str = ''):
        """This function sets the GUID for the specified tendon object. If the GUID is passed in as a
        blank string, the program automatically creates a GUID for the object. This function
        returns zero if the tendon object GUID is successfully set; otherwise it returns
        nonzero.
    
        Name (input): The name of an existing tendon object.
        GUID (input): The GUID (Global Unique ID) for the specified tendon object.
        """
        _r = self._raw.SetGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetGUID falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroupAssign(self, Name: str, GroupName: str, Remove: bool, ItemType: int = 0):
        """This function adds or removes tendon objects from a specified group. The function returns
        zero if the group assignment is successful, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        GroupName (input): The name of an existing group to which the assignment is made.
        Remove (input): If this item is False, the specified tendon objects are added to the
            group specified by the GroupName item. If it is True, the tendon objects are
            removed from the group.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the tendon
            object specified by the Name item is added or removed from the group specified
            by the GroupName item. If this item is Group, all tendon objects in the group
            specified by the Name item are added or removed from the group specified by the
            GroupName item. If this item is SelectedObjects, all selected tendon objects are
            added or removed from the group specified by the GroupName item, and the Name
            item is ignored.
        """
        _r = self._raw.SetGroupAssign(Name, GroupName, Remove, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetGroupAssign falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadDeformation(self, Name: str, LoadPat: str, d: float, ItemType: int = 0):
        """This function assigns deformation loads to tendon objects. The function returns zero if the
        loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        d (input): This is the axial deformation load value. [L]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects and the Name item is ignored.
        """
        _r = self._raw.SetLoadDeformation(Name, LoadPat, d, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetLoadDeformation falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadForceStress(self, Name: str, LoadPat: str, JackFrom: int, LoadType: int, Value: float, CurvatureCoeff: float, WobbleCoeff: float, LossAnchorage: float, LossShortening: float, LossCreep: float, LossShrinkage: float, LossSteelRelax: float, Replace: bool = True, ItemType: int = 0):
        """This function assigns force/stress loads to tendon objects. The function returns zero if the
        loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        JackFrom (input): This is 1, 2 or 3, indicating how the tendon is jacked. 1 = Tendon
            jacked from I-End 2 = Tendon jacked from J-End 3 = Tendon jacked from both ends
        LoadType (input): This is either 0 or 1, indicating how the type of load. 0 = Force
            1 = Stress
        Value (input): This is the load value. [F] whenLoadType is 0, and [F/L 2 ] when
            Loadtype is 1
        CurvatureCoeff (input): The curvature coefficient used when calculating friction
            losses.
        WobbleCoeff (input): The wobble coefficient used when calculating friction losses.
            [1/L]
        LossAnchorage (input): The anchorage set slip. [L]
        LossShortening (input): The tendon stress loss due to elastic shortening. [F/L 2 ]
        LossCreep (input): The tendon stress loss due to creep. [F/L 2 ]
        LossShrinkage (input): The tendon stress loss due to shrinkage. [F/L 2 ]
        LossSteelRelax (input): The tendon stress loss due to tendon steel relaxation. [F/L
            2 ]
        Replace (input): If this item is True, all previous force/stress loads, if any,
            assigned to the specified tendon object(s), in the specified load case, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadForceStress(Name, LoadPat, JackFrom, LoadType, Value, CurvatureCoeff, WobbleCoeff, LossAnchorage, LossShortening, LossCreep, LossShrinkage, LossSteelRelax, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetLoadForceStress falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadGravity(self, Name: str, LoadPat: str, x: float, y: float, z: float, Replace: bool = True, CSys: str = 'Global', ItemType: int = 0):
        """This function assigns gravity load multipliers to tendon objects. The function returns zero
        if the loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Replace (input): If this item is True, all previous gravity loads, if any, assigned
            to the specified tendon object(s), in the specified load pattern, are deleted
            before making the new assignment.
        CSys (input): The coordinate system in which the x, y and z multipliers are
            specified.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects and the Name item is ignored.
        """
        _r = self._raw.SetLoadGravity(Name, LoadPat, x, y, z, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadStrain(self, Name: str, LoadPat: str, Strain: float, Replace: bool = True, PatternName: str = '', ItemType: int = 0):
        """This function assigns strain loads to tendon objects. The function returns zero if the loads
        are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Strain (input): This is the axial strain load value. [L/L]
        Replace (input): If this item is True, all previous strain loads, if any, assigned
            to the specified tendon object(s), in the specified load pattern, are deleted
            before making the new assignment.
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the strain load for the tendon object is uniform along the object at the
            value specified by Strain. If PatternName is the name of a defined joint
            pattern, the strain load for the tendon object is based on the specified strain
            value multiplied by the pattern value at the joints at each end of the tendon
            object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadStrain(Name, LoadPat, Strain, Replace, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadTemperature(self, Name: str, LoadPat: str, Val: float, PatternName: str = '', Replace: bool = True, ItemType: int = 0):
        """This function assigns temperature loads to tendon objects. The function returns zero if the
        loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Val (input): This is the temperature change value. [T]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the temperature load for the tendon object is uniform along the object at
            the value specified by Val. If PatternName is the name of a defined joint
            pattern, the temperature load for the tendon object is based on the specified
            temperature value multiplied by the pattern value at the joints at each end of
            the tendon object.
        Replace (input): If this item is True, all previous temperature loads, if any,
            assigned to the specified tendon object(s), in the specified load case, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadTemperature(Name, LoadPat, Val, PatternName, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadedGroup(self, Name: str, GroupName: str, ItemType: int = 0):
        """This function makes the loaded group assignment to tendon objects. A tendon object transfers
        its load to any object that is in the specified group. The function returns zero if
        the group is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        GroupName (input): This is the name of an existing group. All objects in the
            specified group can be loaded by the tendon.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadedGroup(Name, GroupName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetLoadedGroup falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxes(self, Name: str, Ang: float, ItemType: int = 0):
        """This function assigns a local axis angle to tendon objects. The function returns zero if the
        local axis angle is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        Ang (input): This is the angle that the local 2 and 3 axes are rotated about the
            positive local 1 axis, from the default orientation. The rotation for a positive
            angle appears counter clockwise when the local +1 axis is pointing toward you.
            [deg]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLocalAxes(Name, Ang, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetLocalAxes falhou (ret={_r})".format(_r=_r))
        return None

    def SetMatTemp(self, Name: str, Temp: float, PatternName: str = '', ItemType: int = 0):
        """This function assigns material temperatures to tendon objects. The function returns zero if
        the material temperatures are successfully assigned, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        Temp (input): This is the material temperature value assigned to the tendon object.
            [T]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the tendon object is uniform along the
            object at the value specified by Temp. If PatternName is the name of a defined
            joint pattern, the material temperature for the tendon object may vary from one
            end to the other. The material temperature at each end of the object is equal to
            the specified temperature multiplied by the pattern value at the joint at the
            end of the tendon object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetMatTemp(Name, Temp, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetMatTemp falhou (ret={_r})".format(_r=_r))
        return None

    def SetProperty(self, name: str, PropName: str, ItemType: int = 0):
        """This function assigns a tendon property to a tendon object. The function returns zero if the
        tendon property is successfully assigned, otherwise it returns a nonzero value.
    
        PropName (input): This is None or the name of a tendon property to be assigned to
            the specified tendon object(s). None means that no property is assigned to the
            tendon.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetProperty(name, PropName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def SetSelected(self, Name: str, Selected: bool, ItemType: int = 0):
        """This function sets the selected status for a tendon object. The function returns zero if the
        selected status is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        Selected (input): This item is True if the specified tendon object is selected,
            otherwise it is False.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the selected
            status is set for the tendon object specified by the Name item. If this item is
            Group, the selected status is set for all tendon objects in the group specified
            by the Name item. If this item is SelectedObjects, the selected status is set
            for all selected tendon objects, and the Name item is ignored.
        """
        _r = self._raw.SetSelected(Name, Selected, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetSelected falhou (ret={_r})".format(_r=_r))
        return None

    def SetTCLimits(self, Name: str, LimitCompressionExists: bool, LimitCompression: float, LimitTensionExists: bool, LimitTension: float, ItemType: int = 0):
        """This function makes tension/compression force limit assignments to tendon objects. The
        function returns zero if the assignments are successfully applied, otherwise it
        returns a nonzero value. Note that the tension and compression limits are used in
        nonlinear analyses only.
    
        Name (input): The name of an existing tendon object or group, depending on the value
            of the ItemType item.
        LimitCompressionExists (input): This item is True if a compression force limit
            exists for the tendon object.
        LimitCompression (input): The compression force limit for the tendon object. [F]
        LimitTensionExists (input): This item is True if a tension force limit exists for
            the tendon object.
        LimitTension (input): The tension force limit for the tendon object. [F]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the tendon object specified by the Name item. If this item is Group,
            the assignment is made to all tendon objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected tendon
            objects and the Name item is ignored.
        """
        _r = self._raw.SetTCLimits(Name, LimitCompressionExists, LimitCompression, LimitTensionExists, LimitTension, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetTCLimits falhou (ret={_r})".format(_r=_r))
        return None

    def SetTendonData(self, Name: str, NumberPoints: int, MyType: list[int], x: list[float], y: list[float], z: list[float], CSys: str = 'Global'):
        """This function assigns the tendon geometric definition parameters to a tendon object. The
        function returns zero if the tendon object is successfully defined, otherwise it
        returns a nonzero value. If the tendon object is not successfully defined, it may be
        deleted.
    
        Name (input): The name of a defined tendon object.
        NumberPoints (input): The number of items used to define the tendon geometry.
        MyType (input): This is an array of values that are 1, 3, 6, 7, 8, or 9, indicating
            the tendon geometry definition parameter for the specified point. 1 = Start of
            tendon 2 = The segment preceding the point is linear 6 = The specified point is
            the end of a parabola 7 = The specified point is an intermediate point on a
            parabola 8 = The specified point is the end of a circle 9 = The specified point
            is an intermediate point on a parabola The first point should always have a
            MyType value of 1. If it is not equal to 1, the program uses 1 anyway. MyType of
            6 through 9 is based on using three points to calculate a parabolic or circular
            arc. MyType 6 and 8 use the specified point and the two previous points as the
            three points. MyType 7 and 9 use the specified point and the points just before
            and after the specified point as the three points.
        x (input): This is an array of the X (or local 1) coordinate of each point in the
            coordinate system specified by CSys. [L]
        y (input): This is an array of the Y (or local 2) coordinate of each point in the
            coordinate system specified by CSys. [L]
        z (input): This is an array of the Z (or local 3) coordinate of each point in the
            coordinate system specified by CSys. [L]
        CSys (input): This is the coordinate system in which the x, y and z coordinate
            parameters are defined. It is Local or the name of a defined coordinate system.
            Local means that the point coordinates are in the local system of the specified
            tendon object with the origin assumed to be at the I-End of the tendon.
        """
        _r = self._raw.SetTendonData(Name, NumberPoints, MyType, x, y, z, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.TendonObj.SetTendonData falhou (ret={_r})".format(_r=_r))
        return None


