"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PointObj:
    """Wrapper para SapModel.PointObj."""

    def __init__(self, raw):
        self._raw = raw

    def AddCartesian(self, x: float, y: float, z: float, userName: str = '', csys: str = 'Global', MergeOff: bool = False, MergeNumber: int = 0):
        """This function adds a point object to a model. The added point object will be tagged as a
        Special Point except if it was merged with another point object. Special points are
        allowed to exist in the model with no objects connected to them. The function
        returns zero if the point object is successfully added or merged, otherwise it
        returns a nonzero value.
    
        x (input): The X-coordinate of the added point object in the specified coordinate
            system. [L]
        y (input): The Y-coordinate of the added point object in the specified coordinate
            system. [L]
        z (input): The Z-coordinate of the added point object in the specified coordinate
            system. [L]
        Name (output): This is the name that the program ultimately assigns for the point
            object. If no UserName is specified, the program assigns a default name to the
            point object. If a UserName is specified and that name is not used for another
            point, the UserName is assigned to the point; otherwise a default name is
            assigned to the point. If a point is merged with another point, this will be the
            name of the point object with which it was merged.
        MergeOff (input): If this item is False, a new point object that is added at the
            same location as an existing point object will be merged with the existing point
            object (assuming the two point objects have the same MergeNumber) and thus only
            one point object will exist at the location. If this item is True, the points
            will not merge and two point objects will exist at the same location.
        MergeNumber (input): Two points objects in the same location will merge only if
            their merge number assignments are the same. By default all pointobjects have a
            merge number of zero.
        """
        _r = self._raw.AddCartesian(x, y, z, "", userName, csys, MergeOff, MergeNumber)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.AddCartesian falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def AddCylindrical(self, r: float, Theta: float, z: float, userName: str = '', csys: str = 'Global', MergeOff: bool = False, MergeNumber: int = 0):
        """This function adds a point object to a model. The added point object will be tagged as a
        Special Point except if it was merged with another point object. Special points are
        allowed to exist in the model with no objects connected to them The function returns
        zero if the point object is successfully added or merged, otherwise it returns a
        nonzero value.
    
        r (input): The radius for the added point object in the specified coordinate system.
            [L]
        Theta (input): The angle for the added point object in the specified coordinate
            system. The angle is measured in the XY plane from the positive global X axis.
            When looking in the XY plane with the positive Z axis pointing toward you, a
            positive Theta angle is counter clockwise. [deg]
        z (input): The Z-coordinate of the added point object in the specified coordinate
            system. [L]
        Name (output): This is the name that the program ultimately assigns for the point
            object. If no UserName is specified, the program assigns a default name to the
            point object. If a UserName is specified and that name is not used for another
            point, the UserName is assigned to the point; otherwise a default name is
            assigned to the point. If a point is merged with another point, this will be the
            name of the point object with which it was merged.
        MergeOff (input): If this item is False, a new point object that is added at the
            same location as an existing point object will be merged with the existing point
            object (assuming the two point objects have the same MergeNumber) and thus only
            one point object will exist at the location. If this item is True, the points
            will not merge and two point objects will exist at the same location.
        MergeNumber (input): Two points objects in the same location will merge only if
            their merge number assignments are the same. By default all pointobjects have a
            merge number of zero.
        """
        _r = self._raw.AddCylindrical(r, Theta, z, "", userName, csys, MergeOff, MergeNumber)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.AddCylindrical falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def AddSpherical(self, r: float, a: float, b: float, userName: str = '', csys: str = 'Global', MergeOff: bool = False, MergeNumber: int = 0):
        """This function adds a point object to a model. The added point object will be tagged as a
        Special Point except if it was merged with another point object. Special points are
        allowed to exist in the model with no objects connected to them The function returns
        zero if the point object is successfully added or merged, otherwise it returns a
        nonzero value.
    
        r (input): The radius for the added point object in the specified coordinate system.
            [L]
        a (input): The plan angle for the added point object in the specified coordinate
            system. This angle is measured in the XY plane from the positive global X axis.
            When looking in the XY plane with the positive Z axis pointing toward you, a
            positive a angle is counterclockwise. [deg]
        b (input): The elevation angle for the added point object in the specified
            coordinate system. This angle is measured in an X'Z plane that is perpendicular
            to the XY plane with the positive X' axis oriented at angle a from the positive
            global X axis. Angle b is measured from the positive global Z axis. When looking
            in the XZ plane with the positive Y' axis pointing toward you, a positive b
            angle is counter clockwise. [deg]
        Name (output): This is the name that the program ultimately assigns for the point
            object. If no UserName is specified, the program assigns a default name to the
            point object. If a UserName is specified and that name is not used for another
            point, the UserName is assigned to the point; otherwise a default name is
            assigned to the point. If a point is merged with another point, this will be the
            name of the point object with which it was merged.
        MergeOff (input): If this item is False, a new point object that is added at the
            same location as an existing point object will be merged with the existing point
            object (assuming the two point objects have the same MergeNumber) and thus only
            one point object will exist at the location. If this item is True, the points
            will not merge and two point objects will exist at the same location.
        MergeNumber (input): Two points objects in the same location will merge only if
            their merge number assignments are the same. By default all pointobjects have a
            merge number of zero.
        """
        _r = self._raw.AddSpherical(r, a, b, "", userName, csys, MergeOff, MergeNumber)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.AddSpherical falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value.
    
        Name (input): The existing name of a point object.
        NewName (input): The new name for the point object.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def CountConstraint(self, Name: str = ''):
        """If the Name item is provided, the Count item returns the total number of constraint
        assignments made to the specified point object. If the Name item is not specified,
        or is specified as an empty string, the Count item returns the total number of
        constraint assignments to all point objects in the model. If the Name item is
        specified but it is not recognized by the program as a valid point object, an error
        is returned. This function returns zero if the count is successfully completed,
        otherwise it returns a nonzero value.
    
        Count (output): The number of counted constraints.
        Name (input): This optional item is the name of an existing point object.
        """
        _r = self._raw.CountConstraint(0, Name)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.CountConstraint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def CountLoadDispl(self, Name: str = '', LoadPat: str = ''):
        """If neither the Name item nor the LoadPat item is provided, the Count item returns the total
        number of ground displacement load assignments in the model. If the Name item is
        provided but not the LoadPat item, the Count item returns the total number of ground
        displacement load assignments made for the specified point object. If the Name item
        is not provided but the LoadPat item is specified, the Count item returns the total
        number of ground displacement load assignments made to all point objects for the
        specified load pattern. If both the Name item and the LoadPat item are provided, the
        Count item returns the total number of ground displacement load assignments made to
        the specified point object for the specified load pattern. If the Name item or the
        LoadPat item is provided but is not recognized by the program as valid, an error is
        returned. This function returns zero if the count is successfully completed,
        otherwise it returns a nonzero value.
    
        Count (output): The number of counted ground displacement loads.
        Name (input): This optional item is the name of an existing point object.
        LoadPat (input): This optional item is the name of an existing load pattern.
        """
        _r = self._raw.CountLoadDispl(0, Name, LoadPat)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.CountLoadDispl falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def CountLoadForce(self, Name: str = '', LoadPat: str = ''):
        """If neither the Name item nor the LoadPat item is provided, the Count item returns the total
        number of point load assignments in the model. If the Name item is provided but not
        the LoadPat item, the Count item returns the total number of point load assignments
        made for the specified point object. If the Name item is not provided but the
        LoadPat item is specified, the Count item returns the total number of point load
        assignments made to all point objects for the specified load pattern. If both the
        Name item and the LoadPat item are provided,n the Count item returns the total
        number of point load assignments made to the specified point object for the
        specified load pattern. If the Name item or the LoadPat item is provided but is not
        recognized by the program as valid, an error is returned. This function returns zero
        if the count is successfully completed, otherwise it returns a nonzero value.
    
        Count (output): The number of counted point loads.
        Name (input): This optional item is the name of an existing point object.
        LoadPat (input): This optional item is the name of an existing load pattern.
        """
        _r = self._raw.CountLoadForce(0, Name, LoadPat)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.CountLoadForce falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def CountPanelZone(self):
        """This function returns the total number of panel zone assignments to point objects in the
        model.
        """
        _r = self._raw.CountPanelZone()
        return _r

    def CountRestraint(self):
        """This function returns the total number of point objects in the model with restraint
        assignments.
        """
        _r = self._raw.CountRestraint()
        return _r

    def CountSpring(self):
        """This function returns the total number of point objects in the model with spring
        assignments.
        """
        _r = self._raw.CountSpring()
        return _r

    def Count(self):
        """This function returns the total number of point objects in the model.
        """
        _r = self._raw.Count()
        return _r

    def DeleteConstraint(self, Name: str, ItemType: int = 0):
        """This function deletes all constraint assignments from the specified point object(s). The
        function returns zero if the constraint assignments are successfully deleted,
        otherwise it returns a nonzero value.
    
        Name (input): The name of a point object or a group depending on the value selected
            for ItemType item.
        ItemType (input): This is one of the following items from the eItemType enumeration.
            Object = 0 Group = 1 SelectedObjects = 2 If Object is selected, the Name item
            refers to a point object and the constraint assignments to that point object are
            removed. If Group is selected, the Name item refers to a group and the
            constraint assignments to all point objects in the group are removed. If
            SelectedObjects is selected, the Name item is ignored and the constraint
            assignments to all selected point objects are removed.
        """
        _r = self._raw.DeleteConstraint(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.DeleteConstraint falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadDispl(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes all ground displacement load assignments, for the specified load
        pattern, from the specified point object(s). The function returns zero if the load
        assignments are successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of a point object or a group depending on the value selected
            for ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items from the eItemType enumeration.
            Object = 0 Group = 1 SelectedObjects = 2 If Object is selected, the Name item
            refers to a point object. The ground displacement load assignments, for the
            specified load case, made to that point object, are removed. If Group is
            selected, the Name item refers to a group. The ground displacement load
            assignments, for the specified load pattern, made to all point objects in the
            group, are removed. If SelectedObjects is selected, the Name item is ignored.
            The ground displacement load assignments, for the specified load pattern, made
            to all selected point objects, are removed.
        """
        _r = self._raw.DeleteLoadDispl(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.DeleteLoadDispl falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadForce(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes all point load assignments, for the specified load pattern, from the
        specified point object(s). The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of a point object or a group depending on the value selected
            for ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items from the eItemType enumeration.
            Object = 0 Group = 1 SelectedObjects = 2 If Object is selected, the Name item
            refers to a point object. The point load assignments, for the specified load
            pattern, made to that point object, are removed. If Group is selected, the Name
            item refers to a group. The point load assignments, for the specified load
            pattern, made to all point objects in the group, are removed. If SelectedObjects
            is selected, the Name item is ignored. The point load assignments, for the
            specified load pattern, made to all selected point objects, are removed.
        """
        _r = self._raw.DeleteLoadForce(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.DeleteLoadForce falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteMass(self, Name: str, ItemType: int = 0):
        """This function deletes all mass assignments from the specified point object(s). The function
        returns zero if the mass assignments are successfully deleted, otherwise it returns
        a nonzero value.
    
        Name (input): The name of a point object or a group depending on the value selected
            for ItemType item.
        ItemType (input): This is one of the following items from the eItemType enumeration.
            Object = 0 Group = 1 SelectedObjects = 2 If Object is selected, the Name item
            refers to a point object. The mass assignments for that point object are
            removed. If Group is selected, the Name item refers to a group. The mass
            assignments for all point objects in the group are removed. If SelectedObjects
            is selected, the Name item is ignored. The mass assignments for all selected
            point objects are removed.
        """
        _r = self._raw.DeleteMass(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.DeleteMass falhou (ret={_r})".format(_r=_r))
        return None

    def DeletePanelZone(self, Name: str, ItemType: int = 0):
        """This function deletes all panel zone assignments from the specified point object(s). The
        function returns zero if the panel zone assignments are successfully deleted,
        otherwise it returns a nonzero value.
    
        Name (input): The name of a point object or a group depending on the value selected
            for ItemType item.
        ItemType (input): This is one of the following items from the eItemType enumeration.
            Object = 0 Group = 1 SelectedObjects = 2 If Object is selected, the Name item
            refers to a point object. The panel zone assignments for that point object are
            removed. If Group is selected, the Name item refers to a group. The panel zone
            assignments for all point objects in the group are removed. If SelectedObjects
            is selected, the Name item is ignored. The panel zone assignments for all
            selected point objects are removed.
        """
        _r = self._raw.DeletePanelZone(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.DeletePanelZone falhou (ret={_r})".format(_r=_r))
        return None

    def DeletePatternValue(self, Name: str, PatternName: str, ItemType: int = 0):
        """This function deletes all joint pattern assignments, associated with the specified joint
        pattern, from the specified point object(s). The function returns zero if the joint
        pattern assignments are successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of a point object or a group depending on the value selected
            for ItemType item.
        PatternName (input): The name of a defined joint pattern.
        ItemType (input): This is one of the following items from the eItemType enumeration.
            Object = 0 Group = 1 SelectedObjects = 2 If Object is selected, the Name item
            refers to a point object. The joint pattern assignments, associated with the
            specified joint pattern, for that point object are removed. If Group is
            selected, the Name item refers to a group. The joint pattern assignments,
            associated with the specified joint pattern, for all point objects in the group,
            are removed. If SelectedObjects is selected, the Name item is ignored. The joint
            pattern assignments, associated with the specified joint pattern, for all
            selected point objects, are removed.
        """
        _r = self._raw.DeletePatternValue(Name, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.DeletePatternValue falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteRestraint(self, Name: str, ItemType: int = 0):
        """This function deletes all restraint assignments from the specified point object(s). The
        function returns zero if the restraint assignments are successfully deleted,
        otherwise it returns a nonzero value.
    
        Name (input): The name of a point object or a group depending on the value selected
            for ItemType item.
        ItemType (input): This is one of the following items from the eItemType enumeration.
            Object = 0 Group = 1 SelectedObjects = 2 If Object is selected, the Name item
            refers to a point object. The restraint assignments for that point object are
            removed. If Group is selected, the Name item refers to a group. The restraint
            assignments for all point objects in the group are removed. If SelectedObjects
            is selected, the Name item is ignored. The restraint assignments for all
            selected point objects are removed.
        """
        _r = self._raw.DeleteRestraint(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.DeleteRestraint falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteSpecialPoint(self, Name: str, ItemType: int = 0):
        """The function deletes special point objects that have no other objects connected to them. The
        function returns zero if the function completes successfully, otherwise it returns a
        nonzero value. Point objects can be deleted only if they have no other objects
        (e.g., frame, cable, tendon, area, solid link) connected to them. If a point object
        is not specified to be a Special Point, the program automatically deletes that point
        object when it has no other objects connected to it. If a point object is specified
        to be a Special Point, to delete it, first delete all other objects connected to the
        point and then call this function to delete the point.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the deletion
            applies to the point object specified by the Name item. If this item is Group,
            the deletion applies to all point objects in the group specified by the Name
            item. If this item is SelectedObjects, the deletion applies to all selected
            point objects, and the Name item is ignored.
        """
        _r = self._raw.DeleteSpecialPoint(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.DeleteSpecialPoint falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteSpring(self, Name: str, ItemType: int = 0):
        """This function deletes all point spring assignments from the specified point object(s). The
        function returns zero if the restraint assignments are successfully deleted,
        otherwise it returns a nonzero value.
    
        Name (input): The name of a point object or a group depending on the value selected
            for ItemType item.
        ItemType (input): This is one of the following items from the eItemType enumeration.
            Object = 0 Group = 1 SelectedObjects = 2 If Object is selected, the Name item
            refers to a point object. The point spring assignments for that point object are
            removed. If Group is selected, the Name item refers to a group. The point spring
            assignments for all point objects in the group are removed. If SelectedObjects
            is selected, the Name item is ignored. The point spring assignments for all
            selected point objects are removed.
        """
        _r = self._raw.DeleteSpring(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.DeleteSpring falhou (ret={_r})".format(_r=_r))
        return None

    def GetCommonTo(self, Name: str):
        """This function returns the total number of objects (line, area, solid and link) that connect
        to the specified point object. The function returns zero if the CommonTo is
        successfully calculated, otherwise it returns a nonzero value.
    
        Name (input): The name of a point object or a group depending on the value selected
            for ItemType item.
        CommonTo (output): The total number of objects (line, area, solid and link) that
            connect to the specified point object.
        """
        _r = self._raw.GetCommonTo(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetCommonTo falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetConnectivity(self, Name: str):
        """This function returns a list of objects connected to a specified point object. The function
        returns zero if the list is successfully filled; otherwise it returns nonzero.
    
        Name (input): The name of an existing point object.
        NumberItems (output): This is the total number of objects connected to the specified
            point object.
        ObjectType (output): This is an array that includes the object type of each object
            connected to the specified point object. 2 = Frame object 3 = Cable object 4 =
            Tendon object 5 = Area object 6 = Solid object 7 = Link object
        ObjectName (output): This is an array that includes the object name of each object
            connected to the specified point object.
        PointNumber (output): This is an array that includes the point number within the
            considered object that corresponds to the specified point object.
        """
        _r = self._raw.GetConnectivity(Name, 0, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetConnectivity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetConstraint(self, Name: str, ConstraintName: list[str], ItemType: int = 0):
        """This function returns a list of constraint assignments made to one or more specified point
        objects. The function returns zero if the constraint name list is successfully
        filled, otherwise it returns nonzero. The PointName and ConstraintName items are
        returned in one-dimensional arrays. Each array is created as a dynamic array by the
        API user. In VBA a dynamic string array is defined by: Dim PointName() as String The
        arrays are dimensioned to (NumberItems 1) inside the Sap2000 program, filled with
        values, and returned to the API user. The arrays are zero-based. Thus the first item
        is at array index 0, and the last item is at array index (NumberItems - 1).
    
        Name (input): The name of an existing point object or group, depending on the value
            of the ItemType item.
        NumberItems (output): This is the total number of constraint assignments returned.
        PointName (output): This is an array that includes the name of the point object to
            which the specified constraint assignment applies.
        ConstraintName (input): This is an array that includes the name of the constraint
            that is assigned to the point object specified by the PointName item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the constraint
            assignments are retrieved for the point object specified by the Name item. If
            this item is Group, the constraint assignments are retrieved for all point
            objects in the group specified by the Name item. If this item is
            SelectedObjects, the constraint assignments are retrieved for all selected point
            objects and the Name item is ignored.
        """
        _r = self._raw.GetConstraint(Name, 0, [], ConstraintName, ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetConstraint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCoordCartesian(self, Name: str, Csys: str = 'Global'):
        """The function returns zero if the coordinates are successfully returned; otherwise it returns
        nonzero. If successful, the function returns the x, y and z coordinates of the
        specified point object in the Present Units. The coordinates are reported in the
        coordinate system specified by Csys.
    
        Name (input): The name of a defined point object.
        x (output): The X-coordinate of the specified point object in the specified
            coordinate system. [L]
        y (output): The Y-coordinate of the specified point object in the specified
            coordinate system. [L]
        z (output): The Z-coordinate of the specified point object in the specified
            coordinate system. [L]
        Csys (input): The name of a defined coordinate system. If Csys is not specified, the
            Global coordinate system is assumed.
        """
        _r = self._raw.GetCoordCartesian(Name, 0.0, 0.0, 0.0, Csys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetCoordCartesian falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCoordCylindrical(self, Aame: str, Csys: str = 'Global'):
        """The function returns zero if the coordinates are successfully returned; otherwise it returns
        nonzero. If successful, the function returns the r, theta and z coordinates of the
        specified point object in the Present Units. The coordinates are reported in the
        coordinate system specified by CSys.
    
        r (output): The radius for the specified point object in the specified coordinate
            system. [L]
        Theta (output): The angle for the specified point object in the specified coordinate
            system. The angle is measured in the XY plane from the positive X axis. When
            looking in the XY plane with the positive Z axis pointing toward you, a positive
            Theta angle is counter clockwise [deg]
        z (output): The Z-coordinate of the specified point object in the specified
            coordinate system. [L]
        Csys (input): The name of a defined coordinate system. If Csys is not specified, the
            Global coordinate system is assumed.
        """
        _r = self._raw.GetCoordCylindrical(Aame, 0.0, 0.0, 0.0, Csys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetCoordCylindrical falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCoordSpherical(self, Name: str, CSys: str = 'Global'):
        """The function returns zero if the coordinates are successfully returned; otherwise it returns
        nonzero. If successful, the function returns the r, a and b coordinates of the
        specified point object in the Present Units. The coordinates are reported in the
        coordinate system specified by CSys.
    
        Name (input): The name of an existing point object.
        r (output): The radius for the point object in the specified coordinate system. [L]
        a (output): The plan angle for the point object in the specified coordinate system.
            This angle is measured in the XY plane from the positive global X axis. When
            looking in the XY plane with the positive Z axis pointing toward you, a positive
            a angle is counter clockwise. [deg]
        b (output): The elevation angle for the point object in the specified coordinate
            system. This angle is measured in an X'Z plane that is perpendicular to the XY
            plane with the positive X' axis oriented at angle a from the positive global X
            axis. Angle b is measured from the positive global Z axis. When looking in the
            XZ plane with the positive Y' axis pointing toward you, a positive b angle is
            counter clockwise. [deg]
        CSys (input): The name of the coordinate system in which the joint coordinates are
            returned.
        """
        _r = self._raw.GetCoordSpherical(Name, 0.0, 0.0, 0.0, CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetCoordSpherical falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetElm(self, Name: str):
        """This function retrieves the name of the point element (analysis model point) associated with
        a specified point object in the object-based model. This function returns zero if
        the point element name is successfully returned; otherwise it returns nonzero. An
        error occurs if the analysis model does not currently exist.
    
        Name (input): The name of an existing point object.
        Elm (output): The name of the point element associated with the specified point
            object.
        """
        _r = self._raw.GetElm(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetElm falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGUID(self, name: str):
        """This function retrieves the GUID for specified point object. This function returns zero if
        the point object GUID is successfully retrieved; otherwise it returns nonzero.
    
        GUID (output): The GUID (Global Unique ID) for the specified point object.
        """
        _r = self._raw.GetGUID(name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetGUID falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGroupAssign(self, Name: str):
        """This function retrieves the names of the groups to which a specified point object is
        assigned. The function returns zero if the group assignments are successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object.
        NumberGroups (output): The number of group names retrieved.
        Groups (output): The names of the groups to which the point object is assigned.
        """
        _r = self._raw.GetGroupAssign(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetGroupAssign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDispl(self, Name: str, ItemType: int = 0):
        """This function retrieves the ground displacement load assignments to point objects. The
        function returns zero if the load assignments are successfully retrieved, otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing point object or group, depending on the value
            of the ItemType item.
        NumberItems (output): This is the total number of joint ground displacement
            assignments returned.
        PointName (output): This is an array that includes the name of the point object to
            which the specified ground displacement assignment applies.
        LoadPat (output): This is an array that includes the name of the load pattern for
            the ground displacement load.
        LCStep (output): This is an array that includes the load pattern step for the ground
            displacement load. In most cases, this item does not apply and will be returned
            as 0.
        CSys (output): This is an array that includes the name of the coordinate system for
            the ground displacement load. This is Local or the name of a defined coordinate
            system.
        U1 (output): This is an array that includes the assigned translational ground
            displacement in the local 1-axis or coordinate system X-axis direction,
            depending on the specified CSys. [L]
        U2 (output): This is an array that includes the assigned translational ground
            displacement in the local 2-axis or coordinate system Y-axis direction,
            depending on the specified CSys. [L]
        U3 (output): This is an array that includes the assigned translational ground
            displacement in the local 3-axis or coordinate system Z-axis direction,
            depending on the specified CSys. [L]
        R1 (output): This is an array that includes the assigned rotational ground
            displacement about the local 1-axis or coordinate system X-axis, depending on
            the specified CSys. [rad]
        R2 (output): This is an array that includes the assigned rotational ground
            displacement about the local 2-axis or coordinate system Y-axis, depending on
            the specified CSys. [rad]
        R3 (output): This is an array that includes the assigned rotational ground
            displacement about the local 3-axis or coordinate system Z-axis, depending on
            the specified CSys. [rad]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are retrieved for the point object specified by the Name item. If
            this item is Group, the assignments are retrieved for all point objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are retrieved for all selected point objects, and the Name item is
            ignored.
        """
        _r = self._raw.GetLoadDispl(Name, 0, [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetLoadDispl falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadForce(self, Name: str, ItemType: int = 0):
        """This function retrieves the joint force load assignments to point objects. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing point object or group, depending on the value
            of the ItemType item.
        NumberItems (output): This is the total number of joint force load assignments
            returned.
        PointName (output): This is an array that includes the name of the point object to
            which the specified load assignment applies.
        LoadPat (output): This is an array that includes the name of the load pattern for
            the load.
        LCStep (output): This is an array that includes the load pattern step for the load.
            In most cases, this item does not apply and will be returned as 0.
        CSys (output): This is an array that includes the name of the coordinate system for
            the load. This is Local or the name of a defined coordinate system.
        F1 (output): This is an array that includes the assigned translational force in the
            local 1-axis or coordinate system X-axis direction, depending on the specified
            CSys. [F]
        F2 (output): This is an array that includes the assigned translational force in the
            local 2-axis or coordinate system Y-axis direction, depending on the specified
            CSys. [F]
        F3 (output): This is an array that includes the assigned translational force in the
            local 3-axis or coordinate system Z-axis direction, depending on the specified
            CSys. [F]
        M1 (output): This is an array that includes the assigned moment about the local
            1-axis or coordinate system X-axis, depending on the specified CSys. [FL]
        M2 (output): This is an array that includes the assigned moment about the local
            2-axis or coordinate system Y-axis, depending on the specified CSys. [FL]
        M3 (output): This is an array that includes the assigned moment about the local
            3-axis or coordinate system Z-axis, depending on the specified CSys. [FL]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are retrieved for the point object specified by the Name item. If
            this item is Group, the assignments are retrieved for all point objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are retrieved for all selected point objects, and the Name item is
            ignored.
        """
        _r = self._raw.GetLoadForce(Name, 0, [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetLoadForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxesAdvanced(self, Name: str):
        """This function assigns advanced local axes to point objects. The function returns zero if the
        advanced local axes assignments are assigned successfully; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing point object.
        Active (output): This is True if advanced local axes exist.
        Plane2 (output): This is 12, 13, 21, 23, 31 or 32, indicating that the local plane
            determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, or 3-2
            plane. This item applies only when the Active item is True.
        """
        _r = self._raw.GetLocalAxesAdvanced(Name, False, 0, "", [], [], [], 0, 0, "", [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetLocalAxesAdvanced falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str, Advanced: bool):
        """This function retrieves the local axes angles for a point object. The function returns zero
        if the local axes angles are successfully retrieved, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing point object.
        Advanced (input): This item is True if the point object local axes orientation was
            obtained using advanced local axes parameters.
        """
        _r = self._raw.GetLocalAxes(Name, 0.0, 0.0, 0.0, Advanced)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMass(self, Name: str):
        """This function retrieves the point mass assignment values for a point object. The masses are
        always returned in the point local coordinate system. The function returns zero if
        the mass is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object.
        m (output): This is an array of six mass assignment values. Value(0) = U1 [M]
            Value(1) = U2 [M] Value(2) = U3 [M] Value(3) = R1 [ML 2 ] Value(4) = R2 [ML 2 ]
            Value(5) = R3 [ML 2 ]
        """
        _r = self._raw.GetMass(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetMass falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMergeNumber(self, Name: str, MergeNumber: int):
        """This function retrieves the merge number for a point object. By default the merge number for
        a point is zero. Points with different merge numbers are not automatically merged by
        the program. The function returns zero if the merge number is successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object.
        MergeNumber (input): The merge number assigned to the specified point object.
        """
        _r = self._raw.GetMergeNumber(Name, MergeNumber)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetMergeNumber falhou (ret={_r})".format(_r=_r))
        return None

    def GetNameList(self):
        """This function retrieves the names of all defined point objects. The function returns zero if
        the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of point object names retrieved by the program.
        MyName (output): This is a one-dimensional array of point object names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames 1) inside the Sap2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPanelZone(self, Name: str):
        """This function retrieves the panel zone assignment data for a point object. The function
        returns zero if the panel zone data is successfully retrieved, otherwise it returns
        a nonzero value. If no panel zone assignment is made to the point object, an error
        is returned.
    
        Name (input): The name of an existing point object.
        PropType (output): This is 0, 1, 2, or 3. 0 = Properties are elastic from column 1 =
            Properties are elastic from column and doubler plate 2 = Properties are from
            specified spring stiffnesses 3 = Properties are from a specified link property
        Thickness (output): The thickness of the doubler plate. This item applies only when
            PropType = 1. [L]
        K1 (output): The spring stiffness for major axis bending (about the local 3 axis of
            the column and panel zone). This item applies only when PropType = 2. [FL/rad]
        K2 (output): The spring stiffness for minor axis bending (about the local 2 axis of
            the column and panel zone). This item applies only when PropType = 2. [FL/rad]
        LinkProp (output): The name of the link property used to define the panel zone. This
            item applies only when PropType = 3.
        Connectivity (output): This is 0 or 1. 0 = Panel zone connects beams to other
            objects 1 = Panel zone connects braces to other objects
        LocalAxisFrom (output): This is 0 or 1. 0 = Panel zone local axis angle is from
            column 1 = Panel zone local axis angle is user defined The LocalAxisFrom item
            can be 1 only when the PropType item is 3.
        LocalAxisAngle (output): This item applies only when PropType = 3 and LocalAxisFrom
            = 1. It is the angle measured counter clockwise from the positive global X-axis
            to the local 2-axis of the panel zone. [deg]
        """
        _r = self._raw.GetPanelZone(Name, 0, 0.0, 0.0, 0.0, "", 0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetPanelZone falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPatternValue(self, Name: str, PatternName: str):
        """This function retrieves the joint pattern value for a specific point object and joint
        pattern. The function returns zero if the value is successfully retrieved, otherwise
        it returns a nonzero value. Joint pattern values are unitless.
    
        Name (input): The name of an existing point object.
        PatternName (input): The name of a defined joint pattern.
        Value (output): The value that the specified point object has for the specified
            joint pattern.
        """
        _r = self._raw.GetPatternValue(Name, PatternName, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetPatternValue falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetRestraint(self, Name: str):
        """This function retrieves the restraint assignments for a point object. The restraint
        assignments are always returned in the point local coordinate system. The function
        returns zero if the restraint assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing point object.
        Value (output): This is an array of six restraint values. Value(0) = U1 Value(1) =
            U2 Value(2) = U3 Value(3) = R1 Value(4) = R2 Value(5) = R3
        """
        _r = self._raw.GetRestraint(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetRestraint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSelected(self, Name: str):
        """This function retrieves the selected status for a point object. The function returns zero if
        the selected status is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object.
        Selected (output): This item returns True if the specified point object is selected,
            otherwise it returns False.
        """
        _r = self._raw.GetSelected(Name, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetSelected falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSpecialPoint(self, Name: str, SpecialPoint: bool):
        """This function retrieves the special point status for a point object. The function returns
        zero if the special point status is successfully retrieved, otherwise it returns a
        nonzero value. Special points are allowed to exist in the model even if no objects
        (line, area, solid, link) are connected to them. Points that are not special are
        automatically deleted if no objects connect to them.
    
        Name (input): The name of an existing point object.
        SpecialPoint (input): This item is True if the point object is specified as a
            special point, otherwise it is False.
        """
        _r = self._raw.GetSpecialPoint(Name, SpecialPoint)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetSpecialPoint falhou (ret={_r})".format(_r=_r))
        return None

    def GetSpringCoupled(self, Name: str):
        """This function retrieves coupled spring stiffness assignments for a point object. The spring
        stiffnesses reported are the sum of all springs assigned to the point object. The
        spring stiffness values are reported in the point local coordinate system. The
        function returns zero if the stiffnesses are successfully retrieved, otherwise it
        returns a nonzero value. If no springs exist at the point object, the function
        returns a nonzero value.
    
        Name (input): The name of an existing point object.
        k (output): This is an array of twenty one spring stiffness values. Value(0) = U1U1
            [F/L] Value(1) = U1U2 [F/L] Value(2) = U2U2 [F/L] Value(3) = U1U3 [F/L] Value(4)
            = U2U3 [F/L] Value(5) = U3U3 [F/L] Value(6) = U1R1 [F/rad] Value(7) = U2R1
            [F/rad] Value(8) = U3R1 [F/rad] Value(9) = R1R1 [FL/rad] Value(10) = U1R2
            [F/rad] Value(11) = U2R2 [F/rad] Value(12) = U3R2 [F/rad] Value(13) = R1R2
            [FL/rad] Value(14) = R2R2 [FL/rad] Value(15) = U1R3 [F/rad] Value(16) = U2R3
            [F/rad] Value(17) = U3R3 [F/rad] Value(18) = R1R3 [FL/rad] Value(19) = R2R3
            [FL/rad] Value(20) = R3R3 [FL/rad]
        """
        _r = self._raw.GetSpringCoupled(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetSpringCoupled falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSpring(self, Name: str):
        """This function retrieves uncoupled spring stiffness assignments for a point object, that is,
        it retrieves the diagonal terms in the 6x6 spring matrix for the point object. The
        spring stiffnesses reported are the sum of all springs assigned to the point object.
        The spring stiffness values are reported in the point local coordinate system. The
        function returns zero if the stiffnesses are successfully retrieved, otherwise it
        returns a nonzero value. If no springs exist at the point object, the function
        returns a nonzero value.
    
        Name (input): The name of an existing point object.
        k (output): This is an array of six spring stiffness values. Value(0) = U1 [F/L]
            Value(1) = U2 [F/L] Value(2) = U3 [F/L] Value(3) = R1 [FL/rad] Value(4) = R2
            [FL/rad] Value(5) = R3 [FL/rad]
        """
        _r = self._raw.GetSpring(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetSpring falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetTransformationMatrix(self, Name: str, IsGlobal: bool = True):
        """The function returns zero if the point object transformation matrix is successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the point object local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array; (Local1, Local2, Local3)
            are an item (such as a point load) in the point object local coordinate system;
            and (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate
            system. The transformation from the local coordinate system to the present
            coordinate system is the same as that shown above for the global system if you
            substitute the present system for the global system.
        IsGlobal (input): If this item is True, the transformation matrix is between the
            Global coordinate system and the point object local coordinate system. If this
            item is False, the transformation matrix is between the present coordinate
            system and the point object local coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [], IsGlobal)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointObj.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def IsSpringCoupled(self, Name: str, IsCoupled: bool):
        """This function indicates if the spring assignments to a point object are coupled, that is, if
        they have off-diagonal terms in the 6x6 spring matrix for the point object. The
        function returns zero if the coupled status is successfully retrieved, otherwise it
        returns a nonzero value. If no springs exist at the point object,n the function
        returns a nonzero value.
    
        Name (input): The name of an existing point object.
        IsCoupled (input): This item is True if the spring assigned to the specified point
            object is coupled, otherwise it is False.
        """
        _r = self._raw.IsSpringCoupled(Name, IsCoupled)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.IsSpringCoupled falhou (ret={_r})".format(_r=_r))
        return None

    def SetConstraint(self, Name: str, ConstraintName: str, ItemType: int = 0, Replace: bool = True):
        """This function makes joint constraint assignments to point objects. The function returns 0 if
        the assignment is successfully made, otherwise it returns nonzero.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        ConstraintName (input): The name of an existing joint constraint.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the constraint
            assignment is made to the point object specified by the Name item. If this item
            is Group, the constraint assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the constraint
            assignment is made to all selected point objects and the Name item is ignored.
        Replace (input): If this item is True, all previous joint constraints, if any,
            assigned to the specified point object(s) are deleted before making the new
            assignment.
        """
        _r = self._raw.SetConstraint(Name, ConstraintName, ItemType, Replace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetConstraint falhou (ret={_r})".format(_r=_r))
        return None

    def SetGUID(self, Name: str, GUID: str = ''):
        """This function sets the GUID for specified point object. If the GUID is passed in as a blank
        string, the program automatically creates a GUID for the object. This function
        returns zero if the point object GUID is successfully set; otherwise it returns
        nonzero.
    
        Name (input): The name of an existing point object.
        GUID (input): The GUID (Global Unique ID) for the specified point object.
        """
        _r = self._raw.SetGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetGUID falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroupAssign(self, Name: str, GroupName: str, Remove: bool = False, ItemType: int = 0):
        """This function adds or removes point objects from a specified group. The function returns
        zero if the group assignment is successful, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        GroupName (input): The name of an existing group to which the assignment is made.
        Remove (input): If this item is False, the specified point objects are added to the
            group specified by the GroupName item. If it is True, the point objects are
            removed from the group.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the point
            object specified by the Name item is added or removed from the group specified
            by the GroupName item. If this item is Group, all point objects in the group
            specified by the Name item are added or removed from the group specified by the
            GroupName item. If this item is SelectedObjects, all selected point objects are
            added or removed from the group specified by the GroupName item and the Name
            item is ignored.
        """
        _r = self._raw.SetGroupAssign(Name, GroupName, Remove, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetGroupAssign falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadDispl(self, Name: str, LoadPat: str, Value: list[float], Replace: bool = False, CSys: str = 'Global', ItemType: int = 0):
        """This function makes ground displacement load assignments to point objects. The function
        returns zero if the load assignments are successfully made, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        LoadPat (input): The name of the load pattern for the ground displacement load.
        Value (input): This is an array of six ground displacement load values. Value(0) =
            U1 [L] Value(1) = U2 [L] Value(2) = U3 [L] Value(3) = R1 [rad] Value(4) = R2
            [rad] Value(5) = R3 [rad]
        Replace (input): If this item is True, all previous ground displacement loads, if
            any, assigned to the specified point object(s) in the specified load pattern are
            deleted before making the new assignment.
        CSys (input): The name of the coordinate system for the considered ground
            displacement load. This is Local or the name of a defined coordinate system.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignment is made to the point object specified by the Name item. If this item
            is Group, the load assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the load assignment
            is made to all selected point objects and the Name item is ignored.
        """
        _r = self._raw.SetLoadDispl(Name, LoadPat, Value, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetLoadDispl falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadForce(self, Name: str, LoadPat: str, Value: list[float], Replace: bool = False, CSys: str = 'Global', ItemType: int = 0):
        """This function makes point load assignments to point objects. The function returns zero if
        the load assignments are successfully made, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        LoadPat (input): The name of the load pattern for the point load.
        Value (input): This is an array of six point load values. Value(0) = F1 [F] Value(1)
            = F2 [F] Value(2) = F3 [F] Value(3) = M1 [FL] Value(4) = M2 [FL] Value(5) = M3
            [FL]
        Replace (input): If this item is True, all previous point loads, if any, assigned to
            the specified point object(s) in the specified load pattern are deleted before
            making the new assignment.
        CSys (input): The name of the coordinate system for the considered point load. This
            is Local or the name of a defined coordinate system.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignment is made to the point object specified by the Name item. If this item
            is Group, the load assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the load assignment
            is made to all selected point objects and the Name item is ignored.
        """
        _r = self._raw.SetLoadForce(Name, LoadPat, Value, Replace, CSys, ItemType)
        if _r[1] != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetLoadForce falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxesAdvanced(self, Name: str, Active: bool, AxVectOpt: int, AxCSys: str, AxDir: list[int], AxPt: list[str], AxVect: list[float], Plane2: int, PlVectOpt: int, PlCSys: str, PlDir: list[int], PlPt: list[str], PlVect: list[float], ItemType: int = 0):
        """This function assigns advanced local axes to point objects. The function returns zero if the
        advanced local axes assignments are assigned successfully; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing point object or group, depending on the value
            of the ItemType item.
        Active (input): This is True if advanced local axes exist.
        Plane2 (input): This is 12, 13, 21, 23, 31 or 32, indicating that the local plane
            determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, 0r 3-2
            plane. This item applies only when the Active item is True.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 Selection = 2 If this item is Object, the assignment is
            made to the point object specified by the Name item. If this item is Group, the
            assignment is made to all point objects in the group specified by the Name item.
            If this item is Selection, assignment is made to all selected point objects and
            the Name item is ignored.
        """
        _r = self._raw.SetLocalAxesAdvanced(Name, Active, AxVectOpt, AxCSys, AxDir, AxPt, AxVect, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetLocalAxesAdvanced falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxes(self, Name: str, a: float, b: float, c: float, ItemType: int = 0):
        """This function sets the local axes angles for point objects. The function returns zero if the
        local axes angles are successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the local axes
            assignment is made to the point object specified by the Name item. If this item
            is Group, the local axes assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the local axes
            assignment is made to all selected point objects and the Name item is ignored.
        """
        _r = self._raw.SetLocalAxes(Name, a, b, c, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetLocalAxes falhou (ret={_r})".format(_r=_r))
        return None

    def SetMass(self, Name: str, m: list[float], ItemType: int = 0, IsLocalCSys: bool = True, Replace: bool = False):
        """This function assigns point mass to a point object. The function returns zero if the mass is
        successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        m (input): This is an array of six mass assignment values. Value(0) = U1 [M]
            Value(1) = U2 [M] Value(2) = U3 [M] Value(3) = R1 [ML 2 ] Value(4) = R2 [ML 2 ]
            Value(5) = R3 [ML 2 ]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the mass
            assignment is made to the point object specified by the Name item. If this item
            is Group, the mass assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the mass assignment
            is made to all selected point objects and the Name item is ignored.
        IsLocalCSys (input): If this item is True, the specified mass assignments are in the
            point object local coordinate system. If it is False, the assignments are in the
            Global coordinate system.
        Replace (input): If this item is True, all existing point mass assignments to the
            specified point object(s) are deleted prior to making the assignment. If it is
            False, the mass assignments are added to any existing assignments.
        """
        _r = self._raw.SetMass(Name, m, ItemType, IsLocalCSys, Replace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetMass falhou (ret={_r})".format(_r=_r))
        return None

    def SetMassByVolume(self, Name: str, MatProp: str, m: list[float], ItemType: int = 0, IsLocalCSys: bool = True, Replace: bool = False):
        """This function assigns point mass to a point object. The program calculates the mass by
        multiplying the specified values by the mass per unit volume of the specified
        material property. The function returns zero if the mass is successfully assigned;
        otherwise, it returns a nonzero value.
    
        Name (input): The name of an existing point object or group, depending on the value
            of the ItemType item.
        MatProp (input): The name of an existing material property.
        m (input): This is an array of six mass assignment values. Value(0) = U1 [L 3 ]
            Value(1) = U2 [L 3 ] Value(2) = U3 [L 3 ] Value(3) = R1 [L 5 ] Value(4) = R2 [L
            5 ] Value(5) = R3 [L 5 ]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the mass
            assignment is made to the point object specified by the Name item. If this item
            is Group, the mass assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the mass assignment
            is made to all selected point objects and the Name item is ignored.
        IsLocalCSys (input): If this item is True, the specified mass assignments are in the
            point object local coordinate system. If it is False, the assignments are in the
            Global coordinate system.
        Replace (input): If this item is True, all existing point mass assignments to the
            specified point object(s) are deleted prior to making the assignment. If it is
            False, the mass assignments are added to any previously existing assignments.
        """
        _r = self._raw.SetMassByVolume(Name, MatProp, m, ItemType, IsLocalCSys, Replace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetMassByVolume falhou (ret={_r})".format(_r=_r))
        return None

    def SetMassByWeight(self, Name: str, m: list[float], ItemType: int = 0, IsLocalCSys: bool = True, Replace: bool = False):
        """This function assigns point mass to a point object. The program calculates the mass by
        dividing the specified values by the acceleration of gravity. The function returns
        zero if the mass is successfully assigned; otherwise. it returns a nonzero value.
    
        Name (input): The name of an existing point object or group, depending on the value
            of the ItemType item.
        m (input): This is an array of six mass assignment values. Value(0) = U1 [F]
            Value(1) = U2 [F] Value(2) = U3 [F] Value(3) = R1 [FL 2 ] Value(4) = R2 [FL 2 ]
            Value(5) = R3 [FL 2 ]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the mass
            assignment is made to the point object specified by the Name item. If this item
            is Group, the mass assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the mass assignment
            is made to all selected point objects and the Name item is ignored.
        IsLocalCSys (input): If this item is True, the specified mass assignments are in the
            point object local coordinate system. If it is False, the assignments are in the
            Global coordinate system.
        Replace (input): If this item is True, all existing point mass assignments to the
            specified point object(s) are deleted prior to making the assignment. If it is
            False, the mass assignments are added to any previously existing assignments.
        """
        _r = self._raw.SetMassByWeight(Name, m, ItemType, IsLocalCSys, Replace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetMassByWeight falhou (ret={_r})".format(_r=_r))
        return None

    def SetMergeNumber(self, Name: str, MergeNumber: int, ItemType: int = 0):
        """This function assigns a merge number to a point object. By default the merge number for a
        point is zero. Points with different merge numbers are not automatically merged by
        the program. The function returns zero if the merge number is successfully assigned,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        MergeNumber (input): The merge number for the specified point object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the merge
            number assignment is made to the point object specified by the Name item. If
            this item is Group, the merge number assignment is made to all point objects in
            the group specified by the Name item. If this item is SelectedObjects, the merge
            number assignment is made to all selected point objects and the Name item is
            ignored.
        """
        _r = self._raw.SetMergeNumber(Name, MergeNumber, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetMergeNumber falhou (ret={_r})".format(_r=_r))
        return None

    def SetPatternByPressure(self, Name: str, PatternName: str, Z: float, w: float, u: float, r: int, ItemType: int = 0, Restriction: int = 0, Replace: bool = False):
        """This function sets the joint pattern value for a specified point object and joint pattern.
        The joint pattern value is calculated as: Value = [(z zpoint) * w] + u where z, w
        and u are described in the Parameters section and zpoint is the Z coordinate of the
        considered point object in the present coordinate system. All appropriate unit
        conversions are used to calculate the value in the database units, but thereafter it
        is assumed to be unitless. The function returns zero if the pattern value is
        successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        PatternName (input): The name of a defined joint pattern.
        w (input): A weight per unit volume. [F/L 3 ]
        u (input): An added uniform force per unit area. [F/L 2 ]
        r (input): This is 0, 1, or 2. 0 = All values are used 1 = Negative values are set
            to zero 2 = Positive values are set to zero This restriction applies before the
            pattern value has been added to any existing pattern value assigned to the point
            object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the joint
            pattern assignment is made to the point object specified by the Name item. If
            this item is Group, the joint pattern assignment is made to all point objects in
            the group specified by the Name item. If this item is SelectedObjects, the joint
            pattern assignment is made to all selected point objects and the Name item is
            ignored.
        Restriction (input): This is 0, 1, or 2. 0 = All values are used 1 = Negative values
            are set to zero 2 = Positive values are set to zero This restriction applies
            after the pattern value has been added to any existing pattern value assigned to
            the point object. This restriction applies even if there was no existing joint
            pattern value on the point object.
        Replace (input): If this item is True, the joint pattern value calculated as shown
            in the Remarks section replaces any previous joint pattern value for the point
            object. If this item is False, the joint pattern value calculated as shown in
            the Remarks section is added to any previous joint pattern value for the point
            object and then the Restriction items are checked.
        """
        _r = self._raw.SetPatternByPressure(Name, PatternName, Z, w, u, r, ItemType, Restriction, Replace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetPatternByPressure falhou (ret={_r})".format(_r=_r))
        return None

    def SetPatternByXYZ(self, Name: str, PatternName: str, a: float, b: float, c: float, d: float, ItemType: int = 0, Restriction: int = 0, Replace: bool = False):
        """This function sets the joint pattern value for a specified point object and joint pattern.
        The joint pattern value is calculated as: Value = ax + by + cz + d where a, b, c and
        d are function input parameters and x, y and z are the coordinates of the considered
        point object in the present coordinate system The function returns zero if the
        pattern value is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        PatternName (input): The name of a defined joint pattern.
        a (input): The value a in the equation shown in the Remarks section. [1/L]
        b (input): The value b in the equation shown in the Remarks section. [1/L]
        c (input): The value c in the equation shown in the Remarks section. [1/L]
        d (input): The value d in the equation shown in the Remarks section. This item is
            unitless.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the joint
            pattern assignment is made to the point object specified by the Name item. If
            this item is Group, the joint pattern assignment is made to all point objects in
            the group specified by the Name item. If this item is SelectedObjects, the joint
            pattern assignment is made to all selected point objects and the Name item is
            ignored.
        Restriction (input): This is either 0, 1, or 2. 0 = All values are used 1 = Negative
            values are set to zero 2 = Positive values are set to zero
        Replace (input): If this item is True, the joint pattern value calculated as shown
            in the Remarks section replaces any previous joint pattern value for the point
            object. If this item is False, the joint pattern value calculated as shown in
            the Remarks section is added to any previous joint pattern value for the point
            object and then the Restriction items are checked.
        """
        _r = self._raw.SetPatternByXYZ(Name, PatternName, a, b, c, d, ItemType, Restriction, Replace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetPatternByXYZ falhou (ret={_r})".format(_r=_r))
        return None

    def SetRestraint(self, Name: str, Value: list[bool], ItemType: int = 0):
        """This function assigns the restraint assignments for a point object. The restraint
        assignments are always set in the point local coordinate system. The function
        returns zero if the restraint assignments are successfully assigned, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        Value (input): This is an array of six restraint values. Value(0) = U1 Value(1) = U2
            Value(2) = U3 Value(3) = R1 Value(4) = R2 Value(5) = R3
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the restraint
            assignment is made to the point object specified by the Name item. If this item
            is Group, the restraint assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the restraint
            assignment is made to all selected point objects and the Name item is ignored.
        """
        _r = self._raw.SetRestraint(Name, Value, ItemType)
        if _r[1] != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetRestraint falhou (ret={_r})".format(_r=_r))
        return None

    def SetSelected(self, Name: str, Selected: bool, ItemType: int = 0):
        """This function sets the selected status for a point object. The function returns zero if the
        selected status is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        Selected (input): This item is True if the specified point object is selected,
            otherwise it is False.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the selected
            status is set for the point object specified by the Name item. If this item is
            Group, the selected status is set for all point objects in the group specified
            by the Name item. If this item is SelectedObjects, the selected status is set
            for all selected point objects and the Name item is ignored.
        """
        _r = self._raw.SetSelected(Name, Selected, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetSelected falhou (ret={_r})".format(_r=_r))
        return None

    def SetSpecialPoint(self, Name: str, SpecialPoint: bool, ItemType: int = 0):
        """This function sets the special point status for a point object. The function returns zero if
        the special point status is successfully set, otherwise it returns a nonzero value.
        Special points are allowed to exist in the model even if no objects (line, area,
        solid, link) are connected to them. Points that are not special are automatically
        deleted if no objects connect to them.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        SpecialPoint (input): This item is True if the point object is specified as a
            special point, otherwise it is False.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the special
            point status is set for the point object specified by the Name item. If this
            item is Group, the special point status is set for all point objects in the
            group specified by the Name item. If this item is SelectedObjects, the special
            point status is set for all selected point objects and the Name item is ignored.
        """
        _r = self._raw.SetSpecialPoint(Name, SpecialPoint, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetSpecialPoint falhou (ret={_r})".format(_r=_r))
        return None

    def SetSpring(self, Name: str, k: list[float], ItemType: int = 0, IsLocalCSys: bool = False, Replace: bool = False):
        """This function assigns coupled springs to a point object. The function returns zero if the
        stiffnesses are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        k (input): This is an array of six spring stiffness values. Value(0) = U1 [F/L]
            Value(1) = U2 [F/L] Value(2) = U3 [F/L] Value(3) = R1 [FL/rad] Value(4) = R2
            [FL/rad] Value(5) = R3 [FL/rad]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the spring
            assignment is made to the point object specified by the Name item. If this item
            is Group, the spring assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the spring
            assignment is made to all selected point objects and the Name item is ignored.
        IsLocalCSys (input): If this item is True, the specified spring assignments are in
            the point object local coordinate system. If it is False, the assignments are in
            the Global coordinate system.
        Replace (input): If this item is True, all existing point spring assignments to the
            specified point object(s) are deleted prior to making the assignment. If it is
            False, the spring assignments are added to any existing assignments.
        """
        _r = self._raw.SetSpring(Name, k, ItemType, IsLocalCSys, Replace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetSpring falhou (ret={_r})".format(_r=_r))
        return None

    def SetSpringCoupled(self, Name: str, k: list[float], ItemType: int = 0, IsLocalCSys: bool = False, Replace: bool = False):
        """This function assigns coupled springs to a point object. The function returns zero if the
        stiffnesses are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object or group depending on the value
            of the ItemType item.
        k (input): This is an array of twenty one spring stiffness values. Value(0) = U1U1
            [F/L] Value(1) = U1U2 [F/L] Value(2) = U2U2 [F/L] Value(3) = U1U3 [F/L] Value(4)
            = U2U3 [F/L] Value(5) = U3U3 [F/L] Value(6) = U1R1 [F/rad] Value(7) = U2R1
            [F/rad] Value(8) = U3R1 [F/rad] Value(9) = R1R1 [FL/rad] Value(10) = U1R2
            [F/rad] Value(11) = U2R2 [F/rad] Value(12) = U3R2 [F/rad] Value(13) = R1R2
            [FL/rad] Value(14) = R2R2 [FL/rad] Value(15) = U1R3 [F/rad] Value(16) = U2R3
            [F/rad] Value(17) = U3R3 [F/rad] Value(18) = R1R3 [FL/rad] Value(19) = R2R3
            [FL/rad] Value(20) = R3R3 [FL/rad]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the spring
            assignment is made to the point object specified by the Name item. If this item
            is Group, the spring assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the spring
            assignment is made to all selected point objects and the Name item is ignored.
        IsLocalCSys (input): If this item is True, the specified spring assignments are in
            the point object local coordinate system. If it is False, the assignments are in
            the Global coordinate system.
        Replace (input): If this item is True, all existing point spring assignments to the
            specified point object(s) are deleted prior to making the assignment. If it is
            False, the spring assignments are added to any existing assignments.
        """
        _r = self._raw.SetSpringCoupled(Name, k, ItemType, IsLocalCSys, Replace)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointObj.SetSpringCoupled falhou (ret={_r})".format(_r=_r))
        return None


