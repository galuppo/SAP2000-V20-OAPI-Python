"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PropArea:
    """Wrapper para SapModel.PropArea."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing area property. The function returns zero if
        the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined area property.
        NewName (input): The new name for the area property.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropArea.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self, PropType: int = 0):
        """This function returns the total number of defined area properties in the model. If desired,
        counts can be returned for all area properties of a specified type in the model.
    
        PropType (input): This optional value is 0, 1, 2 or 3, indicating the type of area
            properties included in the count. 0 = All 1 = Shell 2 = Plane 3 = Asolid
        """
        _r = self._raw.Count(PropType)
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified area property. The function returns zero if the area
        property is successfully deleted; otherwise it returns a nonzero value. It returns
        an error if the specified area property can not be deleted, for example, if it is
        being used by an area object.
    
        Name (input): The name of an existing area property.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropArea.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetAsolid(self, Name: str, Incompatible: bool, Color: int, Notes: str, GUID: str):
        """This function retrieves area property data for an asolid-type area section. The function
        returns zero if the property data is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing asolid-type area property.
        MatProp (output): The name of the material property for the area property.
        MatAng (output): The material angle. [deg]
        Arc (output): The arc angle through which the area object is passed to define the
            asolid element. [deg] A value of zero means 1 radian (approximately 57.3
            degrees).
        Incompatible (input): If this item is True, incompatible bending modes are included
            in the stiffness formulation. In general, incompatible modes significantly
            improve the bending behavior of the object.
        CSys (output): The area object is rotated about the Z-axis in this coordinate system
            to define the asolid element.
        Color (input): The display color assigned to the property.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetAsolid(Name, "", 0.0, 0.0, Incompatible, "", Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropArea.GetAsolid falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetModifiers(self, Name: str):
        """This function retrieves the modifier assignments for an area property. The default value for
        all modifiers is one. The function returns zero if the modifier assignments are
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area property.
        Value (output): This is an array of 10 unitless modifiers. Value(0) = Membrane f11
            modifier Value(1) = Membrane f22 modifier Value(2) = Membrane f12 modifier
            Value(3) = Bending m11 modifier Value(4) = Bending m22 modifier Value(5) =
            Bending m12 modifier Value(6) = Shear v13 modifier Value(7) = Shear v23 modifier
            Value(8) = Mass modifier Value(9) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropArea.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self, PropType: int = 0):
        """This function retrieves the names of all defined area properties of the specified type. The
        function returns zero if the names are successfully retrieved; otherwise it returns
        nonzero.
    
        NumberNames (output): The number of area property names retrieved by the program.
        MyName (output): This is a one-dimensional array of area property names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames - 1) inside the SAP2000
            program, filled with the names, and returned to the API user.
        PropType (input): This optional value is 0, 1, 2 or 3, indicating the type of area
            properties included in the name list. 0 = All 1 = Shell 2 = Plane 3 = Asolid
        """
        _r = self._raw.GetNameList(0, [], PropType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropArea.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPlane(self, Name: str, Incompatible: bool, Color: int, Notes: str, GUID: str):
        """This function retrieves area property data for a plane-type area section. The function
        returns zero if the property data is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing plane-type area property.
        MyType (output): This is either 1 or 2, indicating the plane type. 1 = Plane-stress
            2 = Plane-strain
        MatProp (output): The name of the material property for the area property.
        MatAng (output): The material angle. [deg]
        Thickness (output): The plane thickness. [L]
        Incompatible (input): If this item is True, incompatible bending modes are included
            in the stiffness formulation. In general, incompatible modes significantly
            improve the bending behavior of the object.
        Color (input): The display color assigned to the property.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetPlane(Name, 0, "", 0.0, 0.0, Incompatible, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropArea.GetPlane falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetShellDesign(self, Name: str):
        """This function retrieves area property design parameters for a shell-type area section. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing shell-type area property.
        MatProp (output): The name of the material property for the area property.
        SteelLayoutOption (output): This is 0, 1 or 2 indicating, the rebar layout option. 0
            = Default 1 = One layer 2 = Two layers
        """
        _r = self._raw.GetShellDesign(Name, "", 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropArea.GetShellDesign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetShellLayer_1(self, Name: str):
        """This function retrieves area property layer parameters for a shell-type area section. The
        function returns zero if the parameters are successfully retrieved, otherwise it
        returns a nonzero value. The function returns an error if the specified area
        property is not a shell-type property specified to be a layered shell.
    
        Name (input): The name of an existing shell-type area property that is specified to
            be a layered shell property.
        NumberLayers (output): The number of layers in the area property.
        LayerName (output): This is an array that includes the name of each layer.
        Dist (output): This is an array that includes the distance from the area reference
            surface (area object joint location plus offsets) to the mid-height of the
            layer. [L]
        Thickness (output): This is an array that includes the thickness of each layer. [L]
        NumIntegrationPts (output): The number of integration points in the thickness
            direction for the layer. The locations are determined by the program using
            standard Guass-quadrature rules.
        MatProp (output): This is an array that includes the name of the material property
            for the layer.
        """
        _r = self._raw.GetShellLayer_1(Name, 0, [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropArea.GetShellLayer_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetShell(self, Name: str, IncludeDrillingDOF: bool, Color: int, Notes: str, GUID: str):
        """This function retrieves area property data for a shell-type area section. The function
        returns zero if the property data is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing shell-type area property.
        ShellType (output): This is 1, 2, 3, 4, 5 or 6, indicating the shell type. 1 = Shell
            - thin 2 = Shell - thick 3 = Plate - thin 4 = Plate - thick 5 = Membrane 6 =
            Shell layered/nonlinear
        IncludeDrillingDOF (input): This item is True if drilling degrees of freedom are
            included in the element formulation in the analysis model. This item does not
            apply when ShellType = 3, 4 or 6.
        MatProp (output): The name of the material property for the area property. This item
            does not apply when ShellType = 6.
        MatAng (output): The material angle. [deg] This item does not apply when ShellType =
            6.
        Thickness (output): The membrane thickness. [L] This item does not apply when
            ShellType = 6.
        Bending (output): The bending thickness. [L] This item does not apply when ShellType
            = 6.
        Color (input): The display color assigned to the property.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetShell(Name, 0, IncludeDrillingDOF, "", 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropArea.GetShell falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTypeOAPI(self, Name: str):
        """This function retrieves the property type for the specified area property. The function
        returns zero if the type is successfully retrieved; otherwise it returns nonzero.
    
        Name (input): The name of an existing area property.
        PropType (output): This is 1, 2 or 3, indicating the type of area property. 1 =
            Shell 2 = Plane 3 = Asolid
        """
        _r = self._raw.GetTypeOAPI(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropArea.GetTypeOAPI falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetAsolid(self, Name: str, MatProp: str, MatAng: float, Arc: float, Incompatible: bool, CSys: str = 'Global', Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes an asolid-type area property. If this function is called for an
        existing area property, all items for the property are reset to their default value.
        The function returns zero if the property is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new area property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        MatProp (input): The name of the material property for the area property.
        MatAng (input): The material angle. [deg]
        Arc (input): The arc angle through which the area object is passed to define the
            asolid element. [deg] A value of zero means 1 radian (approximately 57.3
            degrees).
        Incompatible (input): If this item is True, incompatible bending modes are included
            in the stiffness formulation. In general, incompatible modes significantly
            improve the bending behavior of the object.
        CSys (input): The area object is rotated about the Z-axis in this coordinate system
            to define the asolid element.
        Color (input): The display color assigned to the property. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetAsolid(Name, MatProp, MatAng, Arc, Incompatible, CSys, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropArea.SetAsolid falhou (ret={_r})".format(_r=_r))
        return None

    def SetModifiers(self, Name: str, Value: list[float]):
        """This function assigns property modifiers to an area property. The default value for all
        modifiers is one. The function returns zero if the modifiers are successfully
        assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area property.
        Value (input): This is an array of 10 unitless modifiers. Value(0) = Membrane f11
            modifier Value(1) = Membrane f22 modifier Value(2) = Membrane f12 modifier
            Value(3) = Bending m11 modifier Value(4) = Bending m22 modifier Value(5) =
            Bending m12 modifier Value(6) = Shear v13 modifier Value(7) = Shear v23 modifier
            Value(8) = Mass modifier Value(9) = Weight modifier
        """
        _r = self._raw.SetModifiers(Name, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropArea.SetModifiers falhou (ret={_r})".format(_r=_r))
        return None

    def SetPlane(self, Name: str, MyType: int, MatProp: str, MatAng: float, Thickness: float, Incompatible: bool, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a plane-type area property. If this function is called for an
        existing area property, all items for the property are reset to their default value.
        The function returns zero if the property is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new area property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        MyType (input): This is either 1 or 2, indicating the plane type. 1 = Plane-stress 2
            = Plane-strain
        MatProp (input): The name of the material property for the area property.
        MatAng (input): The material angle. [deg]
        Thickness (input): The plane thickness. [L]
        Incompatible (input): If this item is True, incompatible bending modes are included
            in the stiffness formulation. In general, incompatible modes significantly
            improve the bending behavior of the object.
        Color (input): The display color assigned to the property. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetPlane(Name, MyType, MatProp, MatAng, Thickness, Incompatible, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropArea.SetPlane falhou (ret={_r})".format(_r=_r))
        return None

    def SetShellDesign(self, Name: str, MatProp: str, SteelLayoutOption: int, DesignCoverTopDir1: float, DesignCoverTopDir2: float, DesignCoverBotDir1: float, DesignCoverBotDir2: float):
        """This function assigns the design parameters for shell-type area properties. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing shell-type area property.
        MatProp (input): The name of the material property for the area property.
        SteelLayoutOption (input): This is 0, 1 or 2, indicating the rebar layout option. 0
            = Default 1 = One layer 2 = Two layers
        """
        _r = self._raw.SetShellDesign(Name, MatProp, SteelLayoutOption, DesignCoverTopDir1, DesignCoverTopDir2, DesignCoverBotDir1, DesignCoverBotDir2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropArea.SetShellDesign falhou (ret={_r})".format(_r=_r))
        return None

    def SetShellLayer_1(self, Name: str, NumberLayers: int, LayerName: list[str], Dist: list[float], Thickness: list[float], MatProp: list[str], NonLinear: list[bool], MatAng: list[float], NumIntegrationPts: list[int]):
        """This function assigns the layer parameters for shell-type area properties. The function
        returns zero if the parameters are successfully assigned; otherwise, it returns a
        nonzero value. The function returns an error if the specified area property is not a
        shell-type property specified to be a layered shell.
    
        Name (input): The name of an existing shell-type area property that is specified to
            be a layered shell property.
        NumberLayers (input): The number of layers in the area property.
        LayerName (input): This is an array that includes the name of each layer.
        Dist (input): This is an array that includes the distance from the area reference
            surface (area object joint location plus offsets) to the mid-height of the
            layer. [L]
        Thickness (input): This is an array that includes the thickness of each layer. [L]
        MatProp (input): This is an array that includes the name of the material property
            for the layer.
        MatAng (input): This is an array that includes the material angle for the layer.
            [deg]
        NumIntegrationPts (input): The number of integration points in the thickness
            direction for the layer. The locations are determined by the program using
            standard Guass-quadrature rules.
        """
        _r = self._raw.SetShellLayer_1(Name, NumberLayers, LayerName, Dist, Thickness, MatProp, NonLinear, MatAng, NumIntegrationPts)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropArea.SetShellLayer_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetShell_1(self, Name: str, ShellType: int, IncludeDrillingDOF: bool, MatProp: str, MatAng: float, Thickness: float, Bending: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a shell-type area property. If this function is called for an
        existing area property, all items for the property are reset to their default value.
        The function returns zero if the property is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new area property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        ShellType (input): This is 1, 2, 3, 4, 5 or 6, indicating the shell type. 1 = Shell
            - thin 2 = Shell - thick 3 = Plate - thin 4 = Plate - thick 5 = Membrane 6 =
            Shell layered/nonlinear
        IncludeDrillingDOF (input): This item is True if drilling degrees of freedom are
            included in the element formulation in the analysis model. This item does not
            apply when ShellType = 3, 4 or 6.
        MatProp (input): The name of the material property for the area property. This item
            does not apply when ShellType = 6.
        MatAng (input): The material angle. [deg] This item does not apply when ShellType =
            6.
        Thickness (input): The membrane thickness. [L] This item does not apply when
            ShellType = 6.
        Bending (input): The bending thickness. [L] This item does not apply when ShellType
            = 6.
        Color (input): The display color assigned to the property. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, then the program assigns a GUID to the
            property.
        """
        _r = self._raw.SetShell_1(Name, ShellType, IncludeDrillingDOF, MatProp, MatAng, Thickness, Bending, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropArea.SetShell_1 falhou (ret={_r})".format(_r=_r))
        return None

    def GetNotionalSize(self, Name: str):
        """This function retrieves the method to determine the notional size of an area section for the
        creep and shrinkage calculations. This function is currently worked for shell type
        area section. The function returns zero if the parameters are successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing shell-type area section property.
        stype (output): The type to define the notional size of a section. It can be: "Auto"
            = Program will determine the notional size based on the average thickness of an
            area element. "User" = The notional size is based on the user-defined value.
            "None" = Notional size will not be considered. In other words, the time-
            dependent effect of this section will not be considered.
        Value (output): For stype is "Auto", the Value represents for the scale factor to
            the program - determined notional size; for stype is User, the Value represents
            for the user-defined notional size [L]; for stype is None, the Value will not be
            used and can be set to 1.
        """
        _r = self._raw.GetNotionalSize(Name, "", 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropArea.GetNotionalSize falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetNotionalSize(self, Name: str, stype: str, Value: float):
        """This function assigns the method to determine the notional size of an area section for the
        creep and shrinkage calculations. This function is currently worked for shell type
        area section. The function returns zero if the parameters are successfully assigned;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing shell-type area section property.
        stype (input): The type to define the notional size of a section. It can be: "Auto"
            = Program will determine the notional size based on the average thickness of an
            area element. "User" = The notional size is based on the user-defined value.
            "None" = Notional size will not be considered. In other words, the time-
            dependent effect of this section will not be considered.
        Value (input): For stype is "Auto", the Value represents for the scale factor to the
            program - determined notional size; for stype is User, the Value represents for
            the user-defined notional size [L]; for stype is None, the Value will not be
            used and can be set to 1.
        """
        _r = self._raw.SetNotionalSize(Name, stype, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropArea.SetNotionalSize falhou (ret={_r})".format(_r=_r))
        return None


