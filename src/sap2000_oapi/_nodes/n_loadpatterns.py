"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_LoadPatterns:
    """Wrapper para SapModel.LoadPatterns."""

    def __init__(self, raw):
        self._raw = raw

    def Add(self, Name: str, MyType: int, SelfWTMultiplier: float = 0, AddLoadCase: bool = True):
        """This function adds a new load pattern. The function returns 0 if the load pattern is
        successfully added; otherwise it returns nonzero. An error is returned if the Name
        item is already used for an existing load pattern.
    
        Name (input): The name for the new load pattern.
        MyType (input): This is one of the following items in the eLoadPatternType
            enumeration: LTYPE_DEAD = 1 LTYPE_SUPERDEAD = 2 LTYPE_LIVE = 3 LTYPE_REDUCELIVE
            = 4 LTYPE_QUAKE = 5 LTYPE_WIND= 6 LTYPE_SNOW = 7 LTYPE_OTHER = 8 LTYPE_MOVE = 9
            LTYPE_TEMPERATURE = 10 LTYPE_ROOFLIVE = 11 LTYPE_NOTIONAL = 12 LTYPE_PATTERNLIVE
            = 13 LTYPE_WAVE= 14 LTYPE_BRAKING = 15 LTYPE_CENTRIFUGAL = 16 LTYPE_FRICTION =
            17 LTYPE_ICE = 18 LTYPE_WINDONLIVELOAD = 19 LTYPE_HORIZONTALEARTHPRESSURE = 20
            LTYPE_VERTICALEARTHPRESSURE = 21 LTYPE_EARTHSURCHARGE = 22 LTYPE_DOWNDRAG = 23
            LTYPE_VEHICLECOLLISION = 24 LTYPE_VESSELCOLLISION = 25 LTYPE_TEMPERATUREGRADIENT
            = 26 LTYPE_SETTLEMENT = 27 LTYPE_SHRINKAGE = 28 LTYPE_CREEP = 29
            LTYPE_WATERLOADPRESSURE = 30 LTYPE_LIVELOADSURCHARGE = 31 LTYPE_LOCKEDINFORCES =
            32 LTYPE_PEDESTRIANLL = 33 LTYPE_PRESTRESS = 34 LTYPE_HYPERSTATIC = 35
            LTYPE_BOUYANCY = 36 LTYPE_STREAMFLOW = 37 LTYPE_IMPACT = 38 LTYPE_CONSTRUCTION =
            39
        SelfWTMultiplier (input): The self weight multiplier for the new load pattern.
        AddLoadCase (input): If this item is True, a linear static load case corresponding
            to the new load pattern is added.
        """
        _r = self._raw.Add(Name, MyType, SelfWTMultiplier, AddLoadCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.Add falhou (ret={_r})".format(_r=_r))
        return None

    def ChangeName(self, Name: str, NewName: str):
        """This function applies a new name to a load pattern. The function returns zero if the new
        name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The name of a defined load pattern.
        NewName (input): The new name for the load pattern.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """The function returns the number of defined load patterns.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes the specified load pattern. The function returns zero if the load
        pattern is successfully deleted, otherwise it returns a nonzero value. The load
        pattern is not deleted and the function returns an error if the load pattern is
        assigned to an load case or if it is the only defined load pattern.
    
        Name (input): The name of an existing load pattern.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetAutoSeismicCode(self, Name: str):
        """This function retrieves the code name used for auto seismic parameters in Quake-type load
        patterns. The function returns zero if the code is successfully retrieved; otherwise
        it returns a nonzero value. An error is returned if the specified load pattern is
        not a Quake-type load pattern.
    
        Name (input): The name of an existing Quake-type load pattern.
        CodeName (output): This is either blank or the name code used for the auto seismic
            parameters. Blank means no auto seismic load is specified for the Quake-type
            load pattern.
        """
        _r = self._raw.GetAutoSeismicCode(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.GetAutoSeismicCode falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetAutoWaveCode(self, Name: str):
        """This function retrieves the code name used for auto wave parameters in Wave-type load
        patterns. The function returns zero if the code is successfully retrieved; otherwise
        it returns a nonzero value. An error is returned if the specified load pattern is
        not a Wave-type load pattern.
    
        Name (input): The name of an existing Wave-type load pattern.
        CodeName (output): This is either blank or the name code used for the auto wave
            parameters. Blank means no auto wave load is specified for the Wave-type load
            pattern.
        """
        _r = self._raw.GetAutoWaveCode(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.GetAutoWaveCode falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetAutoWindCode(self, Name: str):
        """This function retrieves the code name used for auto wind parameters in Wind-type load
        patterns. The function returns zero if the code is successfully retrieved; otherwise
        it returns a nonzero value. An error is returned if the specified load pattern is
        not a Wind-type load pattern.
    
        Name (input): The name of an existing Wind-type load pattern.
        CodeName (output): This is either blank or the name code used for the auto wind
            parameters. Blank means no auto wind load is specified for the Wind-type load
            pattern.
        """
        _r = self._raw.GetAutoWindCode(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.GetAutoWindCode falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoadType(self, Name: str):
        """This function retrieves the load type for a specified load pattern. The function returns
        zero if the load type is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing load pattern.
        MyType (output): This is one of the following items in the eLoadPatternType
            enumeration: LTYPE_DEAD = 1 LTYPE_SUPERDEAD = 2 LTYPE_LIVE = 3 LTYPE_REDUCELIVE
            = 4 LTYPE_QUAKE = 5 LTYPE_WIND= 6 LTYPE_SNOW = 7 LTYPE_OTHER = 8 LTYPE_MOVE = 9
            LTYPE_TEMPERATURE = 10 LTYPE_ROOFLIVE = 11 LTYPE_NOTIONAL = 12 LTYPE_PATTERNLIVE
            = 13 LTYPE_WAVE= 14 LTYPE_BRAKING = 15 LTYPE_CENTRIFUGAL = 16 LTYPE_FRICTION =
            17 LTYPE_ICE = 18 LTYPE_WINDONLIVELOAD = 19 LTYPE_HORIZONTALEARTHPRESSURE = 20
            LTYPE_VERTICALEARTHPRESSURE = 21 LTYPE_EARTHSURCHARGE = 22 LTYPE_DOWNDRAG = 23
            LTYPE_VEHICLECOLLISION = 24 LTYPE_VESSELCOLLISION = 25 LTYPE_TEMPERATUREGRADIENT
            = 26 LTYPE_SETTLEMENT = 27 LTYPE_SHRINKAGE = 28 LTYPE_CREEP = 29
            LTYPE_WATERLOADPRESSURE = 30 LTYPE_LIVELOADSURCHARGE = 31 LTYPE_LOCKEDINFORCES =
            32 LTYPE_PEDESTRIANLL = 33 LTYPE_PRESTRESS = 34 LTYPE_HYPERSTATIC = 35
            LTYPE_BOUYANCY = 36 LTYPE_STREAMFLOW = 37 LTYPE_IMPACT = 38 LTYPE_CONSTRUCTION =
            39
        """
        _r = self._raw.GetLoadType(Name, None)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.GetLoadType falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined load cases. The function returns zero if
        the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of load pattern names retrieved by the program.
        MyName (output): This is a one-dimensional array of load pattern names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames 1) inside the Sap2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSelfWtMultiplier(self, Name: str):
        """This function retrieves the self weight multiplier for a specified load pattern. The
        function returns zero if the multiplier is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing load pattern.
        SelfWTMultiplier (output): The self weight multiplier for the specified load
            pattern.
        """
        _r = self._raw.GetSelfWtMultiplier(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.GetSelfWtMultiplier falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetLoadType(self, Name: str, MyType: int):
        """This function assigns a load type to a load pattern. The function returns zero if the load
        type is successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load pattern.
        MyType (input): This is one of the following items in the eLoadPatternType
            enumeration: LTYPE_DEAD = 1 LTYPE_SUPERDEAD = 2 LTYPE_LIVE = 3 LTYPE_REDUCELIVE
            = 4 LTYPE_QUAKE = 5 LTYPE_WIND= 6 LTYPE_SNOW = 7 LTYPE_OTHER = 8 LTYPE_MOVE = 9
            LTYPE_TEMPERATURE = 10 LTYPE_ROOFLIVE = 11 LTYPE_NOTIONAL = 12 LTYPE_PATTERNLIVE
            = 13 LTYPE_WAVE= 14 LTYPE_BRAKING = 15 LTYPE_CENTRIFUGAL = 16 LTYPE_FRICTION =
            17 LTYPE_ICE = 18 LTYPE_WINDONLIVELOAD = 19 LTYPE_HORIZONTALEARTHPRESSURE = 20
            LTYPE_VERTICALEARTHPRESSURE = 21 LTYPE_EARTHSURCHARGE = 22 LTYPE_DOWNDRAG = 23
            LTYPE_VEHICLECOLLISION = 24 LTYPE_VESSELCOLLISION = 25 LTYPE_TEMPERATUREGRADIENT
            = 26 LTYPE_SETTLEMENT = 27 LTYPE_SHRINKAGE = 28 LTYPE_CREEP = 29
            LTYPE_WATERLOADPRESSURE = 30 LTYPE_LIVELOADSURCHARGE = 31 LTYPE_LOCKEDINFORCES =
            32 LTYPE_PEDESTRIANLL = 33 LTYPE_PRESTRESS = 34 LTYPE_HYPERSTATIC = 35
            LTYPE_BOUYANCY = 36 LTYPE_STREAMFLOW = 37 LTYPE_IMPACT = 38 LTYPE_CONSTRUCTION =
            39
        """
        _r = self._raw.SetLoadType(Name, MyType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.SetLoadType falhou (ret={_r})".format(_r=_r))
        return None

    def SetSelfWtMultiplier(self, Name: str, SelfWTMultiplier: float):
        """This function assigns a self weight multiplier to a load case. The function returns zero if
        the multiplier is successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load pattern.
        SelfWTMultiplier (input): The self weight multiplier for the specified load pattern.
        """
        _r = self._raw.SetSelfWtMultiplier(Name, SelfWTMultiplier)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.SetSelfWtMultiplier falhou (ret={_r})".format(_r=_r))
        return None

    @cached_property
    def AutoSeastate(self):
        return N_LoadPatterns_AutoSeastate(self._raw.AutoSeastate)

    @cached_property
    def AutoSeismic(self):
        return N_LoadPatterns_AutoSeismic(self._raw.AutoSeismic)

    @cached_property
    def AutoWind(self):
        return N_LoadPatterns_AutoWind(self._raw.AutoWind)


class N_LoadPatterns_AutoSeastate:
    """Wrapper para SapModel.LoadPatterns.AutoSeastate."""

    def __init__(self, raw):
        self._raw = raw

    def GetAuto(self, Name: str):
        """This function retrieves auto seastate loading parameters. The function returns zero if the
        parameters are successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing seastate-type load pattern.
        LoadMethod (output): This is one of the following three options defining what
            parameters are being specified. 1 = Rotation / Translations Vertical Input 2 =
            Rotations / Translations Full Input 3 = Accelerations / Velocities
        CSys (output): The coordinate system used as a reference for specifying the center
            of rotation location and the inertia load parameters.
        AdjustGravityLat (output): This item only applies when using LoadMethod 1 or 2. It
            is True if generated lateral loads should include the effects of the rotated
            structure, otherwise it is False.
        AdjustGravityLatFactor (output): This item only applies when using LoadMethod 1 or
            2. This is a scale factor on the lateral effects generated as a result of the
            rotated structure.
        AdjustGravityVert (output): This item only applies when using LoadMethod 1 or 2. It
            is True if generated vertical loads should include the effects of the rotated
            structure, otherwise it is False.
        AdjustGravityVertFactor (output): This item only applies when using LoadMethod 1 or
            2. This is a scale factor on the vertical effects generated as a result of the
            rotated structure.
        CenterRotation (output): This is an array dimensioned to 2 (3 doubles) that defines
            the coordinates of the center of rotation, with respect to the selected
            coordinate system.
        Parameters (output): This is an array of the inertia load parameters, based on the
            specified LoadMethod, as described below. If LoadMethod = 1, the following 9
            parameters should be input: Parameters(0) - UZ amplitude Parameters(1) - UZ
            period Parameters(2) - UZ phase Parameters(3) - RX amplitude Parameters(4) - RX
            period Parameters(5) - RX phase Parameters(6) - RY amplitude Parameters(7) - RY
            period Parameters(8) - RY phase If the LoadMethod = 2, the following 18
            parameters should be input: Parameters(0) - UX amplitude Parameters(1) - UX
            period Parameters(2) - UX phase Parameters(3) - UY amplitude Parameters(4) - UY
            period Parameters(5) - UY phase Parameters(6) - UZ amplitude Parameters(7) - UZ
            period Parameters(8) - UZ phase Parameters(9) - RX amplitude Parameters(10) - RX
            period Parameters(11) - RX phase Parameters(12) - RY amplitude Parameters(13) -
            RY period Parameters(14) - RY phase Parameters(15) - RZ amplitude Parameters(16)
            - RZ period Parameters(17) - RZ phase If the LoadMethod = 3, the following 9
            parameters should be input: Parameters(0) - Acceleration UX Parameters(1) -
            Acceleration UY Parameters(2) - Acceleration UZ Parameters(3) - Acceleration RX
            Parameters(4) - Acceleration RY Parameters(5) - Acceleration RZ Parameters(6) -
            Velocity RX Parameters(7) - Velocity RY Parameters(8) - Velocity RZ
        IgnorePhase (output): This item only applies when using LoadMethod 1 or 2. It is
            True if the input phases should be ignored, otherwise it is False.
        """
        _r = self._raw.GetAuto(Name, 0, "", False, 0.0, False, 0.0, [], [], False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeastate.GetAuto falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetAuto(self, Name: str, LoadMethod: int, CSys: str, AdjustGravityLat: bool, AdjustGravityLatFactor: float, AdjustGravityVert: bool, AdjustGravityVertFactor: float, CenterRotation: list[float], Parameters: list[float], IgnorePhase: bool):
        """This function retrieves auto seastate loading parameters. The function returns zero if the
        parameters are successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing seastate-type load pattern.
        LoadMethod (input): This is one of the following three options defining what
            parameters are being specified. 1 = Rotation / Translations Vertical Input 2 =
            Rotations / Translations Full Input 3 = Accelerations / Velocities
        CSys (input): The coordinate system used as a reference for specifying the center of
            rotation location and the inertia load parameters.
        AdjustGravityLat (input): This item only applies when using LoadMethod 1 or 2. It is
            True if generated lateral loads should include the effects of the rotated
            structure, otherwise it is False.
        AdjustGravityLatFactor (input): This item only applies when using LoadMethod 1 or 2.
            This is a scale factor on the lateral effects generated as a result of the
            rotated structure.
        AdjustGravityVert (input): This item only applies when using LoadMethod 1 or 2. It
            is True if generated vertical loads should include the effects of the rotated
            structure, otherwise it is False.
        AdjustGravityVertFactor (input): This item only applies when using LoadMethod 1 or
            2. This is a scale factor on the vertical effects generated as a result of the
            rotated structure.
        CenterRotation (input): This is an array dimensioned to 2 (3 doubles) that defines
            the coordinates of the center of rotation, with respect to the selected
            coordinate system.
        Parameters (input): This is an array of the inertia load parameters, based on the
            specified LoadMethod, as described below. If LoadMethod = 1, the following 9
            parameters should be input: Parameters(0) - UZ amplitude Parameters(1) - UZ
            period Parameters(2) - UZ phase Parameters(3) - RX amplitude Parameters(4) - RX
            period Parameters(5) - RX phase Parameters(6) - RY amplitude Parameters(7) - RY
            period Parameters(8) - RY phase If the LoadMethod = 2, the following 18
            parameters should be input: Parameters(0) - UX amplitude Parameters(1) - UX
            period Parameters(2) - UX phase Parameters(3) - UY amplitude Parameters(4) - UY
            period Parameters(5) - UY phase Parameters(6) - UZ amplitude Parameters(7) - UZ
            period Parameters(8) - UZ phase Parameters(9) - RX amplitude Parameters(10) - RX
            period Parameters(11) - RX phase Parameters(12) - RY amplitude Parameters(13) -
            RY period Parameters(14) - RY phase Parameters(15) - RZ amplitude Parameters(16)
            - RZ period Parameters(17) - RZ phase If the LoadMethod = 3, the following 9
            parameters should be input: Parameters(0) - Acceleration UX Parameters(1) -
            Acceleration UY Parameters(2) - Acceleration UZ Parameters(3) - Acceleration RX
            Parameters(4) - Acceleration RY Parameters(5) - Acceleration RZ Parameters(6) -
            Velocity RX Parameters(7) - Velocity RY Parameters(8) - Velocity RZ
        IgnorePhase (input): This item only applies when using LoadMethod 1 or 2. It is True
            if the input phases should be ignored, otherwise it is False.
        """
        _r = self._raw.SetAuto(Name, LoadMethod, CSys, AdjustGravityLat, AdjustGravityLatFactor, AdjustGravityVert, AdjustGravityVertFactor, CenterRotation, Parameters, IgnorePhase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeastate.SetAuto falhou (ret={_r})".format(_r=_r))
        return None

    def SetNone(self, Name: str):
        """This function sets the auto seastate loading type for the specified load pattern to None.
        The function returns zero if the loading type is successfully assigned; otherwise it
        returns a nonzero vale.
    
        Name (input): The name of an existing seastate-type load pattern.
        """
        _r = self._raw.SetNone(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeastate.SetNone falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadPatterns_AutoWind:
    """Wrapper para SapModel.LoadPatterns.AutoWind."""

    def __init__(self, raw):
        self._raw = raw

    def GetAPI4F2008_1(self, Name: str, UserZ: bool):
        """This function retrieves auto wind loading parameters for API 4F 2008. The function returns
        zero if the parameters are successfully assigned; otherwise, it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load case with an API 4F 2008 auto
            wind assignment.
        ExposureFrom (output): This is 2, 3, or 4, indicating the source of the wind
            exposure. 2 = From area objects 3 = From frame objects (open structure) 4 = From
            area objects and frame objects (open structure)
        DirAngle (output): The direction angle for the wind load.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The design reference wind velocity, Vref, in knots.
        SSLFactor (output): The structural safety level multiplier.
        ShieldingFactor (output): The shielding factor.
        """
        _r = self._raw.GetAPI4F2008_1(Name, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetAPI4F2008_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetAPI4F2013(self, Name: str, UserZ: bool):
        """This function retrieves auto wind loading parameters for API 4F 2013. The function returns
        zero if the parameters are successfully assigned; otherwise, it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load case with an API 4F 2013 auto
            wind assignment.
        ExposureFrom (output): This is 2, 3, or 4, indicating the source of the wind
            exposure. 2 = From area objects 3 = From frame objects (open structure) 4 = From
            area objects and frame objects (open structure)
        DirAngle (output): The direction angle for the wind load.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The design reference wind velocity, Vref, in knots.
        SSLFactor (output): The structural safety level multiplier.
        ShieldingFactor (output): The shielding factor.
        """
        _r = self._raw.GetAPI4F2013(Name, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetAPI4F2013 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetASCE702(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for ASCE 7-02. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern with an ASCE7-02 auto
            wind assignment.
        ExposureFrom (output): This is 1, 2, 3 or 4, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects 3 = From
            frame objects (open structure) 4 = From area objects and frame objects (open
            structure)
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        ASCECase (output): This is 1, 2, 3, 4 or 5, indicating the desired case from
            ASCE7-02 Figure 6-9. 1, 2, 3 and 4 refer to cases 1 through 4 in the figure. 5
            means to create all cases. This item applies only when ExposureFrom = 1.
        ASCEe1 (output): This is the value e1 in ASCE7-02 Figure 6-9. This item applies only
            when ExposureFrom = 1.
        ASCEe2 (output): This is the value e2 in ASCE7-02 Figure 6-9. This item applies only
            when ExposureFrom = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in miles per hour.
        ExposureType (output): This is 1, 2, 3 or 4, indicating the exposure category. 1 = A
            2 = B 3 = C 4 = D
        ImportanceFactor (output): The importance factor.
        Kzt (output): The topographical factor.
        GustFactor (output): The gust factor.
        Kd (output): The directionality factor.
        SolidGrossRatio (output): The solid area divided by gross area ratio for open frame
            structure loading. This item applies only when the loading is from open
            structure wind loading (ExposureFrom = 3 or ExposureFrom = 4).
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetASCE702(Name, 0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetASCE702 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetASCE705(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for ASCE 7-05. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern with an ASCE7-05 auto
            wind assignment.
        ExposureFrom (output): This is 1, 2, 3 or 4, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects 3 = From
            frame objects (open structure) 4 = From area objects and frame objects (open
            structure)
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        ASCECase (output): This is 1, 2, 3, 4 or 5, indicating the desired case from
            ASCE7-05 Figure 6-9. 1, 2, 3 and 4 refer to cases 1 through 4 in the figure. 5
            means to create all cases. This item applies only when ExposureFrom = 1.
        ASCEe1 (output): This is the value e1 in ASCE7-05 Figure 6-9. This item applies only
            when ExposureFrom = 1.
        ASCEe2 (output): This is the value e2 in ASCE7-05 Figure 6-9. This item applies only
            when ExposureFrom = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in miles per hour.
        ExposureType (output): This is 1, 2 or 3, indicating the exposure category. 1 = B 2
            = C 3 = D
        ImportanceFactor (output): The importance factor.
        Kzt (output): The topographical factor.
        GustFactor (output): The gust factor.
        Kd (output): The directionality factor.
        SolidGrossRatio (output): The solid area divided by the gross area ratio for open
            frame structure loading. This item applies only when the loading is from open
            structure wind loading (ExposureFrom = 3 or ExposureFrom = 4).
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetASCE705(Name, 0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetASCE705 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetASCE788(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for ASCE 7-88. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern with an ASCE7-88 auto
            wind assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in miles per hour.
        ExposureType (output): This is 1, 2, 3 or 4, indicating the exposure category. 1 = A
            2 = B 3 = C 4 = D
        ImportanceFactor (output): The importance factor.
        GustFactor (output): The gust factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetASCE788(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetASCE788 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetASCE795(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for ASCE 7-95. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern with an ASCE7-95 auto
            wind assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in miles per hour.
        ExposureType (output): This is 1, 2, 3 or 4, indicating the exposure category. 1 = A
            2 = B 3 = C 4 = D
        ImportanceFactor (output): The importance factor.
        Kzt (output): The topographical factor.
        GustFactor (output): The gust factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetASCE795(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetASCE795 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetASNZS117022002(self, Name: str, Cpw: float, Cpl: float, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for AS/NZS 1170.2:2002. The function
        returns zero if the parameters are successfully assigned; otherwise, it returns a
        nonzero value.
    
        Name (input): The name of an existing Wind-type load case with an AS/NZS 1170.2:2002
            auto wind assignment.
        ExposureFrom (output): This is 1, or 2, indicating the source of the wind exposure.
            1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        Ka (output): The area reduction factor, Ka.
        Kc (output): The combination factor, Kc.
        Kl (output): The local pressure factor, Kl.
        Kp (output): The porous cladding factor, Kp.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The regional wind speed, Vr, in m/s.
        Cat (output): This is 1, 2, 3 or 4, indicating the terrain category.
        CycloneRegion (output): This is True or False, indicating if the structure is in a
            cyclone region.
        Md (output): The directional multiplier, Md.
        Ms (output): The shielding multiplier, Ms.
        Mt (output): The topographic multiplier, Mt.
        Cdyn (output): The dynamic response factor, Cdyn.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetASNZS117022002(Name, 0, 0.0, Cpw, Cpl, 0.0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, False, 0.0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetASNZS117022002 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetBOCA96(self, Name: str, UserZ: bool, UserGust: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for BOCA 96. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an BOCA 96 auto
            wind assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in miles per hour.
        ExposureType (output): This is 1, 2, 3 or 4, indicating the exposure category. 1 = A
            2 = B 3 = C 4 = D
        ImportanceFactor (output): The importance factor.
        UserGust (input): If this item is True, the gust factor is user defined. If it is
            False, the gust factor is determined from the code specified values.
        GustFactor (output): The user defined gust factor. This item applies only when
            UserGust is True.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetBOCA96(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, UserGust, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetBOCA96 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetBS639995(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for BS6399-95. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern with an BS6399-95 auto
            wind assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The front coefficient, Cp. This item applies only when ExposureFrom =
            1.
        Cpl (output): The rear coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        Ve (output): The effective wind speed in meters per second.
        Ca (output): The size effect factor.
        Cr (output): The dynamic augmentation factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetBS639995(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetBS639995 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetChinese2010(self, Name: str, UniformTaper: bool, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for Chinese 2010. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern with an Chinese 2010
            auto wind assignment.
        ExposureFrom (output): This is 1 or 2 indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        BuildingWidth (output): The building width. [L]
        Us (output): The shape coefficient. This item applies only when ExposureFrom = 1.
        UniformTaper (input): This item is True if a correction is to be applied to the wind
            load for a uniform taper.
        BHoverB0 (output): The taper ratio, Bh/B0. This item applies only when UniformTaper
            = True.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        wzero (output): The basic wind pressure in kN/m 2 .
        Rt (output): This is 1, 2, 3 or 4, indicating the ground roughness. 1 = A 2 = B 3 =
            C 4 = D
        PhiZOpt (output): This is 0 or 1, indicating the Phi Z source. 0 = Modal analysis 1
            = Z/H ratio
        T1Opt (output): This is 0 or 1, indicating the T1 source. 0 = Modal analysis 1 =
            User defined
        UserT (output): This item only applies when the T1 source is user defined (T1Opt =
            1). It is the user defined T1 period. [s]
        DampRatio (output): The damping ratio.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetChinese2010(Name, 0, 0.0, 0.0, 0.0, UniformTaper, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetChinese2010 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetEurocode12005_1(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for Eurocode 1 2005. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with a Eurocode 1 2005
            auto wind assignment.
        ExposureFrom (output): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The basic wind speed, vb, in meters per second.
        Terrain (output): This is 0, 1, 2, 3 or 4, indicating the terrain category. 0 = 0 1
            = I 2 = II 3 = III 4 = IV
        Orography (output): The orography factor, Co.
        k1 (output): The turbulence factor, k1.
        CsCd (output): The structural factor, CsCd.
        Rho (output): The air density in kg/m 3 , Rho.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetEurocode12005_1(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetEurocode12005_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetExposure_1(self, Name: str):
        """This function retrieves exposure parameters for auto wind loads determined from extents of
        rigid diaphragms. This function does not apply for User-type auto wind loads. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern that has an auto wind
            load assigned.
        Num (output): The number of diaphragms at which exposure data is reported.
        Diaph (output): This is an array that includes the names of the diaphragms that have
            eccentricity overrides.
        x (output): This is an array that includes the global X-coordinate of the point
            where the wind force load is applied to the diaphragm. [L]
        y (output): This is an array that includes the global Y-coordinate of the point
            where the wind force load is applied to the diaphragm. [L]
        MyWidth (output): This is an array that includes the exposure width for the wind
            load applied to the specified diaphragm. [L]
        MyDepth (output): This is an array that includes the exposure depth for the wind
            load applied to the specified diaphragm. [L]
        Height (output): This is an array that includes the exposure height for the wind
            load applied to the specified diaphragm. [L]
        """
        _r = self._raw.GetExposure_1(Name, 0, [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetExposure_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIS8751987(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for Indian IS875-1987. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an Indian
            IS875-1987 auto wind assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in meters per second.
        Terrain (output): This is 1, 2, 3 or 4, indicating the terrain category.
        Class (output): This is 1, 2 or 3, indicating the terrain category. 1 = A 2 = B 3 =
            C
        K1 (output): The risk coefficient (k1 factor).
        K3 (output): The topography factor (k3 factor).
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetIS8751987(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetIS8751987 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIS8752015(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for Indian IS875-2015. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an Indian IS
            875:2015 auto wind assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in meters per second.
        TerrainCategory (output): This is 1, 2, 3 or 4, indicating the terrain category.
        ImportanceFactor (output): This is 1, 2 or 3, depending on the importance factor. 1
            = 1.00 2 = 1.15 3 = 1.30
        k1 (output): The risk coefficient (k1 factor).
        k3 (output): The topography factor (k3 factor).
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetIS8752015(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetIS8752015 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMexican(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves the Mexican auto wind loading parameters. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an Indian
            IS875-1987 auto wind assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in meters per second.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetMexican(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetMexican falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC2005(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for NBCC 2005. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern with an NBCC 2005 auto
            wind assignment.
        ExposureFrom (output): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        q (output): The velocity pressure in kPa.
        GustFactor (output): The gust effect factor.
        ImportanceFactor (output): The importance factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetNBCC2005(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetNBCC2005 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC2010_1(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for NBCC 2010. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern with an NBCC 2010 auto
            wind assignment.
        ExposureFrom (output): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        q (output): The velocity pressure in kPa.
        GustFactor (output): The gust effect factor.
        ImportanceFactor (output): The importance factor.
        TerrainType (output): This is 1, 2, or 3, indicating the terrain type. 1 = Open 2 =
            Rough 3 = User
        CeWindward (output): The windward exposure factor, Ce. This item applies only when
            TerrainType = 3.
        CeLeeward (output): The windward exposure factor, Ce. This item applies only when
            TerrainType = 3.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetNBCC2010_1(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetNBCC2010_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC2015(self, Name: str, ExposureFrom: int, NBCCCase: int, e1: float, e2: float, UserZ: bool, TopZ: float, BottomZ: float, TopographicFactor: float, UserExposure: bool):
        """This function retrieves auto wind loading parameters for NBCC 2015. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern with an NBCC 2015 auto
            wind assignment..
        ExposureFrom (input): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        NBCCCase (input): This is 1, 2, 3, 4, or 5, indicating the desired case from NBCC
            2105 Figure A-4.1.7.9(1). 1,2,3, and 4 refer to cases 1 through 4 in the figure,
            while 5 means all cases. This item applies only when ExposureFrom = 1.
        e1 (input): This is the value e1 in the NBCC 2015 Figure A-4.1.7.9(1). This item
            applies only when ExposureFrom = 1.
        e2 (input): This is the value e2 in the NBCC 2015 Figure A-4.1.7.9(1). This item
            applies only when ExposureFrom = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        q (output): The velocity pressure in kPa.
        GustFactor (output): The gust effect factor, Cg.
        TopographicFactor (input): The importance factor, Ct.
        ImportanceFactor (output): The importance Factor, Iw.
        TerrainType (output): This is 1, 2, or 3, indicating the terrain type. 1 = Open 2 =
            Rough 3 = User
        CeWindward (output): The windward exposure factor, Ce. This item applies only when
            TerrainType = 3.
        CeLeeward (output): The windward exposure factor, Ce. This item applies only when
            TerrainType = 3.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetNBCC2015(Name, ExposureFrom, 0.0, 0.0, 0.0, NBCCCase, e1, e2, UserZ, TopZ, BottomZ, 0.0, 0.0, TopographicFactor, 0.0, 0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetNBCC2015 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC95(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for NBCC 95. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an NBCC 95 auto
            wind assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        q (output): The velocity pressure in kPa.
        GustFactor (output): The gust effect factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetNBCC95(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetNBCC95 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNTC2008(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for NTC 2008. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an NTC 2008 auto
            wind assignment.
        ExposureFrom (output): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        Vb (output): The wind velocity in m/s.
        ExposureCategory (output): This is 1, 2, 3, 4, or 5, indicating the exposure
            category. 1 = I 2 = II 3 = III 4 = IV 5 = V
        ct (output): The topography factor, ct.
        cd (output): The dynamic coefficient, cd.
        cp (output): The shape factor, cp.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetNTC2008(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetNTC2008 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNTC2018(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for NTC 2018. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an NTC 2018 auto
            wind assignment.
        ExposureFrom (output): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        Vb (output): The wind velocity in m/s.
        ExposureCategory (output): This is 1, 2, 3, 4, or 5, indicating the exposure
            category. 1 = I 2 = II 3 = III 4 = IV 5 = V
        ct (output): The topography factor, ct.
        cd (output): The dynamic coefficient, cd.
        cp (output): The shape factor, cp.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetNTC2018(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetNTC2018 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUBC94(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for 1994 UBC. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an UBC94 auto wind
            assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in miles per hour.
        ExposureType (output): This is 1, 2 or 3, indicating the exposure category. 1 = B 2
            = C 3 = D
        ImportanceFactor (output): The importance factor.
        GustFactor (output): The gust factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetUBC94(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetUBC94 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUBC97(self, Name: str, UserZ: bool, UserExposure: bool):
        """This function retrieves auto wind loading parameters for 1997 UBC. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an UBC97 auto wind
            assignment.
        ExposureFrom (output): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (output): The direction angle for the wind load. This item applies only
            when ExposureFrom = 1.
        Cpw (output): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (output): The leeward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (output): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (output): This item is the global Z-coordinate at the lowest level where
            auto wind loads are applied. [L]
        WindSpeed (output): The wind speed in miles per hour.
        ExposureType (output): This is 1, 2 or 3, indicating the exposure category. 1 = B 2
            = C 3 = D
        ImportanceFactor (output): The importance factor.
        GustFactor (output): The gust factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.GetUBC97(Name, 0, 0.0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, UserExposure)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetUBC97 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUserLoad(self, Name: str, Fx: list[float], Fx_2: list[float], Mz: list[float]):
        """This function retrieves auto wind loading parameters for User-type wind loading. The
        function returns zero if the parameters are successfully assigned, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern that has a User-type
            auto wind load assigned.
        Num (output): The number of diaphragms at which user wind loads are reported.
        Diaph (output): This is an array that includes the names of the diaphragms that have
            user wind loads.
        Fx (input): This is an array that includes the global X direction force assigned to
            the specified diaphragm. [F]
        Mz (input): This is an array that includes the moment about the global Z axis
            assigned to the specified diaphragm. [FL]
        x (output): This is an array that includes the global X-coordinate of the point
            where the wind force load is applied to the diaphragm. [L]
        y (output): This is an array that includes the global Y-coordinate of the point
            where the wind force load is applied to the diaphragm. [L]
        """
        _r = self._raw.GetUserLoad(Name, 0, [], Fx, Fx_2, Mz, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.GetUserLoad falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetAPI4F2008_1(self, Name: str, ExposureFrom: int, DirAngle: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, SSLFactor: float, ShieldingFactor: float):
        """This function assigns auto wind loading parameters for API 4F 2008. The function returns
        zero if the parameters are successfully assigned; otherwise, it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load case.
        ExposureFrom (input): This is 2, 3, or 4, indicating the source of the wind
            exposure. 2 = From area objects 3 = From frame objects (open structure) 4 = From
            area objects and frame objects (open structure)
        DirAngle (input): The direction angle for the wind load.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (input): This item is the global Z-coordinate at the lowest level where auto
            wind loads are applied. [L]
        WindSpeed (input): The design reference wind velocity, Vref, in knots.
        SSLFactor (input): The structural safety level multiplier.
        ShieldingFactor (input): The shielding factor.
        """
        _r = self._raw.SetAPI4F2008_1(Name, ExposureFrom, DirAngle, UserZ, TopZ, BottomZ, WindSpeed, SSLFactor, ShieldingFactor)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetAPI4F2008_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetAPI4F2013(self, Name: str, ExposureFrom: int, DirAngle: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, SSLFactor: float, ShieldingFactor: float):
        """This function assigns auto wind loading parameters for API 4F 2013. The function returns
        zero if the parameters are successfully assigned; otherwise, it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load case.
        ExposureFrom (input): This is 2, 3, or 4, indicating the source of the wind
            exposure. 2 = From area objects 3 = From frame objects (open structure) 4 = From
            area objects and frame objects (open structure)
        DirAngle (input): The direction angle for the wind load.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (input): This item is the global Z-coordinate at the lowest level where auto
            wind loads are applied. [L]
        WindSpeed (input): The design reference wind velocity, Vref, in knots.
        SSLFactor (input): The structural safety level multiplier.
        ShieldingFactor (input): The shielding factor.
        """
        _r = self._raw.SetAPI4F2013(Name, ExposureFrom, DirAngle, UserZ, TopZ, BottomZ, WindSpeed, SSLFactor, ShieldingFactor)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetAPI4F2013 falhou (ret={_r})".format(_r=_r))
        return None

    def SetASCE702(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, ASCECase: int, ASCEe1: float, ASCEe2: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, ExposureType: int, ImportanceFactor: float, Kzt: float, GustFactor: float, Kd: float, SolidGrossRatio: float = 0.2, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for ASCE 7-02. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is 1, 2, 3 or 4, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects 3 = From
            frame objects (open structure) 4 = From area objects and frame objects (open
            structure)
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        ASCECase (input): This is either 1, 2, 3, 4 or 5, indicating the desired case from
            ASCE7-02 Figure 6-9. 1, 2, 3 and 4 refer to cases 1 through 4 in the figure. 5
            means to create all cases. This item applies only when ExposureFrom = 1.
        ASCEe1 (input): This is the value e1 in ASCE7-02 Figure 6-9. This item applies only
            when ExposureFrom = 1.
        ASCEe2 (input): This is the value e2 in ASCE7-02 Figure 6-9. This item applies only
            when ExposureFrom = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies pnly when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in miles per hour.
        ExposureType (input): This is 1, 2, 3 or 4, indicating the exposure category. 1 = A
            2 = B 3 = C 4 = D
        ImportanceFactor (input): The importance factor.
        Kzt (input): The topographical factor.
        GustFactor (input): The gust factor.
        Kd (input): The directionality factor.
        SolidGrossRatio (input): The solid area divided by gross area ratio for open frame
            structure loading. This item applies only when the loading is from open
            structure wind loading (ExposureFrom = 3 or ExposureFrom = 4).
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetASCE702(Name, ExposureFrom, DirAngle, Cpw, Cpl, ASCECase, ASCEe1, ASCEe2, UserZ, TopZ, BottomZ, WindSpeed, ExposureType, ImportanceFactor, Kzt, GustFactor, Kd, SolidGrossRatio, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetASCE702 falhou (ret={_r})".format(_r=_r))
        return None

    def SetASCE705(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, ASCECase: int, ASCEe1: float, ASCEe2: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, ExposureType: int, ImportanceFactor: float, Kzt: float, GustFactor: float, Kd: float, SolidGrossRatio: float = 0.2, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for ASCE 7-05. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is 1, 2, 3 or 4, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects 3 = From
            frame objects (open structure) 4 = From area objects and frame objects (open
            structure)
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        ASCECase (input): This is 1, 2, 3, 4 or 5, indicating the desired case from ASCE7-05
            Figure 6-9. 1, 2, 3 and 4 refer to cases 1 through 4 in the figure. 5 means to
            create all cases. This item applies only when ExposureFrom = 1.
        ASCEe1 (input): This is the value e1 in ASCE7-05 Figure 6-9. This item applies only
            when ExposureFrom = 1.
        ASCEe2 (input): This is the value e2 in ASCE7-05 Figure 6-9. This item applies only
            when ExposureFrom = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in miles per hour.
        ExposureType (input): This is 1, 2 or 3, indicating the exposure category. 1 = B 2 =
            C 3 = D
        ImportanceFactor (input): The importance factor.
        Kzt (input): The topographical factor.
        GustFactor (input): The gust factor.
        Kd (input): The directionality factor.
        SolidGrossRatio (input): The solid area divided by gross area ratio for open frame
            structure loading. This item applies only when the loading is from open
            structure wind loading (ExposureFrom = 3 or ExposureFrom = 4).
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetASCE705(Name, ExposureFrom, DirAngle, Cpw, Cpl, ASCECase, ASCEe1, ASCEe2, UserZ, TopZ, BottomZ, WindSpeed, ExposureType, ImportanceFactor, Kzt, GustFactor, Kd, SolidGrossRatio, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetASCE705 falhou (ret={_r})".format(_r=_r))
        return None

    def SetASCE788(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, ExposureType: int, ImportanceFactor: float, GustFactor: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for ASCE 7-88. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in miles per hour.
        ExposureType (input): This is 1, 2, 3 or 4, indicating the exposure category. 1 = A
            2 = B 3 = C 4 = D
        ImportanceFactor (input): The importance factor.
        GustFactor (input): The gust factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetASCE788(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, ExposureType, ImportanceFactor, GustFactor, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetASCE788 falhou (ret={_r})".format(_r=_r))
        return None

    def SetASCE795(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, ExposureType: int, ImportanceFactor: float, Kzt: float, GustFactor: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for ASCE 7-95. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in miles per hour.
        ExposureType (input): This is 1, 2, 3 or 4, indicating the exposure category. 1 = A
            2 = B 3 = C 4 = D
        ImportanceFactor (input): The importance factor.
        Kzt (input): The topographical factor.
        GustFactor (input): The gust factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetASCE795(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, ExposureType, ImportanceFactor, Kzt, GustFactor, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetASCE795 falhou (ret={_r})".format(_r=_r))
        return None

    def SetASNZS117022002(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, Ka: float, Kc: float, Kl: float, Kp: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, Cat: int, CycloneRegion: bool, Md: float, Ms: float, Mt: float, Cdyn: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for AS/NZS 1170.2:2002. The function
        returns zero if the parameters are successfully assigned; otherwise, it returns a
        nonzero value.
    
        Name (input): The name of an existing Wind-type load case.
        ExposureFrom (input): This is 1, or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        Ka (input): The area reduction factor, Ka.
        Kc (input): The combination factor, Kc.
        Kl (input): The local pressure factor, Kl.
        Kp (input): The porous cladding factor, Kp.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item is the global Z-coordinate at the highest level where auto
            wind loads are applied. [L]
        BottomZ (input): This item is the global Z-coordinate at the lowest level where auto
            wind loads are applied. [L]
        WindSpeed (input): The regional wind speed, Vr, in m/s.
        Cat (input): This is 1, 2, 3 or 4, indicating the terrain category.
        CycloneRegion (input): This is True or False, indicating if the structure is in a
            cyclone region.
        Md (input): The directional multiplier, Md.
        Ms (input): The shielding multiplier, Ms.
        Mt (input): The topographic multiplier, Mt.
        Cdyn (input): The dynamic response factor, Cdyn.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetASNZS117022002(Name, ExposureFrom, DirAngle, Cpw, Cpl, Ka, Kc, Kl, Kp, UserZ, TopZ, BottomZ, WindSpeed, Cat, CycloneRegion, Md, Ms, Mt, Cdyn, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetASNZS117022002 falhou (ret={_r})".format(_r=_r))
        return None

    def SetBOCA96(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, ExposureType: int, ImportanceFactor: float, GustFactor: float, UserGust: bool = False, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for BOCA 96. The function returns zero if
        the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in miles per hour.
        ExposureType (input): This is 1, 2, 3 or 4, indicating the exposure category. 1 = A
            2 = B 3 = C 4 = D
        ImportanceFactor (input): The importance factor.
        GustFactor (input): The user defined gust factor. This item applies only when
            UserGust is True.
        UserGust (input): If this item is True, the gust factor is user defined. If it is
            False, the gust factor is determined from the code specified values.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetBOCA96(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, ExposureType, ImportanceFactor, GustFactor, UserGust, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetBOCA96 falhou (ret={_r})".format(_r=_r))
        return None

    def SetBS639995(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, Ve: float, Ca: float, Cr: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for BS6399-95. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The front coefficient, Cp. This item applies only when ExposureFrom =
            1.
        Cpl (input): The rear coefficient, Cp. This item applies only when ExposureFrom = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        Ve (input): The effective wind speed in meters per second.
        Ca (input): The size effect factor.
        Cr (input): The dynamic augmentation factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetBS639995(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, Ve, Ca, Cr, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetBS639995 falhou (ret={_r})".format(_r=_r))
        return None

    def SetChinese2010(self, Name: str, ExposureFrom: int, DirAngle: float, BuildingWidth: float, Us: float, UniformTaper: bool, BHoverB0: float, UserZ: bool, TopZ: float, BottomZ: float, wzero: float, Rt: int, PhiZOpt: int, T1Opt: int, UserT: float, DampRatio: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for Chinese 2010. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item only applies when
            ExposureFrom = 1.
        BuildingWidth (input): The building width. [L]
        Us (input): The shape coefficient. This item applies only when ExposureFrom = 1.
        UniformTaper (input): This item is True if a correction is to be applied to the wind
            load for a uniform taper.
        BHoverB0 (input): The taper ratio, Bh/B0. This item applies only when UniformTaper =
            True.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        wzero (input): The basic wind pressure in kN/m 2 .
        Rt (input): This is 1, 2, 3 or 4, indicating the ground roughness. 1 = A 2 = B 3 = C
            4 = D
        PhiZOpt (input): This is 0 or 1, indicating the Phi Z source. 0 = Modal analysis 1 =
            Z/H ratio
        T1Opt (input): This is 0 or 1, indicating the T1 source. 0 = Modal analysis 1 = User
            defined
        UserT (input): This item applies only when the T1 source is user defined (T1Opt =
            1). It is the user defined T1 period. [s]
        DampRatio (input): The damping ratio.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetChinese2010(Name, ExposureFrom, DirAngle, BuildingWidth, Us, UniformTaper, BHoverB0, UserZ, TopZ, BottomZ, wzero, Rt, PhiZOpt, T1Opt, UserT, DampRatio, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetChinese2010 falhou (ret={_r})".format(_r=_r))
        return None

    def SetEurocode12005_1(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, Terrain: int, Orography: float, k1: float, CsCd: float, Rho: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for Eurocode 1 2005. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The basic wind speed, vb, in meters per second.
        Terrain (input): This is 0, 1, 2, 3 or 4, indicating the terrain category. 0 = 0 1 =
            I 2 = II 3 = III 4 = IV
        Orography (input): The orography factor, Co.
        k1 (input): The turbulence factor, k1.
        CsCd (input): The structural factor, CsCd.
        Rho (input): The air density in kg/m 3 , Rho.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetEurocode12005_1(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, Terrain, Orography, k1, CsCd, Rho, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetEurocode12005_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetExposure_1(self, Name: str, Diaph: str, x: float, y: float, Width: float, Depth: float, Height: float):
        """This function assigns exposure parameters for auto wind loads determined from extents of
        rigid diaphragms. This function does not apply for User-type auto wind loads. The
        function returns zero if the parameters are successfully assigned; otherwise it
        returns a nonzero value. The function returns an error if the auto wind load is not
        specified to have user exposure parameters.
    
        Name (input): The name of an existing Wind-type load pattern that has an auto wind
            load assigned.
        Diaph (input): The name of an existing special rigid diaphragm constraint, that is,
            a diaphragm constraint with the following features: 1. The constraint type is
            CONSTRAINT_DIAPHRAGM = 2. 2. The constraint coordinate system is Global. 3. The
            constraint axis is Z.
        x (input): The global X-coordinate of the point where the wind force is applied. [L]
        y (input): The global Y-coordinate of the point where the wind force is applied. [L]
        Width (input): The exposure width for the wind load applied to the specified
            diaphragm. [L]
        Depth (input): The exposure depth for the wind load applied to the specified
            diaphragm. [L]
        Height (input): The exposure height for the wind load applied to the specified
            diaphragm. [L]
        """
        _r = self._raw.SetExposure_1(Name, Diaph, x, y, Width, Depth, Height)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetExposure_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetIS8751987(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, Terrain: int, Class: int, K1: float, K3: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for Indian IS875-1987. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in meters per second.
        Terrain (input): This is 1, 2, 3 or 4, indicating the terrain category.
        Class (input): This is 1, 2 or 3, indicating the terrain category. 1 = A 2 = B 3 = C
        K1 (input): The risk coefficient (k1 factor).
        K3 (input): The topography factor (k3 factor).
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetIS8751987(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, Terrain, Class, K1, K3, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetIS8751987 falhou (ret={_r})".format(_r=_r))
        return None

    def SetIS8752015(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, TerrainCategory: int, ImportanceFactor: int, k1: float, k3: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for Indian IS875:2015. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern with an Indian IS
            875:2015 auto wind assignment.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in meters per second.
        TerrainCategory (input): This is 1, 2, 3 or 4, indicating the terrain category.
        ImportanceFactor (input): This is 1, 2 or 3, depending on the importance factor. 1 =
            1.00 2 = 1.15 3 = 1.30
        k1 (input): The risk coefficient (k1 factor).
        k3 (input): The topography factor (k3 factor).
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetIS8752015(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, TerrainCategory, ImportanceFactor, k1, k3, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetIS8752015 falhou (ret={_r})".format(_r=_r))
        return None

    def SetMexican(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, UserExposure: bool = False):
        """This function assigns the Mexican auto wind loading parameters. The function returns zero if
        the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in meters per second.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetMexican(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetMexican falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC2005(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, q: float, GustFactor: float, ImportanceFactor: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for NBCC 2005. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        q (input): The velocity pressure in kPa.
        GustFactor (input): The gust effect factor.
        ImportanceFactor (input): The importance factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetNBCC2005(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, q, GustFactor, ImportanceFactor, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetNBCC2005 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC2010_1(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, q: float, GustFactor: float, ImportanceFactor: float, TerrainType: int, CeWindward: float, CeLeeward: float, UserExposure: bool = False):
        """This function retrieves auto wind loading parameters for NBCC 2010. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        q (input): The velocity pressure in kPa.
        GustFactor (input): The gust effect factor.
        ImportanceFactor (input): The importance factor.
        TerrainType (input): This is 1, 2, or 3, indicating the terrain type. 1 = Open 2 =
            Rough 3 = User
        CeWindward (input): The windward exposure factor, Ce. This item applies only when
            TerrainType = 3.
        CeLeeward (input): The windward exposure factor, Ce. This item applies only when
            TerrainType = 3.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetNBCC2010_1(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, q, GustFactor, ImportanceFactor, TerrainType, CeWindward, CeLeeward, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetNBCC2010_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC2015(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, NBCCCase: int, e1: float, e2: float, UserZ: bool, TopZ: float, BottomZ: float, q: float, GustFactor: float, TopographicFactor: float, ImportanceFactor: float, TerrainType: int, CeWindward: float, CeLeeward: float, UserExposure: bool = False):
        """This function retrieves auto wind loading parameters for NBCC 2015. The function returns
        zero if the parameters are successfully assigned; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        NBCCCase (input): This is 1, 2, 3, 4, or 5, indicating the desired case from NBCC
            2105 Figure A-4.1.7.9(1). 1,2,3, and 4 refer to cases 1 through 4 in the figure,
            while 5 means all cases. This item applies only when ExposureFrom = 1.
        e1 (input): This is the value e1 in the NBCC 2015 Figure A-4.1.7.9(1). This item
            applies only when ExposureFrom = 1.
        e2 (input): This is the value e2 in the NBCC 2015 Figure A-4.1.7.9(1). This item
            applies only when ExposureFrom = 1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        q (input): The velocity pressure in kPa.
        GustFactor (input): The gust effect factor, Cg.
        ImportanceFactor (input): The importance Factor, Iw.
        TerrainType (input): This is 1, 2, or 3, indicating the terrain type. 1 = Open 2 =
            Rough 3 = User
        CeWindward (input): The windward exposure factor, Ce. This item applies only when
            TerrainType = 3.
        CeLeeward (input): The windward exposure factor, Ce. This item applies only when
            TerrainType = 3.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetNBCC2015(Name, ExposureFrom, DirAngle, Cpw, Cpl, NBCCCase, e1, e2, UserZ, TopZ, BottomZ, q, GustFactor, TopographicFactor, ImportanceFactor, TerrainType, CeWindward, CeLeeward, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetNBCC2015 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC95(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, q: float, GustFactor: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for NBCC 95. The function returns zero if
        the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        q (input): The velocity pressure in kPa.
        GustFactor (input): The gust effect factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetNBCC95(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, q, GustFactor, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetNBCC95 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNTC2008(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, Vb: float, ExposureCategory: int, ct: float, cd: float, cp: float, UserExposure: bool):
        """This function retrieves auto wind loading parameters for NTC 2008. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        Vb (input): The wind velocity in m/s.
        ExposureCategory (input): This is 1, 2, 3, 4, or 5, indicating the exposure
            category. 1 = I 2 = II 3 = III 4 = IV 5 = V
        ct (input): The topography factor, ct.
        cd (input): The dynamic coefficient, cd.
        cp (input): The shape factor, cp.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetNTC2008(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, Vb, ExposureCategory, ct, cd, cp, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetNTC2008 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNTC2018(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, Vb: float, ExposureCategory: int, ct: float, cd: float, cp: float, UserExposure: bool):
        """This function retrieves auto wind loading parameters for NTC 2018. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is 1 or 2, indicating the source of the wind exposure. 1
            = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cp. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cp. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        Vb (input): The wind velocity in m/s.
        ExposureCategory (input): This is 1, 2, 3, 4, or 5, indicating the exposure
            category. 1 = I 2 = II 3 = III 4 = IV 5 = V
        ct (input): The topography factor, ct.
        cd (input): The dynamic coefficient, cd.
        cp (input): The shape factor, cp.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetNTC2018(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, Vb, ExposureCategory, ct, cd, cp, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetNTC2018 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNone(self, Name: str):
        """This function set the auto wind loading type for the specified load pattern to None. The
        function returns zero if the loading type is successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        """
        _r = self._raw.SetNone(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetNone falhou (ret={_r})".format(_r=_r))
        return None

    def SetUBC94(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, ExposureType: int, ImportanceFactor: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for 1994 UBC. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cq. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cq. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in miles per hour.
        ExposureType (input): This is 1, 2 or 3, indicating the exposure category. 1 = B 2 =
            C 3 = D
        ImportanceFactor (input): The importance factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetUBC94(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, ExposureType, ImportanceFactor, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetUBC94 falhou (ret={_r})".format(_r=_r))
        return None

    def SetUBC97(self, Name: str, ExposureFrom: int, DirAngle: float, Cpw: float, Cpl: float, UserZ: bool, TopZ: float, BottomZ: float, WindSpeed: float, ExposureType: int, ImportanceFactor: float, UserExposure: bool = False):
        """This function assigns auto wind loading parameters for 1997 UBC. The function returns zero
        if the parameters are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern.
        ExposureFrom (input): This is either 1 or 2, indicating the source of the wind
            exposure. 1 = From extents of rigid diaphragms 2 = From area objects
        DirAngle (input): The direction angle for the wind load. This item applies only when
            ExposureFrom = 1.
        Cpw (input): The windward coefficient, Cq. This item applies only when ExposureFrom
            = 1.
        Cpl (input): The leeward coefficient, Cq. This item applies only when ExposureFrom =
            1.
        UserZ (input): This item is True if the top and bottom elevations of the wind load
            are user specified. It is False if the elevations are determined by the program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto wind loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto wind loads are applied. [L]
        WindSpeed (input): The wind speed in miles per hour.
        ExposureType (input): This is 1, 2 or 3, indicating the exposure category. 1 = B 2 =
            C 3 = D
        ImportanceFactor (input): The importance factor.
        UserExposure (input): If this item is True, the wind exposure widths are provided by
            the user. If it is False, the wind exposure widths are calculated by the program
            from the extents of the diaphragms.
        """
        _r = self._raw.SetUBC97(Name, ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, ExposureType, ImportanceFactor, UserExposure)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetUBC97 falhou (ret={_r})".format(_r=_r))
        return None

    def SetUserLoad(self, Name: str, Diaph: str, Fx: float, Fy: float, Mz: float, x: float, y: float):
        """This function assigns auto wind loading parameters for User-type wind loads. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Wind-type load pattern that has an auto wind
            load assigned.
        Diaph (input): The name of an existing special rigid diaphragm constraint, that is,
            a diaphragm constraint with the following features: 1. The constraint type is
            CONSTRAINT_DIAPHRAGM = 2. 2. The constraint coordinate system is Global. 3. The
            constraint axis is Z.
        Fx (input): The global X direction force assigned to the specified diaphragm. [F]
        Fy (input): The global Y direction force assigned to the specified diaphragm. [F]
        Mz (input): The moment about the global Z axis assigned to the specified diaphragm.
            [FL]
        x (input): The global X-coordinate of the point where the wind force is applied. [L]
        y (input): The global Y-coordinate of the point where the wind force is applied. [L]
        """
        _r = self._raw.SetUserLoad(Name, Diaph, Fx, Fy, Mz, x, y)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoWind.SetUserLoad falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadPatterns_AutoSeismic:
    """Wrapper para SapModel.LoadPatterns.AutoSeismic."""

    def __init__(self, raw):
        self._raw = raw

    def GetAS11702007(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the AS 1170 2007 code. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a AS 1170 2007
            auto seismic load assignment.
        DirFlag (output): This is 1 or 2, indicating the seismic load direction. 1 = Global
            X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (output): The code-specified kt factor. This item applies when the PeriodFlag
            item is 1.
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        AS2007SiteClass (output): This is 1, 2, 3, 4 or 5, indicating the site class. 1 = A
            2 = B 3 = C 4 = D 5 = E
        AS2007kp (output): The probability factor, kp.
        AS2007Z (output): The hazard factor, Z.
        AS2007Sp (output): The structural performance factor, Sp.
        AS2007Mu (output): The structural ductility factor, u.
        """
        _r = self._raw.GetAS11702007(Name, 0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetAS11702007 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetBOCA96(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 1996 BOCA code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a BOCA96 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (output): The code-specified CT factor. This item applies when the PeriodFlag
            item is 1 or 2.
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        BOCA96Aa (output): The effective peak acceleration coefficient.
        BOCA96Av (output): The effective peak velocity-related coefficient.
        BOCA96S (output): This is 1, 1.2, 1.5 or 2, indicating the site coefficient.
        BOCA96R (output): The response modification factor.
        """
        _r = self._raw.GetBOCA96(Name, 0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetBOCA96 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetChinese2010(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the Chinese 2010 code. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a Chinese 2010
            auto seismic load assignment.
        DirFlag (output): This is 1, 2 or 3, indicating the seismic load direction. 1 =
            Global X 2 = Global Y 3 = Global Z
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is either 2 or 3, indicating the time period option. 2 =
            Program calculated 3 = User defined
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        JGJ32010AlphaMax (output): The maximum influence factor.
        JGJ32010SI (output): This is 1, 2, 3, 4, 5 or 6, indicating the seismic intensity. 1
            = 6 (0.05g) 2 = 7 (0.10g) 3 = 7 (0.15g) 4 = 8 (0.20g) 5 = 8 (0.30g) 6 = 9
            (0.40g)
        JGJ32010DampRatio (output): The damping ratio.
        JGJ32010Tg (output): The characteristic ground period. [s]
        JGJ32010PTDF (output): The period time discount factor.
        EnhancementFactor (output): The enhancement factor.
        """
        _r = self._raw.GetChinese2010(Name, 0, 0.0, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetChinese2010 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDiaphragmEccentricityOverride(self, Name: str):
        """This function retrieves diaphragm eccentricity overrides for auto seismic loads. This
        function does not apply for User Load type auto seismic loads. The function returns
        zero if the overrides are successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing Quake-type load pattern that has an auto
            seismic load assigned.
        Num (output): The number of diaphragm eccentricity overrides for the specified load
            pattern.
        Diaph (output): This is an array that includes the names of the diaphragms which
            have eccentricity overrides.
        Eccen (output): This is an array that includes the eccentricity applied to each
            diaphragm. [L]
        """
        _r = self._raw.GetDiaphragmEccentricityOverride(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetDiaphragmEccentricityOverride falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetEurocode82004_1(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the Eurocode 8 2004 code. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a Eurocode 8 2004
            auto seismic load assignment.
        DirFlag (output): This is 1 or 2, indicating the seismic load direction. 1 = Global
            X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (output): The code-specified Ct factor. This item applies when the PeriodFlag
            item is 1.
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        EURO2004Country (output): This is 0, 1, 5, 6 or 10 indicating the country for which
            the Nationally Determined Parameters (NDPs) are specified. 0 = Other (NDPs are
            user specified) 1 = CEN Default 5 = Norway 6 = Singapore 10 = Portugal
        EURO2004SpectrumType (output): This is 1 or 2, indicating the spectrum type. 1 =
            Type 1 2 = Type 2 (Does not apply when EURO2004Country = 5 or 6)
        EURO2004GroundType (output): This is 1, 2, 3, 4 or 5, or 6, indicating the ground
            type. 1 = A (Does not apply when EURO2004Country = 6) 2 = B (Does not apply when
            EURO2004Country = 6) 3 = C 4 = D 5 = E (Does not apply when EURO2004Country = 6)
            6 = S1 (Only applies when EURO2004Country = 6)
        EURO2004ag (output): The design ground acceleration in g, ag.
        EURO2004S (output): The soil factor, S.
        EURO2004Tb (output): The lower limit of period of the constant spectral acceleration
            branch, Tb.
        EURO2004Tc (output): The upper limit of period of the constant spectral acceleration
            branch, Tc.
        EURO2004Td (output): The period defining the start of the constant displacement
            range, Td.
        EURO2004Beta (output): The lower bound factor, Beta.
        EURO2004q (output): The behavior factor, q.
        EURO2004Lambda (output): The correction factor, Lambda.
        """
        _r = self._raw.GetEurocode82004_1(Name, 0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetEurocode82004_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIBC2003(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 2003 IBC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a IBC2003 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (output): The code-specified CT factor (ft). This item applies when the
            PeriodFlag item is 1 or 2.
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        IBC2003SG (output): This is 1, 2 or 3, indicating the seismic group. 1 = I 2 = II 3
            = III
        IBC2003SeismicCoeffFlag (output): This is either 1 or 2, indicating the seismic
            coefficient option. 1 = Coefficients are per code 2 = Coefficients are user
            defined
        IBC2003Site (output): This is either 1, 2, 3, 4 or 5, indicating the site class.
            This item is filled only when the IBC2003SeismicCoeffFlag = 1. 1 = A 2 = B 3 = C
            4 = D 5 = E
        IBC2003SS (output): The response acceleration for short periods, (g).
        IBC2003S1 (output): The response acceleration for a one second period, (g).
        IBC2003Fa (output): The site coefficient Fa.
        IBC2003Fv (output): The site coefficient Fv.
        IBC2003R (output): The response modification factor.
        IBC2003Omega (output): The system overstrength factor.
        IBC2003Cd (output): The deflection amplification factor.
        """
        _r = self._raw.GetIBC2003(Name, 0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetIBC2003 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIBC2006(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 2006 IBC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a IBC2006 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        IBC2006CtType (output): This is 0, 1, 2 or 3, indicating the values of Ct and x.
            This item is meaningful when the PeriodFlag item is 1 or 2. 0 = Ct = 0.028 (ft),
            x = 0.8 1 = Ct = 0.016 (ft), x = 0.9 2 = Ct = 0.03 (ft), x = 0.75 3 = Ct = 0.02
            (ft), x = 0.75
        UserT (output): The user specified time period. This item is meaningful when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        IBC2006R (output): The response modification factor.
        IBC2006Omega (output): The system overstrength factor.
        IBC2006Cd (output): The deflection amplification factor.
        IBC2006I (output): The occupancy importance factor.
        IBC2006Option (output): This is 0, 1 or 2, indicating the seismic coefficient
            option. 0 = Ss and S1 from USGS by latitude and longitude 1 = Ss and S1 from
            USGS by zip code 2 = Ss and S1 are user defined
        IBC2006ZipCode (output): The zip code for which the seismic coefficients are
            obtained. This item is meaningful only when IBC2006Option = 1.
        IBC2006TL (output): The long-period transition period. [s]
        IBC2006SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1
            = A 2 = B 3 = C 4 = D 5 = E 6 = F
        """
        _r = self._raw.GetIBC2006(Name, 0, 0.0, 0, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, "", 0.0, 0.0, 0.0, 0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetIBC2006 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIBC2009(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 2009 IBC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a IBC2009 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CtType (output): This is 0, 1, 2 or 3, indicating the values of Ct and x. This item
            is meaningful when the PeriodFlag item is 1 or 2. 0 = Ct = 0.028 (ft), x = 0.8 1
            = Ct = 0.016 (ft), x = 0.9 2 = Ct = 0.03 (ft), x = 0.75 3 = Ct = 0.02 (ft), x =
            0.75
        UserT (output): The user specified time period. This item is meaningful when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        R (output): The response modification factor.
        Omega (output): The system overstrength factor.
        Cd (output): The deflection amplification factor.
        I (output): The occupancy importance factor.
        IBC2009Option (output): This is 0, 1 or 2, indicating the seismic coefficient
            option. 0 = Ss and S1 from USGS by latitude and longitude 1 = Ss and S1 from
            USGS by zip code 2 = Ss and S1 are user defined
        ZipCode (output): The zip code for which the seismic coefficients are obtained. This
            item is meaningful only when IBC2009Option = 1.
        TL (output): The long-period transition period. [s]
        SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        """
        _r = self._raw.GetIBC2009(Name, 0, 0.0, 0, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, "", 0.0, 0.0, 0.0, 0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetIBC2009 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIBC2012(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 2012 IBC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a IBC2012 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CtType (output): This is 0, 1, 2 or 3, indicating the values of Ct and x. This item
            is meaningful when the PeriodFlag item is 1 or 2. 0 = Ct = 0.028 (ft), x = 0.8 1
            = Ct = 0.016 (ft), x = 0.9 2 = Ct = 0.03 (ft), x = 0.75 3 = Ct = 0.02 (ft), x =
            0.75
        UserT (output): The user specified time period. This item is meaningful when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        R (output): The response modification factor.
        Omega (output): The system overstrength factor.
        Cd (output): The deflection amplification factor.
        I (output): The occupancy importance factor.
        IBC2012Option (output): This is 0, 1 or 2, indicating the seismic coefficient
            option. 0 = Ss and S1 from USGS by latitude and longitude 1 = Ss and S1 from
            USGS by zip code 2 = Ss and S1 are user defined
        ZipCode (output): The zip code for which the seismic coefficients are obtained. This
            item is meaningful only when IBC2012Option = 1.
        TL (output): The long-period transition period. [s]
        SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        """
        _r = self._raw.GetIBC2012(Name, 0, 0.0, 0, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, "", 0.0, 0.0, 0.0, 0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetIBC2012 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIS1893_2002(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 2002 IS1893 code. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with an IS1893_2002
            auto seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (output): The code-specified CT factor (m). This item applies when the PeriodFlag
            item is 1.
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        INZFlag (output): This is either 1 or 2, indicating if the seismic zone factor is
            per code or user defined. 1 = Per code 2 = User defined
        INZ (output): The seismic zone factor, Z. If the seismic zone factor is per code
            (INZFlag = 1), this item should be one of the following: 0.10, 0.16, 0.24, 0.36.
        INS (output): This is 1, 2 or 3, indicating the soil type. 1 = I 2 = II 3 = III
        INR (output): The response modification factor.
        """
        _r = self._raw.GetIS1893_2002(Name, 0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0, 0.0, 0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetIS1893_2002 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC2005(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 2005 NBCC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a NBCC2005 auto
            seismic load assignment.
        DirFlag (output): This is 1 or 2, indicating the seismic load direction. 1 = Global
            X 2 = Global Y
        NBCC2005CtType (output): This is 0, 1, 2, 3 or 4, indicating the structure type. 0 =
            Steel moment frame 1 = Concrete moment frame 2 = Other moment frame 3 = Braced
            frame 4 = Shear wall
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 = Code
            2 = Program calculated 3 = User defined
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        NBCC2005PGA (output): The peak ground acceleration.
        NBCC2005S02 (output): The spectral acceleration at a 0.2 second period.
        NBCC2005S05 (output): The spectral acceleration at a 0.52 second period.
        NBCC2005S1 (output): The spectral acceleration at a 1 second period.
        NBCC2005S2 (output): The spectral acceleration at a 2 second period.
        NBCC2005SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1
            = A 2 = B 3 = C 4 = D 5 = E 6 = F
        NBCC2005Fa (output): The site coefficient, Fa.
        NBCC2005Fv (output): The site coefficient, Fv.
        NBCC2005I (output): The importance factor.
        NBCC2005Mv (output): The higher mode factor.
        NBCC2005Rd (output): The ductility modifier.
        NBCC2005Ro (output): The overstrength modifier.
        """
        _r = self._raw.GetNBCC2005(Name, 0, 0.0, 0, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetNBCC2005 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC2010(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 2010 NBCC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a NBCC2010 auto
            seismic load assignment.
        DirFlag (output): This is 1 or 2, indicating the seismic load direction. 1 = Global
            X 2 = Global Y
        CtType (output): This is 0, 1, 2, 3 or 4, indicating the structure type. 0 = Steel
            moment frame 1 = Concrete moment frame 2 = Other moment frame 3 = Braced frame 4
            = Shear wall
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 = Code
            2 = Program calculated 3 = User defined
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        PGA (output): The peak ground acceleration.
        S02 (output): The spectral acceleration at a 0.2 second period.
        S05 (output): The spectral acceleration at a 0.5 second period.
        S1 (output): The spectral acceleration at a 1 second period.
        S2 (output): The spectral acceleration at a 2 second period.
        S4 (output): The spectral acceleration at a 4 second period.
        SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        Fa (output): The site coefficient, Fa.
        Fv (output): The site coefficient, Fv.
        I (output): The importance factor.
        Mv (output): The higher mode factor.
        Rd (output): The ductility modifier.
        Ro (output): The overstrength modifier.
        """
        _r = self._raw.GetNBCC2010(Name, 0, 0.0, 0, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetNBCC2010 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC2015(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 2015 NBCC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a NBCC2015 auto
            seismic load assignment.
        DirFlag (output): This is 1 or 2, indicating the seismic load direction. 1 = Global
            X 2 = Global Y
        CtType (output): This is 0, 1, 2, 3 or 4, indicating the structure type. 0 = Steel
            moment frame 1 = Concrete moment frame 2 = Other moment frame 3 = Braced frame 4
            = Shear wall
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 = Code
            2 = Program calculated 3 = User defined
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        PGA (output): The peak ground acceleration.
        S02 (output): The spectral acceleration at a 0.2 second period.
        S05 (output): The spectral acceleration at a 0.5 second period.
        S1 (output): The spectral acceleration at a 1 second period.
        S2 (output): The spectral acceleration at a 2 second period.
        S5 (output): The spectral acceleration at a 5 second period.
        S10 (output): The spectral acceleration at a 10 second period.
        SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        F02 (output): The site coefficient at a 0.2 second period. This item is read when
            the site class is F only.
        F05 (output): The site coefficient at a 0.5 second period. This item is read when
            the site class is F only.
        F1 (output): The site coefficient at a 1 second period. This item is read when the
            site class is F only.
        F2 (output): The site coefficient at a 2 second period. This item is read when the
            site class is F only.
        F5 (output): The site coefficient at a 5 second period. This item is read when the
            site class is F only.
        F10 (output): The site coefficient at a 10 second period. This item is read when the
            site class is F only.
        I (output): The importance factor.
        Mv (output): The higher mode factor.
        Rd (output): The ductility modifier.
        Ro (output): The overstrength modifier.
        """
        _r = self._raw.GetNBCC2015(Name, 0, 0.0, 0, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetNBCC2015 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC95(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 1995 NBCC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a NBCC95 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        NBCCPFlag (output): This is either 1 or 2, indicating the structure type. 1 = Moment
            frame 2 = Other
        NBCC95DS (output): This item applies only when the NBCCPFlag = 2. It is the
            dimension of the lateral load resisting system in the direction of the applied
            forces. [L]
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 = Code
            2 = Program calculated 3 = User defined
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        NBCC95ZA (output): This is 0, 1, 2, 3, 4, 5 or 6, indicating the acceleration
            related zone, Za.
        NBCC95ZV (output): This is 0, 1, 2, 3, 4, 5 or 6, indicating the velocity related
            zone, Zv.
        NBCC95ZVFlag (output): This is either 1 or 2, indicating how the zonal velocity
            ratio, V, is specified. 1 = From code based on Zv 2 = User specified
        NBCC95ZVR (output): The zonal velocity ratio, V.
        NBCC95I (output): The importance factor.
        NBCC95F (output): The foundation factor.
        NBCC95R (output): The force modification factor.
        """
        _r = self._raw.GetNBCC95(Name, 0, 0.0, 0, 0.0, 0, 0.0, UserZ, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetNBCC95 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNEHRP97(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 1997 NEHRP code. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a NEHRP97 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (output): The code-specified CT factor. This item applies when the PeriodFlag
            item is 1 or 2.
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        NEHRP97SG (output): This is 1, 2 or 3, indicating the seismic group. 1 = I 2 = II 3
            = III
        NEHRP97SeismicCoeffFlag (output): This is 1 or 2, indicating the seismic coefficient
            option. 1 = Coefficients are per code 2 = Coefficients are user defined
        NEHRP97Site (output): This is 1, 2, 3, 4 or 5, indicating the site class. This item
            is only filled when the NEHRP97SeismicCoeffFlag = 1. 1 = A 2 = B 3 = C 4 = D 5 =
            E
        NEHRP97SS (output): The response acceleration for short periods, (g).
        NEHRP97S1 (output): The response acceleration for a one second period, (g).
        NEHRP97Fa (output): The site coefficient Fa.
        NEHRP97Fv (output): The site coefficient Fv.
        NEHRP97R (output): The response modification factor.
        """
        _r = self._raw.GetNEHRP97(Name, 0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetNEHRP97 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNTC2008(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the NTC 2008 code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a NTC 2008 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        UserT (output): The user specified time period. This item is meaningful when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        ParamsOption (output): This is 1, 2, or 3, indicating the option for defining the
            parameters. 1 = by latitude and longitude 2 = by island 3 = user specified
        Island (output): This is one of the following values. This item is used only when
            ParamsOption = 2. 1 = Alicudi 2 = Arcipelago Toscano 3 = Filcudi 4 = Isole Egadi
            5 = Lampedusa 6 = Linosa 7 = Lipari 8 = Palmarola 9 = Panarea 1 0 = Pantelleria
            11 = Ponza 12 = Salina 13 = Santo Stefano 14 = Sardegna 15 = Stromboli 16 =
            Tremiti 17 = Ustica 18 = Ventotene 19 = Vulcano 20 = Zannone
        LimitState (output): This is 1, 2, 3, or 4, indicating the limit state. 1 = SLO 2 =
            SLD 3 = SLV 4 = SLC
        UsageClass (output): This is 1, 2, 3, or 4, indicating the usage class. 1 = I 2 = II
            3 = III 4 = IV
        NomLife (output): The nominal life to be considered.
        PeakAccel (output): The peak ground acceleration, ag/g.
        F0 (output): The magnitude factor, F0.
        Tcs (output): The reference period, Tc* [s].
        SpecType (output): This is 1, 2, 3, or 4, indicating the type of spectrum to
            consider. 1 = Elastic horizontal 2 = Elastic vertical 3 = Design horizontal 4 =
            Design vertical
        SoilType (output): This is 1, 2, 3, 4, or 5, indicating the subsoil type. 1 = A 2 =
            B 3 = C 4 = D 5 = E
        Topography (output): This is 1, 2, 3, or 4, indicating the topography type. 1 = T1 2
            = T2 3 = T3 4 = T4
        hRatio (output): The ratio for the site altitude at the base of the hill to the
            height of the hill.
        Damping (output): The damping, in percent. This is only applicable for SpecType 1
            and 2.
        q (output): The behavior correction factor. This is only applicable for SpecType 3
            and 4.
        lambda (output): A correction factor.
        """
        _r = self._raw.GetNTC2008(Name, 0, 0.0, 0, 0, 0.0, UserZ, 0.0, 0.0, 0, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetNTC2008 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNTC2018(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the NTC 2018 code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a NTC 2018 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        UserT (output): The user specified time period. This item is meaningful when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        ParamsOption (output): This is 1, 2, or 3, indicating the option for defining the
            parameters. 1 = by latitude and longitude 2 = by island 3 = user specified
        Island (output): This is one of the following values. This item is used only when
            ParamsOption = 2. 1 = Alicudi 2 = Arcipelago Toscano 3 = Filcudi 4 = Isole Egadi
            5 = Lampedusa 6 = Linosa 7 = Lipari 8 = Palmarola 9 = Panarea 1 0 = Pantelleria
            11 = Ponza 12 = Salina 13 = Santo Stefano 14 = Sardegna 15 = Stromboli 16 =
            Tremiti 17 = Ustica 18 = Ventotene 19 = Vulcano 20 = Zannone
        LimitState (output): This is 1, 2, 3, or 4, indicating the limit state. 1 = SLO 2 =
            SLD 3 = SLV 4 = SLC
        UsageClass (output): This is 1, 2, 3, or 4, indicating the usage class. 1 = I 2 = II
            3 = III 4 = IV
        NomLife (output): The nominal life to be considered.
        PeakAccel (output): The peak ground acceleration, ag/g.
        F0 (output): The magnitude factor, F0.
        Tcs (output): The reference period, Tc* [s].
        SpecType (output): This is 1, 2, 3, or 4, indicating the type of spectrum to
            consider. 1 = Elastic horizontal 2 = Elastic vertical 3 = Design horizontal 4 =
            Design vertical
        SoilType (output): This is 1, 2, 3, 4, or 5, indicating the subsoil type. 1 = A 2 =
            B 3 = C 4 = D 5 = E
        Topography (output): This is 1, 2, 3, or 4, indicating the topography type. 1 = T1 2
            = T2 3 = T3 4 = T4
        hRatio (output): The ratio for the site altitude at the base of the hill to the
            height of the hill.
        Damping (output): The damping, in percent. This is only applicable for SpecType 1
            and 2.
        q (output): The behavior correction factor. This is only applicable for SpecType 3
            and 4.
        lambda (output): A correction factor.
        """
        _r = self._raw.GetNTC2018(Name, 0, 0.0, 0, 0.0, UserZ, 0.0, 0.0, 0, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetNTC2018 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNZS11702004(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the NZS 1170 2004 code. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a NZS 1170 2004
            auto seismic load assignment.
        DirFlag (output): This is 1 or 2, indicating the seismic load direction. 1 = Global
            X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        NZS2004SiteClass (output): This is 1, 2, 3, 4 or 5, indicating the site class. 1 = A
            2 = B 3 = C 4 = D 5 = E
        NZS2004Z (output): The hazard factor, Z.
        NZS2004R (output): The return period factor, R.
        NZS2004DIST (output): Distance to the fault in km, used to calculate the near fault
            factor..
        NZS2004Sp (output): The structural performance factor, Sp.
        NZS2004Mu (output): The structural ductility factor, u.
        """
        _r = self._raw.GetNZS11702004(Name, 0, 0.0, 0, 0.0, UserZ, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetNZS11702004 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUBC94(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 1994 UBC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a UBC94 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (output): The code-specified CT factor. This item applies when the PeriodFlag
            item is 1 or 2.
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        UBC94ZFlag (output): This is 1 or 2, indicating if the seismic zone factor is per
            code or user defined. 1 = Per code 2 = User defined
        UBC94Z (output): The seismic zone factor, Z. If the seismic zone factor is per code
            (UBC94ZFlag = 1), this item should be one of the following: 0.075, 0.15, 0.20,
            0.30, 0.40.
        UBC94S (output): This is 1, 1.2, 1.5 or 2, indicating the site coefficient.
        UBC94I (output): The importance factor.
        UBC94RW (output): The numerical coefficient, Rw.
        """
        _r = self._raw.GetUBC94(Name, 0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetUBC94 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUBC97Iso(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for seismically isolated buildings
        using the 1997 UBC code. The function returns zero if the parameters are
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a UBC97Iso auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        UBC97IsoSeismicCoeffFlag (output): This is either 1 or 2, indicating if the seismic
            coefficient Cv is per code or user defined. 1 = Per code 2 = User defined
        UBC97IsoSoilProfileType (output): This is 1, 2, 3, 4 or 5, indicating the soil
            profile type. 1 = SA 2 = SB 3 = SC 4 = SD 5 = SE This item is applicable only
            when the seismic coefficients Ca and Cv are calculated per code
            (UBC97SeismicCoeffFlag = 1).
        UBC97IsoZ (output): This is 0.075, 0.15, 0.2, 0.3 or 0.4, indicating the seismic
            zone factor. This item is applicable only when the seismic coefficient Cv is
            calculated per code (UBC97IsoSeismicCoeffFlag = 1).
        UBC97IsoCv (output): The seismic coefficient, Cv.
        UBC97IsoNearSourceFlag (output): This is either 1 or 2, indicating if the near
            source factor coefficient Nv is per code or user defined. 1 = Per code 2 = User
            defined This item is applicable only when the seismic coefficient Cv is
            calculated per code (UBC97IsoSeismicCoeffFlag = 1) and UBC97IsoZ = 0.4.
        UBC97IsoSourceType (output): This is 1, 2 or 3, indicating the seismic source type.
            1 = A 2 = B 3 = C This item is applicable only when the seismic coefficient Cv
            is calculated per code (UBC97IsoSeismicCoeffFlag = 1), UBC97IsoZ = 0.4, and the
            near source factor coefficient Nv is calculated per code (UBC97IsoNearSourceFlag
            = 1).
        UBC97IsoDist (output): This is the distance to the seismic source in kilometers.
            This item is applicable only when the seismic coefficient Cv is calculated per
            code (UBC97IsoSeismicCoeffFlag = 1), UBC97IsoZ = 0.4, and the near source factor
            coefficient Nv is calculated per code (UBC97IsoNearSourceFlag = 1).
        UBC97IsoNv (output): The near source factor coefficient, Nv. This item is applicable
            only when the seismic coefficient Cv is user defined (UBC97IsoSeismicCoeffFlag =
            2).
        UBC97IsoRI (output): The overstrength factor, Ri.
        UBC97IsoBD (output): The coefficient for damping.
        UBC97IsoKDmax (output): The maximum effective stiffness of the isolation system.
            [F/L]
        UBC97IsoKDmin (output): The minimum effective stiffness of the isolation system.
            [F/L]
        """
        _r = self._raw.GetUBC97Iso(Name, 0, 0.0, UserZ, 0.0, 0.0, 0, 0, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetUBC97Iso falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUBC97(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for the 1997 UBC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a UBC97 auto
            seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (output): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (output): The code-specified CT factor. This item applies when the PeriodFlag
            item is 1 or 2.
        UserT (output): The user specified time period. This item applies when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        UBC97SeismicCoeffFlag (output): This is either 1 or 2, indicating if the seismic
            coefficients Ca and Cv are per code or user defined. 1 = Per code 2 = User
            defined
        UBC97SoilProfileType (output): This is 1, 2, 3, 4 or 5, indicating the soil profile
            type. 1 = SA 2 = SB 3 = SC 4 = SD 5 = SE This item is applicable only when the
            seismic coefficients Ca and Cv are calculated per code (UBC97SeismicCoeffFlag =
            1).
        UBC97Z (output): This is 0.075, 0.15, 0.2, 0.3 or 0.4, indicating the seismic zone
            factor. This item is applicable only when the seismic coefficients Ca and Cv are
            calculated in accordance with code (UBC97SeismicCoeffFlag = 1).
        UBC97Ca (output): The seismic coefficient, Ca.
        UBC97Cv (output): The seismic coefficient, Cv.
        UBC97NearSourceFlag (output): This is 1 or 2, indicating if the near source factor
            coefficients Na and Nv are per code or user defined. 1 = Per code 2 = User
            defined This item is applicable only when the seismic coefficients Ca and Cv are
            calculated per code (UBC97SeismicCoeffFlag = 1) and UBC97Z = 0.4.
        UBC97SourceType (output): This is 1, 2 or 3, indicating the seismic source type. 1 =
            A 2 = B 3 = C This item is applicable only when the seismic coefficients Ca and
            Cv are calculated per code (UBC97SeismicCoeffFlag = 1), UBC97Z = 0.4, and the
            near source factor coefficients Na and Nv are calculated per code
            (UBC97NearSourceFlag = 1).
        UBC97Dist (output): This is the distance to the seismic source in kilometers. This
            item is only applicable when the seismic coefficients Ca and Cv are calculated
            per code (UBC97SeismicCoeffFlag = 1), UBC97Z = 0.4, and the near source factor
            coefficients Na and Nv are calculated per code (UBC97NearSourceFlag = 1).
        UBC97Na (output): The near source factor coefficient, Na. This item is applicable
            only when the seismic coefficients Ca and Cv are user defined
            (UBC97SeismicCoeffFlag = 2).
        UBC97Nv (output): The near source factor coefficient, Nv. This item is applicable
            only when the seismic coefficients Ca and Cv are user defined
            (UBC97SeismicCoeffFlag = 2).
        UBC97I (output): The importance factor.
        UBC97R (output): The overstrength factor.
        """
        _r = self._raw.GetUBC97(Name, 0, 0.0, 0, 0.0, 0.0, UserZ, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetUBC97 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUserCoefficient(self, Name: str, UserZ: bool):
        """This function retrieves auto seismic loading parameters for User Coefficient type loading.
        The function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a User
            Coefficient auto seismic load assignment.
        DirFlag (output): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (output): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (output): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        c (output): The base shear coefficient.
        k (output): The building height exponent.
        """
        _r = self._raw.GetUserCoefficient(Name, 0, 0.0, UserZ, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetBOCA96 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUserLoad(self, Name: str, Fx: list[float], Fy: list[float]):
        """This function retrieves auto seismic loading parameters for User Load type auto seismic
        loads. The function returns zero if the parameters are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern which has been
            assigned a User Load auto seismic type.
        MyType (output): This is either 1 or 2, indicating the application point type for
            the user load. 1 = User specified application point 2 = At center of mass with
            optional additional eccentricity
        Eccen (output): The eccentricity ratio that applies to all diaphragms. This item is
            only applicable when MyType = 2.
        Num (output): The number of diaphragms that can be loaded by the auto seismic load.
        Diaph (output): This is an array that includes the names of the diaphragms that can
            be loaded by the auto seismic load.
        Fx (input): This is an array that includes the global X direction force assigned to
            each diaphragm. [F]
        Fy (input): This is an array that includes the global Y direction force assigned to
            each diaphragm. [F]
        Mz (output): This is an array that includes the moment about the global Z axis for
            each diaphragm. [FL]
        x (output): This is an array that includes the global X-coordinate of the point
            where the seismic force is applied to each diaphragm. [L] This item is
            applicable only when MyType = 1.
        y (output): This is an array that includes the global Y-coordinate of the point
            where the seismic force is applied to each diaphragm. [L] This item is
            applicable only when MyType = 1.
        """
        _r = self._raw.GetUserLoad(Name, 0, 0.0, 0, [], Fx, Fy, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.GetUserLoad falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetAS11702007(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CT: float, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, AS2007SiteClass: int, AS2007kp: float, AS2007Z: float, AS2007Sp: float, AS2007Mu: float):
        """This function assigns auto seismic loading parameters for the AS 1170.4 2007 code. The
        function returns zero if the parameters are successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is 1 or 2, indicating the seismic load direction. 1 = Global X
            2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (input): The code-specified kt factor. This item applies when the PeriodFlag item
            is 1.
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        AS2007SiteClass (input): This is 1, 2, 3, 4 or 5, indicating the site class. 1 = A 2
            = B 3 = C 4 = D 5 = E
        AS2007kp (input): The probability factor, kp.
        AS2007Z (input): The hazard factor, Z.
        AS2007Sp (input): The structural performance factor, Sp.
        AS2007Mu (input): The structural ductility factor, u.
        """
        _r = self._raw.SetAS11702007(Name, DirFlag, Eccen, PeriodFlag, CT, UserT, UserZ, TopZ, BottomZ, AS2007SiteClass, AS2007kp, AS2007Z, AS2007Sp, AS2007Mu)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetAS11702007 falhou (ret={_r})".format(_r=_r))
        return None

    def SetBOCA96(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CT: float, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, BOCA96Aa: float, BOCA96Av: float, BOCA96S: float, BOCA96R: float):
        """This function assigns auto seismic loading parameters for the 1996 BOCA code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (input): The code-specified CT factor. This item applies when the PeriodFlag item
            is 1 or 2.
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        BOCA96Aa (input): The effective peak acceleration coefficient.
        BOCA96Av (input): The effective peak velocity-related coefficient.
        BOCA96S (input): This is 1, 1.2, 1.5 or 2, indicating the site coefficient.
        BOCA96R (input): The response modification factor.
        """
        _r = self._raw.SetBOCA96(Name, DirFlag, Eccen, PeriodFlag, CT, UserT, UserZ, TopZ, BottomZ, BOCA96Aa, BOCA96Av, BOCA96S, BOCA96R)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetBOCA96 falhou (ret={_r})".format(_r=_r))
        return None

    def SetChinese2010(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, JGJ32010AlphaMax: float, JGJ32010SI: int, JGJ32010DampRatio: float, JGJ32010Tg: float, JGJ32010PTDF: float, EnhancementFactor: float):
        """This function assigns auto seismic loading parameters for the Chinese 2010 code. The
        function returns zero if the parameters are successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is 1, 2 or 3, indicating the seismic load direction. 1 =
            Global X 2 = Global Y 3 = Global Z
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is either 2 or 3, indicating the time period option. 2 =
            Program calculated 3 = User defined
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        JGJ32010AlphaMax (input): The maximum influence factor.
        JGJ32010SI (input): This is 1, 2, 3, 4, 5 or 6, indicating the seismic intensity. 1
            = 6 (0.05g) 2 = 7 (0.10g) 3 = 7 (0.15g) 4 = 8 (0.20g) 5 = 8 (0.30g) 6 = 9
            (0.40g)
        JGJ32010DampRatio (input): The damping ratio.
        JGJ32010Tg (input): The characteristic ground period. [s]
        JGJ32010PTDF (input): The period time discount factor.
        EnhancementFactor (input): The enhancement factor.
        """
        _r = self._raw.SetChinese2010(Name, DirFlag, Eccen, PeriodFlag, UserT, UserZ, TopZ, BottomZ, JGJ32010AlphaMax, JGJ32010SI, JGJ32010DampRatio, JGJ32010Tg, JGJ32010PTDF, EnhancementFactor)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetChinese2010 falhou (ret={_r})".format(_r=_r))
        return None

    def SetDiaphragmEccentricityOverride(self, Name: str, Diaph: str, Eccen: float, Delete: bool = False):
        """This function assigns diaphragm eccentricity overrides for auto seismic loads. This function
        does not apply for User Load type auto seismic loads. The function returns zero if
        the overrides are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern that has an auto
            seismic load assigned.
        Diaph (input): The name of an existing special rigid diaphragm constraint, that is,
            a diaphragm constraint with the following features: 1. The constraint type is
            CONSTRAINT_DIAPHRAGM = 2. 2. The constraint coordinate system is Global. 3. The
            constraint axis is Z.
        Eccen (input): The eccentricity applied to the specified diaphragm. [L]
        Delete (input): If this item is True, the eccentricity override for the specified
            diaphragm is deleted.
        """
        _r = self._raw.SetDiaphragmEccentricityOverride(Name, Diaph, Eccen, Delete)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetDiaphragmEccentricityOverride falhou (ret={_r})".format(_r=_r))
        return None

    def SetEurocode82004_1(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CT: float, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, EURO2004Country: int, EURO2004SpectrumType: int, EURO2004GroundType: int, EURO2004ag: float, EURO2004S: float, EURO2004Tb: float, EURO2004Tc: float, EURO2004Td: float, EURO2004Beta: float, EURO2004q: float, EURO2004Lambda: float):
        """This function assigns auto seismic loading parameters for the Eurocode 8 2004 code. The
        function returns zero if the parameters are successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is 1 or 2, indicating the seismic load direction. 1 = Global X
            2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (input): The code-specified Ct factor. This item applies when the PeriodFlag item
            is 1.
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3.[s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        EURO2004Country (input): This is 0, 1, 5, 6, or 10 indicating the country for which
            the Nationally Determined Parameters (NDPs) are specified. 0 = Other (NDPs are
            user specified) 1 = CEN Default 5 = Norway 6 = Singapore 10 = Portugal
        EURO2004SpectrumType (input): This is 1 or 2, indicating the spectrum type. 1 = Type
            1 2 = Type 2 (Does not apply when EURO2004Country = 6)
        EURO2004GroundType (input): This is 1, 2, 3, 4, 5, or 6, indicating the ground type.
            1 = A (Does not apply when EURO2004Country = 6) 2 = B (Does not apply when
            EURO2004Country = 6) 3 = C 4 = D 5 = E (Does not apply when EURO2004Country = 6)
            6 = S1 (Only applies when EURO2004Country = 6)
        EURO2004ag (input): The design ground acceleration in g, ag.
        EURO2004S (input): The soil factor, S. If the EURO2004Country item is not 0, the
            input value for this item is ignored.
        EURO2004Tb (input): The lower limit of period of the constant spectral acceleration
            branch, Tb. If the EURO2004Country item is not 0, the input value for this item
            is ignored.
        EURO2004Tc (input): The upper limit of period of the constant spectral acceleration
            branch, Tc. If the EURO2004Country item is not 0, the input value for this item
            is ignored.
        EURO2004Td (input): The period defining the start of the constant displacement
            range, Td. If the EURO2004Country item is not 0, the input value for this item
            is ignored.
        EURO2004Beta (input): The lower bound factor, Beta. If the EURO2004Country item is
            not 0, the input value for this item is ignored.
        EURO2004q (input): The behavior factor, q.
        EURO2004Lambda (input): The correction factor, Lambda.
        """
        _r = self._raw.SetEurocode82004_1(Name, DirFlag, Eccen, PeriodFlag, CT, UserT, UserZ, TopZ, BottomZ, EURO2004Country, EURO2004SpectrumType, EURO2004GroundType, EURO2004ag, EURO2004S, EURO2004Tb, EURO2004Tc, EURO2004Td, EURO2004Beta, EURO2004q, EURO2004Lambda)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetEurocode82004_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetIBC2003(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CT: float, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, IBC2003SG: int, IBC2003SeismicCoeffFlag: int, IBC2003Site: int, IBC2003SS: float, IBC2003S1: float, IBC2003Fa: float, IBC2003Fv: float, IBC2003R: float, IBC2003Omega: float, IBC2003Cd: float):
        """This function assigns auto seismic loading parameters for the 2003 IBC code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (input): The code-specified CT factor (ft). This item applies when the PeriodFlag
            item is 1 or 2.
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        IBC2003SG (input): This is 1, 2 or 3, indicating the seismic group. 1 = I 2 = II 3 =
            III
        IBC2003SeismicCoeffFlag (input): This is either 1 or 2, indicating the seismic
            coefficient option. 1 = Coefficients are per code 2 = Coefficients are user
            defined
        IBC2003Site (input): This is 1, 2, 3, 4 or 5, indicating the site class. This item
            is only used when the IBC2003SeismicCoeffFlag = 1. 1 = A 2 = B 3 = C 4 = D 5 = E
        IBC2003SS (input): The response acceleration for short periods, (g).
        IBC2003S1 (input): The response acceleration for a one second period, (g).
        IBC2003Fa (input): The site coefficient Fa. This item is used only when the
            IBC2003SeismicCoeffFlag = 2.
        IBC2003Fv (input): The site coefficient Fv. This item is used only when the
            IBC2003SeismicCoeffFlag = 2
        IBC2003R (input): The response modification factor.
        IBC2003Omega (input): The system overstrength factor.
        IBC2003Cd (input): The deflection amplification factor.
        """
        _r = self._raw.SetIBC2003(Name, DirFlag, Eccen, PeriodFlag, CT, UserT, UserZ, TopZ, BottomZ, IBC2003SG, IBC2003SeismicCoeffFlag, IBC2003Site, IBC2003SS, IBC2003S1, IBC2003Fa, IBC2003Fv, IBC2003R, IBC2003Omega, IBC2003Cd)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetIBC2003 falhou (ret={_r})".format(_r=_r))
        return None

    def SetIBC2006(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, IBC2006CtType: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, IBC2006R: float, IBC2006Omega: float, IBC2006Cd: float, IBC2006I: float, IBC2006Option: int, IBC2006Latitude: float, IBC2006Longitude: float, IBC2006ZipCode: str, IBC2006SS: float, IBC2006S1: float, IBC2006TL: float, IBC2006SiteClass: int, IBC2006Fa: float, IBC2006Fv: float):
        """This function assigns auto seismic loading parameters for the 2006 IBC code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        IBC2006CtType (input): This is 0, 1, 2 or 3, indicating the values of Ct and x. This
            item applies when the PeriodFlag item is 1 or 2. 0 = Ct = 0.028 (ft), x = 0.8 1
            = Ct = 0.016 (ft), x = 0.9 2 = Ct = 0.03 (ft), x = 0.75 3 = Ct = 0.02 (ft), x =
            0.75
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        IBC2006R (input): The response modification factor.
        IBC2006Omega (input): The system overstrength factor.
        IBC2006Cd (input): The deflection amplification factor.
        IBC2006I (input): The occupancy importance factor.
        IBC2006Option (input): This is 0, 1 or 2, indicating the seismic coefficient option.
            0 = Ss and S1 from USGS by latitude and longitude 1 = Ss and S1 from USGS by zip
            code 2 = Ss and S1 are user defined
        IBC2006ZipCode (input): The zip code for which the seismic coefficients are
            obtained. This item is used only when IBC2006Option = 1.
        IBC2006TL (input): The long-period transition period. [s]
        IBC2006SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 =
            A 2 = B 3 = C 4 = D 5 = E 6 = F
        """
        _r = self._raw.SetIBC2006(Name, DirFlag, Eccen, PeriodFlag, IBC2006CtType, UserT, UserZ, TopZ, BottomZ, IBC2006R, IBC2006Omega, IBC2006Cd, IBC2006I, IBC2006Option, IBC2006Latitude, IBC2006Longitude, IBC2006ZipCode, IBC2006SS, IBC2006S1, IBC2006TL, IBC2006SiteClass, IBC2006Fa, IBC2006Fv)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetIBC2006 falhou (ret={_r})".format(_r=_r))
        return None

    def SetIBC2009(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CtType: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, R: float, Omega: float, Cd: float, I: float, IBC2009Option: int, Latitude: float, Longitude: float, ZipCode: str, SS: float, S1: float, TL: float, SiteClass: int, Fa: float, Fv: float):
        """This function assigns auto seismic loading parameters for the 2009 IBC code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CtType (input): This is 0, 1, 2 or 3, indicating the values of Ct and x. This item
            applies when the PeriodFlag item is 1 or 2. 0 = Ct = 0.028 (ft), x = 0.8 1 = Ct
            = 0.016 (ft), x = 0.9 2 = Ct = 0.03 (ft), x = 0.75 3 = Ct = 0.02 (ft), x = 0.75
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        R (input): The response modification factor.
        Omega (input): The system overstrength factor.
        Cd (input): The deflection amplification factor.
        I (input): The occupancy importance factor.
        IBC2009Option (input): This is 0, 1 or 2, indicating the seismic coefficient option.
            0 = Ss and S1 from USGS by latitude and longitude 1 = Ss and S1 from USGS by zip
            code 2 = Ss and S1 are user defined
        ZipCode (input): The zip code for which the seismic coefficients are obtained. This
            item is used only when IBC2009Option = 1.
        TL (input): The long-period transition period. [s]
        SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        """
        _r = self._raw.SetIBC2009(Name, DirFlag, Eccen, PeriodFlag, CtType, UserT, UserZ, TopZ, BottomZ, R, Omega, Cd, I, IBC2009Option, Latitude, Longitude, ZipCode, SS, S1, TL, SiteClass, Fa, Fv)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetIBC2009 falhou (ret={_r})".format(_r=_r))
        return None

    def SetIBC2012(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CtType: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, R: float, Omega: float, Cd: float, I: float, IBC2012Option: int, Latitude: float, Longitude: float, ZipCode: str, SS: float, S1: float, TL: float, SiteClass: int, Fa: float, Fv: float):
        """This function assigns auto seismic loading parameters for the 2012 IBC code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CtType (input): This is 0, 1, 2 or 3, indicating the values of Ct and x. This item
            applies when the PeriodFlag item is 1 or 2. 0 = Ct = 0.028 (ft), x = 0.8 1 = Ct
            = 0.016 (ft), x = 0.9 2 = Ct = 0.03 (ft), x = 0.75 3 = Ct = 0.02 (ft), x = 0.75
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        R (input): The response modification factor.
        Omega (input): The system overstrength factor.
        Cd (input): The deflection amplification factor.
        I (input): The occupancy importance factor.
        IBC2012Option (input): This is 0, 1 or 2, indicating the seismic coefficient option.
            0 = Ss and S1 from USGS by latitude and longitude 1 = Ss and S1 from USGS by zip
            code 2 = Ss and S1 are user defined
        ZipCode (input): The zip code for which the seismic coefficients are obtained. This
            item is used only when IBC2012Option = 1.
        TL (input): The long-period transition period. [s]
        SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        """
        _r = self._raw.SetIBC2012(Name, DirFlag, Eccen, PeriodFlag, CtType, UserT, UserZ, TopZ, BottomZ, R, Omega, Cd, I, IBC2012Option, Latitude, Longitude, ZipCode, SS, S1, TL, SiteClass, Fa, Fv)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetIBC2012 falhou (ret={_r})".format(_r=_r))
        return None

    def SetIS1893_2002(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CT: float, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, INZFlag: int, INZ: float, INS: int, INI: float, INR: float):
        """This function assigns auto seismic loading parameters for the 2002 IS1893 code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (input): The code-specified CT factor (m). This item applies when the PeriodFlag
            item is 1.
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        INZFlag (input): This is either 1 or 2, indicating if the seismic zone factor is per
            code or user defined. 1 = Per code 2 = User defined
        INZ (input): The seismic zone factor, Z. If the seismic zone factor is per code
            (INZFlag = 1), this item should be one of the following: 0.10, 0.16, 0.24, 0.36.
        INS (input): This is 1, 2 or 3, indicating the soil type. 1 = I 2 = II 3 = III
        INR (input): The response modification factor.
        """
        _r = self._raw.SetIS1893_2002(Name, DirFlag, Eccen, PeriodFlag, CT, UserT, UserZ, TopZ, BottomZ, INZFlag, INZ, INS, INI, INR)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetIS1893_2002 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC2005(self, Name: str, DirFlag: int, eccen: float, NBCC2005CtType: int, PeriodFlag: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, NBCC2005PGA: float, NBCC2005S02: float, NBCC2005S05: float, NBCC2005S1: float, NBCC2005S2: float, NBCC2005SiteClass: int, NBCC2005Fa: float, NBCC2005Fv: float, NBCC2005I: float, NBCC2005Mv: float, NBCC2005Rd: float, NBCC2005Ro: float):
        """This function assigns auto seismic loading parameters for the 2005 NBCC code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is 1 or 2, indicating the seismic load direction. 1 = Global X
            2 = Global Y
        NBCC2005CtType (input): This is 0, 1, 2, 3 or 4, indicating the structure type. 0 =
            Steel moment frame 1 = Concrete moment frame 2 = Other moment frame 3 = Braced
            frame 4 = Shear wall
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 = Code 2
            = Program calculated 3 = User defined
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        NBCC2005PGA (input): The peak ground acceleration.
        NBCC2005S02 (input): The spectral acceleration at a 0.2 second period.
        NBCC2005S05 (input): The spectral acceleration at a 0.52 second period.
        NBCC2005S1 (input): The spectral acceleration at a 1 second period.
        NBCC2005S2 (input): The spectral acceleration at a 2 second period.
        NBCC2005SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1
            = A 2 = B 3 = C 4 = D 5 = E 6 = F
        NBCC2005Fa (input): The site coefficient, Fa. This item is read when the site class
            is F only.
        NBCC2005Fv (input): The site coefficient, Fv. This item is read when the site class
            is F only.
        NBCC2005I (input): The importance factor.
        NBCC2005Mv (input): The higher mode factor.
        NBCC2005Rd (input): The ductility modifier.
        NBCC2005Ro (input): The overstrength modifier.
        """
        _r = self._raw.SetNBCC2005(Name, DirFlag, eccen, NBCC2005CtType, PeriodFlag, UserT, UserZ, TopZ, BottomZ, NBCC2005PGA, NBCC2005S02, NBCC2005S05, NBCC2005S1, NBCC2005S2, NBCC2005SiteClass, NBCC2005Fa, NBCC2005Fv, NBCC2005I, NBCC2005Mv, NBCC2005Rd, NBCC2005Ro)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetNBCC2005 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC2010(self, Name: str, DirFlag: int, Eccen: float, CtType: int, PeriodFlag: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, PGA: float, S02: float, S05: float, S1: float, S2: float, S4: float, SiteClass: int, Fa: float, Fv: float, I: float, Mv: float, Rd: float, Ro: float):
        """This function retrieves auto seismic loading parameters for the 2010 NBCC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern with a NBCC2010 auto
            seismic load assignment.
        DirFlag (input): This is 1 or 2, indicating the seismic load direction. 1 = Global X
            2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        CtType (input): This is 0, 1, 2, 3 or 4, indicating the structure type. 0 = Steel
            moment frame 1 = Concrete moment frame 2 = Other moment frame 3 = Braced frame 4
            = Shear wall
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 = Code 2
            = Program calculated 3 = User defined
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        PGA (input): The peak ground acceleration.
        S02 (input): The spectral acceleration at a 0.2 second period.
        S05 (input): The spectral acceleration at a 0.5 second period.
        S1 (input): The spectral acceleration at a 1 second period.
        S2 (input): The spectral acceleration at a 2 second period.
        S4 (input): The spectral acceleration at a 4 second period.
        SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        Fa (input): The site coefficient, Fa. This item is read when the site class is F
            only.
        Fv (input): The site coefficient, Fv. This item is read when the site class is F
            only.
        I (input): The importance factor.
        Mv (input): The higher mode factor.
        Rd (input): The ductility modifier.
        Ro (input): The overstrength modifier.
        """
        _r = self._raw.SetNBCC2010(Name, DirFlag, Eccen, CtType, PeriodFlag, UserT, UserZ, TopZ, BottomZ, PGA, S02, S05, S1, S2, S4, SiteClass, Fa, Fv, I, Mv, Rd, Ro)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetNBCC2010 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC2015(self, Name: str, DirFlag: int, Eccen: float, CtType: int, PeriodFlag: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, PGA: float, S02: float, S05: float, S1: float, S2: float, S5: float, S10: float, SiteClass: int, F02: float, F05: float, F1: float, F2: float, F5: float, F10: float, I: float, Mv: float, Rd: float, Ro: float):
        """This function retrieves auto seismic loading parameters for the 2015 NBCC code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern
        DirFlag (input): This is 1 or 2, indicating the seismic load direction. 1 = Global X
            2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        CtType (input): This is 0, 1, 2, 3 or 4, indicating the structure type. 0 = Steel
            moment frame 1 = Concrete moment frame 2 = Other moment frame 3 = Braced frame 4
            = Shear wall
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 = Code 2
            = Program calculated 3 = User defined
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        PGA (input): The peak ground acceleration.
        S02 (input): The spectral acceleration at a 0.2 second period.
        S05 (input): The spectral acceleration at a 0.5 second period.
        S1 (input): The spectral acceleration at a 1 second period.
        S2 (input): The spectral acceleration at a 2 second period.
        S5 (input): The spectral acceleration at a 5 second period.
        S10 (input): The spectral acceleration at a 10 second period.
        SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        F02 (input): The site coefficient at a 0.2 second period. This item is read when the
            site class is F only.
        F05 (input): The site coefficient at a 0.5 second period. This item is read when the
            site class is F only.
        F1 (input): The site coefficient at a 1 second period. This item is read when the
            site class is F only.
        F2 (input): The site coefficient at a 2 second period. This item is read when the
            site class is F only.
        F5 (input): The site coefficient at a 5 second period. This item is read when the
            site class is F only.
        F10 (input): The site coefficient at a 10 second period. This item is read when the
            site class is F only.
        I (input): The importance factor.
        Mv (input): The higher mode factor.
        Rd (input): The ductility modifier.
        Ro (input): The overstrength modifier.
        """
        _r = self._raw.SetNBCC2015(Name, DirFlag, Eccen, CtType, PeriodFlag, UserT, UserZ, TopZ, BottomZ, PGA, S02, S05, S1, S2, S5, S10, SiteClass, F02, F05, F1, F2, F5, F10, I, Mv, Rd, Ro)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetNBCC2015 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC95(self, Name: str, DirFlag: int, eccen: float, NBCCPFlag: int, NBCC95DS: float, PeriodFlag: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, NBCC95ZA: int, NBCC95ZV: int, NBCC95ZVFlag: int, NBCC95ZVR: float, NBCC95I: float, NBCC95F: float, NBCC95R: float):
        """This function assigns auto seismic loading parameters for the 1995 NBCC code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        NBCCPFlag (input): This is either 1 or 2, indicating the structure type. 1 = Moment
            frame 2 = Other
        NBCC95DS (input): This item applies only when the NBCCPFlag = 2. It is the dimension
            of the lateral load resisting system in the direction of the applied forces. [L]
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 = Code 2
            = Program calculated 3 = User defined
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        NBCC95ZA (input): This is 0, 1, 2, 3, 4, 5 or 6, indicating the acceleration related
            zone, Za.
        NBCC95ZV (input): This is 0, 1, 2, 3, 4, 5 or 6, indicating the velocity related
            zone, Zv.
        NBCC95ZVFlag (input): This is either 1 or 2, indicating how the zonal velocity
            ratio, V, is specified. 1 = From code based on Zv 2 = User specified
        NBCC95ZVR (input): The zonal velocity ratio, V. This item is used only when
            NBCC95ZVFlag = 2.
        NBCC95I (input): The importance factor.
        NBCC95F (input): The foundation factor.
        NBCC95R (input): The force modification factor.
        """
        _r = self._raw.SetNBCC95(Name, DirFlag, eccen, NBCCPFlag, NBCC95DS, PeriodFlag, UserT, UserZ, TopZ, BottomZ, NBCC95ZA, NBCC95ZV, NBCC95ZVFlag, NBCC95ZVR, NBCC95I, NBCC95F, NBCC95R)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetNBCC95 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNEHRP97(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CT: float, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, NEHRP97SG: int, NEHRP97SeismicCoeffFlag: int, NEHRP97Site: int, NEHRP97SS: float, NEHRP97S1: float, NEHRP97Fa: float, NEHRP97Fv: float, NEHRP97R: float):
        """This function assigns auto seismic loading parameters for the 1997 NEHRP code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (input): The code-specified CT factor. This item applies when the PeriodFlag item
            is 1 or 2.
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        NEHRP97SG (input): This is 1, 2 or 3, indicating the seismic group. 1 = I 2 = II 3 =
            III
        NEHRP97SeismicCoeffFlag (input): This is either 1 or 2, indicating the seismic
            coefficient option. 1 = Coefficients are per code 2 = Coefficients are user
            defined
        NEHRP97Site (input): This is 1, 2, 3, 4 or 5, indicating the site class. This item
            is used only when the NEHRP97SeismicCoeffFlag = 1. 1 = A 2 = B 3 = C 4 = D 5 = E
        NEHRP97SS (input): The response acceleration for short periods, (g).
        NEHRP97S1 (input): The response acceleration for a one second period, (g).
        NEHRP97Fa (input): The site coefficient Fa. This item is used only when the
            NEHRP97SeismicCoeffFlag = 2.
        NEHRP97Fv (input): The site coefficient Fv. This item is used only when the
            NEHRP97SeismicCoeffFlag = 2
        NEHRP97R (input): The response modification factor.
        """
        _r = self._raw.SetNEHRP97(Name, DirFlag, Eccen, PeriodFlag, CT, UserT, UserZ, TopZ, BottomZ, NEHRP97SG, NEHRP97SeismicCoeffFlag, NEHRP97Site, NEHRP97SS, NEHRP97S1, NEHRP97Fa, NEHRP97Fv, NEHRP97R)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetNEHRP97 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNTC2008(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, C1Type: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, ParamsOption: int, Latitude: float, Longitude: float, Island: int, LimitState: int, UsageClass: int, NomLife: float, PeakAccel: float, F0: float, Tcs: float, SpecType: int, SoilType: int, Topography: int, hRatio: float, Damping: float, q: float, lambda_: float):
        """This function assigns auto seismic loading parameters for the NTC 2008 code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        UserT (input): The user specified time period. This item is meaningful when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        ParamsOption (input): This is 1, 2, or 3, indicating the option for defining the
            parameters. 1 = by latitude and longitude 2 = by island 3 = user specified
        Island (input): This is one of the following values. This item is used only when
            ParamsOption = 2. 1 = Alicudi 2 = Arcipelago Toscano 3 = Filcudi 4 = Isole Egadi
            5 = Lampedusa 6 = Linosa 7 = Lipari 8 = Palmarola 9 = Panarea 1 0 = Pantelleria
            11 = Ponza 12 = Salina 13 = Santo Stefano 14 = Sardegna 15 = Stromboli 16 =
            Tremiti 17 = Ustica 18 = Ventotene 19 = Vulcano 20 = Zannone
        LimitState (input): This is 1, 2, 3, or 4, indicating the limit state. 1 = SLO 2 =
            SLD 3 = SLV 4 = SLC
        UsageClass (input): This is 1, 2, 3, or 4, indicating the usage class. 1 = I 2 = II
            3 = III 4 = IV
        NomLife (input): The nominal life to be considered.
        PeakAccel (input): The peak ground acceleration, ag/g.
        F0 (input): The magnitude factor, F0.
        Tcs (input): The reference period, Tc* [s].
        SpecType (input): This is 1, 2, 3, or 4, indicating the type of spectrum to
            consider. 1 = Elastic horizontal 2 = Elastic vertical 3 = Design horizontal 4 =
            Design vertical
        SoilType (input): This is 1, 2, 3, 4, or 5, indicating the subsoil type. 1 = A 2 = B
            3 = C 4 = D 5 = E
        Topography (input): This is 1, 2, 3, or 4, indicating the topography type. 1 = T1 2
            = T2 3 = T3 4 = T4
        hRatio (input): The ratio for the site altitude at the base of the hill to the
            height of the hill.
        Damping (input): The damping, in percent. This is only applicable for SpecType 1 and
            2.
        q (input): The behavior correction factor. This is only applicable for SpecType 3
            and 4.
        lambda (input): A correction factor.
        """
        _r = self._raw.SetNTC2008(Name, DirFlag, Eccen, PeriodFlag, C1Type, UserT, UserZ, TopZ, BottomZ, ParamsOption, Latitude, Longitude, Island, LimitState, UsageClass, NomLife, PeakAccel, F0, Tcs, SpecType, SoilType, Topography, hRatio, Damping, q, lambda_)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetNTC2008 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNTC2018(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, ParamsOption: int, Latitude: float, Longitude: float, Island: int, LimitState: int, UsageClass: int, NomLife: float, PeakAccel: float, F0: float, Tcs: float, SpecType: int, SoilType: int, Topography: int, hRatio: float, Damping: float, q: float, lambda_: float):
        """This function assigns auto seismic loading parameters for the NTC 2018 code. The function
        returns zero if the parameters are successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        UserT (input): The user specified time period. This item is meaningful when the
            PeriodFlag item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        ParamsOption (input): This is 1, 2, or 3, indicating the option for defining the
            parameters. 1 = by latitude and longitude 2 = by island 3 = user specified
        Island (input): This is one of the following values. This item is used only when
            ParamsOption = 2. 1 = Alicudi 2 = Arcipelago Toscano 3 = Filcudi 4 = Isole Egadi
            5 = Lampedusa 6 = Linosa 7 = Lipari 8 = Palmarola 9 = Panarea 1 0 = Pantelleria
            11 = Ponza 12 = Salina 13 = Santo Stefano 14 = Sardegna 15 = Stromboli 16 =
            Tremiti 17 = Ustica 18 = Ventotene 19 = Vulcano 20 = Zannone
        LimitState (input): This is 1, 2, 3, or 4, indicating the limit state. 1 = SLO 2 =
            SLD 3 = SLV 4 = SLC
        UsageClass (input): This is 1, 2, 3, or 4, indicating the usage class. 1 = I 2 = II
            3 = III 4 = IV
        NomLife (input): The nominal life to be considered.
        PeakAccel (input): The peak ground acceleration, ag/g.
        F0 (input): The magnitude factor, F0.
        Tcs (input): The reference period, Tc* [s].
        SpecType (input): This is 1, 2, 3, or 4, indicating the type of spectrum to
            consider. 1 = Elastic horizontal 2 = Elastic vertical 3 = Design horizontal 4 =
            Design vertical
        SoilType (input): This is 1, 2, 3, 4, or 5, indicating the subsoil type. 1 = A 2 = B
            3 = C 4 = D 5 = E
        Topography (input): This is 1, 2, 3, or 4, indicating the topography type. 1 = T1 2
            = T2 3 = T3 4 = T4
        hRatio (input): The ratio for the site altitude at the base of the hill to the
            height of the hill.
        Damping (input): The damping, in percent. This is only applicable for SpecType 1 and
            2.
        q (input): The behavior correction factor. This is only applicable for SpecType 3
            and 4.
        lambda (input): A correction factor.
        """
        _r = self._raw.SetNTC2018(Name, DirFlag, Eccen, PeriodFlag, UserT, UserZ, TopZ, BottomZ, ParamsOption, Latitude, Longitude, Island, LimitState, UsageClass, NomLife, PeakAccel, F0, Tcs, SpecType, SoilType, Topography, hRatio, Damping, q, lambda_)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetNTC2018 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNZS11702004(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, NZS2004SiteClass: int, NZS2004Z: float, NZS2004R: float, NZS2004DIST: float, NZS2004Sp: float, NZS2004Mu: float):
        """This function assigns auto seismic loading parameters for the NZS 1170.5 2004 code. The
        function returns zero if the parameters are successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is 1 or 2, indicating the seismic load direction. 1 = Global X
            2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        NZS2004SiteClass (input): This is 1, 2, 3, 4 or 5, indicating the site class. 1 = A
            2 = B 3 = C 4 = D 5 = E
        NZS2004Z (input): The hazard factor, Z.
        NZS2004R (input): The return period factor, R.
        NZS2004DIST (input): Distance to the fault in km, used to calculate the near fault
            factor.
        NZS2004Sp (input): The structural performance factor, Sp.
        NZS2004Mu (input): The structural ductility factor, u.
        """
        _r = self._raw.SetNZS11702004(Name, DirFlag, Eccen, PeriodFlag, UserT, UserZ, TopZ, BottomZ, NZS2004SiteClass, NZS2004Z, NZS2004R, NZS2004DIST, NZS2004Sp, NZS2004Mu)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetNZS11702004 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNone(self, Name: str):
        """This function sets the auto seismic loading type for the specified load pattern to None. The
        function returns zero if the loading type is successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        """
        _r = self._raw.SetNone(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetNone falhou (ret={_r})".format(_r=_r))
        return None

    def SetUBC94(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CT: float, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, UBC94ZFlag: int, UBC94Z: float, UBC94S: float, UBC94I: float, UBC94RW: float):
        """This function assigns auto seismic loading parameters for the 1994 UBC code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (input): The code-specified CT factor. This item applies when the PeriodFlag item
            is 1 or 2.
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        UBC94ZFlag (input): This is either 1 or 2, indicating if the seismic zone factor is
            per code or user defined. 1 = Per code 2 = User defined
        UBC94Z (input): The seismic zone factor, Z. If the seismic zone factor is per code
            (UBC94ZFlag = 1), this item should be one of the following: 0.075, 0.15, 0.20,
            0.30, 0.40.
        UBC94S (input): This is 1, 1.2, 1.5 or 2, indicating the site coefficient.
        UBC94I (input): The importance factor.
        UBC94RW (input): The numerical coefficient, Rw.
        """
        _r = self._raw.SetUBC94(Name, DirFlag, Eccen, PeriodFlag, CT, UserT, UserZ, TopZ, BottomZ, UBC94ZFlag, UBC94Z, UBC94S, UBC94I, UBC94RW)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetUBC94 falhou (ret={_r})".format(_r=_r))
        return None

    def SetUBC97Iso(self, Name: str, DirFlag: int, Eccen: float, UserZ: bool, TopZ: float, BottomZ: float, UBC97IsoSeismicCoeffFlag: int, UBC97IsoSoilProfileType: int, UBC97IsoZ: float, UBC97IsoCv: float, UBC97IsoNearSourceFlag: int, UBC97IsoSourceType: int, UBC97IsoDist: float, UBC97IsoNv: float, UBC97IsoRI: float, UBC97IsoBD: float, UBC97IsoKDmax: float, UBC97IsoKDmin: float):
        """This function assigns auto seismic loading parameters for seismically isolated buildings
        using the 1997 UBC code. The function returns zero if the parameters are
        successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        UBC97IsoSeismicCoeffFlag (input): This is either 1 or 2, indicating if the seismic
            coefficient Cv is per code or user defined. 1 = Per code 2 = User defined
        UBC97IsoSoilProfileType (input): This is 1, 2, 3, 4 or 5, indicating the soil
            profile type. 1 = SA 2 = SB 3 = SC 4 = SD 5 = SE This item is applicable only
            when the seismic coefficients Ca and Cv are calculated in accordance with code
            (UBC97SeismicCoeffFlag = 1).
        UBC97IsoZ (input): This is 0.075, 0.15, 0.2, 0.3 or 0.4, indicating the seismic zone
            factor. This item is applicable only when the seismic coefficient Cv is
            calculated in accordance with code (UBC97IsoSeismicCoeffFlag = 1).
        UBC97IsoCv (input): The seismic coefficient, Cv. This item is applicable only when
            the seismic coefficient Cv is user defined (UBC97IsoSeismicCoeffFlag = 2).
        UBC97IsoNearSourceFlag (input): This is either 1 or 2, indicating if the near source
            factor coefficient Nv is per code or user defined. 1 = Per code 2 = User defined
            This item is applicable only when the seismic coefficient Cv is calculated per
            code (UBC97IsoSeismicCoeffFlag = 1) and UBC97IsoZ = 0.4.
        UBC97IsoSourceType (input): This is 1, 2 or 3, indicating the seismic source type. 1
            = A 2 = B 3 = C This item is applicable only when the seismic coefficient Cv is
            calculated in accordance with code (UBC97IsoSeismicCoeffFlag = 1), UBC97IsoZ =
            0.4, and the near source factor coefficient Nv is calculated in accordance with
            code (UBC97IsoNearSourceFlag = 1).
        UBC97IsoDist (input): This is the distance to the seismic source in kilometers. This
            item is only applicable when the seismic coefficient Cv is calculated in
            accordance with code (UBC97IsoSeismicCoeffFlag = 1), UBC97IsoZ = 0.4, and the
            near source factor coefficient Nv is calculated in accordance with code
            (UBC97IsoNearSourceFlag = 1).
        UBC97IsoNv (input): The near source factor coefficient, Nv. This item is applicable
            only when the seismic coefficient Cv is user defined (UBC97IsoSeismicCoeffFlag =
            2) and the near source factor coefficient Nv is user defined
            (UBC97IsoNearSourceFlag = 2).
        UBC97IsoRI (input): The overstrength factor, Ri.
        UBC97IsoBD (input): The coefficient for damping.
        UBC97IsoKDmax (input): The maximum effective stiffness of the isolation system.
            [F/L]
        UBC97IsoKDmin (input): The minimum effective stiffness of the isolation system.
            [F/L]
        """
        _r = self._raw.SetUBC97Iso(Name, DirFlag, Eccen, UserZ, TopZ, BottomZ, UBC97IsoSeismicCoeffFlag, UBC97IsoSoilProfileType, UBC97IsoZ, UBC97IsoCv, UBC97IsoNearSourceFlag, UBC97IsoSourceType, UBC97IsoDist, UBC97IsoNv, UBC97IsoRI, UBC97IsoBD, UBC97IsoKDmax, UBC97IsoKDmin)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetUBC97Iso falhou (ret={_r})".format(_r=_r))
        return None

    def SetUBC97(self, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CT: float, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, UBC97SeismicCoeffFlag: int, UBC97SoilProfileType: int, UBC97Z: float, UBC97Ca: float, UBC97Cv: float, UBC97NearSourceFlag: int, UBC97SourceType: int, UBC97Dist: float, UBC97Na: float, UBC97Nv: float, UBC97I: float, UBC97R: float):
        """This function assigns auto seismic loading parameters for the 1997 UBC code. The function
        returns zero if the parameters are successfully assigned; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        PeriodFlag (input): This is 1, 2 or 3, indicating the time period option. 1 =
            Approximate 2 = Program calculated 3 = User defined
        CT (input): The code-specified CT factor. This item applies when the PeriodFlag item
            is 1 or 2.
        UserT (input): The user specified time period. This item applies when the PeriodFlag
            item is 3. [s]
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        UBC97SeismicCoeffFlag (input): This is either 1 or 2, indicating if the seismic
            coefficients Ca and Cv are per code or user defined. 1 = Per code 2 = User
            defined
        UBC97SoilProfileType (input): This is 1, 2, 3, 4 or 5, indicating the soil profile
            type. 1 = SA 2 = SB 3 = SC 4 = SD 5 = SE This item is applicable only when the
            seismic coefficients Ca and Cv are calculated in accordance with the code
            (UBC97SeismicCoeffFlag = 1).
        UBC97Z (input): This is 0.075, 0.15, 0.2, 0.3 or 0.4, indicating the seismic zone
            factor. This item is applicable only when the seismic coefficients Ca and Cv are
            calculated in accordance with code (UBC97SeismicCoeffFlag = 1).
        UBC97Ca (input): The seismic coefficient, Ca. This item is applicable only when the
            seismic coefficients Ca and Cv are user defined (UBC97SeismicCoeffFlag = 2).
        UBC97Cv (input): The seismic coefficient, Cv. This item is applicable only when the
            seismic coefficients Ca and Cv are user defined (UBC97SeismicCoeffFlag = 2).
        UBC97NearSourceFlag (input): This is either 1 or 2, indicating if the near source
            factor coefficients Na and Nv are per code or user defined. 1 = Per code 2 =
            User defined This item is applicable only when the seismic coefficients Ca and
            Cv are calculated in accordance with the code (UBC97SeismicCoeffFlag = 1) and
            UBC97Z = 0.4.
        UBC97SourceType (input): This is 1, 2 or 3, indicating the seismic source type. 1 =
            A 2 = B 3 = C This item is applicable only when the seismic coefficients Ca and
            Cv are calculated in accordance with code (UBC97SeismicCoeffFlag = 1), UBC97Z =
            0.4, and the near source factor coefficients Na and Nv are calculated in
            accordance with code (UBC97NearSourceFlag = 1).
        UBC97Dist (input): This is the distance to the seismic source in kilometers. This
            item is applicable only when the seismic coefficients Ca and Cv are calculated
            in accordance with code (UBC97SeismicCoeffFlag = 1), UBC97Z = 0.4, and the near
            source factor coefficients Na and Nv are calculated in accordance with code
            (UBC97NearSourceFlag = 1).
        UBC97Na (input): The near source factor coefficient, Na. This item is applicable
            only when the seismic coefficients Ca and Cv are user defined
            (UBC97SeismicCoeffFlag = 2) and the near source factor coefficients Na and Nv
            are user defined (UBC97NearSourceFlag = 2).
        UBC97Nv (input): The near source factor coefficient, Nv. This item is applicable
            only when the seismic coefficients Ca and Cv are user defined
            (UBC97SeismicCoeffFlag = 2) and the near source factor coefficients Na and Nv
            are user defined (UBC97NearSourceFlag = 2).
        UBC97I (input): The importance factor.
        UBC97R (input): The overstrength factor.
        """
        _r = self._raw.SetUBC97(Name, DirFlag, Eccen, PeriodFlag, CT, UserT, UserZ, TopZ, BottomZ, UBC97SeismicCoeffFlag, UBC97SoilProfileType, UBC97Z, UBC97Ca, UBC97Cv, UBC97NearSourceFlag, UBC97SourceType, UBC97Dist, UBC97Na, UBC97Nv, UBC97I, UBC97R)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetUBC97 falhou (ret={_r})".format(_r=_r))
        return None

    def SetUserCoefficient(self, Name: str, DirFlag: int, Eccen: float, UserZ: bool, TopZ: float, BottomZ: float, c: float, k: float):
        """This function assigns auto seismic loading parameters for User Coefficient type loading. The
        function returns zero if the parameters are successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        DirFlag (input): This is either 1 or 2, indicating the seismic load direction. 1 =
            Global X 2 = Global Y
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        UserZ (input): This item is True if the top and bottom elevations of the seismic
            load are user specified. It is False if the elevations are determined by the
            program.
        TopZ (input): This item applies only when the UserZ item is True. It is the global
            Z-coordinate at the highest level where auto seismic loads are applied. [L]
        BottomZ (input): This item applies only when the UserZ item is True. It is the
            global Z-coordinate at the lowest level where auto seismic loads are applied.
            [L]
        c (input): The base shear coefficient.
        k (input): The building height exponent.
        """
        _r = self._raw.SetUserCoefficient(Name, DirFlag, Eccen, UserZ, TopZ, BottomZ, c, k)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetUserCoefficient falhou (ret={_r})".format(_r=_r))
        return None

    def SetUserLoadValue(self, Name: str, Diaph: str, Fx: float, Fy: float, Mz: float, x: float = 0, y: float = 0):
        """This function assigns loading to an auto seismic load that is a User Load type. The
        SetUserLoad function is used to specify that an auto seismic load is a User Load
        type The function returns zero if the loading is successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern that has been assigned
            a User Load auto seismic type.
        Diaph (input): The name of an existing special rigid diaphragm constraint, that is,
            a diaphragm constraint with the following features: 1. The constraint type is
            CONSTRAINT_DIAPHRAGM = 2. 2. The constraint coordinate system is Global. 3. The
            constraint axis is Z.
        Fx (input): The global X direction force assigned to the specified diaphragm. [F]
        Fy (input): The global Y direction force assigned to the specified diaphragm. [F]
        Mz (input): The moment about the global Z axis assigned to the specified diaphragm.
            [FL]
        x (input): The global X-coordinate of the point where the seismic force is applied.
            [L] This item is applicable only when the auto seismic load is specified to have
            a user specified application point (see the SetUserLoad function).
        y (input): The global Y-coordinate of the point where the seismic force is applied.
            [L] This item is applicable only when the auto seismic load is specified to have
            a user specified application point (see the SetUserLoad function).
        """
        _r = self._raw.SetUserLoadValue(Name, Diaph, Fx, Fy, Mz, x, y)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetUserLoadValue falhou (ret={_r})".format(_r=_r))
        return None

    def SetUserLoad(self, Name: str, MyType: int, Eccen: float = 0.05):
        """This function sets the auto seismic load type to User Load. User load values are assigned
        using the SetUserLoadValue function. The function returns zero if the load type is
        successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Quake-type load pattern.
        MyType (input): This is either 1 or 2, indicating the application point type for the
            user load. 1 = User specified application point 2 = At center of mass with
            optional additional eccentricity
        Eccen (input): The eccentricity ratio that applies to all diaphragms. This item is
            only applicable when MyType = 2.
        """
        _r = self._raw.SetUserLoad(Name, MyType, Eccen)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadPatterns.AutoSeismic.SetUserLoad falhou (ret={_r})".format(_r=_r))
        return None


