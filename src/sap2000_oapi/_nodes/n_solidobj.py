"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_SolidObj:
    """Wrapper para SapModel.SolidObj."""

    def __init__(self, raw):
        self._raw = raw

    def AddByCoord(self, x: list[float], y: list[float], z: list[float], PropName: str = 'Default', UserName: str = '', CSys: str = 'Global'):
        """This function adds a new solid object whose corner points are at the specified coordinates.
        Note that solid objects always are defined with eight corner points. The function
        returns zero if the solid object is successfully added; otherwise it returns a
        nonzero value.
    
        Name (output): This is the name that the program ultimately assigns for the solid
            object. If no UserName is specified, the program assigns a default name to the
            solid object. If a UserName is specified and that name is not used for another
            solid object, the UserName is assigned to the solid object; otherwise a default
            name is assigned to the solid object.
        PropName (input): This is either Default or the name of a defined solid property. If
            it is Default, the program assigns a default solid property to the solid object.
            If it is the name of a defined solid property, that property is assigned to the
            solid object.
        UserName (input): This is an optional user specified name for the solid object. If a
            UserName is specified and that name is already used for another solid object,
            the program ignores the UserName.
        CSys (input): The name of the coordinate system in which the solid object point
            coordinates are defined.
        """
        _r = self._raw.AddByCoord(x, y, z, "", PropName, UserName, CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.AddByCoord falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def AddByPoint(self, Point: list[str], PropName: str = 'Default', UserName: str = ''):
        """This function adds a new solid object whose corner points are specified by name. The
        function returns zero if the solid object is successfully added; otherwise it
        returns a nonzero value.
    
        Point (input): This is an array containing the names of the eight point objects that
            define the corner points of the added solid object.
        Name (output): This is the name that the program ultimately assigns for the solid
            object. If no UserName is specified, the program assigns a default name to the
            solid object. If a UserName is specified and that name is not used for another
            solid object, the UserName is assigned to the solid object; otherwise a default
            name is assigned to the solid object.
        PropName (input): This is either Default or the name of a defined solid property. If
            it is Default, the program assigns a default solid property to the solid object.
            If it is the name of a defined solid property, that property is assigned to the
            solid object.
        UserName (input): This is an optional user specified name for the solid object. If a
            UserName is specified and that name is already used for another solid object,
            the program ignores the UserName.
        """
        _r = self._raw.AddByPoint(Point, "", PropName, UserName)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.AddByPoint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ChangeName(self, Name: str, NewName: str):
        """This function applies a new name to a solid object. The function returns zero if the new
        name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined solid object.
        NewName (input): The new name for the solid object.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns a count of the solid objects in the model.
        """
        _r = self._raw.Count()
        return _r

    def DeleteLoadGravity(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the gravity load assignments to the specified solid objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the solid object specified by the Name item. If this
            item is Group, the load assignments are deleted for all solid objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected solid objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadGravity(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.DeleteLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadPorePressure(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the pore pressure load assignments to the specified solid objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the solid object specified by the Name item. If this
            item is Group, the load assignments are deleted for all solid objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected solid objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadPorePressure(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.DeleteLoadPorePressure falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadStrain(self, Name: str, LoadPat: str, Component: int, ItemType: int = 0):
        """This function deletes the strain load assignments to the specified solid objects, for the
        specified load pattern, for the specified components. The function returns zero if
        the load assignments are successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Component (input): This is 1, 2, 3, 4, 5 or 6, indicating the component for which
            the strain load is to be deleted. 1 = Strain11 2 = Strain22 3 = Strain33 4 =
            Strain12 5 = Strain13 6 = Strain23
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the solid object specified by the Name item. If this
            item is Group, the load assignments are deleted for all solid objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected solid objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadStrain(Name, LoadPat, Component, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.DeleteLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadSurfacePressure(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the surface pressure load assignments to the specified solid objects
        for the specified load pattern. The function returns zero if the load assignments
        are successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the solid object specified by the Name item. If this
            item is Group, the load assignments are deleted for all solid objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected solid objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadSurfacePressure(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.DeleteLoadSurfacePressure falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadTemperature(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the temperature load assignments to the specified solid objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the solid object specified by the Name item. If this
            item is Group, the load assignments are deleted for all solid objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected solid objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadTemperature(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.DeleteLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteSpring(self, Name: str, ItemType: int = 0):
        """This function deletes all spring assignments for the specified solid objects. The function
        returns zero if the assignments are successfully deleted; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the spring
            assignments are deleted for the solid object specified by the Name item. If this
            item is Group, the spring assignments are deleted for all solid objects in the
            group specified by the Name item. If this item is SelectedObjects, the spring
            assignments are deleted for all selected solid objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteSpring(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.DeleteSpring falhou (ret={_r})".format(_r=_r))
        return None

    def Delete(self, Name: str, ItemType: int = 0):
        """The function deletes solid objects. The function returns zero if the solid objects are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the solid
            object specified by the Name item is deleted. If this item is Group, the all
            solid objects in the group specified by the Name item are deleted. If this item
            is SelectedObjects, all selected solid objects are deleted, and the Name item is
            ignored.
        """
        _r = self._raw.Delete(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetAutoMesh(self, Name: str, MaxSize1: float, MaxSize2: float):
        """This function retrieves the automatic meshing assignments to solid objects. The function
        returns zero if the meshing assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing solid object.
        MeshType (output): This item is 0, 1 or 2, indicating the automatic mesh type for
            the solid object. 0 = No automatic meshing 1 = Mesh solid into a specified
            number of objects 2 = Mesh solid into objects of a specified maximum size
        n1 (output): This item applies when MeshType = 1. It is the number of objects
            created along the edge of the meshed solid object that runs from point 1 to
            point 2.
        n2 (output): This item applies when MeshType = 1. It is the number of objects
            created along the edge of the meshed solid object that runs from point 1 to
            point 3.
        MaxSize1 (input): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed solid object that runs from point 1
            to point 2. [L] If this item is input as 0, the default value is used. The
            default value is 48 inches if the database units are English or 120 centimeters
            if the database units are metric.
        MaxSize2 (input): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed solid object that runs from point 1
            to point 3. [L] If this item is input as 0, the default value is used. The
            default value is 48 inches if the database units are English or 120 centimeters
            if the database units are metric.
        RestraintsOnEdge (output): If this item is True, and if both points along an edge of
            the original solid object have the same restraint/constraint, then, if the an
            added point on that edge and the original corner points have the same local axes
            definition, the program assigns the restraint/constraint to the added point.
        RestraintsOnFace (output): If this item is True, and if all corner points on an
            solid object face have the same restraint/constraint, then, if an added point on
            that face and the original corner points for the face have the same local axes
            definition, the program assigns the restraint/constraint to the added point.
        """
        _r = self._raw.GetAutoMesh(Name, 0, 0, 0, MaxSize1, MaxSize2, False, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetAutoMesh falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetEdgeConstraint(self, Name: str, ConstraintExists: bool):
        """This function retrieves the generated edge constraint assignments to solid objects. The
        function returns zero if the assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing solid object.
        ConstraintExists (input): This item is True if an automatic edge constraint is
            generated by the program for the solid object in the analysis model.
        """
        _r = self._raw.GetEdgeConstraint(Name, ConstraintExists)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetEdgeConstraint falhou (ret={_r})".format(_r=_r))
        return None

    def GetElm(self, Name: str):
        """This function retrieves the names of the solid elements (analysis model solid) associated
        with a specified solid object in the object-based model. This function returns zero
        if the solid element information is successfully returned; otherwise it returns
        nonzero. An error occurs if the analysis model does not exist.
    
        Name (input): The name of an existing solid object.
        nelm (output): The number of solid elements created from the specified solid object.
        Elm (output): An array that includes the name of a solid element created from the
            specified solid object.
        """
        _r = self._raw.GetElm(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetElm falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetGUID(self, name: str):
        """This function retrieves the GUID for the specified solid object. This function returns zero
        if the solid object GUID is successfully retrieved; otherwise it returns nonzero.
    
        GUID (output): The GUID (Global Unique ID) for the specified solid object.
        """
        _r = self._raw.GetGUID(name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetGUID falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGroupAssign(self, Name: str):
        """This function retrieves the names of the groups to which a specified solid object is
        assigned. The function returns zero if the group assignments are successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object.
        NumberGroups (output): The number of group names retrieved.
        Groups (output): The names of the groups to which the solid object is assigned.
        """
        _r = self._raw.GetGroupAssign(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetGroupAssign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadGravity(self, Name: str, ItemType: int = 0):
        """This function retrieves the gravity load assignments to solid objects. The function returns
        zero if the load assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            solid objects.
        SolidName (output): This is an array that includes the name of the solid object
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the solid object specified by the Name item. If this item is
            Group, the assignments are retrieved for all solid objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected solid objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadPorePressure(self, Name: str, ItemType: int = 0):
        """This function retrieves the pore pressure load assignments to solid objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of pore pressure loads retrieved for the
            specified solid objects.
        SolidName (output): This is an array that includes the name of the solid object
            associated with each pore pressure load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each pore pressure load.
        Value (output): This is an array that includes the pore pressure load value. [F/L 2
            ]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the pore pressure load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the solid object specified by the Name item. If this item is
            Group, the assignments are retrieved for all solid objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected solid objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadPorePressure(Name, 0, [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetLoadPorePressure falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadStrain(self, Name: str, ItemType: int = 0):
        """This function retrieves the strain load assignments to solid objects. The function returns
        zero if the strain load assignments are successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of strain loads retrieved for the specified
            solid objects.
        SolidName (output): This is an array that includes the name of the solid object
            associated with each strain load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each strain load.
        Component (output): This is 1, 2, 3, 4, 5 or 6, indicating the component to which
            the strain load is applied. 1 = Strain11 2 = Strain22 3 = Strain33 4 = Strain12
            5 = Strain13 6 = Strain23
        Value (output): This is an array that includes the strain value. [L/L]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the strain load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the solid object specified by the Name item. If this item is
            Group, the assignments are retrieved for all solid objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected solid objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadStrain(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetLoadStrain falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadSurfacePressure(self, Name: str, ItemType: int = 0):
        """This function retrieves the surface pressure load assignments to solid objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of surface pressure loads retrieved for the
            specified solid objects.
        SolidName (output): This is an array that includes the name of the solid object
            associated with each surface pressure load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each surface pressure load.
        Face (output): This is an array that includes 1, 2, 3, 4, 5 or 6, indicating the
            solid object face to which the specified load assignment applies.
        Value (output): This is an array that includes the surface pressure load value. [F/L
            2 ]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the surface pressure load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the solid object specified by the Name item. If this item is
            Group, the assignments are retrieved for all solid objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected solid objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadSurfacePressure(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetLoadSurfacePressure falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTemperature(self, Name: str, ItemType: int = 0):
        """This function retrieves the temperature load assignments to solid objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of temperature loads retrieved for the
            specified solid objects.
        SolidName (output): This is an array that includes the name of the solid object
            associated with each temperature load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each temperature load.
        Value (output): This is an array that includes the temperature load value. [T]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the temperature load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the solid object specified by the Name item. If this item is
            Group, the assignments are retrieved for all solid objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected solid objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadTemperature(Name, 0, [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetLoadTemperature falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxesAdvanced(self, Name: str):
        """This function assigns advanced local axes to solid objects. The function returns zero if the
        advanced local axes assignments are assigned successfully; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing solid object.
        Active (output): This is True if advanced local axes exist.
        Plane2 (output): This is 12, 13, 21, 23, 31 or 32, indicating that the local plane
            determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, 0r 3-2
            plane. This item applies only when the Active item is True.
        """
        _r = self._raw.GetLocalAxesAdvanced(Name, False, 0, "", [], [], [], 0, 0, "", [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetLocalAxesAdvanced falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str, Advanced: bool):
        """This function retrieves the local axes angles for a solid object. The function returns zero
        if the local axes angles are successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing solid object.
        Advanced (input): This item is True if the solid object local axes orientation was
            obtained using advanced local axes parameters.
        """
        _r = self._raw.GetLocalAxes(Name, 0.0, 0.0, 0.0, Advanced)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMatTemp(self, Name: str, Temp: float):
        """This function retrieves the material temperature assignments to solid objects. The function
        returns zero if the material temperature assignments are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object.
        Temp (input): This is the material temperature value assigned to the solid object.
            [T]
        PatternName (output): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the solid object is uniform over the object
            at the value specified by Temp. If PatternName is the name of a defined joint
            pattern, the material temperature for the solid object may vary. The material
            temperature at each corner point of the solid object is equal to the specified
            temperature multiplied by the pattern value at the associated point object. The
            material temperature at other points in the solid object is calculated by
            interpolation from the corner points.
        """
        _r = self._raw.GetMatTemp(Name, Temp, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetMatTemp falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined solid objects. The function returns zero if
        the names are successfully retrieved; otherwise it returns nonzero.
    
        NumberNames (output): The number of solid object names retrieved by the program.
        MyName (output): This is a one-dimensional array of solid object names. The MyName
            array is created as a dynamic, zero-based, array by the APIuser: Dim MyName() as
            String The array is dimensioned to (NumberNames 1) inside the SAP2000 program,
            filled with the names, and returned to the APIuser.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoints(self, Name: str):
        """This function retrieves the names of the corner point objects of a solid object. The
        function returns zero if the point object names are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a defined solid object.
        Point (output): This is an array containing the names of the corner point objects of
            the solid object.
        """
        _r = self._raw.GetPoints(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetProperty(self, Name: str, PropName: str):
        """This function retrieves the solid property assigned to a solid object. The function returns
        zero if the property is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of a defined solid object.
        PropName (input): The name of the solid property assigned to the solid object.
        """
        _r = self._raw.GetProperty(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def GetSelected(self, Name: str, Selected: bool):
        """This function retrieves the selected status for a solid object. The function returns zero if
        the selected status is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object.
        Selected (input): This item is True if the specified solid object is selected;
            otherwise it is False.
        """
        _r = self._raw.GetSelected(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetSelected falhou (ret={_r})".format(_r=_r))
        return None

    def GetSpring(self, Name: str, LinkProp: list[str]):
        """This function retrieves the spring assignments to a solid object face. The function returns
        zero if the assignments are successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing solid object.
        NumberSprings (output): The number of springs assignments made to the specified
            solid object.
        MyType (output): Each value in this array is either 1 or 2, indicating the spring
            property type. 1 = Simple spring 2 = Link property
        s (output): Each value in this array is the simple spring stiffness per unit area of
            the specified solid object face. This item applies only when the corresponding
            MyType = 1. [F/L 3 ]
        SimpleSpringType (output): Each value in this array is 1, 2 or 3, indicating the
            simple spring type. This item applies only when the corresponding MyType = 1. 1
            = Spring resists tension and compression 2 = Spring resists compression only 3 =
            Spring resists tension only
        LinkProp (input): Each value in this array is the name of the link property assigned
            to the spring. This item applies only when the corresponding MyType = 2.
        Face (output): This is 1, 2, 3, 4, 5 or 6, indicating the solid object face to which
            the specified spring assignment applies.
        SpringLocalOneType (output): Each value in this array is 1, 2 or 3, indicating the
            method used to specify the spring positive local 1-axis orientation. 1 =
            Parallel to solid object local axis 2 = Normal to specified solid object face 3
            = User specified direction vector
        Dir (output): Each value in this array is 1, 2, 3, -1, -2 or -3, indicating the
            solid object local axis that corresponds to the positive local 1-axis of the
            spring. This item applies only when the corresponding SpringLocalOneType = 1.
        Outward (output): Each value in this array is True if the spring positive local 1
            axis is outward from the specified solid object face. This item applies only
            when SpringLocalOneType = 2.
        VecX (output): Each value in this array is the X-axis or solid object local 1-axis
            component (depending on the CSys specified) of the user specified direction
            vector for the spring local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when the corresponding
            SpringLocalOneType = 3.
        VecY (output): Each value in this array is the Y-axis or solid object local 2-axis
            component (depending on the CSys specified) of the user specified direction
            vector for the spring local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when the corresponding
            SpringLocalOneType = 3.
        VecZ (output): Each value in this array is the X-axis or solid object local 3-axis
            component (depending on the CSys specified) of the user specified direction
            vector for the spring local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when the corresponding
            SpringLocalOneType = 3.
        CSys (output): Each value in this array is Local (meaning the solid object local
            coordinate system) or the name of a defined coordinate system. This item is the
            coordinate system in which the user specified direction vector, Vec, is
            specified. This item applies only when the corresponding SpringLocalOneType = 3.
        Ang (output): Each value in this array is the angle that the link local 2-axis is
            rotated from its default orientation. This item applies only when the
            corresponding MyType = 2. [deg]
        """
        _r = self._raw.GetSpring(Name, 0, [], [], [], LinkProp, [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetSpring falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTransformationMatrix(self, Name: str, IsGlobal: bool = True):
        """The function returns zero if the solid object transformation matrix is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the solid object local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array, (Local1, Local2, Local3)
            are an item (such as a load) in the object local coordinate system, and
            (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.
            The transformation from the local coordinate system to the present coordinate
            system is the same as that shown above for the global system if you substitute
            the present system for the global system.
        IsGlobal (input): If this item is True, the transformation matrix is between the
            Global coordinate system and the solid object local coordinate system. If this
            item is False, the transformation matrix is between the present coordinate
            system and the solid object local coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [], IsGlobal)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidObj.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetAutoMesh(self, Name: str, MeshType: int, n1: int = 2, n2: int = 2, n3: int = 2, MaxSize1: float = 0, MaxSize2: float = 0, MaxSize3: float = 0, RestraintsOnEdge: bool = False, RestraintsOnFace: bool = False):
        """This function makes automatic meshing assignments to solid objects. The function returns
        zero if the meshing options are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        MeshType (input): This item is 0, 1 or 2, indicating the automatic mesh type for the
            solid object. 0 = No automatic meshing 1 = Mesh solid into a specified number of
            objects 2 = Mesh solid into objects of a specified maximum size
        n1 (input): This item applies when MeshType = 1. It is the number of objects created
            along the edge of the meshed solid object that runs from point 1 to point 2.
        n2 (input): This item applies when MeshType = 1. It is the number of objects created
            along the edge of the meshed solid object that runs from point 1 to point 3.
        n3 (input): This item applies when MeshType = 1. It is the number of objects created
            along the edge of the meshed solid object that runs from point 1 to point 5.
        MaxSize1 (input): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed solid object that runs from point 1
            to point 2. [L] If this item is input as 0, the default value is used. The
            default value is 48 inches if the database units are English or 120 centimeters
            if the database units are metric.
        MaxSize2 (input): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed solid object that runs from point 1
            to point 3. [L] If this item is input as 0, the default value is used. The
            default value is 48 inches if the database units are English or 120 centimeters
            if the database units are metric.
        MaxSize3 (input): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed solid object that runs from point 1
            to point 5. [L] If this item is input as 0, the default value is used. The
            default value is 48 inches if the database units are English or 120 centimeters
            if the database units are metric.
        RestraintsOnEdge (input): If this item is True, and if both points along an edge of
            the original solid object have the same restraint/constraint, then, if the an
            added point on that edge and the original corner points have the same local axes
            definition, the program assigns the restraint/constraint to the added point.
        RestraintsOnFace (input): If this item is True, and if all corner points on an solid
            object face have the same restraint/constraint, then, if an added point on that
            face and the original corner points for the face have the same local axes
            definition, the program assigns the restraint/constraint to the added point.
        """
        _r = self._raw.SetAutoMesh(Name, MeshType, n1, n2, n3, MaxSize1, MaxSize2, MaxSize3, RestraintsOnEdge, RestraintsOnFace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetAutoMesh falhou (ret={_r})".format(_r=_r))
        return None

    def SetEdgeConstraint(self, Name: str, ConstraintExists: bool, ItemType: int = 0):
        """This function makes generated edge constraint assignments to solid objects. The function
        returns zero if the edge constraint option is successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        ConstraintExists (input): This item is True if an automatic edge constraint is
            generated by the program for the solid object in the analysis model.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the solid object specified by the Name item. If this item is Group,
            the assignment is made to all solid objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected solid
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetEdgeConstraint(Name, ConstraintExists, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetEdgeConstraint falhou (ret={_r})".format(_r=_r))
        return None

    def SetGUID(self, Name: str, GUID: str = ''):
        """This function sets the GUID for the specified solid object. If the GUID is passed in as a
        blank string, the program automatically creates a GUID for the object. This function
        returns zero if the solid object GUID is successfully set; otherwise it returns
        nonzero.
    
        Name (input): The name of an existing solid object.
        GUID (input): The GUID (Global Unique ID) for the specified solid object.
        """
        _r = self._raw.SetGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetGUID falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroupAssign(self, Name: str, GroupName: str, Remove: bool, ItemType: int = 0):
        """This function adds or removes solid objects from a specified group. The function returns
        zero if the group assignment is successful; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        GroupName (input): The name of an existing group to which the assignment is made.
        Remove (input): If this item is False, the specified solid objects are added to the
            group specified by the GroupName item. If it is True, the solid objects are
            removed from the group.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the solid
            object specified by the Name item is added or removed from the group specified
            by the GroupName item. If this item is Group, all solid objects in the group
            specified by the Name item are added or removed from the group specified by the
            GroupName item. If this item is SelectedObjects, all selected solid objects are
            added or removed from the group specified by the GroupName item, and the Name
            item is ignored.
        """
        _r = self._raw.SetGroupAssign(Name, GroupName, Remove, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetGroupAssign falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadGravity(self, Name: str, LoadPat: str, x: float, y: float, z: float, Replace: bool = True, CSys: str = 'Global', ItemType: int = 0):
        """This function assigns gravity load multipliers to solid objects. The function returns zero
        if the loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Replace (input): If this item is True, all previous gravity loads, if any, assigned
            to the specified solid object(s), in the specified load pattern, are deleted
            before making the new assignment.
        CSys (input): The coordinate system in which the x, y and z multipliers are
            specified.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the solid object specified by the Name item. If this item is Group,
            the assignment is made to all solid objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected solid
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadGravity(Name, LoadPat, x, y, z, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadPorePressure(self, Name: str, LoadPat: str, Value: float, PatternName: str = '', Replace: bool = True, ItemType: int = 0):
        """This function assigns pore pressure loads to solid objects. The function returns zero if the
        loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Value (input): This is the pore pressure value. [F/L 2 ]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the pore pressure load for the solid object is uniform over the object at
            the value specified by Value. If PatternName is the name of a defined joint
            pattern, the pore pressure load for the solid object is based on the specified
            pore pressure value multiplied by the pattern value at the corner point objects
            of the solid object.
        Replace (input): If this item is True, all previous pore pressure loads, if any,
            assigned to the specified solid object(s), in the specified load case, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the solid object specified by the Name item. If this item is Group,
            the assignment is made to all solid objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected solid
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadPorePressure(Name, LoadPat, Value, PatternName, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetLoadPorePressure falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadStrain(self, Name: str, LoadPat: str, Component: int, Value: float, Replace: bool = True, PatternName: str = '', ItemType: int = 0):
        """This function assigns strain loads to solid objects. The function returns zero if the loads
        are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Component (input): This is 1, 2, 3, 4, 5 or 6, indicating the component to which the
            strain load is applied. 1 = Strain11 2 = Strain22 3 = Strain33 4 = Strain12 5 =
            Strain13 6 = Strain23
        Value (input): This is the strain load value. [L/L]
        Replace (input): If this item is True, all previous strain loads, if any, assigned
            to the specified solid object(s), in the specified load pattern, for the
            specified degree of freedom, are deleted before making the new assignment.
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the strain load for the solid object is uniform over the object at the
            value specified by Value. If PatternName is the name of a defined joint pattern,
            the strain load for the solid object is based on the specified strain value
            multiplied by the pattern value at the corner point objects of the solid object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the solid object specified by the Name item. If this item is Group,
            the assignment is made to all solid objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected solid
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadStrain(Name, LoadPat, Component, Value, Replace, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadSurfacePressure(self, Name: str, LoadPat: str, Face: int, Value: float, PatternName: str = '', Replace: bool = True, ItemType: int = 0):
        """This function assigns surface pressure loads to solid objects. The function returns zero if
        the loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Face (input): This is 1, 2, 3, 4, 5 or 6, indicating the solid object face to which
            the specified load assignment applies.
        Value (input): This is the surface pressure value. [F/L 2 ]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the surface pressure load for the solid object is uniform over the object
            at the value specified by Value. If PatternName is the name of a defined joint
            pattern, the surface pressure load for the solid object is based on the
            specified surface pressure value multiplied by the pattern value at the corner
            point objects of the solid object.
        Replace (input): If this item is True, all previous surface pressure loads, if any,
            assigned to the specified solid object(s), on the specified face, in the
            specified load pattern, are deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the solid object specified by the Name item. If this item is Group,
            the assignment is made to all solid objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected solid
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadSurfacePressure(Name, LoadPat, Face, Value, PatternName, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetLoadSurfacePressure falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadTemperature(self, Name: str, LoadPat: str, Value: float, PatternName: str = '', Replace: bool = True, ItemType: int = 0):
        """This function assigns temperature loads to solid objects. The function returns zero if the
        loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Value (input): This is the temperature change value. [T]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the temperature load for the solid object is uniform over the object at
            the value specified by Value. If PatternName is the name of a defined joint
            pattern, the temperature load for the solid object is based on the specified
            temperature value multiplied by the pattern value at the corner point objects of
            the solid object.
        Replace (input): If this item is True, all previous temperature loads, if any,
            assigned to the specified solid object(s), in the specified load case, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the solid object specified by the Name item. If this item is Group,
            the assignment is made to all solid objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected solid
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadTemperature(Name, LoadPat, Value, PatternName, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxesAdvanced(self, Name: str, Active: bool, AxVectOpt: int, AxCSys: str, AxDir: list[int], AxPt: list[str], AxVect: list[float], Plane2: int, PlVectOpt: int, PlCSys: str, PlDir: list[int], PlPt: list[str], PlVect: list[float], ItemType: int = 0):
        """This function assigns advanced local axes to solid objects. The function returns zero if the
        advanced local axes assignments are assigned successfully; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        Active (input): This is True if advanced local axes exist.
        Plane2 (input): This is 12, 13, 21, 23, 31 or 32, indicating that the local plane
            determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, or 3-2
            plane. This item applies only when the Active item is True.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 Selection = 2 If this item is Object, the assignment is
            made to the solid object specified by the Name item. If this item is Group, the
            assignment is made to all solid objects in the group specified by the Name item.
            If this item is Selection, assignment is made to all selected solid objects and
            the Name item is ignored.
        """
        _r = self._raw.SetLocalAxesAdvanced(Name, Active, AxVectOpt, AxCSys, AxDir, AxPt, AxVect, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetLocalAxesAdvanced falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxes(self, Name: str, a: float, b: float, c: float, ItemType: int = 0):
        """This function sets the local axes angles for solid objects. The function returns zero if the
        local axes angles are successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the local axes
            assignment is made to the solid object specified by the Name item. If this item
            is Group, the local axes assignment is made to all solid objects in the group
            specified by the Name item. If this item is SelectedObjects, the local axes
            assignment is made to all selected solid objects, and the Name item is ignored.
        """
        _r = self._raw.SetLocalAxes(Name, a, b, c, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetLocalAxes falhou (ret={_r})".format(_r=_r))
        return None

    def SetMatTemp(self, Name: str, Temp: float, PatternName: str = '', ItemType: int = 0):
        """This function assigns material temperatures to solid objects. The function returns zero if
        the material temperatures are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        Temp (input): This is the material temperature value assigned to the solid object.
            [T]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the solid object is uniform over the object
            at the value specified by Temp. If PatternName is the name of a defined joint
            pattern, the material temperature for the solid object may vary. The material
            temperature at each corner point of the solid object is equal to the specified
            temperature multiplied by the pattern value at the associated point object. The
            material temperature at other points in the solid object is calculated by
            interpolation from the corner points.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the solid object specified by the Name item. If this item is Group,
            the assignment is made to all solid objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected solid
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetMatTemp(Name, Temp, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetMatTemp falhou (ret={_r})".format(_r=_r))
        return None

    def SetProperty(self, name: str, PropName: str, ItemType: int = 0):
        """This function assigns a solid property to solid objects. The function returns zero if the
        property is successfully assigned; otherwise it returns a nonzero value.
    
        PropName (input): This is the name of a solid property to be assigned to the
            specified solid object(s).
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the solid object specified by the Name item. If this item is Group,
            the assignment is made to all solid objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected solid
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetProperty(name, PropName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def SetSelected(self, Name: str, Selected: bool, ItemType: int = 0):
        """This function sets the selected status for solid objects. The function returns zero if the
        selected status is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        Selected (input): This item is True if the specified solid object is selected,
            otherwise it is False.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the selected
            status is set for the solid object specified by the Name item. If this item is
            Group, the selected status is set for all solid objects in the group specified
            by the Name item. If this item is SelectedObjects, the selected status is set
            for all selected solid objects, and the Name item is ignored.
        """
        _r = self._raw.SetSelected(Name, Selected, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetSelected falhou (ret={_r})".format(_r=_r))
        return None

    def SetSpring(self, Name: str, MyType: int, s: float, SimpleSpringType: int, LinkProp: str, Face: int, SpringLocalOneType: int, Dir: int, Outward: bool, Vec: list[float], Ang: float, Replace: bool, CSys: str = 'Local', ItemType: int = 0):
        """This function makes spring assignments to solid objects. The springs are assigned to a
        specified solid object face. The function returns zero if the assignments are
        successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object or group, depending on the value
            of the ItemType item.
        MyType (input): This is either 1 or 2, indicating the spring property type. 1 =
            Simple spring 2 = Link property
        s (input): The simple spring stiffness per unit area of the specified solid object
            face. This item applies only when MyType = 1. [F/L 3 ]
        SimpleSpringType (input): This is 1, 2 or 3, indicating the simple spring type. This
            item applies only when MyType = 1. 1 = Spring resists tension and compression 2
            = Spring resists compression only 3 = Spring resists tension only
        LinkProp (input): The name of the link property assigned to the spring. This item
            applies only when MyType = 2.
        Face (input): This is 1, 2, 3, 4, 5 or 6, indicating the solid object face to which
            the specified spring assignment applies.
        SpringLocalOneType (input): This is 1, 2 or 3, indicating the method used to specify
            the spring positive local 1-axis orientation. 1 = Parallel to solid object local
            axis 2 = Normal to specified solid object face 3 = User specified direction
            vector
        Dir (input): This is 1, 2, 3, -1, -2 or -3, indicating the solid object local axis
            that corresponds to the positive local 1-axis of the spring. This item applies
            only when SpringLocalOneType = 1.
        Outward (input): This item is True if the spring positive local 1 axis is outward
            from the specified solid object face. This item applies only when
            SpringLocalOneType = 2.
        Vec (input): This is an array of three values that define the direction vector of
            the spring positive local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when
            SpringLocalOneType = 3.
        Ang (input): This is the angle that the link local 2-axis is rotated from its
            default orientation. This item applies only when MyType = 2. [deg]
        Replace (input): If this item is True, all existing spring assignments to the solid
            object are removed before assigning the specified spring. If it is False, the
            specified spring is added to any existing springs already assigned to the solid
            object.
        CSys (input): This is Local (meaning the solid object local coordinate system) or
            the name of a defined coordinate system. This item is the coordinate system in
            which the user specified direction vector, Vec, is specified. This item applies
            only when SpringLocalOneType = 3.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the solid object specified by the Name item. If this item is Group,
            the assignment is made to all solid objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected solid
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetSpring(Name, MyType, s, SimpleSpringType, LinkProp, Face, SpringLocalOneType, Dir, Outward, Vec, Ang, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidObj.SetSpring falhou (ret={_r})".format(_r=_r))
        return None


