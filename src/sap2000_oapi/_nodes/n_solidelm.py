"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_SolidElm:
    """Wrapper para SapModel.SolidElm."""

    def __init__(self, raw):
        self._raw = raw

    def Count(self):
        """This function returns the total number of solid elements in the analysis model.
        """
        _r = self._raw.Count()
        return _r

    def GetLoadGravity(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the gravity load assignments to solid elements. The function returns
        zero if the load assignments are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing solid element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            solid elements.
        SolidName (output): This is an array that includes the name of the solid element
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the solid elements
            corresponding to the solid object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the solid element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the solid elements corresponding to all solid objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for solid elements corresponding to all selected solid objects,
            and the Name item is ignored.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadPorePressure(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the pore pressure load assignments to solid elements. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing solid element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of pore pressure loads retrieved for the
            specified solid elements.
        SolidName (output): This is an array that includes the name of the solid element
            associated with each pore pressure load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each pore pressure load.
        Value (output): This is an array that includes the pore pressure load value. [F/L 2
            ]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the pore pressure load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the solid elements
            corresponding to the solid object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the solid element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the solid elements corresponding to all solid objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for solid elements corresponding to all selected solid objects,
            and the Name item is ignored.
        """
        _r = self._raw.GetLoadPorePressure(Name, 0, [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetLoadPorePressure falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadStrain(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the strain load assignments to solid elements. The function returns
        zero if the strain load assignments are successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing solid element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of strain loads retrieved for the specified
            solid elements.
        SolidName (output): This is an array that includes the name of the solid element
            associated with each strain load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each strain load.
        Component (output): This is 1, 2, 3, 4, 5 or 6, indicating the component to which
            the strain load is applied. 1 = Strain11 2 = Strain22 3 = Strain33 4 = Strain12
            5 = Strain13 6 = Strain23
        Value (output): This is an array that includes the strain value. [L/L]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the strain load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the solid elements
            corresponding to the solid object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the solid element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the solid elements corresponding to all solid objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for solid elements corresponding to all selected solid objects,
            and the Name item is ignored.
        """
        _r = self._raw.GetLoadStrain(Name, 0, [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetLoadStrain falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadSurfacePressure(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the surface pressure load assignments to solid objects. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing solid element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of surface pressure loads retrieved for the
            specified solid elements.
        SolidName (output): This is an array that includes the name of the solid element
            associated with each surface pressure load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each surface pressure load.
        Face (output): This is an array that includes 1, 2, 3, 4, 5 or 6, indicating the
            solid element face to which the specified load assignment applies.
        Value (output): This is an array that includes the surface pressure load value. [F/L
            2 ]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the surface pressure load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the solid elements
            corresponding to the solid object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the solid element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the solid elements corresponding to all solid objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for solid elements corresponding to all selected solid objects,
            and the Name item is ignored.
        """
        _r = self._raw.GetLoadSurfacePressure(Name, 0, [], [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetLoadSurfacePressure falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTemperature(self, Name: str, ItemTypeElm: int = 1):
        """This function retrieves the temperature load assignments to solid elements. The function
        returns zero if the load assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing solid element or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of temperature loads retrieved for the
            specified solid elements.
        SolidName (output): This is an array that includes the name of the solid element
            associated with each temperature load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each temperature load.
        Value (output): This is an array that includes the temperature load value. [T]
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the temperature load.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the load assignments are retrieved for the solid elements
            corresponding to the solid object specified by the Name item. If this item is
            Element, the load assignments are retrieved for the solid element specified by
            the Name item. If this item is GroupElm, the load assignments are retrieved for
            the solid elements corresponding to all solid objects included in the group
            specified by the Name item. If this item is SelectionElm, the load assignments
            are retrieved for solid elements corresponding to all selected solid objects,
            and the Name item is ignored.
        """
        _r = self._raw.GetLoadTemperature(Name, 0, [], [], [], [], ItemTypeElm)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetLoadTemperature falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str):
        """This function retrieves the local axis angle assignment for solid elements. The function
        returns zero if the assignment is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing solid element.
        """
        _r = self._raw.GetLocalAxes(Name, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMatTemp(self, Name: str, Temp: float):
        """This function retrieves the material temperature assignments to solid elements. The function
        returns zero if the material temperature assignments are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid element.
        Temp (input): This is the material temperature value assigned to the solid element.
            [T]
        PatternName (output): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the solid element is uniform over the
            element at the value specified by Temp. If PatternName is the name of a defined
            joint pattern, the material temperature for the solid element may vary. The
            material temperature at each corner point of the solid element is equal to the
            specified temperature multiplied by the pattern value at the associated point
            element. The material temperature at other locations in the solid element is
            calculated by interpolation from the corner points.
        """
        _r = self._raw.GetMatTemp(Name, Temp, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetMatTemp falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined solid elements. The function returns zero
        if the names are successfully retrieved; otherwise it returns nonzero.
    
        NumberNames (output): The number of solid element names retrieved by the program.
        MyName (output): This is a one-dimensional array of solid element names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames 1) inside the SAP2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetObj(self, Name: str):
        """This function retrieves the name of the solid object from which a solid element was created.
        The function returns zero if the information is successfully retrieved; otherwise it
        returns nonzero.
    
        Name (input): The name of an existing solid element.
        Obj (output): The name of the solid object from which the solid element was created.
        """
        _r = self._raw.GetObj(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetObj falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPoints(self, Name: str):
        """This function retrieves the names of the eight point elements that define a solid element.
        The function returns zero if the point element names are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an solid element.
        Point (output): This is an array containing the names of the eight point elements
            that define the solid element. The point names are in order around the solid
            element.
        """
        _r = self._raw.GetPoints(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetProperty(self, Name: str, PropName: str):
        """This function retrieves the solid property assigned to a solid element. The function returns
        zero if the property is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of a defined solid element.
        PropName (input): The name of the solid property assigned to the solid element.
        """
        _r = self._raw.GetProperty(Name, PropName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetProperty falhou (ret={_r})".format(_r=_r))
        return None

    def GetTransformationMatrix(self, Name: str):
        """The function returns zero if the transformation matrix is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing solid element.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the solid element local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array, (Local1, Local2, Local3)
            are an item (such as a load) in the element local coordinate system, and
            (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SolidElm.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


