"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_LineElm:
    """Wrapper para SapModel.LineElm."""

    def __init__(self, raw):
        self._raw = raw

    def Count(self):
        """This function returns the total number of line elements in the analysis model.
        """
        _r = self._raw.Count()
        return _r

    def GetEndLengthOffset(self, Name: str):
        """This function retrieves the line element end offsets along the 1-axis of the element. The
        function returns zero if the offsets are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing line element.
        Length1 (output): The offset length along the 1-axis of the line element at the
            I-End of the line element. [L]
        Length2 (output): The offset along the 1-axis of the line element at the J-End of
            the line element. [L]
        rz (output): The rigid zone factor. This is the fraction of the end offset length
            assumed to be rigid for bending and shear deformations.
        """
        _r = self._raw.GetEndLengthOffset(Name, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetEndLengthOffset falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetInsertionPoint(self, Name: str):
        """This function retrieves line element insertion point assignments. The assignments are
        reported as end joint offsets. The function returns zero if the insertion point data
        is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing line element.
        Offset1 (output): This is an array of three joint offset distances, in the Global
            coordinate system, at the I-End of the line element. [L] Offset1(0) = I-End
            offset in the global X-axis direction Offset1(1) = I-End offset in the global
            Y-axis direction Offset1(2) = I-End offset in the global Z-axis direction
        Offset2 (output): This is an array of three joint offset distances, in the Global
            coordinate system, at the J-End of the line element. [L] Offset2(0) = J-End
            offset in the global X-axis direction Offset2(1) = J-End offset in the global
            Y-axis direction Offset2(2) = J-End offset in the global Z-axis direction
        """
        _r = self._raw.GetInsertionPoint(Name, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetInsertionPoint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDeformation(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the deformation load assignments to line elements. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing line object, line element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified line elements.
        LineName (output): This is an array that includes the name of the line element
            associated with each deformation load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each deformation load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the line elements
            corresponding to the line object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the line element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the line elements corresponding to all line objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for line elements corresponding to all selected line objects, and
            the Name item is ignored.
        """
        _r = self._raw.GetLoadDeformation(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetLoadDeformation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDistributed(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the distributed load assignments to line elements. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing line object, line element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of distributed loads retrieved for the
            specified line elements.
        LineName (output): This is an array that includes the name of the line element
            associated with each distributed load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the distributed loads are specified.
        MyType (output): This is an array that includes either 1 or 2, indicating the type
            of distributed load. 1 = Force 2 = Moment
        CSys (output): This is an array that includes the name of the coordinate system in
            which each distributed load is defined. It may be Local or the name of a defined
            coordinate system.
        Dir (output): This is an array that includes an integer between 1 and 11, indicating
            the direction of the load. 1 = Local 1 axis (only applies when CSys is Local) 2
            = Local 2 axis (only applies when CSys is Local) 3 = Local 3 axis (only applies
            when CSys is Local) 4 = X direction (does not apply when CSys is Local) 5 = Y
            direction (does not apply when CSys is Local) 6 = Z direction (does not apply
            when CSys is Local) 7 = Projected X direction (does not apply when CSys is
            Local) 8 = Projected Y direction (does not apply when CSys is Local) 9 =
            Projected Z direction (does not apply when CSys is Local) 10 = Gravity direction
            (only applies when CSys is Global) 11 = Projected Gravity direction (only
            applies when CSys is Global) The positive gravity direction (see Dir = 10 and
            11) is in the negative Global Z direction.
        RD1 (output): This is an array that includes the relative distance from the I-End of
            the line element to the start of the distributed load.
        RD2 (output): This is an array that includes the relative distance from the I-End of
            the line element to the end of the distributed load.
        Dist1 (output): This is an array that includes the actual distance from the I-End of
            the line element to the start of the distributed load. [L]
        Dist2 (output): This is an array that includes the actual distance from the I-End of
            the line element to the end of the distributed load. [L]
        Val1 (output): This is an array that includes the load value at the start of the
            distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2
        Val2 (output): This is an array that includes the load value at the end of the
            distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the line elements
            corresponding to the line object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the line element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the line elements corresponding to all line objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for line elements corresponding to all selected line objects, and
            the Name item is ignored.
        """
        _r = self._raw.GetLoadDistributed(Name, 0, [], [], [], [], [], [], [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetLoadDistributed falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadGravity(self, Name: str, ItemType: int = 0):
        """This function retrieves the gravity load assignments to line elements. The function returns
        zero if the load assignments are successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing line object, line element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            line elements.
        LineName (output): This is an array that includes the name of the line element
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadPoint(self, Name: str, ItemType: int = 0):
        """This function retrieves the point load assignments to line elements. The function returns
        zero if the load assignments are successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing line object, line element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of point loads retrieved for the specified
            line elements.
        LineName (output): This is an array that includes the name of the line element
            associated with each point load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the point loads are specified.
        MyType (output): This is an array that includes either 1 or 2, indicating the type
            of point load. 1 = Force 2 = Moment
        CSys (output): This is an array that includes the name of the coordinate system in
            which each point load is defined. It may be Local or the name of a defined
            coordinate system.
        Dir (output): This is an array that includes an integer between 1 and 11, indicating
            the direction of the load. 1 = Local 1 axis (only applies when CSys is Local) 2
            = Local 2 axis (only applies when CSys is Local) 3 = Local 3 axis (only applies
            when CSys is Local) 4 = X direction (does not apply when CSys is Local) 5 = Y
            direction (does not apply when CSys is Local) 6 = Z direction (does not apply
            when CSys is Local) 7 = Projected X direction (does not apply when CSys is
            Local) 8 = Projected Y direction (does not apply when CSys is Local) 9 =
            Projected Z direction (does not apply when CSys is Local) 10 = Gravity direction
            (only applies when CSys is Global) 11 = Projected Gravity direction (only
            applies when CSys is Global) The positive gravity direction (see Dir = 10 and
            11) is in the negative Global Z direction.
        RelDist (output): This is an array that includes the relative distance from the
            I-End of the line element to the location where the point load is applied.
        Dist (output): This is an array that includes the actual distance from the I-End of
            the line element to the location where the point load is applied. [L]
        Val (output): This is an array that includes the value of the point load. [F] when
            MyType is 1 and [FL] when MyType is 2
        """
        _r = self._raw.GetLoadPoint(Name, 0, [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetLoadPoint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadStrain(self, Name: str, ItemType: int = 0):
        """This function retrieves the strain load assignments to line elements. The function returns
        zero if the strain load assignments are successfully retrieved, otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing line object, line element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of strain loads retrieved for the specified
            line elements.
        LineName (output): This is an array that includes the name of the line element
            associated with each strain load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each strain load.
        DOF (output): This is an array that includes 1, 2, 3, 4, 5 or 6, indicating the
            degree of freedom associated with each strain load. 1 = Strain11 2 = Strain12 3
            = Strain13 4 = Curvature1 5 = Curvature2 6 = Curvature3
        Val (output): This is an array that includes the strain value. [L/L] for DOF = 1, 2
            and 3 and [1/L] for DOF = 4, 5 and 6
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the strain load.
        """
        _r = self._raw.GetLoadStrain(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetLoadStrain falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTargetForce(self, Name: str, ItemType: int = 0):
        """This function retrieves the target force assignments to line elements. The function returns
        zero if the target force assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing line object, line element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified line elements.
        LineName (output): This is an array that includes the name of the line element
            associated with each target force.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each target force.
        """
        _r = self._raw.GetLoadTargetForce(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetLoadTargetForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTemperature(self, Name: str, ItemType: int = 0):
        """This function retrieves the temperature load assignments to line elements. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing line object, line element or group of objects,
            depending on the value of the ItemTypeElm item.
        NumberItems (output): The total number of temperature loads retrieved for the
            specified line elements.
        LineName (output): This is an array that includes the name of the line element
            associated with each temperature load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each temperature load.
        MyType (output): This is an array that includes 1, 2 or 3, indicating the type of
            temperature load. 1 = Temperature 2 = Temperature gradient along local 2 axis 3
            = Temperature gradient along local 3 axis
        Val (output): This is an array that includes the temperature load value. [T] for
            MyType= 1 and [T/L] for MyType= 2 and 3
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the temperature load.
        """
        _r = self._raw.GetLoadTemperature(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetLoadTemperature falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str):
        """This function retrieves the local axis angle assignment for line elements. The function
        returns zero if the assignment is successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing line element.
        Ang (output): This is the angle that the local 2 and 3 axes are rotated about the
            positive local 1 axis, from the default orientation. The rotation for a positive
            angle appears counterclockwise when the local +1 axis is pointing toward you.
            [deg]
        """
        _r = self._raw.GetLocalAxes(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMatTemp(self, Name: str, Temp: float):
        """This function retrieves the material temperature assignments to line elements. The function
        returns zero if the material temperature assignments are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing line element.
        Temp (input): This is the material temperature value assigned to the line element.
            [T]
        PatternName (output): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the line element is uniform along the
            element at the value specified by Temp. If PatternName is the name of a defined
            joint pattern, the material temperature for the line element may vary from one
            end to the other. The material temperature at each end of the element is equal
            to the specified temperature multiplied by the pattern value at the joint at the
            end of the line element.
        """
        _r = self._raw.GetMatTemp(Name, Temp, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetMatTemp falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMaterialOverwrite(self, Name: str):
        """This function retrieves the material overwrite assigned to a line element, if any. It
        returns None if there is no material overwrite assignment. The function returns zero
        if the material overwrite assignment is successfully retrieved, otherwise it returns
        a nonzero value.
    
        Name (input): The name of a defined line element.
        PropName (output): This is None, indicating that no material overwrite exists for
            the specified line element, or it is the name of an existing material property.
        """
        _r = self._raw.GetMaterialOverwrite(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetMaterialOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetModifiers(self, Name: str):
        """This function retrieves the section modifier assignment for line elements. The default value
        for all modifiers is one. The function returns zero if the modifier assignments are
        successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing line element.
        Value (output): This is an array of eight unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Shear area in local 2 direction modifier
            Value(2) = Shear area in local 3 direction modifier Value(3) = Torsional
            constant modifier Value(4) = Moment of inertia about local 2 axis modifier
            Value(5) = Moment of inertia about local 3 axis modifier Value(6) = Mass
            modifier Value(7) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined line elements. The function returns zero if
        the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of line element names retrieved by the program.
        MyName (output): This is a one-dimensional array of line element names. The MyName
            array is created as a dynamic, zero-based, array by the APIuser: Dim MyName() as
            String The array is dimensioned to (NumberNames 1) inside the Sap2000 program,
            filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetObj(self, Name: str):
        """This function retrieves information about the object from which a line element was created.
        The function returns zero if the information is successfully retrieved, otherwise it
        returns nonzero.
    
        Name (input): The name of an existing line element.
        Obj (output): The name of the frame, cable or tendon object from which the line
            element was created.
        ObjType (output): This is 0, 1, 2 or 3, indicating the type of object from which the
            line element was created. 0 = Straight frame object 1 = Curved frame object 2 =
            Cable object 3 = Tendon object
        RDI (output): The relative distance from the I-End of the object identified by the
            Obj item to the I-End of the considered line element. The relative distance is
            calculated as the distance from the I-End of the object to the I-End of the line
            element divided by the length of the object.
        RDJ (output): The relative distance from the I-End of the object identified by the
            Obj item to the J-End of the considered line element. The relative distance is
            calculated as the distance from the I-End of the object to the J-End of the line
            element divided by the length of the object.
        """
        _r = self._raw.GetObj(Name, "", 0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetObj falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPDeltaForce(self, Name: str, NumberForces: int, PDeltaForce: list[float]):
        """This function retrieves the P-Delta force assignments to line elements. The function returns
        zero if the assignments are successfully retrieved, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing line element.
        NumberForces (input): The number of P-Delta forces assigned to the line element.
        PDeltaForce (input): This is an array of the P-Delta force values assigned to the
            line element. [F]
        Dir (output): This is an array that contains 0, 1, 2 or 3, indicating the direction
            of each P-Delta force assignment. 0 = Frame object local 1-axis direction 1 =
            Projected X direction in CSys coordinate system 2 = Projected Y direction in
            CSys coordinate system 3 = Projected Z direction in CSys coordinate system
        CSys (output): This is an array that contains the name of the coordinate system in
            which each projected P-Delta force is defined. This item is blank when the Dir
            item is zero, that is, when the P-Delta force is defined in the line element
            local 1-axis direction.
        """
        _r = self._raw.GetPDeltaForce(Name, NumberForces, PDeltaForce, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetPDeltaForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoints(self, Name: str):
        """This function retrieves the names of the point elements at each end of a specified line
        element. The function returns zero if the point names are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of a defined line element.
        Point1 (output): The name of the point element at the I-End of the specified line
            element.
        Point2 (output): The name of the point element at the J-End of the specified line
            element.
        """
        _r = self._raw.GetPoints(Name, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetProperty(self, Name: str, PropName: str, Var: bool):
        """This function retrieves the property assignment to a line element. The function returns zero
        if the property data is successfully retrieved, otherwise it returns a nonzero
        value. The sVarTotalLength and sVarRelStartLoc items apply only when the Var item is
        True.
    
        Name (input): The name of an existing line element.
        PropName (input): The name of the frame section, cable or tendon property assigned
            to the line element.
        ObjType (output): This is 0, 1, 2 or 3, indicating the type of object from which the
            line element was created. 0 = Straight frame object 1 = Curved frame object 2 =
            Cable object 3 = Tendon object
        Var (input): This item is True if the specified property is a nonprismatic
            (variable) frame section property.
        sVarRelStartLoc (output): This is the relative distance along the nonprismatic
            section to the I-End (start) of the line element. This item is ignored when the
            sVarTotalLengthitem is 0.
        sVarTotalLength (output): This is the total assumed length of the nonprismatic
            section. A zero value for this item means that the section length is the same as
            the line element length.
        """
        _r = self._raw.GetProperty(Name, PropName, 0, Var, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetProperty falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetReleases(self, Name: str):
        """This function retrieves the line element end release and partial fixity assignments. The
        function returns zero if the assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing line element.
        """
        _r = self._raw.GetReleases(Name, [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetReleases falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTCLimits(self, Name: str, LimitCompressionExists: bool, LimitTensionExists: bool):
        """This function retrieves the tension/compression force limit assignments to line elements.
        The function returns zero if the assignments are successfully retrieved, otherwise
        it returns a nonzero value. Note that the tension and compression limits are only
        used in nonlinear analyses.
    
        Name (input): The name of an existing line element.
        LimitCompressionExists (input): This item is True if a compression force limit
            exists for the line element.
        LimitCompression (output): The compression force limit for the line element. [F]
        LimitTensionExists (input): This item is True if a tension force limit exists for
            the line element.
        LimitTension (output): The tension force limit for the line element. [F]
        """
        _r = self._raw.GetTCLimits(Name, LimitCompressionExists, 0.0, LimitTensionExists, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetTCLimits falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTransformationMatrix(self, Name: str):
        """The function returns zero if the transformation matrix is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing line element.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the line element local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array, (Local1, Local2, Local3)
            are an item (such as a load) in the element local coordinate system, and
            (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LineElm.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


