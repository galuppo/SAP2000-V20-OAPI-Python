"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PropMaterial:
    """Wrapper para SapModel.PropMaterial."""

    def __init__(self, raw):
        self._raw = raw

    def AddMaterial(self, MatType: int, Region: str, Standard: str, Grade: str, UserName: str = ''):
        """This function adds a new material property to the model based on the Code-specified and
        other pre-defined material properties defined in the installed file
        "CSiMaterialLibrary*.xml" located in subfolder "Property Libraries" under the
        CSiBridge installation folder. The function returns zero if the material property is
        successfully added, otherwise it returns a nonzero value.
    
        Name (output): This item is returned by the program. It is the name that the program
            ultimately assigns for the material property. If no UserName is specified, the
            program assigns a default name to the material property. If a UserName is
            specified and that name is not used for another material property, the UserName
            is assigned to the material property.
        MatType (input): This is one of the following items in the eMatType enumeration.
            MATERIAL_STEEL = 1 MATERIAL_CONCRETE = 2 MATERIAL_NODESIGN = 3 MATERIAL_ALUMINUM
            = 4 MATERIAL_COLDFORMED = 5 MATERIAL_REBAR = 6 MATERIAL_TENDON = 7
        Region (input): The region name of the material property that is user-predefined in
            the file "CSiMaterialLibrary*.xml" located in subfolder "Property Libraries"
            under the CSiBridge installation.
        Standard (input): The Standard name of the material property with the specified
            MatType within the specified region.
        Grade (input): The Grade name of the material property with the specified MatType
            within the specified region and Standard.
        UserName (input): This is an optional user specified name for the material property.
            If a UserName is specified and that name is already used for another material
            property, the program ignores the UserName.
        """
        _r = self._raw.AddMaterial("", MatType, Region, Standard, Grade, UserName)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.AddMaterial falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing material property. The function returns zero
        if the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined material property.
        NewName (input): The new name for the material property.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self, MatType: int = None):
        """This function returns the total number of defined material properties in the model. If
        desired, counts can be returned for all material properties of a specified type in
        the model.
    
        MatType (input): This optional value is one of the following items in the eMatType
            enumeration. MATERIAL_STEEL = 1 MATERIAL_CONCRETE = 2 MATERIAL_NODESIGN = 3
            MATERIAL_ALUMINUM = 4 MATERIAL_COLDFORMED = 5 MATERIAL_REBAR = 6 MATERIAL_TENDON
            = 7 If no value is input for MatType, a count is returned for all material
            properties in the model regardless of type.
        """
        _r = self._raw.Count(MatType)
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified material property. The function returns zero if the
        material property is successfully deleted; otherwise it returns a nonzero value. It
        returns an error if the specified material property can not be deleted, for example,
        if it is being used in a section property.
    
        Name (input): The name of an existing material property.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetDamping(self, Name: str, Temp: float = 0):
        """This function retrieves the additional material damping data for the material. The function
        returns zero if the data is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing material property.
        ModalRatio (output): The modal damping ratio.
        ViscousMassCoeff (output): The mass coefficient for viscous proportional damping.
        ViscousStiffCoeff (output): The stiffness coefficient for viscous proportional
            damping.
        HystereticMassCoeff (output): The mass coefficient for hysteretic proportional
            damping.
        HystereticStiffCoeff (output): The stiffness coefficient for hysteretic proportional
            damping.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            previously defined for the material.
        """
        _r = self._raw.GetDamping(Name, 0.0, 0.0, 0.0, 0.0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetDamping falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMPAnisotropic(self, Name: str, Temp: float = 0):
        """This function retrieves the mechanical properties for a material with an anisotropic
        directional symmetry type. The function returns zero if the data is successfully
        retrieved; otherwise it returns a nonzero value. The function returns an error if
        the symmetry type of the specified material is not anisotropic.
    
        Name (input): The name of an existing material property.
        e (output): This is an array that includes the modulus of elasticity. e(0) = E1 [F/L
            2 ] e(1) = E2 [F/L 2 ] e(2) = E3 [F/L 2 ]
        u (output): This is an array that includes poissons ratio. u(0) = U12 u(1) = U13
            u(2) = U23 u(3) = U14 u(4) = U24 u(5) = U34 u(6) = U15 u(7) = U25 u(8) = U35
            u(9) = U45 u(10) = U16 u(11) = U26 u(12) = U36 u(13) = U46 u(14) = U56
        a (output): This is an array that includes the thermal coefficient. a(0) = A1 [1/T]
            a(1) = A2 [1/T] a(2) = A3 [1/T] a(3) = A12 [1/T] a(4) = A13 [1/T] a(5) = A23
            [1/T]
        g (output): This is an array that includes the shear modulus. g(0) = G12 [F/L 2 ]
            g(1) = G13 [F/L 2 ] g(2) = G23 [F/L 2 ]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            previously defined for the material.
        """
        _r = self._raw.GetMPAnisotropic(Name, 0.0, 0.0, 0.0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetMPAnisotropic falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMPIsotropic(self, Name: str, Temp: float = 0):
        """This function retrieves the mechanical properties for a material with an isotropic
        directional symmetry type. The function returns zero if the data is successfully
        retrieved; otherwise it returns a nonzero value. The function returns an error if
        the symmetry type of the specified material is not isotropic.
    
        Name (input): The name of an existing material property.
        e (output): The modulus of elasticity. [F/L 2 ]
        u (output): Poissons ratio.
        a (output): The thermal coefficient. [1/T]
        g (output): The shear modulus. For isotropic materials this value is program
            calculated from the modulus of elasticity and poissons ratio. [F/L 2 ]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetMPIsotropic(Name, 0.0, 0.0, 0.0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetMPIsotropic falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMPOrthotropic(self, Name: str, Temp: float = 0):
        """This function retrieves the mechanical properties for a material with an orthotropic
        directional symmetry type. The function returns zero if the data is successfully
        retrieved; otherwise it returns a nonzero value. The function returns an error if
        the symmetry type of the specified material is not orthotropic.
    
        Name (input): The name of an existing material property.
        e (output): This is an array that includes the modulus of elasticity. e(0) = E1 [F/L
            2 ] e(1) = E2 [F/L 2 ] e(2) = E3 [F/L 2 ]
        u (output): This is an array that includes poissons ratio. u(0) = U12 u(1) = U13
            u(2) = U23
        a (output): This is an array that includes the thermal coefficient. a(0) = A1 [1/T]
            a(1) = A2 [1/T] a(2) = A3 [1/T]
        g (output): This is an array that includes the shear modulus. g(0) = G12 [F/L 2 ]
            g(1) = G13 [F/L 2 ] g(2) = G23 [F/L 2 ]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetMPOrthotropic(Name, 0.0, 0.0, 0.0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetMPOrthotropic falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMPUniaxial(self, Name: str, Temp: float = 0):
        """This function retrieves the mechanical properties for a material with a uniaxial directional
        symmetry type. The function returns zero if the data is successfully retrieved;
        otherwise it returns a nonzero value. The function returns an error if the symmetry
        type of the specified material is not uniaxial.
    
        Name (input): The name of an existing material property.
        e (output): The modulus of elasticity. [F/L 2 ]
        a (output): The thermal coefficient. [1/T]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            previously defined for the material.
        """
        _r = self._raw.GetMPUniaxial(Name, 0.0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetMPUniaxial falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMassSource(self):
        """This function retrieves the mass source for the model. The function returns zero if the mass
        source is successfully retrieved; otherwise it returns a nonzero value.
    
        MyOption (output): This is 1, 2 or 3, indicating the mass source option. 1 = From
            element self mass and additional masses 2 = From loads 3 = From element self
            mass and additional masses and loads
        NumberLoads (output): The number of load patterns from which mass is obtained. This
            item applies only when MyOption is 2 or 3.
        LoadPat (output): This is an array of the names of the load patterns from which mass
            is obtained. This item applies only when MyOption is 2 or 3.
        sf (output): This is an array of load patterns multipliers used to calculate the
            mass. This item applies only when MyOption is 2 or 3.
        """
        _r = self._raw.GetMassSource(0, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetMassSource falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMaterial(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves some basic material property data. The function returns zero if the
        material is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing material property.
        MatType (output): This is one of the following items in the eMatType enumeration.
            MATERIAL_STEEL = 1 MATERIAL_CONCRETE = 2 MATERIAL_NODESIGN = 3 MATERIAL_ALUMINUM
            = 4 MATERIAL_COLDFORMED = 5 MATERIAL_REBAR = 6 MATERIAL_TENDON = 7
        Color (input): The display color assigned to the material.
        Notes (input): The notes, if any, assigned to the material.
        GUID (input): The GUID (global unique identifier), if any, assigned to the material.
        """
        _r = self._raw.GetMaterial(Name, None, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetMaterial falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self, MatType: int = None):
        """This function retrieves the names of all defined material properties of the specified type.
        The function returns zero if the names are successfully retrieved; otherwise it
        returns nonzero.
    
        NumberNames (output): The number of material property names retrieved by the
            program.
        MyName (output): This is a one-dimensional array of material property names. The
            MyName array is created as a dynamic, zero-based, array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames - 1) inside the
            SAP2000 program, filled with the names, and returned to the API user.
        MatType (input): This optional value is one of the following items in the eMatType
            enumeration. MATERIAL_STEEL = 1 MATERIAL_CONCRETE = 2 MATERIAL_NODESIGN = 3
            MATERIAL_ALUMINUM = 4 MATERIAL_COLDFORMED = 5 MATERIAL_REBAR = 6 MATERIAL_TENDON
            = 7 If no value is input for MatType, names are returned for all material
            properties in the model regardless of type.
        """
        _r = self._raw.GetNameList(0, [], MatType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOAluminum(self, Name: str, MyType: int, Temp: float = 0):
        """This function retrieves the other material property data for aluminum materials. The
        function returns zero if the data is successfully retrieved; otherwise it returns a
        nonzero value. The function returns an error if the specified material is not
        aluminum.
    
        Name (input): The name of an existing aluminum material property.
        MyType (input): This is 1, 2 or 3, indicating the type of aluminum. 1 = Wrought 2 =
            Cast-Mold 3 = Cast-Sand
        Alloy (output): The Alloy designation for the aluminum, for example, 2014-T6 for
            wrought or 356.0-T7 for cast (mold or sand) aluminum.
        Fcy (output): The compressive yield strength of aluminum. [F/L 2 ]
        Fty (output): The tensile yield strength of aluminum. [F/L 2 ]
        Ftu (output): The tensile ultimate strength of aluminum. [F/L 2 ]
        Fsu (output): The shear ultimate strength of aluminum. [F/L 2 ]
        SSHysType (output): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetOAluminum(Name, MyType, "", 0.0, 0.0, 0.0, 0.0, 0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetOAluminum falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOColdFormed(self, Name: str, Temp: float = 0):
        """This function retrieves the other material property data for cold formed materials. The
        function returns zero if the data is successfully retrieved; otherwise it returns a
        nonzero value. The function returns an error if the specified material is not cold
        formed.
    
        Name (input): The name of an existing cold formed material property.
        Fy (output): The minimum yield stress. [F/L 2 ]
        Fu (output): The minimum tensile stress. [F/L 2 ]
        SSHysType (output): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetOColdFormed(Name, 0.0, 0.0, 0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetOColdFormed falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOConcrete_2(self, Name: str, IsLightweight: bool, Temp: float = 0):
        """This function retrieves the other material property data for concrete materials. The
        function returns zero if the data is successfully retrieved; otherwise it returns a
        nonzero value. The function returns an error if the specified material is not
        concrete.
    
        Name (input): The name of an existing concrete material property.
        fc (output): The concrete compressive strength. [F/L 2 ]
        efc (output): The expected concrete compressive strength. [F/L 2 ]
        IsLightweight (input): If this item is True, the concrete is assumed to be
            lightweight concrete.
        fcsfactor (output): The shear strength reduction factor for lightweight concrete.
        SSType (output): This is 0, 1 or 2, indicating the stress-strain curve type. 0 =
            User defined 1 = Parametric - Simple 2 = Parametric - Mander
        SSHysType (output): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        StrainAtfc (output): This item applies only to parametric stress-strain curves. It
            is the strain at the unconfined compressive strength.
        StrainUltimate (output): This item applies only to parametric stress-strain curves.
            It is the ultimate unconfined strain capacity.
        FinalSlope (output): This item applies only to parametric stress-strain curves. It
            is a multiplier on the material modulus of elasticity, E. This value multiplied
            times E gives the final slope on the compression side of the curve.
        FrictionAngle (output): The Drucker-Prager friction angle, 0 <= FrictionAngle < 90.
            [deg]
        DilatationalAngle (output): The Drucker-Prager dilatational angle, 0 <=
            DilatationalAngle < 90. [deg]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetOConcrete_2(Name, 0.0, 0.0, IsLightweight, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetOConcrete_2 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetONoDesign(self, Name: str, Temp: float = 0):
        """This function retrieves the other material property data for no design type materials. The
        function returns zero if the data is successfully retrieved; otherwise it returns a
        nonzero value. The function returns an error if the specified material is not
        concrete.
    
        Name (input): The name of an existing concrete material property.
        FrictionAngle (output): The Drucker-Prager friction angle, 0 <= FrictionAngle < 90.
            [deg]
        DilatationalAngle (output): The Drucker-Prager dilatational angle, 0 <=
            DilatationalAngle < 90. [deg]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetONoDesign(Name, 0.0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetONoDesign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetORebar_1(self, Name: str, UseCaltransSSDefaults: bool, Temp: float = 0):
        """This function retrieves the other material property data for rebar materials. The function
        returns zero if the data is successfully retrieved; otherwise it returns a nonzero
        value. The function returns an error if the specified material is not rebar.
    
        Name (input): The name of an existing rebar material property.
        Fy (output): The minimum yield stress. [F/L 2 ]
        Fu (output): The minimum tensile stress. [F/L 2 ]
        eFy (output): The expected yield stress. [F/L 2 ]
        eFu (output): The expected tensile stress. [F/L 2 ]
        SSType (output): This is 0, 1 or 2, indicating the stress-strain curve type. 0 =
            User defined 1 = Parametric - Simple 2 = Parametric - Park
        SSHysType (output): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        StrainAtHardening (output): This item applies only when parametric stress-strain
            curves are used and when UseCaltransSSDefaults is False. It is the strain at the
            onset of strain hardening.
        StrainUltimate (output): This item applies only when parametric stress-strain curves
            are used and when UseCaltransSSDefaults is False. It is the ultimate strain
            capacity. This item must be larger than the StrainAtHardening item.
        FinalSlope (output): This item applies only to parametric stress-strain curves. It
            is a multiplier on the material modulus of elasticity, E. This value multiplied
            times E gives the final slope of the curve.
        UseCaltransSSDefaults (input): If this item is True, the program uses Caltrans
            default controlling strain values, which are bar size dependent.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetORebar_1(Name, 0.0, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, UseCaltransSSDefaults, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetORebar_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOSteel_1(self, Name: str, Temp: float = 0):
        """This function retrieves the other material property data for steel materials. The function
        returns zero if the data is successfully retrieved; otherwise it returns a nonzero
        value. The function returns an error if the specified material is not steel.
    
        Name (input): The name of an existing steel material property.
        Fy (output): The minimum yield stress. [F/L 2 ]
        Fu (output): The minimum tensile stress. [F/L 2 ]
        eFy (output): The expected yield stress. [F/L 2 ]
        eFu (output): The expected tensile stress. [F/L 2 ]
        SSType (output): This is 0 or 1. indicating the stress-strain curve type. 0 = User
            defined 1 = Parametric - Simple
        SSHysType (output): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        StrainAtHardening (output): This item applies only to parametric stress-strain
            curves. It is the strain at the onset of strain hardening.
        StrainAtMaxStress (output): This item applies only to parametric stress-strain
            curves. It is the strain at maximum stress.
        StrainAtRupture (output): This item applies only to parametric stress-strain curves.
            It is the strain at rupture.
        FinalSlope (output): This item applies only to parametric stress-strain curves. It
            is a multiplier on the material modulus of elasticity, E. This value multiplied
            times E gives the final slope of the curve.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetOSteel_1(Name, 0.0, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetOSteel_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOTendon_1(self, Name: str, Temp: float = 0):
        """This function retrieves the other material property data for tendon materials. The function
        returns zero if the data is successfully retrieved; otherwise it returns a nonzero
        value. The function returns an error if the specified material is not tendon.
    
        Name (input): The name of an existing tendon material property.
        Fy (output): The minimum yield stress. [F/L 2 ]
        Fu (output): The minimum tensile stress. [F/L 2 ]
        SSType (output): This is 0, 1 or 2, indicating the stress-strain curve type. 0 =
            User defined 1 = Parametric 250 ksi strand 2 = Parametric 270 ksi strand
        SSHysType (output): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        FinalSlope (output): This item applies only to parametric stress-strain curves. It
            is a multiplier on the material modulus of elasticity, E. This value multiplied
            times E gives the final slope of the curve.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetOTendon_1(Name, 0.0, 0.0, 0, 0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetOTendon_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSSCurve(self, Name: str, SectName: str = '', RebarArea: float = 0, Temp: float = 0):
        """This function retrieves the material stress-strain curve. The function returns zero if the
        data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing material property.
        NumberPoints (output): The number of points in the stress-strain curve.
        PointID (output): This is one of the following integers which sets the point ID. The
            point ID controls the color that will be displayed for hinges in a deformed
            shape plot. -5 = -E -4 = -D -3 = -C -2 = -B 0 = None 1 = A 2 = B 3 = C 4 = D 5 =
            E
        Strain (output): This is an array that includes the strain at each point on the
            stress strain curve.
        Stress (output): This is an array that includes the stress at each point on the
            stress strain curve. [F/L 2 ]
        SectName (input): This item applies only if the specified material is concrete with
            a Mander concrete type. This is the frame section property for which the Mander
            stress-strain curve is retrieved. The section must be round or rectangular.
        RebarArea (input): This item applies only if the specified material is rebar, which
            does not have a user-defined stress-strain curve and is specified to use
            Caltrans default controlling strain values, which are bar size dependent. This
            is the area of the rebar for which the stress-strain curve is retrieved.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetSSCurve(Name, 0, [], [], [], SectName, RebarArea, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetSSCurve falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTemp(self, Name: str):
        """This function retrieves the temperatures at which properties are specified for a material.
        The function returns zero if the temperatures are successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of a material property.
        NumberItems (output): The number of different temperatures at which properties are
            specified for the material.
        Temp (output): This is an array that includes the different temperatures at which
            properties are specified for the material.
        """
        _r = self._raw.GetTemp(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetTemp falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTypeOAPI(self, Name: str):
        """This function retrieves the material type for the specified material. The function returns
        zero if the type is successfully retrieved; otherwise it returns nonzero.
    
        Name (input): The name of an existing material property.
        MatType (output): This is one of the following items in the eMatType enumeration.
            MATERIAL_STEEL = 1 MATERIAL_CONCRETE = 2 MATERIAL_NODESIGN = 3 MATERIAL_ALUMINUM
            = 4 MATERIAL_COLDFORMED = 5 MATERIAL_REBAR = 6 MATERIAL_TENDON = 7
        SymType (output): This is 0, 1, 2 or 3, indicating the material directional symmetry
            type. 0 = Isotropic 1 = Orthotropic 2 = Anisotropic 3 = Uniaxial
        """
        _r = self._raw.GetTypeOAPI(Name, None, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetTypeOAPI falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetWeightAndMass(self, Name: str, Temp: float = 0):
        """This function retrieves the weight per unit volume and mass per unit volume of the material.
        The function returns zero if the data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing material property.
        w (output): The weight per unit volume for the material. [F/L 3 ]
        m (output): The mass per unit volume for the material. [M/L 3 ]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            defined previously for the material.
        """
        _r = self._raw.GetWeightAndMass(Name, 0.0, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetWeightAndMass falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetDamping(self, Name: str, ModalRatio: float, ViscousMassCoeff: float, ViscousStiffCoeff: float, HystereticMassCoeff: float, HystereticStiffCoeff: float, Temp: float = 0):
        """This function sets the additional material damping data for the material. The function
        returns zero if the data is successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing material property.
        ModalRatio (input): The modal damping ratio.
        ViscousMassCoeff (input): The mass coefficient for viscous proportional damping.
        ViscousStiffCoeff (input): The stiffness coefficient for viscous proportional
            damping.
        HystereticMassCoeff (input): The mass coefficient for hysteretic proportional
            damping.
        HystereticStiffCoeff (input): The stiffness coefficient for hysteretic proportional
            damping.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been previously
            defined for the material.
        """
        _r = self._raw.SetDamping(Name, ModalRatio, ViscousMassCoeff, ViscousStiffCoeff, HystereticMassCoeff, HystereticStiffCoeff, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetDamping falhou (ret={_r})".format(_r=_r))
        return None

    def SetMPAnisotropic(self, Name: str, e: list[float], u: list[float], a: list[float], g: list[float], Temp: float = 0):
        """This function sets the material directional symmetry type to anisotropic, and assigns the
        anisotropic mechanical properties. The function returns zero if the data is
        successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing material property.
        e (input): This is an array that includes the modulus of elasticity. e(0) = E1 [F/L
            2 ] e(1) = E2 [F/L 2 ] e(2) = E3 [F/L 2 ]
        u (input): This is an array that includes poissons ratio. u(0) = U12 u(1) = U13 u(2)
            = U23 u(3) = U14 u(4) = U24 u(5) = U34 u(6) = U15 u(7) = U25 u(8) = U35 u(9) =
            U45 u(10) = U16 u(11) = U26 u(12) = U36 u(13) = U46 u(14) = U56
        a (input): This is an array that includes the thermal coefficient. a(0) = A1 [1/T]
            a(1) = A2 [1/T] a(2) = A3 [1/T] a(3) = A12 [1/T] a(4) = A13 [1/T] a(5) = A23
            [1/T]
        g (input): This is an array that includes the shear modulus. g(0) = G12 [F/L 2 ]
            g(1) = G13 [F/L 2 ] g(2) = G23 [F/L 2 ]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetMPAnisotropic(Name, e, u, a, g, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetMPAnisotropic falhou (ret={_r})".format(_r=_r))
        return None

    def SetMPIsotropic(self, Name: str, e: float, u: float, a: float, Temp: float = 0):
        """This function sets the material directional symmetry type to isotropic, and assigns the
        isotropic mechanical properties. The function returns zero if the data is
        successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing material property.
        e (input): The modulus of elasticity. [F/L 2 ]
        u (input): Poissons ratio.
        a (input): The thermal coefficient. [1/T]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetMPIsotropic(Name, e, u, a, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetMPIsotropic falhou (ret={_r})".format(_r=_r))
        return None

    def SetMPOrthotropic(self, Name: str, e: list[float], u: list[float], a: list[float], g: list[float], Temp: float = 0):
        """This function sets the material directional symmetry type to orthotropic, and assigns the
        orthotropic mechanical properties. The function returns zero if the data is
        successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing material property.
        e (input): This is an array that includes the modulus of elasticity. e(0) = E1 [F/L
            2 ] e(1) = E2 [F/L 2 ] e(2) = E3 [F/L 2 ]
        u (input): This is an array that includes poissons ratio. u(0) = U12 u(1) = U13 u(2)
            = U23
        a (input): This is an array that includes the thermal coefficient. a(0) = A1 [1/T]
            a(1) = A2 [1/T] a(2) = A3 [1/T]
        g (input): This is an array that includes the shear modulus. g(0) = G12 [F/L 2 ]
            g(1) = G13 [F/L 2 ] g(2) = G23 [F/L 2 ]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetMPOrthotropic(Name, e, u, a, g, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetMPOrthotropic falhou (ret={_r})".format(_r=_r))
        return None

    def SetMPUniaxial(self, Name: str, e: float, a: float, Temp: float = 0):
        """This function sets the material directional symmetry type to uniaxial, and assigns the
        uniaxial mechanical properties. The function returns zero if the data is
        successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing material property.
        e (input): The modulus of elasticity. [F/L 2 ]
        a (input): The thermal coefficient. [1/T]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetMPUniaxial(Name, e, a, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetMPUniaxial falhou (ret={_r})".format(_r=_r))
        return None

    def SetMassSource(self, MyOption: int, NumberLoads: int, LoadPat: list[str], sf: list[float]):
        """This function sets the mass source for the model. The function returns zero if the mass
        source is successfully set; otherwise it returns a nonzero value. If either the
        MassFromElements or MassFromMasses parameter is specified as True, both values will
        be set to true in the model. Both of these items are currently controlled with a
        single option within the user interface.
    
        MyOption (input): This is 1, 2 or 3, indicating the mass source option. 1 = From
            element self mass and additional masses 2 = From loads 3 = From element self
            mass and additional masses and loads
        NumberLoads (input): The number of load patterns from which mass is obtained. This
            item applies only when MyOption is 2 or 3.
        LoadPat (input): This is an array of the names of the load patterns from which mass
            is obtained. This item applies only when MyOption is 2 or 3.
        sf (input): This is an array of load patterns multipliers used to calculate the
            mass. This item applies only when MyOption is 2 or 3.
        """
        _r = self._raw.SetMassSource(MyOption, NumberLoads, LoadPat, sf)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetMassSource falhou (ret={_r})".format(_r=_r))
        return None

    def SetMaterial(self, Name: str, MatType: int, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a material property. If this function is called for an existing
        material property, all items for the material are reset to their default value. The
        function returns zero if the material is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new material property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatType (input): This is one of the following items in the eMatType enumeration.
            MATERIAL_STEEL = 1 MATERIAL_CONCRETE = 2 MATERIAL_NODESIGN = 3 MATERIAL_ALUMINUM
            = 4 MATERIAL_COLDFORMED = 5 MATERIAL_REBAR = 6 MATERIAL_TENDON = 7
        Color (input): The display color assigned to the material. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the material.
        GUID (input): The GUID (global unique identifier), if any, assigned to the material.
            If this item is input as Default, the program assigns a GUID to the material.
        """
        _r = self._raw.SetMaterial(Name, MatType, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetMaterial falhou (ret={_r})".format(_r=_r))
        return None

    def SetOAluminum(self, Name: str, MyType: int, Alloy: str, Fcy: float, Fty: float, Ftu: float, Fsu: float, SSHysType: int, Temp: float = 0):
        """This function sets the other material property data for aluminum materials. The function
        returns zero if the data is successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing aluminum material property.
        MyType (input): This is 1, 2 or 3, indicating the type of aluminum. 1 = Wrought 2 =
            Cast-Mold 3 = Cast-Sand
        Alloy (input): The Alloy designation for the aluminum, for example, 2014-T6 for
            wrought or 356.0-T7 for cast (mold or sand) aluminum.
        Fcy (input): The compressive yield strength of aluminum. [F/L 2 ]
        Fty (input): The tensile yield strength of aluminum. [F/L 2 ]
        Ftu (input): The tensile ultimate strength of aluminum. [F/L 2 ]
        Fsu (input): The shear ultimate strength of aluminum. [F/L 2 ]
        SSHysType (input): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetOAluminum(Name, MyType, Alloy, Fcy, Fty, Ftu, Fsu, SSHysType, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetOAluminum falhou (ret={_r})".format(_r=_r))
        return None

    def SetOColdFormed(self, Name: str, Fy: float, Fu: float, SSHysType: int, Temp: float = 0):
        """This function sets the other material property data for cold formed materials. The function
        returns zero if the data is successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing cold formed material property.
        Fy (input): The minimum yield stress. [F/L 2 ]
        Fu (input): The minimum tensile stress. [F/L 2 ]
        SSHysType (input): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetOColdFormed(Name, Fy, Fu, SSHysType, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetOColdFormed falhou (ret={_r})".format(_r=_r))
        return None

    def SetOConcrete_2(self, Name: str, fc: float, efc: float, IsLightweight: bool, fcsfactor: float, sstype: int, SSHysType: int, StrainAtfc: float, StrainUltimate: float, FinalSlope: float, FrictionAngle: float = 0, DilatationalAngle: float = 0, Temp: float = 0):
        """This function sets the other material property data for concrete materials. The function
        returns zero if the data is successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing concrete material property.
        fc (input): The concrete compressive strength. [F/L 2 ]
        efc (input): The expected concrete compressive strength. [F/L 2 ]
        IsLightweight (input): If this item is True, the concrete is assumed to be
            lightweight concrete.
        fcsfactor (input): The shear strength reduction factor for lightweight concrete.
        SSHysType (input): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        StrainAtfc (input): This item applies only to parametric stress-strain curves. It is
            the strain at the unconfined compressive strength.
        StrainUltimate (input): This item applies only to parametric stress-strain curves.
            It is the ultimate unconfined strain capacity. This item must be larger than the
            StrainAtfc item.
        FinalSlope (input): This item applies only to parametric stress-strain curves. It is
            a multiplier on the material modulus of elasticity, E. This value multiplied
            times E gives the final slope on the compression side of the curve.
        FrictionAngle (input): The Drucker-Prager friction angle, 0 <= FrictionAngle < 90.
            [deg]
        DilatationalAngle (input): The Drucker-Prager dilatational angle, 0 <=
            DilatationalAngle < 90. [deg]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetOConcrete_2(Name, fc, efc, IsLightweight, fcsfactor, sstype, SSHysType, StrainAtfc, StrainUltimate, FinalSlope, FrictionAngle, DilatationalAngle, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetOConcrete_2 falhou (ret={_r})".format(_r=_r))
        return None

    def SetONoDesign(self, Name: str, FrictionAngle: float = 0, DilatationalAngle: float = 0, Temp: float = 0):
        """This function sets the other material property data for no design type materials. The
        function returns zero if the data is successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing concrete material property.
        FrictionAngle (input): The Drucker-Prager friction angle, 0 <= FrictionAngle < 90.
            [deg]
        DilatationalAngle (input): The Drucker-Prager dilatational angle, 0 <=
            DilatationalAngle < 90. [deg]
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetONoDesign(Name, FrictionAngle, DilatationalAngle, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetONoDesign falhou (ret={_r})".format(_r=_r))
        return None

    def SetORebar_1(self, Name: str, Fy: float, Fu: float, eFy: float, eFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainUltimate: float, FinalSlope: float, UseCaltransSSDefaults: bool, Temp: float = 0):
        """This function sets the other material property data for rebar materials. The function
        returns zero if the data is successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing rebar material property.
        Fy (input): The minimum yield stress. [F/L 2 ]
        Fu (input): The minimum tensile stress. [F/L 2 ]
        eFy (input): The expected yield stress. [F/L 2 ]
        eFu (input): The expected tensile stress. [F/L 2 ]
        SSType (input): This is 0, 1 or 2, indicating the stress-strain curve type. 0 = User
            defined 1 = Parametric - Simple 2 = Parametric - Park
        SSHysType (input): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        StrainAtHardening (input): This item applies only when parametric stress-strain
            curves are used and when UseCaltransSSDefaults is False. It is the strain at the
            onset of strain hardening.
        StrainUltimate (input): This item applies only when parametric stress-strain curves
            are used and when UseCaltransSSDefaults is False. It is the ultimate strain
            capacity. This item must be larger than the StrainAtHardening item.
        FinalSlope (input): This item applies only to parametric stress-strain curves. It is
            a multiplier on the material modulus of elasticity, E. This value multiplied
            times E gives the final slope of the curve.
        UseCaltransSSDefaults (input): If this item is True, the program uses Caltrans
            default controlling strain values, which are bar size dependent.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetORebar_1(Name, Fy, Fu, eFy, eFu, SSType, SSHysType, StrainAtHardening, StrainUltimate, FinalSlope, UseCaltransSSDefaults, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetORebar_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetOSteel_1(self, Name: str, Fy: float, Fu: float, eFy: float, eFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainAtMaxStress: float, StrainAtRupture: float, FinalSlope: float, Temp: float = 0):
        """This function sets the other material property data for steel materials. The function
        returns zero if the data is successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing steel material property.
        Fy (input): The minimum yield stress. [F/L 2 ]
        Fu (input): The minimum tensile stress. [F/L 2 ]
        eFy (input): The expected yield stress. [F/L 2 ]
        eFu (input): The expected tensile stress. [F/L 2 ]
        SSType (input): This is 0 or 1, indicating the stress-strain curve type. 0 = User
            defined 1 = Parametric - Simple
        SSHysType (input): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        StrainAtHardening (input): This item applies only to parametric stress-strain
            curves. It is the strain at the onset of strain hardening.
        StrainAtMaxStress (input): This item applies only to parametric stress-strain
            curves. It is the strain at maximum stress. This item must be larger than the
            StrainAtHardening item.
        StrainAtRupture (input): This item applies only to parametric stress-strain curves.
            It is the strain at rupture. This item must be larger than the StrainAtMaxStress
            item.
        FinalSlope (input): This item applies only to parametric stress-strain curves. It is
            a multiplier on the material modulus of elasticity, E. This value multiplied
            times E gives the final slope of the curve.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetOSteel_1(Name, Fy, Fu, eFy, eFu, SSType, SSHysType, StrainAtHardening, StrainAtMaxStress, StrainAtRupture, FinalSlope, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetOSteel_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetOTendon_1(self, Name: str, Fy: float, Fu: float, SSType: int, SSHysType: int, FinalSlope: float, Temp: float = 0):
        """This function sets the other material property data for tendon materials. The function
        returns zero if the data is successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing tendon material property.
        Fy (input): The minimum yield stress. [F/L 2 ]
        Fu (input): The minimum tensile stress. [F/L 2 ]
        SSType (input): This is 0, 1 or 2, indicating the stress-strain curve type. 0 = User
            defined 1 = Parametric 250 ksi strand 2 = Parametric 270 ksi strand
        SSHysType (input): This is 0, 1 or 2, indicating the stress-strain hysteresis type.
            0 = Elastic 1 = Kinematic 2 = Takeda
        FinalSlope (input): This item applies only to parametric stress-strain curves. It is
            a multiplier on the material modulus of elasticity, E. This value multiplied
            times E gives the final slope of the curve.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetOTendon_1(Name, Fy, Fu, SSType, SSHysType, FinalSlope, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetOTendon_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetSSCurve(self, Name: str, NumberPoints: int, PointID: list[int], Strain: list[float], Stress: list[float], Temp: float = 0):
        """This function sets the material stress-strain curve for materials that are specified to have
        user-defined stress-strain curves. The function returns zero if the data is
        successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing material property.
        NumberPoints (input): The number of points in the stress-strain curve. This item
            must be at least 3.
        PointID (input): This is one of the following integers which sets the point ID. The
            point ID controls the color that will be displayed for hinges in a deformed
            shape plot. -5 = -E -4 = -D -3 = -C -2 = -B 0 = None 1 = A 2 = B 3 = C 4 = D 5 =
            E The point IDs must be input in numerically increasing order, except that 0
            (None) values are allowed anywhere. No duplicate values are allowed excepth for
            0 (None).
        Strain (input): This is an array that includes the strain at each point on the
            stress strain curve. The strains must increase monotonically.
        Stress (input): This is an array that includes the stress at each point on the
            stress strain curve. [F/L 2 ] Points that have a negative strain must have a
            zero or negative stress. Similarly, points that have a positive strain must have
            a zero or positive stress. There must be one point defined that has zero strain
            and zero stress.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been defined
            previously for the material.
        """
        _r = self._raw.SetSSCurve(Name, NumberPoints, PointID, Strain, Stress, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetSSCurve falhou (ret={_r})".format(_r=_r))
        return None

    def SetTemp(self, Name: str, NumberItems: int, Temp: list[float]):
        """This function assigns the temperatures at which properties are specified for a material.
        This data is required only for materials whose properties are temperature dependent.
        The function returns zero if the temperatures are successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing material property.
        NumberItems (input): The number of different temperatures at which properties are
            specified for the material.
        Temp (input): This is an array that includes the different temperatures at which
            properties are specified for the material.
        """
        _r = self._raw.SetTemp(Name, NumberItems, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetTemp falhou (ret={_r})".format(_r=_r))
        return None

    def SetWeightAndMass(self, Name: str, MyOption: int, Value: float, Temp: float = 0):
        """This function assigns weight per unit volume or mass per unit volume to a material property.
        The function returns zero if the data is successfully assigned; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing material property.
        MyOption (input): This is either 1 or 2, indicating what is specified by the Value
            item. 1 = Weight per unit volume is specified 2 = Mass per unit volume is
            specified If the weight is specified, the corresponding mass is program
            calculated based on the specified weight. Similarly, if the mass is specified,
            the corresponding weight is program calculated based on the specified mass.
        Value (input): This is either the weight per unit volume or the mass per unit
            volume, depending on the value of the MyOption item. [F/L 3 ] for MyOption = 1
            (weight), and [M/L 3 ] for MyOption = 2 (mass)
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been define
            previously for the material.
        """
        _r = self._raw.SetWeightAndMass(Name, MyOption, Value, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.SetWeightAndMass falhou (ret={_r})".format(_r=_r))
        return None

    def GetConcreteCEBFIP90(self, Name: str, ConsiderConcreteAge: bool, ConsiderConcreteCreep: bool, ConsiderConcreteShrinkage: bool, Temp: float = 0):
        """This function retrieves the time dependent CEB FIP-90 material property data for concrete
        materials. The function returns zero if the data is successfully retrieved;
        otherwise it returns a nonzero value. The function returns an error if the specified
        material is not concrete.
    
        Name (input): The name of an existing concrete material property.
        ConsiderConcreteAge (input): If this item is True, time dependence is considered for
            concrete compressive strength and stiffness (modulus of elasticity).
        ConsiderConcreteCreep (input): If this item is True, time dependence is considered
            for concrete creep.
        ConsiderConcreteShrinkage (input): If this item is True, time dependence is
            considered for concrete shrinkage.
        CEBFIPsCoefficient (output): This is the cement type coefficient. This item applies
            only when ConsiderConcreteAge = True.
        RelativeHumidity (output): This is relative humidity. This item applies only when
            ConsiderConcreteCreep = True or ConsiderConcreteShrinkage = True.
        NotionalSize (output): This is notional size of the member. This item applies only
            when ConsiderConcreteCreep = True or ConsiderConcreteShrinkage = True. As
            defined in Equation 2.1-69 of CEB_FIP Model Code 1990 the notional size is equal
            to two times the cross-sectional area of the member divided by the perimeter of
            the member in contact with the atmosphere.
        ShrinkageCoefficient (output): This is the shrinkage coefficient as defined in
            Equation 2.1-76 of CEB_FIP Model Code 1990. This item applies only when
            ConsiderConcreteShrinkage = True.
        ShrinkageStartAge (output): This is the shrinkage start age in days as used in
            Section 2.1.6.4.4 of CEB_FIP Model Code 1990. This item applies only when
            ConsiderConcreteShrinkage = True.
        UseSeries (output): This is either 0 or 1, indicating the creep integration type. 0
            = Full integration 1 = Dirichlet series This item applies only when
            ConsiderConcreteCreep = True.
        NumberSeriesTerms (output): This is the number of series terms used when integrating
            based on a Dirichlet series. This item applies only when ConsiderConcreteCreep =
            True and UseSeries = 1.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            previously defined for the material.
        """
        _r = self._raw.GetConcreteCEBFIP90(Name, ConsiderConcreteAge, ConsiderConcreteCreep, ConsiderConcreteShrinkage, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetConcreteCEBFIP90 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTendonCEBFIP90(self, Name: str, ConsiderSteelRelaxation: bool, Temp: float = 0):
        """This function retrieves the time dependent CEB FIP-90 material property data for tendon
        materials. The function returns zero if the data is successfully retrieved;
        otherwise it returns a nonzero value. The function returns an error if the specified
        material is not tendon.
    
        Name (input): The name of an existing tendon material property.
        ConsiderSteelRelaxation (input): If this item is True, time dependence is considered
            for tendon steel relaxation.
        CEBFIPClass (output): This is either 1 or 2, indicating the CEB FIP-90 class. This
            item applies only when ConsiderSteelRelaxation = True.
        UseSeries (output): This is either 0 or 1, indicating the steel relaxation
            integration type. 0 = Full integration 1 = Dirichlet series This item applies
            only when ConsiderSteelRelaxation = True.
        NumberSeriesTerms (output): This is the number of series terms used when integrating
            based on a Dirichlet series. This item applies only when ConsiderSteelRelaxation
            = True and UseSeries = 1.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            previously defined for the material.
        """
        _r = self._raw.GetTendonCEBFIP90(Name, ConsiderSteelRelaxation, 0, 0, 0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.GetTendonCEBFIP90 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    @cached_property
    def TimeDep(self):
        return N_PropMaterial_TimeDep(self._raw.TimeDep)


class N_PropMaterial_TimeDep:
    """Wrapper para SapModel.PropMaterial.TimeDep."""

    def __init__(self, raw):
        self._raw = raw

    def GetConcreteScaleFactors(self, Name: str, ScaleFactorAge: float, ScaleFactorCreep: float, ScaleFactorShrinkage: float, Temp: float = 0):
        """This function retrieves the scale factors for the time-dependent material property data for
        concrete materials. The function returns zero if the data is successfully retrieved;
        otherwise it returns a nonzero value. The function returns an error if the specified
        material is not concrete.
    
        Name (input): The name of an existing concrete material property.
        ScaleFactorAge (input): This value multiplies the stiffness (modulus of elasticity)
            computed with age for the material during a time-dependent analysis. It has no
            effect for load cases that do not consider time-dependent effects, or for
            materials that do not consider time-dependent age effects. The default value is
            unity, and the specified value must be positive.
        ScaleFactorCreep (input): This value multiplies the creep coefficient, and hence the
            creep strain, computed for the material during a time-dependent analysis. It has
            no effect for load cases that do not consider time-dependent effects, or for
            materials that do not consider creep effects. The default value is unity, and
            the specified value must be positive.
        ScaleFactorShrinkage (input): This value multiplies the shrinkage strain computed
            for the material during a time-dependent analysis. It has no effect for load
            cases that do not consider time-dependent effects, or for materials that do not
            consider shrinkage effects. The default value is unity, and the specified value
            must be positive.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            previously defined for the material.
        """
        _r = self._raw.GetConcreteScaleFactors(Name, ScaleFactorAge, ScaleFactorCreep, ScaleFactorShrinkage, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.TimeDep.GetConcreteScaleFactors falhou (ret={_r})".format(_r=_r))
        return None

    def GetTendonScaleFactors(self, Name: str, Temp: float = 0):
        """This function retrieves the scale factors for the time-dependent material property data for
        tendon materials. The function returns zero if the data is successfully retrieved;
        otherwise it returns a nonzero value. The function returns an error if the specified
        material is not tendon.
    
        Name (input): The name of an existing tendon material property.
        ScaleFactorRelaxation (output): This value multiplies the relaxation coefficient,
            and hence the relaxation strain, computed for the material during a time-
            dependent analysis. It has no effect for load cases that do not consider time-
            dependent effects, or for materials that do not consider relaxation effects. The
            default value is unity, and the specified value must be positive.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            previously defined for the material.
        """
        _r = self._raw.GetTendonScaleFactors(Name, 0.0, Temp)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.TimeDep.GetTendonScaleFactors falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetConcreteCEBFIP90(self, Name: str, ConsiderConcreteAge: bool, ConsiderConcreteCreep: bool, ConsiderConcreteShrinkage: bool, CEBFIPsCoefficient: float, RelativeHumidity: float, NotionalSize: float, ShrinkageCoefficient: float, ShrinkageStartAge: float, UseSeries: int, NumberSeriesTerms: int, Temp: float = 0):
        """This function sets the time dependent CEB FIP-90 material property data for concrete
        materials. The function returns zero if the data is successfully assigned; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing concrete material property.
        ConsiderConcreteAge (input): If this item is True, time dependence is considered for
            concrete compressive strength and stiffness (modulus of elasticity).
        ConsiderConcreteCreep (input): If this item is True, time dependence is considered
            for concrete creep.
        ConsiderConcreteShrinkage (input): If this item is True, time dependence is
            considered for concrete shrinkage.
        CEBFIPsCoefficient (input): This is the cement type coefficient. This item applies
            only when ConsiderConcreteAge = True.
        RelativeHumidity (input): This is relative humidity. This item applies only when
            ConsiderConcreteCreep = True or ConsiderConcreteShrinkage = True.
        NotionalSize (input): This is notional size of the member. This item applies only
            when ConsiderConcreteCreep = True or ConsiderConcreteShrinkage = True. As
            defined in Equation 2.1-69 of CEB_FIP Model Code 1990 the notional size is equal
            to two times the cross-sectional area of the member divided by the perimeter of
            the member in contact with the atmosphere.
        ShrinkageCoefficient (input): This is the shrinkage coefficient as defined in
            Equation 2.1-76 of CEB_FIP Model Code 1990. This item applies only when
            ConsiderConcreteShrinkage = True.
        ShrinkageStartAge (input): This is the shrinkage start age in days as used in
            Section 2.1.6.4.4 of CEB_FIP Model Code 1990. This item applies only when
            ConsiderConcreteShrinkage = True.
        UseSeries (input): This is either 0 or 1, indicating the creep integration type. 0 =
            Full integration 1 = Dirichlet series This item applies only when
            ConsiderConcreteCreep = True.
        NumberSeriesTerms (input): This is the number of series terms used when integrating
            based on a Dirichlet series. This item applies only when ConsiderConcreteCreep =
            True and UseSeries = 1.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been previously
            defined for the material.
        """
        _r = self._raw.SetConcreteCEBFIP90(Name, ConsiderConcreteAge, ConsiderConcreteCreep, ConsiderConcreteShrinkage, CEBFIPsCoefficient, RelativeHumidity, NotionalSize, ShrinkageCoefficient, ShrinkageStartAge, UseSeries, NumberSeriesTerms, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.TimeDep.SetConcreteCEBFIP90 falhou (ret={_r})".format(_r=_r))
        return None

    def SetConcreteScaleFactors(self, Name: str, ScaleFactorAge: float, ScaleFactorCreep: float, ScaleFactorShrinkage: float, Temp: float = 0):
        """This function sets scale factors for the time-dependent material property data for concrete
        materials. If this function is not called, default values of unity are assumed for
        all scale factors. The function returns zero if the data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing concrete material property.
        ScaleFactorAge (input): This value multiplies the stiffness (modulus of elasticity)
            computed with age for the material during a time-dependent analysis. It has no
            effect for load cases that do not consider time-dependent effects, or for
            materials that do not consider time-dependent age effects. The default value is
            unity, and the specified value must be positive.
        ScaleFactorCreep (input): This value multiplies the creep coefficient, and hence the
            creep strain, computed for the material during a time-dependent analysis. It has
            no effect for load cases that do not consider time-dependent effects, or for
            materials that do not consider creep effects. The default value is unity, and
            the specified value must be positive.
        ScaleFactorShrinkage (input): This value multiplies the shrinkage strain computed
            for the material during a time-dependent analysis. It has no effect for load
            cases that do not consider time-dependent effects, or for materials that do not
            consider shrinkage effects. The default value is unity, and the specified value
            must be positive.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            previously defined for the material.
        """
        _r = self._raw.SetConcreteScaleFactors(Name, ScaleFactorAge, ScaleFactorCreep, ScaleFactorShrinkage, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.TimeDep.SetConcreteScaleFactors falhou (ret={_r})".format(_r=_r))
        return None

    def SetTendonCEBFIP90(self, Name: str, ConsiderSteelRelaxation: bool, CEBFIPClass: int, UseSeries: int, NumberSeriesTerms: int, Temp: float = 0):
        """This function sets the time dependent CEB FIP-90 material property data for tendon
        materials. The function returns zero if the data is successfully assigned; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing tendon material property.
        ConsiderSteelRelaxation (input): If this item is True, time dependence is considered
            for tendon steel relaxation.
        CEBFIPClass (input): This is either 1 or 2, indicating the CEB FIP-90 class. This
            item applies only when ConsiderSteelRelaxation = True.
        UseSeries (input): This is either 0 or 1, indicating the steel relaxation
            integration type. 0 = Full integration 1 = Dirichlet series This item applies
            only when ConsiderSteelRelaxation = True.
        NumberSeriesTerms (input): This is the number of series terms used when integrating
            based on a Dirichlet series. This item applies only when ConsiderSteelRelaxation
            = True and UseSeries = 1.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data applies. The temperature must have been previously
            defined for the material.
        """
        _r = self._raw.SetTendonCEBFIP90(Name, ConsiderSteelRelaxation, CEBFIPClass, UseSeries, NumberSeriesTerms, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.TimeDep.SetTendonCEBFIP90 falhou (ret={_r})".format(_r=_r))
        return None

    def SetTendonScaleFactors(self, Name: str, ScaleFactorRelaxtion: float, Temp: float = 0):
        """This function sets scale factors for the time-dependent material property data for tendon
        materials. If this function is not called, default values of unity are assumed for
        all scale factors. The function returns zero if the data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing tendon material property.
        Temp (input): This item applies only if the specified material has properties that
            are temperature dependent. That is, it applies only if properties are specified
            for the material at more than one temperature. This item is the temperature at
            which the specified data is to be retrieved. The temperature must have been
            previously defined for the material.
        """
        _r = self._raw.SetTendonScaleFactors(Name, ScaleFactorRelaxtion, Temp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropMaterial.TimeDep.SetTendonScaleFactors falhou (ret={_r})".format(_r=_r))
        return None


