"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_AreaObj:
    """Wrapper para SapModel.AreaObj."""

    def __init__(self, raw):
        self._raw = raw

    def AddByCoord(self, NumberPoints: int, x: list[float], y: list[float], z: list[float], PropName: str = 'Default', UserName: str = '', CSys: str = 'Global'):
        """This function adds a new area object, defining points at the specified coordinates. The
        function returns zero if the area object is successfully added, otherwise it returns
        a nonzero value.
    
        NumberPoints (input): The number of points in the area abject.
        Name (output): This is the name that the program ultimately assigns to the area
            object. If no UserName is specified, the program assigns a default name to the
            area object. If a UserName is specified and that name is not used for another
            area object, the UserName is assigned to the area object; otherwise a default
            name is assigned to the area object.
        PropName (input): This is Default, None or the name of a defined area property. If
            it is Default, the program assigns a default area property to the area object.
            If it is None, no area property is assigned to the area object. If it is the
            name of a defined area property, that property is assigned to the area object.
        UserName (input): This is an optional user specified name for the area object. If a
            UserName is specified and that name is already used for another area object, the
            program ignores the UserName.
        CSys (input): The name of the coordinate system in which the area object point
            coordinates are defined.
        """
        _r = self._raw.AddByCoord(NumberPoints, x, y, z, "", PropName, UserName, CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.AddByCoord falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def AddByPoint(self, NumberPoints: int, Point: list[str], PropName: str = 'Default', UserName: str = ''):
        """This function adds a new area object whose defining points are specified by name. The
        function returns zero if the area object is successfully added; otherwise it returns
        a nonzero value.
    
        NumberPoints (input): The number of points in the area abject.
        Point (input): This is an array containing the names of the point objects that
            define the added area object. The point object names should be ordered to run
            clockwise or counter clockwise around the area object.
        Name (output): This is the name that the program ultimately assigns for the area
            object. If no UserName is specified, the program assigns a default name to the
            area object. If a UserName is specified and that name is not used for another
            area object, the UserName is assigned to the area object; otherwise a default
            name is assigned to the area object.
        PropName (input): This is Default, None or the name of a defined area property. If
            it is Default, the program assigns a default area property to the area object.
            If it is None, no area property is assigned to the area object. If it is the
            name of a defined area property, that property is assigned to the area object.
        UserName (input): This is an optional user specified name for the area object. If a
            UserName is specified and that name is already used for another area object, the
            program ignores the UserName.
        """
        _r = self._raw.AddByPoint(NumberPoints, Point, "", PropName, UserName)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.AddByPoint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ChangeName(self, Name: str, NewName: str):
        """This function applies a new name to an area object. The function returns zero if the new
        name is successfully applied, otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined area object.
        NewName (input): The new name for the area object.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """This function returns a count of the area objects in the model.
        """
        _r = self._raw.Count()
        return _r

    def DeleteLoadGravity(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the gravity load assignments to the specified area objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the load assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects,the load
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadGravity(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadPorePressure(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the pore pressure load assignments to the specified area objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the load assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadPorePressure(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteLoadPorePressure falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadRotate(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the rotate load assignments to the specified area objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the load assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadRotate(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteLoadRotate falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadStrain(self, Name: str, LoadPat: str, Component: int, ItemType: int = 0):
        """This function deletes the strain load assignments to the specified area objects, for the
        specified load pattern, for the specified components. The function returns zero if
        the load assignments are successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Component (input): This is 1, 2, 3, 4, 5, 6, 7, 8, or 9, indicating the component to
            which the strain load is applied. 1 = Strain11 2 = Strain12 3 = Strain13 4 =
            Curvature11 5 = Curvature22 6 = Curvature33 7 = Strain13 8 = Strain23 9 =
            Strain33
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the load assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadStrain(Name, LoadPat, Component, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadSurfacePressure(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the surface pressure load assignments to the specified area objects
        for the specified load pattern. The function returns zero if the load assignments
        are successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the load assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadSurfacePressure(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteLoadSurfacePressure falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadTemperature(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the temperature load assignments to the specified area objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the load assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadTemperature(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadUniform(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the uniform load assignments to the specified area objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the load assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadUniform(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteLoadUniform falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadUniformToFrame(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the uniform to frame load assignments to the specified area objects
        for the specified load pattern. The function returns zero if the load assignments
        are successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the load assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadUniformToFrame(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteLoadUniformToFrame falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadWindPressure(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the wind pressure load assignments to the specified area objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the load assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadWindPressure(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteLoadWindPressure falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteMass(self, Name: str, ItemType: int = 0):
        """This function deletes the mass assignments for area objects. The function returns zero if
        the mass assignments are successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the mass
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the mass assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the mass
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteMass(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteMass falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteModifiers(self, Name: str, ItemType: int = 0):
        """This function deletes the modifier assignments for area objects. The function returns zero
        if the modifier assignments are successfully deleted, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the modifier
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the modifier assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the modifier
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteModifiers(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteModifiers falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteSpring(self, Name: str, ItemType: int = 0):
        """This function deletes all spring assignments for the specified area objects. The function
        returns zero if the assignments are successfully deleted; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the spring
            assignments are deleted for the area object specified by the Name item. If this
            item is Group, the spring assignments are deleted for all area objects in the
            group specified by the Name item. If this item is SelectedObjects, the spring
            assignments are deleted for all selected area objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteSpring(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.DeleteSpring falhou (ret={_r})".format(_r=_r))
        return None

    def Delete(self, Name: str, ItemType: int = 0):
        """The function deletes area objects. The function returns zero if the area objects are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the area object
            specified by the Name item is deleted. If this item is Group, all of the area
            objects in the group specified by the Name item are deleted. If this item is
            SelectedObjects, all of the selected area objects are deleted, and the Name item
            is ignored.
        """
        _r = self._raw.Delete(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetAutoMesh(self, Name: str, LocalAxesOnEdge: bool, LocalAxesOnFace: bool, RestraintsOnEdge: bool, RestraintsOnFace: bool, SubMesh: bool):
        """This function retrieves the automatic meshing assignments to area objects. The function
        returns zero if the meshing assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object.
        MeshType (output): This item is 0, 1, 2, 3, 4, 5 or 6, indicating the automatic mesh
            type for the area object. 0 = No automatic meshing 1 = Mesh area into a
            specified number of objects 2 = Mesh area into objects of a specified maximum
            size 3 = Mesh area based on points on area edges 4 = Cookie cut mesh area based
            on lines intersecting edges 5 = Cookie cut mesh area based on points 6 = Mesh
            area using General Divide Tool Mesh options 1, 2 and 3 apply to quadrilaterals
            and triangles only.
        n1 (output): This item applies when MeshType = 1. It is the number of objects
            created along the edge of the meshed area object that runs from point 1 to point
            2.
        n2 (output): This item applies when MeshType = 1. It is the number of objects
            created along the edge of the meshed area object that runs from point 1 to point
            3.
        MaxSize1 (output): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed area object that runs from point 1
            to point 2. [L]
        MaxSize2 (output): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed area object that runs from point 1
            to point 3. [L]
        PointOnEdgeFromLine (output): This item applies when MeshType = 3. If it is True,
            points on the area object edges are determined from intersections of straight
            line objects included in the group specified by the Group item with the area
            object edges.
        PointOnEdgeFromPoint (output): This item applies when MeshType = 3. If it is True,
            points on the area object edges are determined from point objects included in
            the group specified by the Group item that lie on the area object edges.
        ExtendCookieCutLines (output): This item applies when MeshType = 4. MeshType = 4
            provides cookie cut meshing based on straight line objects included in the group
            specified by the Group item that intersect the area object edges. If the
            ExtendCookieCutLines item is True, all straight line objects included in the
            group specified by the Group item are extended to intersect the area object
            edges for the purpose of meshing the area object.
        Rotation (output): This item applies when MeshType = 5. MeshType = 5 provides cookie
            cut meshing based on two perpendicular lines passing through point objects
            included in the group specified by the Group item. By default these lines align
            with the area object local 1 and 2 axes. The Rotation item is an angle in
            degrees that the meshing lines are rotated from their default orientation. [deg]
        MaxSizeGeneral (output): This item applies when MeshType = 6. It is the maximum size
            of objects created by the General Divide Tool.
        LocalAxesOnEdge (input): If this item is True, and if both points along an edge of
            the original area object have the same local axes, the program makes the local
            axes for added points along the edge the same as the edge end points.
        LocalAxesOnFace (input): If this item is True, and if all points around the
            perimeter of the original area object have the same local axes, the program
            makes the local axes for all added points the same as the perimeter points.
        RestraintsOnEdge (input): If this item is True, and if both points along an edge of
            the original area object have the same restraint/constraint, then, if the added
            point and the adjacent corner points have the same local axes definition, the
            program includes the restraint/constraint for added points along the edge.
        RestraintsOnFace (input): If this item is True, and if all points around the
            perimeter of the original area object have the same restraint/constraint, then,
            if an added point and the perimeter points have the same local axes definition,
            the program includes the restraint/constraint for the added point.
        Group (output): The name of a defined group. Some of the meshing options make use of
            point and line objects included in this group.
        SubMesh (input): If this item is True, after initial meshing, the program further
            meshes any area objects that have an edge longer than the length specified by
            the SubMeshSize item.
        SubMeshSize (output): This item applies when the SubMesh item is True. It is the
            maximum size of area objects to remain when the auto meshing is complete. [L]
        """
        _r = self._raw.GetAutoMesh(Name, 0, 0, 0, 0.0, 0.0, False, False, False, 0.0, 0.0, LocalAxesOnEdge, LocalAxesOnFace, RestraintsOnEdge, RestraintsOnFace, "", SubMesh, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetAutoMesh falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetEdgeConstraint(self, Name: str, ConstraintExists: bool):
        """This function retrieves the generated edge constraint assignments to area objects. The
        function returns zero if the assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object.
        ConstraintExists (input): This item is True if an automatic edge constraint is
            generated by the program for the area object in the analysis model.
        """
        _r = self._raw.GetEdgeConstraint(Name, ConstraintExists)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetEdgeConstraint falhou (ret={_r})".format(_r=_r))
        return None

    def GetElm(self, Name: str):
        """This function retrieves the names of the area elements (analysis model area) associated with
        a specified area object in the object-based model. This function returns zero if the
        area element information is successfully returned; otherwise it returns nonzero. An
        error occurs if the analysis model does not currently exist.
    
        Name (input): The name of an existing area object.
        nelm (output): The number of area elements created from the specified area object.
        Elm (output): An array that includes the name of a area element created from the
            specified area object.
        """
        _r = self._raw.GetElm(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetElm falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetGUID(self, name: str):
        """This function retrieves the GUID for the specified area object. This function returns zero
        if the area object GUID is successfully retrieved; otherwise, it returns nonzero.
    
        GUID (output): The GUID (Global Unique ID) for the specified area object.
        """
        _r = self._raw.GetGUID(name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetGUID falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGroupAssign(self, Name: str):
        """This function retrieves the names of the groups to which a specified area object is
        assigned. The function returns zero if the group assignments are successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object.
        NumberGroups (output): The number of group names retrieved.
        Groups (output): The names of the groups to which the area object is assigned.
        """
        _r = self._raw.GetGroupAssign(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetGroupAssign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadGravity(self, Name: str, ItemType: int = 0):
        """This function retrieves the gravity load assignments to area objects. The function returns
        zero if the load assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            area objects.
        AreaName (output): This is an array that includes the name of the area object
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the area object specified by the Name item. If this item is
            Group, the assignments are retrieved for all area objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadPorePressure(self, Name: str, ItemType: int = 0):
        """This function retrieves the pore pressure load assignments to area objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of pore pressure loads retrieved for the
            specified area objects.
        AreaName (output): This is an array that includes the name of the area object
            associated with each pore pressure load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each pore pressure load.
        Value (output): This is an array that includes the pore pressure load value. [F/L 2
            ]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the pore pressure load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the area object specified by the Name item. If this item is
            Group, the assignments are retrieved for all area objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadPorePressure(Name, 0, [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLoadPorePressure falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadRotate(self, Name: str, ItemType: int = 0):
        """This function retrieves the rotate load assignments to area objects. The function returns
        zero if the load assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of rotate loads retrieved for the specified
            area objects.
        AreaName (output): This is an array that includes the name of the area object
            associated with each rotate load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each rotate load.
        Value (output): This is an array that includes the angular velocity value. [Cyc/T]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the area object specified by the Name item. If this item is
            Group, the assignments are retrieved for all area objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadRotate(Name, 0, [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLoadRotate falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadStrain(self, Name: str, ItemType: int = 0):
        """This function retrieves the strain load assignments to area objects. The function returns
        zero if the strain load assignments are successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of strain loads retrieved for the specified
            area objects.
        AreaName (output): This is an array that includes the name of the area object
            associated with each strain load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each strain load.
        Component (output): This is an array that includes 1, 2, 3, 4, 5, 6, 7, 8, or 9,
            indicating the component associated with each strain load. 1 = Strain11 2 =
            Strain22 3 = Strain12 4 = Curvature11 5 = Curvature22 6 = Curvature12 7 =
            Strain13 8 = Strain23 9 = Strain33
        Value (output): This is an array that includes the strain value. [L/L] for Component
            = 1, 2, 3, 7, 8, and 9, and [1/L] for Component = 4, 5 and 6
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the strain load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the area object specified by the Name item. If this item is
            Group, the assignments are retrieved for all area objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadStrain(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLoadStrain falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadSurfacePressure(self, Name: str, ItemType: int = 0):
        """This function retrieves the surface pressure load assignments to area objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of surface pressure loads retrieved for the
            specified area objects.
        AreaName (output): This is an array that includes the name of the area object
            associated with each surface pressure load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each surface pressure load.
        Face (output): This is an array that includes either -1, -2 or a nonzero, positive
            integer, indicating the area object face to which the specified load assignment
            applies. -1 = Bottom face -2 = Top face >0 = Edge face Note that edge face n is
            from area object point n to area object point n + 1. For example, edge face 2 is
            from area object point 2 to area object point 3.
        Value (output): This is an array that includes the surface pressure load value. [F/L
            2 ]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the surface pressure load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the area object specified by the Name item. If this item is
            Group, the assignments are retrieved for all area objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadSurfacePressure(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLoadSurfacePressure falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTemperature(self, Name: str, ItemType: int = 0):
        """This function retrieves the temperature load assignments to area objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of temperature loads retrieved for the
            specified area objects.
        AreaName (output): This is an array that includes the name of the area object
            associated with each temperature load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each temperature load.
        MyType (output): This is an array that includes either 1 or 3, indicating the type
            of temperature load. 1 = Temperature 3 = Temperature gradient along local 3 axis
        Value (output): This is an array that includes the temperature load value. [T] for
            MyType= 1 and [T/L] for MyType= 3
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the temperature load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the area object specified by the Name item. If this item is
            Group, the assignments are retrieved for all area objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadTemperature(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLoadTemperature falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadUniformToFrame(self, Name: str, ItemType: int = 0):
        """This function retrieves the uniform to frame load assignments to area objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of uniform loads retrieved for the specified
            area objects.
        AreaName (output): This is an array that includes the name of the area object
            associated with each uniform load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the uniform load is specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each uniform load.
        Dir (output): This is an integer between 1 and 11, indicating the direction of the
            load. 1 = Local 1 axis (only applies when CSys is Local) 2 = Local 2 axis (only
            applies when CSys is Local) 3 = Local 3 axis (only applies when CSys is Local) 4
            = X direction (does not apply when CSys is Local) 5 = Y direction (does not
            apply when CSys is Local) 6 = Z direction (does not apply when CSys is Local) 7
            = Projected X direction (does not apply when CSys is Local) 8 = Projected Y
            direction (does not apply when CSys is Local) 9 = Projected Z direction (does
            not apply when CSys is Local) 10 = Gravity direction (only applies when CSys is
            Global) 11 = Projected Gravity direction (only applies when CSys is Global) The
            positive gravity direction (see Dir = 10 and 11) is in the negative Global Z
            direction.
        Value (output): The uniform load value. [F/L 2 ]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the area object specified by the Name item. If this item is
            Group, the assignments are retrieved for all area objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadUniformToFrame(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLoadUniformToFrame falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadUniform(self, Name: str, ItemType: int = 0):
        """This function retrieves the uniform load assignments to area objects. The function returns
        zero if the load assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of uniform loads retrieved for the specified
            area objects.
        AreaName (output): This is an array that includes the name of the area object
            associated with each uniform load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the uniform load is specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each uniform load.
        Dir (output): This is an integer between 1 and 11, indicating the direction of the
            load. 1 = Local 1 axis (only applies when CSys is Local) 2 = Local 2 axis (only
            applies when CSys is Local) 3 = Local 3 axis (only applies when CSys is Local) 4
            = X direction (does not apply when CSys is Local) 5 = Y direction (does not
            apply when CSys is Local) 6 = Z direction (does not apply when CSys is Local) 7
            = Projected X direction (does not apply when CSys is Local) 8 = Projected Y
            direction (does not apply when CSys is Local) 9 = Projected Z direction (does
            not apply when CSys is Local) 10 = Gravity direction (only applies when CSys is
            Global) 11 = Projected Gravity direction (only applies when CSys is Global) The
            positive gravity direction (see Dir = 10 and 11) is in the negative Global Z
            direction.
        Value (output): The uniform load value. [F/L 2 ]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the area object specified by the Name item. If this item is
            Group, the assignments are retrieved for all area objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadUniform(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLoadUniform falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadWindPressure(self, Name: str, ItemType: int = 0):
        """This function retrieves the wind pressure load assignments to area objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of wind pressure loads retrieved for the
            specified area objects.
        AreaName (output): This is an array that includes the name of the area object
            associated with each wind pressure load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each wind pressure load.
        MyType (output): This is an array that includes either 1 or 2, indicating the wind
            pressure type. 1 = Windward, pressure varies over height 2 = Other, pressure is
            constant over height
        Cp (output): This is an array that includes the wind pressure coefficient value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the area object specified by the Name item. If this item is
            Group, the assignments are retrieved for all area objects in the group specified
            by the Name item. If this item is SelectedObjects, assignments are retrieved for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadWindPressure(Name, 0, [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLoadWindPressure falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxesAdvanced(self, Name: str):
        """This function retrieves the advanced local axes assignments to area objects. The function
        returns zero if the advanced local axes assignments are retrieved successfully;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object.
        Active (output): This is True if advanced local axes exist.
        Plane2 (output): This is 31 or 32, indicating that the local plane determined by the
            plane reference vector is the 3-1 plane or the 3-2 plane. This item applies only
            when the Active item is True.
        PlVectOpt (output): This is 1, 2, or 3, indicating the plane reference vector
            option. This item applies only when the Active item is True. 1 = Coordinate
            direction 2 = Two joints 3 = User vector
        PlCSys (output): The coordinate system used to define the plane reference vector
            coordinate directions and the plane user vector. This item applies when the
            Active item is True and the PlVectOpt item is 1 or 3.
        PlDir (output): This is an array dimensioned to 1 (2 integers) indicating the plane
            reference vector primary and secondary coordinate directions, PlDir(0) and
            PlDir(1) respectively, taken at the object center in the specified coordinate
            system and used to determine the plane reference vector. This item applies when
            the Active item is True and the PlVectOpt item is 1. Possible coordinate
            direction values are: 1 = +X -1 = -X 2 = +Y -2 = -Y 3 = +Z -3 = -Z 4 = +CR -4 =
            -CR 5 = +CA -5 = -CA 6 = +CZ -6 = -CZ 7 = +SR -7 = -SR 8 = +SA -8 = -SA 9 = +SB
            -9 = -SB
        PlPt (output): This is an array dimensioned to 1 (2 strings) indicating the labels
            of two joints that define the plane reference vector. Either of these joints may
            be specified as None to indicate the center of the specified object. If both
            joints are specified as None, they are not used to define the plane reference
            vector. This item applies when the Active item is True and the PlVectOpt item is
            2.
        PlVect (output): This is an array dimensioned to 2 (3 doubles) that defines the
            plane reference vector. This item applies when the Active item is True and the
            PlVectOpt item is 3.
        """
        _r = self._raw.GetLocalAxesAdvanced(Name, False, 0, 0, "", [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLocalAxesAdvanced falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str, Advanced: bool):
        """This function retrieves the local axis angle assignment for area objects. The function
        returns zero if the assignment is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area object.
        Ang (output): This is the angle that the local 1 and 2 axes are rotated about the
            positive local 3 axis from the default orientation. The rotation for a positive
            angle appears counter clockwise when the local +3 axis is pointing toward you.
            [deg]
        Advanced (input): This item is True if the area object local axes orientation was
            obtained using advanced local axes parameters.
        """
        _r = self._raw.GetLocalAxes(Name, 0.0, Advanced)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMass(self, Name: str, MassOverL2: float):
        """This function retrieves the mass per unit area assignment for area objects. The function
        returns zero if the mass assignment is successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing area object.
        MassOverL2 (input): The mass per unit area assigned to the area object. [M/L 2 ]
        """
        _r = self._raw.GetMass(Name, MassOverL2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetMass falhou (ret={_r})".format(_r=_r))
        return None

    def GetMatTemp(self, Name: str, Temp: float):
        """This function retrieves the material temperature assignments to area objects. The function
        returns zero if the material temperature assignments are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object.
        Temp (input): This is the material temperature value assigned to the area object.
            [T]
        PatternName (output): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the area object is uniform over the object
            at the value specified by Temp. If PatternName is the name of a defined joint
            pattern, the material temperature for the area object may vary. The material
            temperature at each corner point around the area object perimeter is equal to
            the specified temperature multiplied by the pattern value at the associated
            point object. The material temperature at other points in the area object is
            calculated by interpolation from the corner points.
        """
        _r = self._raw.GetMatTemp(Name, Temp, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetMatTemp falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMaterialOverwrite(self, Name: str):
        """This function retrieves the material overwrite assigned to an area object, if any. The
        material property name is indicated as None if there is no material overwrite
        assignment. The function returns zero if the material overwrite assignment is
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a defined area object.
        PropName (output): This is None, indicating that no material overwrite exists for
            the specified area object, or it is the name of an existing material property.
        """
        _r = self._raw.GetMaterialOverwrite(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetMaterialOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetModifiers(self, Name: str):
        """This function retrieves the modifier assignment for area objects. The default value for all
        modifiers is one. The function returns zero if the modifier assignments are
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object.
        Value (output): This is an array of ten unitless modifiers. Value(0) = Membrane f11
            modifier Value(1) = Membrane f22 modifier Value(2) = Membrane f12 modifier
            Value(3) = Bending m11 modifier Value(4) = Bending m22 modifier Value(5) =
            Bending m12 modifier Value(6) = Shear v13 modifier Value(7) = Shear v23 modifier
            Value(8) = Mass modifier Value(9) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined area objects. The function returns zero if
        the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of area object names retrieved by the program.
        MyName (output): This is a one-dimensional array of area object names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames 1) inside the Sap2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOffsets(self, Name: str):
        """This function retrieves the joint offset assignments for area objects. The function returns
        zero if the assignments are successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing area object.
        OffsetType (output): This is 0, 1 or 2, indicating the joint offset type. 0 = No
            joint offsets 1 = User defined joint offsets specified by joint pattern 2 = User
            defined joint offsets specified by point
        OffsetPattern (output): This item applies only when OffsetType = 1. It is the name
            of the defined joint pattern that is used to calculate the joint offsets.
        OffsetPatternSF (output): This item applies only when OffsetType = 1. It is the
            scale factor applied to the joint pattern when calculating the joint offsets.
            [L]
        Offset (output): This item applies only when OffsetType = 2. It is an array of joint
            offsets for each of the points that define the area object. [L]
        """
        _r = self._raw.GetOffsets(Name, 0, "", 0.0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetOffsets falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoints(self, Name: str):
        """This function retrieves the names of the point objects that define an area object. The
        function returns zero if the point object names are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a defined area object.
        NumberPoints (output): The number of point objects that define the area object.
        Point (output): This is an array containing the names of the point objects that
            define the area object. The point names are in order around the area object.
        """
        _r = self._raw.GetPoints(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetProperty(self, Name: str, PropName: str):
        """This function retrieves the area property assigned to an area object. The function returns
        zero if the property is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of a defined area object.
        PropName (input): The name of the area property assigned to the area object. This
            item is None if no area property is assigned to the area object.
        """
        _r = self._raw.GetProperty(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def GetSelectedEdge(self, Name: str):
        """This function retrieves the selected status for area object edges. The function returns zero
        if the selected status is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing area object.
        NumberEdges (output): The number of edges in the specified area object.
        Selected (output): This is an array of items that is True if the specified area
            object edge is selected; otherwise it is False. Selected(0) = Selected status
            for edge 1 Selected(1) = Selected status for edge 2 Selected(n) = Selected
            status for edge (n + 1) This array is internally dimensioned by Sap2000 to
            (NumberEdges 1).
        """
        _r = self._raw.GetSelectedEdge(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetSelectedEdge falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSelected(self, Name: str, Selected: bool):
        """This function retrieves the selected status for an area object. The function returns zero if
        the selected status is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object.
        Selected (input): This item is True if the specified area object is selected;
            otherwise it is False.
        """
        _r = self._raw.GetSelected(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetSelected falhou (ret={_r})".format(_r=_r))
        return None

    def GetSpring(self, Name: str, LinkProp: list[str]):
        """This function retrieves the spring assignments to an area object face. The function returns
        zero if the assignments are successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing area object.
        NumberSprings (output): The number of spring assignments made to the specified area
            object.
        MyType (output): Each value in this array is either 1 or 2, indicating the spring
            property type. 1 = Simple spring 2 = Link property
        s (output): Each value in this array is the simple spring stiffness per unit area of
            the specified area object face. This item applies only when the corresponding
            MyType = 1. [F/L 3 ]
        SimpleSpringType (output): Each value in this array is 1, 2 or 3, indicating the
            simple spring type. This item applies only when the corresponding MyType = 1. 1
            = Spring resists tension and compression 2 = Spring resists compression only 3 =
            Spring resists tension only
        LinkProp (input): Each value in this array is the name of the link property assigned
            to the spring. This item applies only when the corresponding MyType = 2.
        Face (output): Each value in this array is -1, -2 or a nonzero, positive integer,
            indicating the area object face to which the specified spring assignment
            applies. -1 = Bottom face -2 = Top face >0 = Edge face Note that edge face n is
            from area object point n to area object point n + 1. For example, edge face 2 is
            from area object point 2 to area object point 3.
        SpringLocalOneType (output): Each value in this array is 1, 2 or 3, indicating the
            method used to specify the spring positive local 1-axis orientation. 1 =
            Parallel to area object local axis 2 = Normal to specified area object face 3 =
            User specified direction vector
        Dir (output): Each value in this array is 1, 2, 3, -1, -2 or -3, indicating the area
            object local axis that corresponds to the positive local 1-axis of the spring.
            This item applies only when the corresponding SpringLocalOneType = 1.
        Outward (output): Each value in this array is True if the spring positive local 1
            axis is outward from the specified area object face. This item applies only when
            SpringLocalOneType = 2.
        VecX (output): Each value in this array is the X-axis or area object local 1-axis
            component (depending on the CSys specified) of the user specified direction
            vector for the spring local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when the corresponding
            SpringLocalOneType = 3.
        VecY (output): Each value in this array is the Y-axis or area object local 2-axis
            component (depending on the CSys specified) of the user specified direction
            vector for the spring local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when the corresponding
            SpringLocalOneType = 3.
        VecZ (output): Each value in this array is the X-axis or area object local 3-axis
            component (depending on the CSys specified) of the user specified direction
            vector for the spring local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when the corresponding
            SpringLocalOneType = 3.
        CSys (output): Each value in this array is Local (meaning the area object local
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
            raise Sap2000ApiError("SapModel.AreaObj.GetSpring falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetThickness(self, Name: str):
        """This function retrieves the thickness overwrite assignments for area objects. The function
        returns zero if the assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area object.
        ThicknessType (output): This is 0, 1 or 2, indicating the thickness overwrite type.
            0 = No thickness overwrites 1 = User defined thickness overwrites specified by
            joint pattern 2 = User defined thickness overwrites specified by point
        ThicknessPattern (output): This item applies only when ThicknessType = 1. It is the
            name of the defined joint pattern that is used to calculate the thicknesses.
        ThicknessPatternSF (output): This item applies only when ThicknessType = 1. It is
            the scale factor applied to the joint pattern when calculating the thicknesses.
            [L]
        Thickness (output): This item applies only when ThicknessType = 2. It is an array of
            thicknesses at each of the points that define the area object. [L]
        """
        _r = self._raw.GetThickness(Name, 0, "", 0.0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetThickness falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTransformationMatrix(self, Name: str, IsGlobal: bool = True):
        """The function returns zero if the area object transformation matrix is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the area object local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array, (Local1, Local2, Local3)
            are an item (such as a load) in the object local coordinate system, and
            (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.
            The transformation from the local coordinate system to the present coordinate
            system is the same as that shown above for the global system if you substitute
            the present system for the global system.
        IsGlobal (input): If this item is True, the transformation matrix is between the
            Global coordinate system and the area object local coordinate system. If this
            item is False, the transformation matrix is between the present coordinate
            system and the area object local coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [], IsGlobal)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaObj.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetAutoMesh(self, Name: str, MeshType: int, n1: int = 2, n2: int = 2, MaxSize1: float = 0, MaxSize2: float = 0, PointOnEdgeFromLine: bool = False, PointOnEdgeFromPoint: bool = False, ExtendCookieCutLines: bool = False, Rotation: float = 0, MaxSizeGeneral: float = 0, LocalAxesOnEdge: bool = False, LocalAxesOnFace: bool = False, RestraintsOnEdge: bool = False, RestraintsOnFace: bool = False, Group: str = 'ALL', SubMesh: bool = False, SubMeshSize: float = 0, ItemType: int = 0):
        """This function makes automatic meshing assignments to area objects. The function returns zero
        if the meshing options are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        MeshType (input): This item is 0, 1, 2, 3, 4, 5 or 6, indicating the automatic mesh
            type for the area object. 0 = No automatic meshing 1 = Mesh area into a
            specified number of objects 2 = Mesh area into objects of a specified maximum
            size 3 = Mesh area based on points on area edges 4 = Cookie cut mesh area based
            on lines intersecting edges 5 = Cookie cut mesh area based on points 6 = Mesh
            area using General Divide Tool Mesh options 1, 2 and 3 apply to quadrilaterals
            and triangles only.
        n1 (input): This item applies when MeshType = 1. It is the number of objects created
            along the edge of the meshed area object that runs from point 1 to point 2.
        n2 (input): This item applies when MeshType = 1. It is the number of objects created
            along the edge of the meshed area object that runs from point 1 to point 3.
        MaxSize1 (input): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed area object that runs from point 1
            to point 2. [L] If this item is input as 0, the default value is used. The
            default value is 48 inches if the database units are English or 120 centimeters
            if the database units are metric.
        MaxSize2 (input): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed area object that runs from point 1
            to point 3. [L] If this item is input as 0, the default value is used. The
            default value is 48 inches if the database units are English or 120 centimeters
            if the database units are metric.
        PointOnEdgeFromLine (input): This item applies when MeshType = 3. If it is True,
            points on the area object edges are determined from intersections of straight
            line objects included in the group specified by the Group item with the area
            object edges.
        PointOnEdgeFromPoint (input): This item applies when MeshType = 3. If it is True,
            points on the area object edges are determined from point objects included in
            the group specified by the Group item that lie on the area object edges.
        ExtendCookieCutLines (input): This item applies when MeshType = 4. MeshType = 4
            provides cookie cut meshing based on straight line objects included in the group
            specified by the Group item that intersect the area object edges. If the
            ExtendCookieCutLines item is True, all straight line objects included in the
            group specified by the Group item are extended to intersect the area object
            edges for the purpose of meshing the area object.
        Rotation (input): This item applies when MeshType = 5. MeshType = 5 provides cookie
            cut meshing based on two perpendicular lines passing through point objects
            included in the group specified by the Group item. By default these lines align
            with the area object local 1 and 2 axes. The Rotation item is an angle in
            degrees that the meshing lines are rotated from their default orientation. [deg]
        MaxSizeGeneral (input): This item applies when MeshType = 6. It is the maximum size
            of objects created by the General Divide Tool. If this item is input as 0, the
            default value is used. The default value is 48 inches if the database units are
            English or 120 centimeters if the database units are metric.
        LocalAxesOnEdge (input): If this item is True, and if both points along an edge of
            the original area object have the same local axes, then the program makes the
            local axes for added points along the edge the same as the edge end points.
        LocalAxesOnFace (input): If this item is True, and if all points around the
            perimeter of the original area object have the same local axes, the program
            makes the local axes for all added points the same as the perimeter points.
        RestraintsOnEdge (input): If this item is True, and if both points along an edge of
            the original area object have the same restraint/constraint, then, if the added
            point and the adjacent corner points have the same local axes definition, the
            program includes the restraint/constraint for added points along the edge.
        RestraintsOnFace (input): If this item is True, and if all points around the
            perimeter of the original area object have the same restraint/constraint, then,
            if an added point and the perimeter points have the same local axes definition,
            the program includes the restraint/constraint for the added point.
        Group (input): The name of a defined group. Some of the meshing options make use of
            point and line objects included in this group.
        SubMesh (input): If this item is True, after initial meshing, the program further
            meshes any area objects that have an edge longer than the length specified by
            the SubMeshSize item.
        SubMeshSize (input): This item applies when the SubMesh item is True. It is the
            maximum size of area objects to remain when the auto meshing is complete. [L] If
            this item is input as 0, the default value is used. The default value is 12
            inches if the database units are English or 30 centimeters if the database units
            are metric.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetAutoMesh(Name, MeshType, n1, n2, MaxSize1, MaxSize2, PointOnEdgeFromLine, PointOnEdgeFromPoint, ExtendCookieCutLines, Rotation, MaxSizeGeneral, LocalAxesOnEdge, LocalAxesOnFace, RestraintsOnEdge, RestraintsOnFace, Group, SubMesh, SubMeshSize, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetAutoMesh falhou (ret={_r})".format(_r=_r))
        return None

    def SetEdgeConstraint(self, Name: str, ConstraintExists: bool, ItemType: int = 0):
        """This function makes generated edge constraint assignments to area objects. The function
        returns zero if the edge constraint option is successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        ConstraintExists (input): This item is True if an automatic edge constraint is
            generated by the program for the area object in the analysis model.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetEdgeConstraint(Name, ConstraintExists, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetEdgeConstraint falhou (ret={_r})".format(_r=_r))
        return None

    def SetGUID(self, Name: str, GUID: str = ''):
        """This function sets the GUID for the specified area object. If the GUID is passed in as a
        blank string, the program automatically creates a GUID for the object. This function
        returns zero if the area object GUID is successfully set; otherwise, it returns
        nonzero.
    
        Name (input): The name of an existing area object.
        GUID (input): The GUID (Global Unique ID) for the specified area object.
        """
        _r = self._raw.SetGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetGUID falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroupAssign(self, Name: str, GroupName: str, Remove: bool, ItemType: int = 0):
        """This function adds or removes area objects from a specified group. The function returns zero
        if the group assignment is successful; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        GroupName (input): The name of an existing group to which the assignment is made.
        Remove (input): If this item is False, the specified area objects are added to the
            group specified by the GroupName item. If it is True, the area objects are
            removed from the group.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the area object
            specified by the Name item is added or removed from the group specified by the
            GroupName item. If this item is Group, all area objects in the group specified
            by the Name item are added or removed from the group specified by the GroupName
            item. If this item is SelectedObjects, all selected area objects are added or
            removed from the group specified by the GroupName item, and the Name item is
            ignored.
        """
        _r = self._raw.SetGroupAssign(Name, GroupName, Remove, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetGroupAssign falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadGravity(self, Name: str, LoadPat: str, x: float, y: float, z: float, Replace: bool = True, CSys: str = 'Global', ItemType: int = 0):
        """This function assigns gravity load multipliers to area objects. The function returns zero if
        the loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Replace (input): If this item is True, all previous gravity loads, if any, assigned
            to the specified area object(s), in the specified load pattern, are deleted
            before making the new assignment.
        CSys (input): The coordinate system in which the x, y and z multipliers are
            specified.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadGravity(Name, LoadPat, x, y, z, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadPorePressure(self, Name: str, LoadPat: str, Value: float, PatternName: str = '', Replace: bool = True, ItemType: int = 0):
        """This function assigns pore pressure loads to area objects. The function returns zero if the
        loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Value (input): This is the pore pressure value. [F/L 2 ]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the pore pressure load for the area object is uniform over the object at
            the value specified by Value. If PatternName is the name of a defined joint
            pattern, the pore pressure load for the area object is based on the specified
            pore pressure value multiplied by the pattern value at the point objects that
            define the area object.
        Replace (input): If this item is True, all previous pore pressure loads, if any,
            assigned to the specified area object(s), in the specified load case, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadPorePressure(Name, LoadPat, Value, PatternName, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLoadPorePressure falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadRotate(self, Name: str, LoadPat: str, Value: float, ItemType: int = 0):
        """This function assigns rotate loads to area objects. The function returns zero if the loads
        are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Value (input): This is the angular velocity. [Cyc/T]
        """
        _r = self._raw.SetLoadRotate(Name, LoadPat, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLoadRotate falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadStrain(self, Name: str, LoadPat: str, Component: int, Value: float, Replace: bool = True, PatternName: str = '', ItemType: int = 0):
        """This function assigns strain loads to area objects. The function returns zero if the loads
        are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Component (input): This is 1, 2, 3, 4, 5, 6, 7, 8, or 9, indicating the component to
            which the strain load is applied. 1 = Strain11 2 = Strain22 3 = Strain12 4 =
            Curvature11 5 = Curvature22 6 = Curvature12 7 = Strain13 8 = Strain23 9 =
            Strain33
        Value (input): This is the strain load value. [L/L] for Component = 1, 2, 3, 7, 8,
            and 9 and [1/L] for Component = 4, 5 and 6
        Replace (input): If this item is True, all previous strain loads, if any, assigned
            to the specified area object(s), in the specified load pattern, for the
            specified degree of freedom, are deleted before making the new assignment.
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the strain load for the area object is uniform over the object at the
            value specified by Value. If PatternName is the name of a defined joint pattern,
            the strain load for the area object is based on the specified strain value
            multiplied by the pattern value at the corner points of the area object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadStrain(Name, LoadPat, Component, Value, Replace, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadSurfacePressure(self, Name: str, LoadPat: str, Face: int, Value: float, PatternName: str = '', Replace: bool = True, ItemType: int = 0):
        """This function assigns surface pressure loads to area objects. The function returns zero if
        the loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Face (input): This is -1, -2 or a nonzero, positive integer, indicating the area
            object face to which the specified load assignment applies. -1 = Bottom face -2
            = Top face >0 = Edge face Note that edge face n is from area object point n to
            area object point n + 1. For example, edge face 2 is from area object point 2 to
            area object point 3.
        Value (input): This is the surface pressure value. [F/L 2 ]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the surface pressure load for the area object face is uniform over the
            face at the value specified by Value. If PatternName is the name of a defined
            joint pattern, the surface pressure load for the area object face is based on
            the specified surface pressure value multiplied by the pattern value at the
            point objects that are part of the face.
        Replace (input): If this item is True, all previous surface pressure loads, if any,
            assigned to the specified area object(s), in the specified load case, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadSurfacePressure(Name, LoadPat, Face, Value, PatternName, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLoadSurfacePressure falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadTemperature(self, Name: str, LoadPat: str, MyType: int, Value: float, PatternName: str = '', Replace: bool = True, ItemType: int = 0):
        """This function assigns temperature loads to area objects. The function returns zero if the
        loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        MyType (input): This is either 1 or 3, indicating the type of temperature load. 1 =
            Temperature 3 = Temperature gradient along local 3 axis
        Value (input): This is the temperature change value. [T] for MyType = 1 and [T/L]
            for MyType = 3
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the temperature load for the area object is uniform over the object at
            the value specified by Value. If PatternName is the name of a defined joint
            pattern the temperature load for the area object is based on the specified
            temperature value multiplied by the pattern value at the joints that define the
            area object.
        Replace (input): If this item is True, all previous temperature loads, if any,
            assigned to the specified area object(s), in the specified load case, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadTemperature(Name, LoadPat, MyType, Value, PatternName, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadUniform(self, Name: str, LoadPat: str, Value: float, Dir: int, Replace: bool = True, CSys: str = 'Global', ItemType: int = 0):
        """This function assigns uniform loads to area objects. The function returns zero if the loads
        are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Value (input): The uniform load value. [F/L 2 ]
        Dir (input): This is an integer between 1 and 11, indicating the direction of the
            load. 1 = Local 1 axis (only applies when CSys is Local) 2 = Local 2 axis (only
            applies when CSys is Local) 3 = Local 3 axis (only applies when CSys is Local) 4
            = X direction (does not apply when CSys is Local) 5 = Y direction (does not
            apply when CSys is Local) 6 = Z direction (does not apply when CSys is Local) 7
            = Projected X direction (does not apply when CSys is Local) 8 = Projected Y
            direction (does not apply when CSys is Local) 9 = Projected Z direction (does
            not apply when CSys is Local) 10 = Gravity direction (only applies when CSys is
            Global) 11 = Projected Gravity direction (only applies when CSys is Global) The
            positive gravity direction (see Dir = 10 and 11) is in the negative Global Z
            direction.
        Replace (input): If this item is True, all previous uniform loads, if any, assigned
            to the specified area object(s), in the specified load pattern, are deleted
            before making the new assignment.
        CSys (input): This is Local or the name of a defined coordinate system, indicating
            the coordinate system in which the uniform load is specified.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadUniform(Name, LoadPat, Value, Dir, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLoadUniform falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadUniformToFrame(self, Name: str, LoadPat: str, Value: float, Dir: int, DistType: int, Replace: bool = True, CSys: str = 'Global', ItemType: int = 0):
        """This function assigns uniform to frame loads to area objects. The function returns zero if
        the loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group depending on the value of
            the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Value (input): The uniform load value. [F/L 2 ]
        Dir (input): This is an integer between 1 and 11, indicating the direction of the
            load. 1 = Local 1 axis (only applies when CSys is Local) 2 = Local 2 axis (only
            applies when CSys is Local) 3 = Local 3 axis (only applies when CSys is Local) 4
            = X direction (does not apply when CSys is Local) 5 = Y direction (does not
            apply when CSys is Local) 6 = Z direction (does not apply when CSys is Local) 7
            = Projected X direction (does not apply when CSys is Local) 8 = Projected Y
            direction (does not apply when CSys is Local) 9 = Projected Z direction (does
            not apply when CSys is Local) 10 = Gravity direction (only applies when CSys is
            Global) 11 = Projected Gravity direction (only applies when CSys is Global) The
            positive gravity direction (see Dir = 10 and 11) is in the negative Global Z
            direction.
        DistType (input): This is either 1 or 2, indicating the load distribution type. 1 =
            One-way load distribution 2 = Two-way load distribution One-way distribution is
            parallel to the area object local 1 axis. Two-way distribution is parallel to
            the area object local 1 and 2 axes.
        Replace (input): If this item is True, all previous uniform loads, if any, assigned
            to the specified area object(s), in the specified load pattern, are deleted
            before making the new assignment.
        CSys (input): This is Local or the name of a defined coordinate system, indicating
            the coordinate system in which the uniform load is specified.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects and the Name item is ignored.
        """
        _r = self._raw.SetLoadUniformToFrame(Name, LoadPat, Value, Dir, DistType, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLoadUniformToFrame falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadWindPressure(self, Name: str, LoadPat: str, MyType: float, Cp: float, ItemType: int = 0):
        """This function assigns wind pressure loads to area objects. The function returns zero if the
        loads are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        MyType (input): This is either 1 or 2, indicating the wind pressure type. 1 =
            Windward, pressure varies over height 2 = Other, pressure is constant over
            height
        Cp (input): This is the wind pressure coefficient.
        """
        _r = self._raw.SetLoadWindPressure(Name, LoadPat, MyType, Cp, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLoadWindPressure falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxesAdvanced(self, Name: str, Active: bool, Plane2: int, PlVectOpt: int, PlCSys: str, PlDir: list[int], PlPt: list[str], PlVect: list[float], ItemType: int = 0):
        """This function assigns advanced local axes to area objects. The function returns zero if the
        advanced local axes assignments are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area object or group depending on the value of
            the ItemType item.
        Active (input): This is True if advanced local axes exist.
        Plane2 (input): This is 31 or 32, indicating that the local plane determined by the
            plane reference vector is the 3-1 plane or the 3-2 plane. This item applies only
            when the Active item is True.
        PlVectOpt (input): This is 1, 2, or 3, indicating the plane reference vector option.
            This item applies only when the Active item is True. 1 = Coordinate direction 2
            = Two joints 3 = User vector
        PlCSys (input): The coordinate system used to define the plane reference vector
            coordinate directions and the plane user vector. This item applies when the
            Active item is True and the PlVectOpt item is 1 or 3.
        PlDir (input): This is an array dimensioned to 1 (2 integers), indicating the plane
            reference vector primary and secondary coordinate directions, PlDir(0) and
            PlDir(1) respectively, taken at the object center in the specified coordinate
            system and used to determine the plane reference vector. This item applies when
            the Active item is True and the PlVectOpt item is 1. Possible coordinate
            direction values are: 1 = +X -1 = -X 2 = +Y -2 = -Y 3 = +Z -3 = -Z 4 = +CR -4 =
            -CR 5 = +CA -5 = -CA 6 = +CZ -6 = -CZ 7 = +SR -7 = -SR 8 = +SA -8 = -SA 9 = +SB
            -9 = -SB
        PlPt (input): This is an array dimensioned to 1 (2 strings) indicating the labels of
            two joints that define the plane reference vector. Either of these joints may be
            specified as None to indicate the center of the specified object. If both joints
            are specified as None, they are not used to define the plane reference vector.
            This item applies when the Active item is True and the PlVectOpt item is 2.
        PlVect (input): This is an array dimensioned to 2 (3 doubles) that defines the plane
            reference vector. This item applies when the Active item is True and the
            PlVectOpt item is 3.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 Selection = 2 If this item is Object, the assignment is
            made to the area object specified by the Name item. If this item is Group, the
            assignment is made to all area objects in the group specified by the Name item.
            If this item is Selection, assignment is made to all selected area objects and
            the Name item is ignored.
        """
        _r = self._raw.SetLocalAxesAdvanced(Name, Active, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLocalAxesAdvanced falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxes(self, Name: str, Ang: float, ItemType: int = 0):
        """This function assigns a local axis angle to area objects. The function returns zero if the
        local axis angle is successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        Ang (input): This is the angle that the local 1 and 2 axes are rotated about the
            positive local 3 axis from the default orientation. The rotation for a positive
            angle appears counter clockwise when the local +3 axis is pointing toward you.
            [deg]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLocalAxes(Name, Ang, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetLocalAxes falhou (ret={_r})".format(_r=_r))
        return None

    def SetMass(self, Name: str, MassOverL2: float, Replace: bool = False, ItemType: int = 0):
        """This function assigns mass per unit area to area objects. The function returns zero if the
        mass is successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        MassOverL2 (input): The mass per unit area assigned to the area object. [M/L 2 ]
        Replace (input): If this item is True, all existing mass assignments to the area
            object are removed before assigning the specified mas. If it is False, the
            specified mass is added to any existing mass already assigned to the area
            object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects and the Name item is ignored.
        """
        _r = self._raw.SetMass(Name, MassOverL2, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetMass falhou (ret={_r})".format(_r=_r))
        return None

    def SetMatTemp(self, Name: str, Temp: float, PatternName: str = '', ItemType: int = 0):
        """This function assigns material temperatures to area objects. The function returns zero if
        the material temperatures are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        Temp (input): This is the material temperature value assigned to the area object.
            [T]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the area object is uniform over the object
            at the value specified by Temp. If PatternName is the name of a defined joint
            pattern, the material temperature for the area object may vary. The material
            temperature at each corner point around the area object perimeter is equal to
            the specified temperature multiplied by the pattern value at the associated
            point object. The material temperature at other points in the area object is
            calculated by interpolation from the corner points.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetMatTemp(Name, Temp, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetMatTemp falhou (ret={_r})".format(_r=_r))
        return None

    def SetMaterialOverwrite(self, Name: str, PropName: str, ItemType: int = 0):
        """This function sets the material overwrite assignment for area objects. The function returns
        zero if the material overwrite assignment is successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        PropName (input): This is None or a blank string, indicating that any existing
            material overwrites assigned to the specified area objects are to be removed, or
            it is the name of an existing material property.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetMaterialOverwrite(Name, PropName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetMaterialOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetModifiers(self, Name: str, Value: list[float], ItemType: int = 0):
        """This function sets the modifier assignment for area objects. The default value for all
        modifiers is one. The function returns zero if the modifier assignments are
        successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        Value (input): This is an array of ten unitless modifiers. Value(0) = Membrane f11
            modifier Value(1) = Membrane f22 modifier Value(2) = Membrane f12 modifier
            Value(3) = Bending m11 modifier Value(4) = Bending m22 modifier Value(5) =
            Bending m12 modifier Value(6) = Shear v13 modifier Value(7) = Shear v23 modifier
            Value(8) = Mass modifier Value(9) = Weight modifier
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetModifiers(Name, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetModifiers falhou (ret={_r})".format(_r=_r))
        return None

    def SetOffsets(self, Name: str, OffsetType: int, OffsetPattern: str, OffsetPatternSF: float, Offset: list[float], ItemType: int = 0):
        """This function sets the joint offset assignments for area objects. The function returns zero
        if the offsets are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        OffsetType (input): This is 0, 1 or 2, indicating the joint offset type. 0 = No
            joint offsets 1 = User defined joint offsets specified by joint pattern 2 = User
            defined joint offsets specified by point
        OffsetPattern (input): This item applies only when OffsetType = 1. It is the name of
            the defined joint pattern that is used to calculate the joint offsets.
        OffsetPatternSF (input): This item applies only when OffsetType = 1. It is the scale
            factor applied to the joint pattern when calculating the joint offsets. [L]
        Offset (input): This item applies only when OffsetType = 2. It is an array of joint
            offsets for each of the points that define the area object. [L]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOffsets(Name, OffsetType, OffsetPattern, OffsetPatternSF, Offset, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetOffsets falhou (ret={_r})".format(_r=_r))
        return None

    def SetProperty(self, name: str, PropName: str, ItemType: int = 0):
        """This function assigns an area property to area objects. The function returns zero if the
        property is successfully assigned; otherwise it returns a nonzero value.
    
        PropName (input): This is None or the name of a area property to be assigned to the
            specified area object(s). None means that no property is assigned to the area
            object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetProperty(name, PropName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def SetSelectedEdge(self, Name: str, EdgeNum: int, Selected: bool):
        """This function sets the selected status for area object edges. The function returns zero if
        the selected status is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object.
        EdgeNum (input): The area object edge that is have its selected status set.
        Selected (input): This item is True if the specified area object edge is selected;
            otherwise it is False.
        """
        _r = self._raw.SetSelectedEdge(Name, EdgeNum, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetSelectedEdge falhou (ret={_r})".format(_r=_r))
        return None

    def SetSelected(self, Name: str, Selected: bool, ItemType: int = 0):
        """This function sets the selected status for area objects. The function returns zero if the
        selected status is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        Selected (input): This item is True if the specified area object is selected,
            otherwise it is False.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the selected
            status is set for the area object specified by the Name item. If this item is
            Group, the selected status is set for all area objects in the group specified by
            the Name item. If this item is SelectedObjects, the selected status is set for
            all selected area objects, and the Name item is ignored.
        """
        _r = self._raw.SetSelected(Name, Selected, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetSelected falhou (ret={_r})".format(_r=_r))
        return None

    def SetSpring(self, Name: str, MyType: int, s: float, SimpleSpringType: int, LinkProp: str, Face: int, SpringLocalOneType: int, Dir: int, Outward: bool, Vec: list[float], Ang: float, Replace: bool, CSys: str = 'Local', ItemType: int = 0):
        """This function makes spring assignments to area objects. The springs are assigned to a
        specified area object face. The function returns zero if the assignments are
        successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        MyType (input): This is either 1 or 2, indicating the spring property type. 1 =
            Simple spring 2 = Link property
        s (input): The simple spring stiffness per unit area of the specified area object
            face. This item applies only when MyType = 1. [F/L 3 ]
        SimpleSpringType (input): This is 1, 2 or 3, indicating the simple spring type. This
            item applies only when MyType = 1. 1 = Spring resists tension and compression 2
            = Spring resists compression only 3 = Spring resists tension only
        LinkProp (input): The name of the link property assigned to the spring. This item
            applies only when MyType = 2.
        Face (input): This is -1, -2 or a nonzero, positive integer indicating the area
            object face to which the specified spring assignment applies. -1 = Bottom face
            -2 = Top face >0 = Edge face Note that edge face n is from area object point n
            to area object point n + 1. For example, edge face 2 is from area object point 2
            to area object point 3.
        SpringLocalOneType (input): This is 1, 2 or 3, indicating the method used to specify
            the spring positive local 1-axis orientation. 1 = Parallel to area object local
            axis 2 = Normal to specified area object face 3 = User specified direction
            vector
        Dir (input): This is 1, 2, 3, -1, -2 or -3, indicating the area object local axis
            that corresponds to the positive local 1-axis of the spring. This item applies
            only when SpringLocalOneType = 1.
        Outward (input): This item is True if the spring positive local 1 axis is outward
            from the specified area object face. This item applies only when
            SpringLocalOneType = 2.
        Vec (input): This is an array of three values that define the direction vector of
            the spring positive local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when
            SpringLocalOneType = 3.
        Ang (input): This is the angle that the link local 2-axis is rotated from its
            default orientation. This item applies only when MyType = 2. [deg]
        Replace (input): If this item is True, all existing spring assignments to the area
            object are removed before assigning the specified spring. If it is False, the
            specified spring is added to any existing springs already assigned to the area
            object.
        CSys (input): This is Local (meaning the area object local coordinate system) or the
            name of a defined coordinate system. This item is the coordinate system in which
            the user specified direction vector, Vec, is specified. This item applies only
            when SpringLocalOneType = 3.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetSpring(Name, MyType, s, SimpleSpringType, LinkProp, Face, SpringLocalOneType, Dir, Outward, Vec, Ang, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetSpring falhou (ret={_r})".format(_r=_r))
        return None

    def SetThickness(self, Name: str, ThicknessType: int, ThicknessPattern: str, ThicknessPatternSF: float, Thickness: list[float], ItemType: int = 0):
        """This function sets the thickness overwrite assignments for area objects. The function
        returns zero if the thickness overwrites are successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area object or group, depending on the value
            of the ItemType item.
        ThicknessType (input): This is 0, 1 or 2, indicating the thickness overwrite type. 0
            = No thickness overwrites 1 = User defined thickness overwrites specified by
            joint pattern 2 = User defined thickness overwrites specified by point
        ThicknessPattern (input): This item applies only when ThicknessType = 1. It is the
            name of the defined joint pattern that is used to calculate the thicknesses.
        ThicknessPatternSF (input): This item applies only when ThicknessType = 1. It is the
            scale factor applied to the joint pattern when calculating the thicknesses. [L]
        Thickness (input): This item applies only when ThicknessType = 2. It is an array of
            thicknesses at each of the points that define the area object. [L]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the area object specified by the Name item. If this item is Group,
            the assignment is made to all area objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected area
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetThickness(Name, ThicknessType, ThicknessPattern, ThicknessPatternSF, Thickness, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaObj.SetThickness falhou (ret={_r})".format(_r=_r))
        return None


