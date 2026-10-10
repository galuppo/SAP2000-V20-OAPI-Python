"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_AreaElm:
    """Wrapper para SapModel.AreaElm."""

    def __init__(self, raw):
        self._raw = raw

    def Count(self):
        """This function returns the total number of area elements in the analysis model.
        """
        _r = self._raw.Count()
        return _r

    def GetLoadGravity(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the gravity load assignments to area elements. The function returns
        zero if the load assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            area elements.
        AreaName (output): This is an array that includes the name of the area element
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the area elements
            corresponding to the area object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the area element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the area elements corresponding to all area objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for area elements corresponding to all selected area objects, and
            the Name item is ignored.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadPorePressure(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the pore pressure load assignments to area elements. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area element or group depending on the value
            of the ItemType item.
        NumberItems (output): The total number of pore pressure loads retrieved for the
            specified area elements.
        AreaName (output): This is an array that includes the name of the area element
            associated with each pore pressure load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each pore pressure load.
        Value (output): This is an array that includes the pore pressure load value. [F/L 2
            ]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the pore pressure load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the area elements
            corresponding to the area object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the area element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the area elements corresponding to all area objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for area elements corresponding to all selected area objects, and
            the Name item is ignored.
        """
        _r = self._raw.GetLoadPorePressure(Name, 0, [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetLoadPorePressure falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadStrain(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the strain load assignments to area elements. The function returns
        zero if the strain load assignments are successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing area element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of strain loads retrieved for the specified
            area elements.
        AreaName (output): This is an array that includes the name of the area element
            associated with each strain load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each strain load.
        Component (output): This is an array that includes 1, 2, 3, 4, 5, 6, 7 or 8,
            indicating the component associated with each strain load. 1 = Strain11 2 =
            Strain22 3 = Strain12 4 = Curvature11 5 = Curvature22 6 = Curvature12 7 =
            Strain13 8 = Strain23
        Value (output): This is an array that includes the strain value. [L/L] for Component
            = 1, 2, 3, 7 and 8, and [1/L] for Component = 4, 5 and 6
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the strain load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the area elements
            corresponding to the area object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the area element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the area elements corresponding to all area objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for area elements corresponding to all selected area objects, and
            the Name item is ignored.
        """
        _r = self._raw.GetLoadStrain(Name, 0, [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetLoadStrain falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadSurfacePressure(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the surface pressure load assignments to area elements. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of surface pressure loads retrieved for the
            specified area elements.
        AreaName (output): This is an array that includes the name of the area element
            associated with each surface pressure load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each surface pressure load.
        Face (output): This is an array that includes -1, -2 or a nonzero, positive integer,
            indicating the area element face to which the specified load assignment applies.
            -1 = Bottom face -2 = Top face >0 = Edge face Note that edge face n is from area
            element point n to area element point n + 1. For example, edge face 2 is from
            area element point 2 to area element point 3.
        Value (output): This is an array that includes the surface pressure load value. [F/L
            2 ]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the surface pressure load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the area elements
            corresponding to the area object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the area element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the area elements corresponding to all area objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for area elements corresponding to all selected area objects, and
            the Name item is ignored.
        """
        _r = self._raw.GetLoadSurfacePressure(Name, 0, [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetLoadSurfacePressure falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTemperature(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the temperature load assignments to area elements. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing area element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of temperature loads retrieved for the
            specified area elements.
        AreaName (output): This is an array that includes the name of the area element
            associated with each temperature load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each temperature load.
        MyType (output): This is an array that includes either 1 or 3, indicating the type
            of temperature load. 1 = Temperature 3 = Temperature gradient along local 3 axis
        Value (output): This is an array that includes the temperature load value. [T] for
            MyType= 1 and [T/L] for MyType= 3
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the temperature load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the area elements
            corresponding to the area object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the area element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the area elements corresponding to all area objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for area elements corresponding to all selected area objects, and
            the Name item is ignored.
        """
        _r = self._raw.GetLoadTemperature(Name, 0, [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetLoadTemperature falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadUniform(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the uniform load assignments to area elements. The function returns
        zero if the load assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of uniform loads retrieved for the specified
            area elements.
        AreaName (output): This is an array that includes the name of the area element
            associated with each uniform load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the uniform load is specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each uniform load.
        Dir (output): This is an integer between 1 and 11, indicating the direction of the
            load. 1 = Local 1 axis (applies only when CSys is Local) 2 = Local 2 axis
            (applies only when CSys is Local) 3 = Local 3 axis (applies only when CSys is
            Local) 4 = X direction (does not apply when CSys is Local) 5 = Y direction (does
            not apply when CSys is Local) 6 = Z direction (does not apply when CSys is
            Local) 7 = Projected X direction (does not apply when CSys is Local) 8 =
            Projected Y direction (does not apply when CSys is Local) 9 = Projected Z
            direction (does not apply when CSys is Local) 10 = Gravity direction (applies
            only when CSys is Global) 11 = Projected Gravity direction (applies only when
            CSys is Global) The positive gravity direction (see Dir = 10 and 11) is in the
            negative Global Z direction.
        Value (output): The uniform load value. [F/L 2 ]
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the area elements
            corresponding to the area object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the area element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the area elements corresponding to all area objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for area elements corresponding to all selected area objects, and
            the Name item is ignored.
        """
        _r = self._raw.GetLoadUniform(Name, 0, [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetLoadUniform falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str):
        """This function retrieves the local axis angle assignment for area elements. The function
        returns zero if the assignment is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area element.
        Ang (output): This is the angle that the local 1 and 2 axes are rotated about the
            positive local 3 axis from the default orientation. The rotation for a positive
            angle appears counter clockwise when the local +3 axis is pointing toward you.
            [deg]
        """
        _r = self._raw.GetLocalAxes(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMatTemp(self, Name: str, Temp: float):
        """This function retrieves the material temperature assignments to area elements. The function
        returns zero if the material temperature assignments are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area element.
        Temp (input): This is the material temperature value assigned to the area element.
            [T]
        PatternName (output): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the area element is uniform over the element
            at the value specified by Temp. If PatternName is the name of a defined joint
            pattern, the material temperature for the area element may vary. The material
            temperature at each corner point around the area element perimeter is equal to
            the specified temperature multiplied by the pattern value at the associated
            point element. The material temperature at other points in the area element is
            calculated by interpolation from the corner points.
        """
        _r = self._raw.GetMatTemp(Name, Temp, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetMatTemp falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMaterialOverwrite(self, Name: str):
        """This function retrieves the material overwrite assigned to an area element, if any. The
        material property name is indicated as None if there is no material overwrite
        assignment. The function returns zero if the material overwrite assignment is
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a defined area element.
        PropName (output): This is None, indicating that no material overwrite exists for
            the specified area element, or it is the name of an existing material property.
        """
        _r = self._raw.GetMaterialOverwrite(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetMaterialOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetModifiers(self, Name: str):
        """This function retrieves the modifier assignment for area elements. The default value for all
        modifiers is one. The function returns zero if the modifier assignments are
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area element.
        Value (output): This is an array of ten unitless modifiers. Value(0) = Membrane f11
            modifier Value(1) = Membrane f22 modifier Value(2) = Membrane f12 modifier
            Value(3) = Bending m11 modifier Value(4) = Bending m22 modifier Value(5) =
            Bending m12 modifier Value(6) = Shear v13 modifier Value(7) = Shear v23 modifier
            Value(8) = Mass modifier Value(9) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined area elements. The function returns zero if
        the names are successfully retrieved; otherwise it returns nonzero.
    
        NumberNames (output): The number of area element names retrieved by the program.
        MyName (output): This is a one-dimensional array of area element names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames – 1) inside the SAP2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetObj(self, Name: str):
        """This function retrieves the name of the area object from which an area element was created.
        The function returns zero if the information is successfully retrieved; otherwise it
        returns nonzero.
    
        Name (input): The name of an existing area element.
        Obj (output): The name of the area object from which the area element was created.
        """
        _r = self._raw.GetObj(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetObj falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetOffsets(self, Name: str):
        """This function retrieves the joint offset assignments for area elements. The function returns
        zero if the assignments are successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing area element.
        OffsetType (output): This is 0, 1 or 2, indicating the joint offset type. 0 = No
            joint offsets 1 = User defined joint offsets specified by joint pattern 2 = User
            defined joint offsets specified by point
        OffsetPattern (output): This item applies only when OffsetType = 1. It is the name
            of the defined joint pattern that is used to calculate the joint offsets.
        OffsetPatternSF (output): This item only applies when OffsetType = 1. It is the
            scale factor applied to the joint pattern when calculating the joint offsets.
            [L]
        Offset (output): This item applies only when OffsetType = 2. It is an array of joint
            offsets for each of the points that define the area element. [L]
        """
        _r = self._raw.GetOffsets(Name, 0, "", 0.0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetOffsets falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoints(self, Name: str):
        """This function retrieves the names of the point elements that define an area element. The
        function returns zero if the point element names are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an area element.
        NumberPoints (output): The number of point elements that define the area element.
        Point (output): This is an array containing the names of the point elements that
            define the area element. The point names are in order around the area element.
        """
        _r = self._raw.GetPoints(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetProperty(self, Name: str, PropName: str):
        """This function retrieves the area property assigned to an area element. The function returns
        zero if the property is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of a defined area element.
        PropName (input): The name of the area property assigned to the area element. This
            item is None if there is no area property assigned to the area element.
        """
        _r = self._raw.GetProperty(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def GetThickness(self, Name: str):
        """This function retrieves the thickness overwrite assignments for area elements. The function
        returns zero if the assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing area element.
        ThicknessType (output): This is 0, 1 or 2, indicating the thickness overwrite type.
            0 = No thickness overwrites 1 = User defined thickness overwrites specified by
            joint pattern 2 = User defined thickness overwrites specified by point
        ThicknessPattern (output): This item applies only when ThicknessType = 1. It is the
            name of the defined joint pattern that is used to calculate the thicknesses.
        ThicknessPatternSF (output): This item applies only when ThicknessType = 1. It is
            the scale factor applied to the joint pattern when calculating the thicknesses.
            [L]
        Thickness (output): This item applies only when ThicknessType = 2. It is an array of
            thicknesses at each of the points that define the area element. [L]
        """
        _r = self._raw.GetThickness(Name, 0, "", 0.0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetThickness falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTransformationMatrix(self, Name: str):
        """The function returns zero if the transformation matrix is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing area element.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the area element local
            coordinate system to the global coordinate system. In the equation c0 through c8
            are the nine values from the transformation array, (Local1, Local2, Local3) are
            an item (such as a load) in the element local coordinate system, and (GlobalX,
            GlobalY, GlobalZ) are the same item in the global coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.AreaElm.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


