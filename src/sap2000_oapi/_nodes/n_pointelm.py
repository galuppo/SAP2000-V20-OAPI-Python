"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PointElm:
    """Wrapper para SapModel.PointElm."""

    def __init__(self, raw):
        self._raw = raw

    def CountConstraint(self, Name: str = ''):
        """If the Name item is provided, the Count item returns the total number of constraint
        assignments made to the specified point element. If the Name item is not specified
        or is specified as an empty string, the Count item returns the total number of
        constraint assignments to all point elements in the model. If the Name item is
        specified but it is not recognized by the program as a valid point element, an error
        is returned. This function returns zero if the count is successfully completed,
        otherwise it returns a nonzero value.
    
        Count (output): The number of counted constraints.
        Name (input): This optional item is the name of an existing point element.
        """
        _r = self._raw.CountConstraint(0, Name)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.CountConstraint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def CountLoadDispl(self, Name: str = '', LoadPat: str = ''):
        """If neither the Name item nor the LoadPat item is provided, the Count item returns the total
        number of ground displacement load assignments to point elements in the model. If
        the Name item is provided but not the LoadPat item, the Count item returns the total
        number of ground displacement load assignments made for the specified point element.
        If the Name item is not provided but the LoadPat item is specified, the Count item
        returns the total number of ground displacement load assignments made to all point
        elements for the specified load pattern. If both the Name item and the LoadPat item
        are provided, the Count item returns the total number of ground displacement load
        assignments made to the specified point element for the specified load pattern. If
        the Name item or the LoadPat item is provided but is not recognized by the program
        as valid, an error is returned. This function returns zero if the count is
        successfully completed, otherwise it returns a nonzero value.
    
        Count (output): The number of counted ground displacement loads.
        Name (input): This optional item is the name of an existing point element.
        LoadPat (input): This optional item is the name of an existing load pattern.
        """
        _r = self._raw.CountLoadDispl(0, Name, LoadPat)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.CountLoadDispl falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def CountLoadForce(self, Name: str = '', LoadPat: str = ''):
        """If neither the Name item nor the LoadPat item is provided, the Count item returns the total
        number of point load assignments to point elements in the model. If the Name item is
        provided but not the LoadPat item, the Count item returns the total number of point
        load assignments made for the specified point element. If the Name item is not
        provided but the LoadPat item is specified, the Count item returns the total number
        of point load assignments made to all point elements for the specified load pattern.
        If both the Name item and the LoadPat item are provided, the Count item returns the
        total number of point load assignments made to the specified point element for the
        specified load pattern. If the Name item or the LoadPat item is provided but is not
        recognized by the program as valid, an error is returned. This function returns zero
        if the count is successfully completed, otherwise it returns a nonzero value.
    
        Count (output): The number of counted point loads.
        Name (input): This optional item is the name of an existing point element.
        LoadPat (input): This optional item is the name of an existing load pattern.
        """
        _r = self._raw.CountLoadForce(0, Name, LoadPat)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.CountLoadForce falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def CountRestraint(self):
        """This function returns the total number of point elements in the model with restraint
        assignments.
        """
        _r = self._raw.CountRestraint()
        return _r

    def CountSpring(self):
        """This function returns the total number of point elements in the model with spring
        assignments.
        """
        _r = self._raw.CountSpring()
        return _r

    def Count(self):
        """This function returns the total number of point elements in the analysis model.
        """
        _r = self._raw.Count()
        return _r

    def GetConnectivity(self, Name: str):
        """This function returns a list of elements connected to a specified point element. The
        function returns zero if the list is successfully filled; otherwise it returns
        nonzero.
    
        Name (input): The name of an existing point element.
        NumberItems (output): This is the total number of elements connected to the
            specified point element.
        ObjectType (output): This is an array that includes the element type of each element
            connected to the specified point element. 2 = Frame element 3 = Cable element 4
            = Tendon element 5 = Area element 6 = Solid element 7 = Link element
        ObjectName (output): This is an array that includes the element name of each element
            connected to the specified point element.
        PointNumber (output): This is an array that includes the point number within the
            considered element that corresponds to the specified point element.
        """
        _r = self._raw.GetConnectivity(Name, 0, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetConnectivity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetConstraint(self, Name: str, ConstraintName: list[str], ItemTypeElm: int = 1):
        """This function returns a list of constraint assignments made to one or more specified point
        elements. The function returns zero if the constraint name list is successfully
        filled, otherwise it returns nonzero. The PointName and ConstraintName items are
        returned in one-dimensional arrays. Each array is created as a dynamic array by the
        API user. In VBA a dynamic string array is defined by: Dim PointName() as String The
        arrays are dimensioned to (NumberItems 1) inside the Sap2000 program, filled with
        values, and returned to the API user. The arrays are zero-based. Thus the first item
        is at array index 0, and the last item is at array index (NumberItems - 1).
    
        Name (input): The name of an existing point object, point element, or group of
            objects, depending on the value of the ItemTypeElm item.
        NumberItems (output): This is the total number of constraint assignments returned.
        PointName (output): This is an array that includes the name of the point element to
            which the specified constraint assignment applies.
        ConstraintName (input): This is an array that includes the name of the constraint
            that is assigned to the point element specified by the PointName item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the constraint assignments are retrieved for the point
            element corresponding to the point object specified by the Name item. If this
            item is Element, the constraint assignments are retrieved for the point element
            specified by the Name item. If this item is GroupElm, the constraint assignments
            are retrieved for all point elements directly or indirectly specified in the
            group specified by the Name item. If this item is SelectionElm, the constraint
            assignments are retrieved for all point elements directly or indirectly
            selected, and the Name item is ignored. See Item Type for Elements for more
            information.
        """
        _r = self._raw.GetConstraint(Name, 0, [], ConstraintName, ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetConstraint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCoordCartesian(self, Name: str, CSys: str = 'Global'):
        """The function returns zero if the coordinates are successfully returned; otherwise it returns
        nonzero. If successful, the function returns the x, y and z coordinates of the
        specified point element in the Present Units. The coordinates are reported in the
        coordinate system specified by CSys.
    
        Name (input): The name of an existing point element.
        x (output): The X-coordinate of the specified point element in the specified
            coordinate system. [L]
        y (output): The Y-coordinate of the specified point element in the specified
            coordinate system. [L]
        z (output): The Z-coordinate of the specified point element in the specified
            coordinate system. [L]
        CSys (input): The name of the coordinate system in which the joint coordinates are
            returned.
        """
        _r = self._raw.GetCoordCartesian(Name, 0.0, 0.0, 0.0, CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetCoordCartesian falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCoordCylindrical(self, Name: str, CSys: str = 'Global'):
        """The function returns zero if the coordinates are successfully returned; otherwise it returns
        nonzero. If successful, the function returns the r, Theta and z coordinates of the
        specified point element in the Present Units. The coordinates are reported in the
        coordinate system specified by CSys.
    
        Name (input): The name of an existing point element.
        r (output): The radius for the point element in the specified coordinate system. [L]
        Theta (output): The angle for the specified point element in the specified
            coordinate system. The angle is measured in the XY plane from the positive X
            axis. When looking in the XY plane with the positive Z axis pointing toward you,
            a positive Theta angle is counter clockwise. [deg]
        z (output): The Z-coordinate of the specified point element in the specified
            coordinate system. [L]
        CSys (input): The name of the coordinate system in which the joint coordinates are
            returned.
        """
        _r = self._raw.GetCoordCylindrical(Name, 0.0, 0.0, 0.0, CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetCoordCylindrical falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCoordSpherical(self, Name: str, CSys: str = 'Global'):
        """The function returns zero if the coordinates are successfully returned; otherwise it returns
        nonzero. If successful, the function returns the r, a and b coordinates of the
        specified point element in the Present Units. The coordinates are reported in the
        coordinate system specified by CSys.
    
        Name (input): The name of an existing point element.
        r (output): The radius for the point element in the specified coordinate system. [L]
        a (output): The plan angle for the point element in the specified coordinate system.
            This angle is measured in the XY plane from the positive global X axis. When
            looking in the XY plane with the positive Z axis pointing toward you, a positive
            a angle is counter clockwise. [deg]
        b (output): The elevation angle for the point element in the specified coordinate
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
            raise Sap2000ApiError("SapModel.PointElm.GetCoordSpherical falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDispl(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the ground displacement load assignments to point elements. The
        function returns zero if the load assignments are successfully retrieved, otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing point object, point element, or group of
            objects, depending on the value of the ItemTypeElm item.
        NumberItems (output): This is the total number of joint ground displacement
            assignments returned.
        PointName (output): This is an array that includes the name of the point element to
            which the specified ground displacement assignment applies.
        LoadPat (output): This is an array that includes the name of the load pattern for
            the ground displacement load.
        LCStep (output): This is an array that includes the load pattern step for the ground
            displacement load. In most cases, this item does not apply and will be returned
            as 0.
        CSys (output): This is an array that includes the name of the coordinate system for
            the ground displacement load. This is either Local or the name of a defined
            coordinate system.
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
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the ground displacement assignments are retrieved for the
            point element corresponding to the point object specified by the Name item. If
            this item is Element, the ground displacement assignments are retrieved for the
            point element specified by the Name item. If this item is GroupElm, the ground
            displacement assignments are retrieved for all point elements directly or
            indirectly specified in the group specified by the Name item. If this item is
            SelectionElm, the ground displacement assignments are retrieved for all point
            elements directly or indirectly selected, and the Name item is ignored. See Item
            Type for Elements for more information.
        """
        _r = self._raw.GetLoadDispl(Name, 0, [], [], [], [], [], [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetLoadDispl falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadForce(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the joint force load assignments to point elements. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing point object, point element, or group of
            objects, depending on the value of the ItemTypeElm item.
        NumberItems (output): This is the total number of joint force load assignments
            returned.
        PointName (output): This is an array that includes the name of the point element to
            which the specified load assignment applies.
        LoadPat (output): This is an array that includes the name of the load pattern for
            the load.
        LCStep (output): This is an array that includes the load pattern step for the load.
            In most cases this item does not apply and will be returned as 0.
        CSys (output): This is an array that includes the name of the coordinate system for
            the load. This is either Local or the name of a defined coordinate system.
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
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the point element
            corresponding to the point object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the point element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            all point elements directly or indirectly specified in the group specified by
            the Name item. If this item is SelectionElm, the load assignments are retrieved
            for all point elements directly or indirectly selected and the Name item is
            ignored. See Item Type for Elements for more information.
        """
        _r = self._raw.GetLoadForce(Name, 0, [], [], [], [], [], [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetLoadForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str):
        """This function retrieves the local axes angles for a point element. The function returns zero
        if the local axes angles are successfully retrieved, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing point element.
        """
        _r = self._raw.GetLocalAxes(Name, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMergeNumber(self, Name: str, MergeNumber: int):
        """This function retrieves the merge number for a point element. By default the merge number
        for a point is zero. Points with different merge numbers are not automatically
        merged by the program. The function returns zero if the merge number is successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point element.
        MergeNumber (input): The merge number assigned to the specified point element.
        """
        _r = self._raw.GetMergeNumber(Name, MergeNumber)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetMergeNumber falhou (ret={_r})".format(_r=_r))
        return None

    def GetNameList(self):
        """This function retrieves the names of all defined point elements. The function returns zero
        if the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of point element names retrieved by the program.
        MyName (output): This is a one-dimensional array of point element names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames 1) inside the Sap2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetObj(self, Name: str):
        """This function retrieves the object or defined item associated with a specified point
        element. The function returns zero if the object is successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point element.
        Obj (output): The name of the object or defined item associated with the specified
            point element. The type of object or item is determined from the ObjType
            variable.
        ObjType (output): A number indicating the type of object or defined item that is
            associated with the point element. 1 Obj is the point object corresponding to
            the specified point element. 2 Obj is a line object that is internally meshed by
            the program to create the specified point element. 3 Obj is an area object that
            is internally meshed by the program to create the specified point element. 6 Obj
            is a solid object that is internally meshed by the program to create the
            specified point element. 9 Obj is a point object that has a panel zone
            assignment. The specified point element is internally added by the program at
            the point object (panel zone) location to model the panel zone. The specified
            point element does not directly correspond to the point object returned; it is
            an added point at the same location as the point object. 21 Obj is a defined
            diaphragm constraint. The specified point element was internally added by the
            program for application of auto wind and auto seismic loads.
        """
        _r = self._raw.GetObj(Name, "", 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetObj falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPatternValue(self, Name: str, PatternName: str):
        """This function retrieves the joint pattern value for a specific point element and joint
        pattern. The function returns zero if the value is successfully retrieved, otherwise
        it returns a nonzero value. Joint pattern values are unitless.
    
        Name (input): The name of an existing point element.
        PatternName (input): The name of a defined joint pattern.
        Value (output): The value that the specified point element has for the specified
            joint pattern.
        """
        _r = self._raw.GetPatternValue(Name, PatternName, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetPatternValue falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetRestraint(self, Name: str):
        """This function retrieves the restraint assignments for a point element. The restraint
        assignments are always returned in the point local coordinate system. The function
        returns zero if the restraint assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing point element.
        Value (output): This is an array of six restraint values. Value(0) = U1 Value(1) =
            U2 Value(2) = U3 Value(3) = R1 Value(4) = R2 Value(5) = R3
        """
        _r = self._raw.GetRestraint(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetRestraint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSpringCoupled(self, Name: str):
        """This function retrieves coupled spring stiffness assignments for a point element. The spring
        stiffnesses reported are the sum of all springs assigned to the point element either
        directly or indirectly through line, area and solid spring assignments. The spring
        stiffness values are reported in the point local coordinate system. The function
        returns zero if the stiffnesses are successfully retrieved, otherwise it returns a
        nonzero value. If no springs exist at the point element, the function returns a
        nonzero value.
    
        Name (input): The name of an existing point element.
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
            raise Sap2000ApiError("SapModel.PointElm.GetSpringCoupled falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSpring(self, Name: str):
        """This function retrieves uncoupled spring stiffness assignments for a point element; that is,
        it retrieves the diagonal terms in the 6x6 spring matrix for the point element. The
        spring stiffnesses reported are the sum of all springs assigned to the point element
        either directly or indirectly through line, area and solid spring assignments. The
        spring stiffness values are reported in the point local coordinate system. The
        function returns zero if the stiffnesses are successfully retrieved, otherwise it
        returns a nonzero value. If no springs exist at the point element, the function
        returns a nonzero value.
    
        Name (input): The name of an existing point element.
        k (output): This is an array of six spring stiffness values. Value(0) = U1 [F/L]
            Value(1) = U2 [F/L] Value(2) = U3 [F/L] Value(3) = R1 [FL/rad] Value(4) = R2
            [FL/rad] Value(5) = R3 [FL/rad]
        """
        _r = self._raw.GetSpring(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetSpring falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetTransformationMatrix(self, Name: str):
        """The function returns zero if the transformation matrix is successfully retrieved, otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing point element.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the point element local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array; (Local1, Local2, Local3)
            are an item (such as a point load) in the point element local coordinate system;
            and (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate
            system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PointElm.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def IsSpringCoupled(self, Name: str, IsCoupled: bool):
        """This function indicates if the spring assignments to a point element are coupled, that is,
        if there are off-diagonal terms in the 6x6 spring matrix for the point element. The
        function returns zero if the coupled status is successfully retrieved, otherwise it
        returns a nonzero value. If no springs exist at the point object, the function
        returns a nonzero value.
    
        Name (input): The name of an existing point element.
        IsCoupled (input): This item is True if the spring assignment to the specified point
            element is coupled, otherwise it is False.
        """
        _r = self._raw.IsSpringCoupled(Name, IsCoupled)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PointElm.IsSpringCoupled falhou (ret={_r})".format(_r=_r))
        return None


