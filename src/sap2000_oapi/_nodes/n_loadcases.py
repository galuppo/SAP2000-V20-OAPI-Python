"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_LoadCases:
    """Wrapper para SapModel.LoadCases."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing load case. The function returns zero if the
        new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined load case.
        NewName (input): The new name for the load case.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self, CaseType: int = None):
        """This function returns the total number of defined load cases in the model. If desired,
        counts can be returned for all load cases of a specified type in the model.
        """
        _r = self._raw.Count(CaseType)
        return _r

    def Delete(self, Name: str):
        """The function deletes the specified load case. The function returns zero if the load case is
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load case.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetNameList(self, CaseType: int = None):
        """This function retrieves the names of all defined load cases of the specified type. The
        function returns zero if the names are successfully retrieved, otherwise it returns
        nonzero.
        """
        _r = self._raw.GetNameList(0, [], CaseType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTypeOAPI_1(self, Name: str):
        """This function retrieves the case type, design type, and auto flag for the specified load
        case. The function returns zero if the type is successfully retrieved; otherwise it
        returns nonzero. This function supersedes .GetType (LoadCases).
    
        Name (input): The name of an existing load case.
        CaseType (output): This is one of the following items in the eLoadCaseType
            enumeration. CASE_LINEAR_STATIC = 1 CASE_NONLINEAR_STATIC = 2 CASE_MODAL = 3
            CASE_RESPONSE_SPECTRUM = 4 CASE_LINEAR_HISTORY = 5 (Modal Time History)
            CASE_NONLINEAR_HISTORY = 6 (Modal Time History) CASE_LINEAR_DYNAMIC = 7 (Direct
            Integration Time History) CASE_NONLINEAR_DYNAMIC = 8 (Direct Integration Time
            History) CASE_MOVING_LOAD = 9 CASE_BUCKLING = 10 CASE_STEADY_STATE = 11
            CASE_POWER_SPECTRAL_DENSITY = 12 CASE_LINEAR_STATIC_MULTISTEP = 13
            CASE_HYPERSTATIC = 14
        SubType (output): This is an integer representing the load case sub type. This item
            applies only for certain case types. For CASE_NONLINEAR_STATIC: 1 = Nonlinear 2
            = Nonlinear staged construction For CASE_MODAL: 1 = Eigen 2 = Ritz For
            CASE_LINEAR_HISTORY: 1 = Transient 2 = Periodic
        DesignType (output): This is one of the following items in the eLoadPatternType
            enumeration. LTYPE_DEAD = 1 LTYPE_SUPERDEAD = 2 LTYPE_LIVE = 3 LTYPE_REDUCELIVE
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
        DesignTypeOption (output): This is one of the following options for the DesignType
            item. 0 = Program determined 1 = User specified
        Auto (output): This is one of the following values indicating if the load case has
            been automatically created. 0 = Not automatically created 1 = Automatically
            created by the bridge construction scheduler
        """
        _r = self._raw.GetTypeOAPI_1(Name, None, 0, None, 0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.GetTypeOAPI_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetDesignType(self, Name: str, DesignTypeOption: int, DesignType: int = 1):
        """This function sets the design type for the specified load case. The function returns zero if
        the type is successfully set; otherwise it returns nonzero.
    
        Name (input): The name of an existing load case.
        DesignTypeOption (input): This is one of the following options for the DesignType
            item. 0 = Program determined 1 = User specified
        DesignType (input): This item only applies when the DesignTypeOption is 1 (user
            specified). It is one of the following items in the eLoadPatternType
            enumeration. LTYPE_DEAD = 1 LTYPE_SUPERDEAD = 2 LTYPE_LIVE = 3 LTYPE_REDUCELIVE
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
        _r = self._raw.SetDesignType(Name, DesignTypeOption, DesignType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SetDesignType falhou (ret={_r})".format(_r=_r))
        return None

    @cached_property
    def Buckling(self):
        return N_LoadCases_Buckling(self._raw.Buckling)

    @cached_property
    def DirHistLinear(self):
        return N_LoadCases_DirHistLinear(self._raw.DirHistLinear)

    @cached_property
    def DirHistNonlinear(self):
        return N_LoadCases_DirHistNonlinear(self._raw.DirHistNonlinear)

    @cached_property
    def ExternalResults(self):
        return N_LoadCases_ExternalResults(self._raw.ExternalResults)

    @cached_property
    def HyperStatic(self):
        return N_LoadCases_HyperStatic(self._raw.HyperStatic)

    @cached_property
    def ModHistLinear(self):
        return N_LoadCases_ModHistLinear(self._raw.ModHistLinear)

    @cached_property
    def ModHistNonlinear(self):
        return N_LoadCases_ModHistNonlinear(self._raw.ModHistNonlinear)

    @cached_property
    def ModalEigen(self):
        return N_LoadCases_ModalEigen(self._raw.ModalEigen)

    @cached_property
    def ModalRitz(self):
        return N_LoadCases_ModalRitz(self._raw.ModalRitz)

    @cached_property
    def Moving(self):
        return N_LoadCases_Moving(self._raw.Moving)

    @cached_property
    def PSD(self):
        return N_LoadCases_PSD(self._raw.PSD)

    @cached_property
    def ResponseSpectrum(self):
        return N_LoadCases_ResponseSpectrum(self._raw.ResponseSpectrum)

    @cached_property
    def Static_Nonlinear(self):
        return N_LoadCases_Static_Nonlinear(self._raw.Static_Nonlinear)

    @cached_property
    def Static_NonlinearStaged(self):
        return N_LoadCases_Static_NonlinearStaged(self._raw.Static_NonlinearStaged)

    @cached_property
    def StaticLinear(self):
        return N_LoadCases_StaticLinear(self._raw.StaticLinear)

    @cached_property
    def StaticLinearMultistep(self):
        return N_LoadCases_StaticLinearMultistep(self._raw.StaticLinearMultistep)

    @cached_property
    def StaticNonlinear(self):
        return N_LoadCases_StaticNonlinear(self._raw.StaticNonlinear)

    @cached_property
    def StaticNonlinearStaged(self):
        return N_LoadCases_StaticNonlinearStaged(self._raw.StaticNonlinearStaged)

    @cached_property
    def SteadyState(self):
        return N_LoadCases_SteadyState(self._raw.SteadyState)


class N_LoadCases_ExternalResults:
    """Wrapper para SapModel.LoadCases.ExternalResults."""

    def __init__(self, raw):
        self._raw = raw

    def SetCase(self, Name: str):
        """This function initializes an external results load case. If this function is called for an
        existing load case, all items for the case are reset to their default value. The
        function returns zero if the load case is successfully initialized; otherwise it
        returns a nonzero value.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ExternalResults.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetNumberSteps(self, Name: str, FirstStep: int, LastStep: int):
        """In the absence of a call to this function, the default values are FirstStep = 1 and LastStep
        = 1. The number of steps available for this load case will be LastStep FirstStep +
        1. The function returns zero if the number of steps is successfully initialized;
        otherwise it returns a nonzero value.
        """
        _r = self._raw.SetNumberSteps(Name, FirstStep, LastStep)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ExternalResults.SetNumberSteps falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_Moving:
    """Wrapper para SapModel.LoadCases.Moving."""

    def __init__(self, raw):
        self._raw = raw

    def GetDirectionalFactors(self, Name: str):
        """This function retrieves the directional factors for the specified load case. The function
        returns zero if the data is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing moving load case.
        Vertical (output): The moving load directional factor for vertical load.
        Braking (output): The moving load directional factor.
        Centrifugal (output): The moving directional factor for centrifugal load.
        """
        _r = self._raw.GetDirectionalFactors(Name, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        return (*_outs, _ret)

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing moving load load case.
        InitialCase (output): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Moving.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLanesLoaded(self, Name: str, LoadNumber: int):
        """This function retrieves the lanes loaded data for a specified load assignment number in a
        specified load case. The function returns zero if the data is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing moving load case.
        LoadNumber (input): The load assignment number.
        NumberItems (output): The number of lanes loaded for the specified load assignment
            number.
        MyName (output): This is an array that includes the name of each lane loaded for the
            specified load assignment number.
        """
        _r = self._raw.GetLanesLoaded(Name, LoadNumber, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Moving.GetLanesLoaded falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoads(self, Name: str, NumberLoads: int, MyClass: list[str], SF: list[float], Min: list[float], Max: list[float]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing moving load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        MyClass (input): This is an array that includes the vehicle class for each load
            assigned to the load case.
        SF (input): This is an array that includes the scale factor for each load assigned
            to the load case.
        Min (input): This is an array that includes the minimum number of lanes loaded for
            each load assigned to the load case.
        Max (input): This is an array that includes the maximum number of lanes loaded for
            each load assigned to the load case. This item must be 0, or it must be greater
            than or equal to Min. If this item is 0, all available lanes are loaded.
        """
        _r = self._raw.GetLoads(Name, NumberLoads, MyClass, SF, Min, Max)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Moving.GetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def GetMultiLaneSF(self, Name: str):
        """This function retrieves the multilane scale factor data for the specified load case. The
        function returns zero if the data is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing moving load case.
        NumberItems (output): The number of lanes loaded up to which reduction scale factors
            are provided.
        SF (output): This is an array that includes the reduction scale factor for the
            number of lanes loaded from 1 up to NumberItems.
        """
        _r = self._raw.GetMultiLaneSF(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Moving.GetMultiLaneSF falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a moving load load case. If this function is called for an
        existing load case, all items for the case are reset to their default value. The
        function returns zero if the load case is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case
            then that case is modified, otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Moving.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetDirectionalFactors(self, Name: str, Vertical: float, Braking: float, Centrifugal: float):
        """This function sets the directional factors for the specified load case. Calling this
        function is optional. By default, the directional factors are set to Vertical = 1,
        Braking = 0, and Centrifugal = 0 when the moving load case is defied or re-defined.
        If this function is called, the three directional factors must be nonnegative, and
        at least one must be positive. The function returns zero if the data is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing moving load case.
        Vertical (input): The moving load directional factor for vertical load.
        Braking (input): The moving load directional factor.
        Centrifugal (input): The moving directional factor for centrifugal load.
        """
        _r = self._raw.SetDirectionalFactors(Name, Vertical, Braking, Centrifugal)
        return _r

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing moving load load case.
        InitialCase (input): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Moving.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLanesLoaded(self, Name: str, LoadNumber: int, NumberItems: int, MyName: list[str]):
        """This function sets the lanes loaded data for a specified load assignment number in a
        specified load case. The function returns zero if the data is successfully set;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing moving load case.
        LoadNumber (input): The load assignment number.
        NumberItems (input): The number of lanes loaded for the specified load assignment
            number.
        MyName (input): This is an array that includes the name of each lane loaded for the
            specified load assignment number.
        """
        _r = self._raw.SetLanesLoaded(Name, LoadNumber, NumberItems, MyName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Moving.SetMultiLaneSF falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, MyClass: list[str], SF: list[float], Min: list[float], Max: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing moving load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        MyClass (input): This is an array that includes the vehicle class for each load
            assigned to the load case.
        SF (input): This is an array that includes the scale factor for each load assigned
            to the load case.
        Min (input): This is an array that includes the minimum number of lanes loaded for
            each load assigned to the load case.
        Max (input): This is an array that includes the maximum number of lanes loaded for
            each load assigned to the load case. This item must be 0, or it must be greater
            than or equal to Min. If this item is 0, all available lanes are loaded.
        """
        _r = self._raw.SetLoads(Name, NumberLoads, MyClass, SF, Min, Max)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Moving.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetMultiLaneSF(self, Name: str, NumberItems: int, SF: list[float]):
        """This function sets the multilane scale factor data for the specified load case. The function
        returns zero if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing moving load case.
        NumberItems (input): The number of lanes loaded up to which reduction scale factors
            are provided (NumberItems >= 1).
        SF (input): This is an array that includes the reduction scale factor for the number
            of lanes loaded from 1 up to NumberItems.
        """
        _r = self._raw.SetMultiLaneSF(Name, NumberItems, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Moving.SetMultiLaneSF falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_DirHistLinear:
    """Wrapper para SapModel.LoadCases.DirHistLinear."""

    def __init__(self, raw):
        self._raw = raw

    def GetDampProportional(self, Name: str):
        """This function retrieves the proportional modal damping data assigned to the specified load
        case. The function returns zero if the option is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing linear direct integration time history load
            case that has proportional damping.
        DampType (output): This is 1, 2 or 3, indicating the proportional modal damping
            type. 1 = Mass and stiffness proportional damping by direct specification 2 =
            Mass and stiffness proportional damping by period 3 = Mass and stiffness
            proportional damping by frequency
        Dampa (output): The mass proportional damping coefficient.
        Dampb (output): The stiffness proportional damping coefficient.
        Dampf1 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampd1 (output): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (output): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.GetDampProportional(Name, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.GetDampProportional falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing linear direct integration time history load
            case.
        InitialCase (output): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float], TF: list[float], AT: list[float], CSys: list[str]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear direct integration time history load
            case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load or Accel, indicating the type
            of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (output): This is an array that includes the name of the time history function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        TF (input): This is an array that includes the time scale factor of each load
            assigned to the load case.
        AT (input): This is an array that includes the arrival time of each load assigned to
            the load case.
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (output): This is an array that includes the angle between the acceleration
            local 1 axis and the +X-axis of the coordinate system specified by the CSys
            item. The rotation is about the Z-axis of the specified coordinate system. [deg]
            This item applies only when the LoadType item is Accel.
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, [], SF, TF, AT, CSys, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.GetLoads falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTimeIntegration(self, Name: str):
        """This function retrieves the time integration data assigned to the specified load case. The
        function returns zero if the option is successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing linear direct integration time history load
            case.
        IntegrationType (output): This is 1, 2, 3, 4 or 5, indicating the time integration
            type. 1 = Newmark 2 = Wilson 3 = Collocation 4 = Hilber-Hughes-Taylor 5 = Chung
            and Hulbert
        Alpha (output): The alpha factor (-1/3 <= Alpha <= 0). This item applies only when
            IntegrationType = 4 or 5.
        Beta (output): The beta factor (Beta >= 0). This item applies only when
            IntegrationType = 1, 3 or 5. It is returned for informational purposes when
            IntegrationType = 4.
        Gamma (output): The gamma factor (Gamma >= 0.5). This item applies only when
            IntegrationType = 1, 3 or 5. It is returned for informational purposes when
            IntegrationType = 4.
        Theta (output): The theta factor (Theta > 0). This item applies only when
            IntegrationType = 2 or 3.
        m (output): The alpha-m factor. This item only applies when IntegrationType = 5.
        """
        _r = self._raw.GetTimeIntegration(Name, 0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.GetTimeIntegration falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTimeStep(self, Name: str):
        """This function retrieves the time step data for the specified load case. The function returns
        zero if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear direct integration time history load
            case.
        nstep (output): The number of output time steps.
        DT (output): The output time step size.
        """
        _r = self._raw.GetTimeStep(Name, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.GetTimeStep falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a linear direct integration time history load case. If this
        function is called for an existing load case, all items for the case are reset to
        their default value. The function returns zero if the load case is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampProportional(self, Name: str, DampType: int, Dampa: float, Dampb: float, Dampf1: float, Dampf2: float, Dampd1: float, Dampd2: float):
        """This function sets proportional modal damping data for the specified load case. The function
        returns zero if the damping is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing linear direct integration time history load
            case.
        DampType (input): This is 1, 2 or 3, indicating the proportional modal damping type.
            1 = Mass and stiffness proportional damping by direct specification 2 = Mass and
            stiffness proportional damping by period 3 = Mass and stiffness proportional
            damping by frequency
        Dampa (input): The mass proportional damping coefficient. This item applies only
            when DampType = 1.
        Dampb (input): The stiffness proportional damping coefficient. This item applies
            only when DampType = 1.
        Dampf1 (input): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (input): This is either the period or the frequency (depending on the value
            of the DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType
            = 3 This item applies only when DampType = 2 or 3.
        Dampd1 (input): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (input): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.SetDampProportional(Name, DampType, Dampa, Dampb, Dampf1, Dampf2, Dampd1, Dampd2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.SetDampProportional falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing linear direct integration time history load
            case.
        InitialCase (input): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case. the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], Func: list[str], SF: list[float], TF: list[float], AT: list[float], CSys: list[str], Ang: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear direct integration time history load
            case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load or Accel, indicating the type
            of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (input): This is an array that includes the name of the time history function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        TF (input): This is an array that includes the time scale factor of each load
            assigned to the load case.
        AT (input): This is an array that includes the arrival time of each load assigned to
            the load case.
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (input): This is an array that includes the angle between the acceleration local
            1 axis and the +X-axis of the coordinate system specified by the CSys item. The
            rotation is about the Z-axis of the specified coordinate system. [deg] This item
            applies only when the LoadType item is Accel.
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, Func, SF, TF, AT, CSys, Ang)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetTimeIntegration(self, Name: str, IntegrationType: int, Alpha: float, Beta: float, Gamma: float, Theta: float, m: float = 0):
        """This function sets time integration data for the specified load case. The function returns
        zero if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear direct integration time history load
            case.
        IntegrationType (input): This is 1, 2, 3, 4 or 5, indicating the time integration
            type. 1 = Newmark 2 = Wilson 3 = Collocation 4 = Hilber-Hughes-Taylor 5 = Chung
            and Hulbert
        Alpha (input): The alpha factor (-1/3 <= Alpha <= 0). This item applies only when
            IntegrationType = 4 or 5.
        Beta (input): The beta factor (Beta >= 0). This item applies only when
            IntegrationType = 1, 3 or 5.
        Gamma (input): The gamma factor (Gamma >= 0.5). This item applies only when
            IntegrationType = 1, 3 or 5.
        Theta (input): The theta factor (Theta > 0). This item applies only when
            IntegrationType = 2 or 3.
        m (input): The alpha-m factor. This item applies only when IntegrationType = 5.
        """
        _r = self._raw.SetTimeIntegration(Name, IntegrationType, Alpha, Beta, Gamma, Theta, m)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.SetTimeIntegration falhou (ret={_r})".format(_r=_r))
        return None

    def SetTimeStep(self, Name: str, nstep: int, DT: float):
        """This function sets the time step data for the specified load case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear direct integration time history load
            case.
        nstep (input): The number of output time steps.
        DT (input): The output time step size.
        """
        _r = self._raw.SetTimeStep(Name, nstep, DT)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistLinear.SetTimeStep falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_DirHistNonlinear:
    """Wrapper para SapModel.LoadCases.DirHistNonlinear."""

    def __init__(self, raw):
        self._raw = raw

    def GetDampProportional(self, Name: str):
        """This function retrieves the proportional modal damping data assigned to the specified load
        case. The function returns zero if the option is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case that has proportional damping.
        DampType (output): This is 1, 2 or 3, indicating the proportional modal damping
            type. 1 = Mass and stiffness proportional damping by direct specification 2 =
            Mass and stiffness proportional damping by period 3 = Mass and stiffness
            proportional damping by frequency
        Dampa (output): The mass proportional damping coefficient.
        Dampb (output): The stiffness proportional damping coefficient.
        Dampf1 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampd1 (output): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (output): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.GetDampProportional(Name, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.GetDampProportional falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetGeometricNonlinearity(self, Name: str):
        """This function retrieves the geometric nonlinearity option for the specified load case. The
        function returns zero if the option is successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        NLGeomType (output): This is 0, 1 or 2, indicating the geometric nonlinearity option
            selected for the load case. 0 = None 1 = P-delta 2 = P-delta plus large
            displacements
        """
        _r = self._raw.GetGeometricNonlinearity(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.GetGeometricNonlinearity falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        InitialCase (output): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts from the state at the end of a
            nonlinear static or nonlinear direct integration time history load case. If the
            specified initial case is a nonlinear static or nonlinear direct integration
            time history load case, the state at the end of that case is used. If the
            initial case is anything else then zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float], TF: list[float], AT: list[float], CSys: list[str]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load or Accel, indicating the type
            of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (output): This is an array that includes the name of the time history function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        TF (input): This is an array that includes the time scale factor of each load
            assigned to the load case.
        AT (input): This is an array that includes the arrival time of each load assigned to
            the load case.
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (output): This is an array that includes the angle between the acceleration
            local 1 axis and the +X-axis of the coordinate system specified by the CSys
            item. The rotation is about the Z-axis of the specified coordinate system. [deg]
            This item applies only when the LoadType item is Accel.
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, [], SF, TF, AT, CSys, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.GetLoads falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMassSource(self, Name: str):
        """This function sets the mass source to be used for the specified load case. The function
        returns zero if the mass source is data is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        Source (output): This is the name of an existing mass source or a blank string.
            Blank indicates to use the mass source from the previous load case or the
            default mass source if the load case starts from zero initial conditions.
        """
        _r = self._raw.GetMassSource(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.GetMassSource falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSolControlParameters(self, Name: str, UseEventStepping: bool):
        """This function retrieves the solution control parameters for the specified load case. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        DTMax (output): The maximum substep size.
        DTMin (output): The minimum substep size.
        MaxIterCS (output): The maximum constant-stiffness iterations per step.
        MaxIterNR (output): The maximum Newton_Raphson iterations per step.
        TolConvD (output): The relative iteration convergence tolerance.
        UseEventStepping (input): This item is True if event-to-event stepping is used.
        TolEventD (output): The relative event lumping tolerance.
        MaxLineSearchPerIter (output): The maximum number of line searches per iteration.
        TolLineSearch (output): The relative line-search acceptance tolerance.
        LineSearchStepFact (output): The line-search step factor.
        """
        _r = self._raw.GetSolControlParameters(Name, 0.0, 0.0, 0, 0, 0.0, UseEventStepping, 0.0, 0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.GetSolControlParameters falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTimeIntegration(self, Name: str):
        """This function retrieves the time integration data assigned to the specified load case. The
        function returns zero if the option is successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        IntegrationType (output): This is 1, 2, 3, 4 or 5; indicating the time integration
            type. 1 = Newmark 2 = Wilson 3 = Collocation 4 = Hilber-Hughes-Taylor 5 = Chung
            and Hulbert
        Alpha (output): The alpha factor (-1/3 <= Alpha <= 0). This item applies only when
            IntegrationType = 4 or 5.
        Beta (output): The beta factor (Beta >= 0). This item applies only when
            IntegrationType = 1, 3 or 5. It is returned for informational purposes when
            IntegrationType = 4.
        Gamma (output): The gamma factor (Gamma >= 0.5). This item applies only when
            IntegrationType = 1, 3 or 5. It is returned for informational purposes when
            IntegrationType = 4.
        Theta (output): The theta factor (Theta > 0). This item applies only when
            IntegrationType = 2 or 3.
        m (output): The alpha-m factor. This item applies only when IntegrationType = 5.
        """
        _r = self._raw.GetTimeIntegration(Name, 0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.GetTimeIntegration falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTimeStep(self, Name: str):
        """This function retrieves the time step data for the specified load case. The function returns
        zero if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        nstep (output): The number of output time steps.
        DT (output): The output time step size.
        """
        _r = self._raw.GetTimeStep(Name, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.GetTimeStep falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a nonlinear direct integration time history load case. If this
        function is called for an existing load case, all items for the case are reset to
        their default value. The function returns zero if the load case is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampProportional(self, Name: str, DampType: int, Dampa: float, Dampb: float, Dampf1: float, Dampf2: float, Dampd1: float, Dampd2: float):
        """This function sets proportional modal damping data for the specified load case. The function
        returns zero if the damping is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        DampType (input): This is 1, 2 or 3, indicating the proportional modal damping type.
            1 = Mass and stiffness proportional damping by direct specification 2 = Mass and
            stiffness proportional damping by period 3 = Mass and stiffness proportional
            damping by frequency
        Dampa (input): The mass proportional damping coefficient. This item applies only
            when DampType = 1.
        Dampb (input): The stiffness proportional damping coefficient. This item applies
            only when DampType = 1.
        Dampf1 (input): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (input): This is the period or the frequency (depending on the value of the
            DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampd1 (input): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (input): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.SetDampProportional(Name, DampType, Dampa, Dampb, Dampf1, Dampf2, Dampd1, Dampd2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.SetDampProportional falhou (ret={_r})".format(_r=_r))
        return None

    def SetGeometricNonlinearity(self, Name: str, NLGeomType: int):
        """This function sets the geometric nonlinearity option for the specified load case. The
        function returns zero if the option is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        NLGeomType (input): This is 0, 1 or 2, indicating the geometric nonlinearity option
            selected for the load case. 0 = None 1 = P-delta 2 = P-delta plus large
            displacements
        """
        _r = self._raw.SetGeometricNonlinearity(Name, NLGeomType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.SetGeometricNonlinearity falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        InitialCase (input): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts from the state at the end of a
            nonlinear static or nonlinear direct integration time history load case. If the
            specified initial case is a nonlinear static or nonlinear direct integration
            time history load case, the state at the end of that case is used. If the
            initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], Func: list[str], SF: list[float], TF: list[float], AT: list[float], CSys: list[str], Ang: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load or Accel, indicating the type
            of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (input): This is an array that includes the name of the time history function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        TF (input): This is an array that includes the time scale factor of each load
            assigned to the load case.
        AT (input): This is an array that includes the arrival time of each load assigned to
            the load case.
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (input): This is an array that includes the angle between the acceleration local
            1 axis and the +X-axis of the coordinate system specified by the CSys item. The
            rotation is about the Z-axis of the specified coordinate system. [deg] This item
            applies only when the LoadType item is Accel.
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, Func, SF, TF, AT, CSys, Ang)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetMassSource(self, Name: str, Source: str):
        """This function sets the mass source to be used for the specified load case. The function
        returns zero if the mass source is data is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        Source (input): This is the name of an existing mass source or a blank string. Blank
            indicates to use the mass source from the previous load case or the default mass
            source if the load case starts from zero initial conditions.
        """
        _r = self._raw.SetMassSource(Name, Source)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.SetMassSource falhou (ret={_r})".format(_r=_r))
        return None

    def SetSolControlParameters(self, Name: str, DTMax: float, DTMin: float, MaxIterCS: int, MaxIterNR: int, TolConvD: float, UseEventStepping: bool, TolEventD: float, MaxLineSearchPerIter: int, TolLineSearch: float, LineSearchStepFact: float):
        """This function sets the solution control parameters for the specified load case. The function
        returns zero if the parameters are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        DTMax (input): The maximum substep size.
        DTMin (input): The minimum substep size.
        MaxIterCS (input): The maximum constant-stiffness iterations per step.
        MaxIterNR (input): The maximum Newton_Raphson iterations per step.
        TolConvD (input): The relative iteration convergence tolerance.
        UseEventStepping (input): This item is True if event-to-event stepping is used.
        TolEventD (input): The relative event lumping tolerance.
        MaxLineSearchPerIter (input): The maximum number of line searches per iteration.
        TolLineSearch (input): The relative line-search acceptance tolerance.
        LineSearchStepFact (input): The line-search step factor.
        """
        _r = self._raw.SetSolControlParameters(Name, DTMax, DTMin, MaxIterCS, MaxIterNR, TolConvD, UseEventStepping, TolEventD, MaxLineSearchPerIter, TolLineSearch, LineSearchStepFact)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.SetSolControlParameters falhou (ret={_r})".format(_r=_r))
        return None

    def SetTimeIntegration(self, Name: str, IntegrationType: int, Alpha: float, Beta: float, Gamma: float, Theta: float, m: float = 0):
        """This function sets time integration data for the specified load case. The function returns
        zero if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        IntegrationType (input): This is 1, 2, 3, 4 or 5, indicating the time integration
            type. 1 = Newmark 2 = Wilson 3 = Collocation 4 = Hilber-Hughes-Taylor 5 = Chung
            and Hulbert
        Alpha (input): The alpha factor (-1/3 <= Alpha <= 0). This item applies only when
            IntegrationType = 4 or 5.
        Beta (input): The beta factor (Beta >= 0). This item applies only when
            IntegrationType = 1, 3 or 5.
        Gamma (input): The gamma factor (Gamma >= 0.5). This item applies only when
            IntegrationType = 1, 3 or 5.
        Theta (input): The theta factor (Theta > 0). This item applies only when
            IntegrationType = 2 or 3.
        m (input): The alpha-m factor. This item applies only when IntegrationType = 5.
        """
        _r = self._raw.SetTimeIntegration(Name, IntegrationType, Alpha, Beta, Gamma, Theta, m)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.SetTimeIntegration falhou (ret={_r})".format(_r=_r))
        return None

    def SetTimeStep(self, Name: str, nstep: int, DT: float):
        """This function sets the time step data for the specified load case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear direct integration time history load
            case.
        nstep (input): The number of output time steps.
        DT (input): The output time step size.
        """
        _r = self._raw.SetTimeStep(Name, nstep, DT)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.DirHistNonlinear.SetTimeStep falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_Static_NonlinearStaged:
    """Wrapper para SapModel.LoadCases.Static NonlinearStaged."""

    def __init__(self, raw):
        self._raw = raw

    def GetMassSource(self, Name: str):
        """This function sets the mass source to be used for the specified load case. The function
        returns zero if the mass source is data is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear staged load case.
        Source (output): This is the name of an existing mass source or a blank string.
            Blank indicates to use the mass source from the previous load case or the
            default mass source if the load case starts from zero initial conditions.
        """
        _r = self._raw.GetMassSource(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Static NonlinearStaged.GetMassSource falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_LoadCases_StaticNonlinearStaged:
    """Wrapper para SapModel.LoadCases.StaticNonlinearStaged."""

    def __init__(self, raw):
        self._raw = raw

    def GetGeometricNonlinearity(self, Name: str):
        """This function retrieves the geometric nonlinearity option for the specified load case. The
        function returns zero if the option is successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        NLGeomType (output): This is 0, 1 or 2, indicating the geometric nonlinearity option
            selected for the load case. 0 = None 1 = P-delta 2 = P-delta plus large
            displacements
        """
        _r = self._raw.GetGeometricNonlinearity(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.GetGeometricNonlinearity falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetHingeUnloading(self, Name: str):
        """This function retrieves the hinge unloading option for the specified load case. The function
        returns zero if the option is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        UnloadType (output): This is 1, 2 or 3, indicating the hinge unloading option
            selected for the load case. 1 = Unload entire structure 2 = Apply local
            redistribution 3 = Restart using secant stiffness
        """
        _r = self._raw.GetHingeUnloading(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.GetHingeUnloading falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        InitialCase (output): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts from the state at the end of a
            nonlinear static or nonlinear direct integration time history load case. If the
            specified initial case is a nonlinear static or nonlinear direct integration
            time history load case, the state at the end of that case is used. If the
            initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMaterialNonlinearity(self, Name: str):
        """This function retrieves the material nonlinearity options for the specified load case. The
        function returns zero if the options are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        TimeDepMatProp (output): When this is True, any specified time dependent material
            properties are considered in the analysis.
        """
        _r = self._raw.GetMaterialNonlinearity(Name, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.GetMaterialNonlinearity falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetResultsSaved(self, Name: str):
        """This function retrieves the results saved parameters for the specified load case. The
        function returns zero if the parameters are retrieved successfully; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        StagedSaveOption (output): This is 0, 1, 2 or 3, indicating the results saved option
            for the load case. 0 = End of final stage 1 = End of each stage 2 = Start and
            end of each stage 3 = Two or more times in each stage
        StagedMinSteps (output): The minimum number of steps for application of
            instantaneous load. This item applies only when StagedSaveOption = 3.
        StagedMinStepsTD (output): The minimum number of steps for analysis of time
            dependent items. This item applies only when StagedSaveOption = 3.
        """
        _r = self._raw.GetResultsSaved(Name, 0, 0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.GetResultsSaved falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSolControlParameters(self, Name: str, UseEventStepping: bool):
        """This function retrieves the solution control parameters for the specified load case. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        MaxTotalSteps (output): The maximum total steps per stage.
        MaxFailedSubSteps (output): The maximum null (zero) steps per stage.
        MaxIterCS (output): The maximum constant-stiffness iterations per step.
        MaxIterNR (output): The maximum Newton_Raphson iterations per step.
        TolConvD (output): The relative iteration convergence tolerance.
        UseEventStepping (input): This item is True if event-to-event stepping is used.
        TolEventD (output): The relative event lumping tolerance.
        MaxLineSearchPerIter (output): The maximum number of line searches per iteration.
        TolLineSearch (output): The relative line-search acceptance tolerance.
        LineSearchStepFact (output): The line-search step factor.
        """
        _r = self._raw.GetSolControlParameters(Name, 0, 0, 0, 0, 0.0, UseEventStepping, 0.0, 0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.GetSolControlParameters falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTargetForceParameters(self, Name: str, NoStop: bool):
        """This function retrieves the target force iteration parameters for the specified load case.
        The function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        TolConvF (output): The relative convergence tolerance for target force iteration.
        MaxIter (output): The maximum iterations per stage for target force iteration.
        AccelFact (output): The acceleration factor.
        NoStop (input): If this item is True, the analysis is continued when there is no
            convergence in the target force iteration.
        """
        _r = self._raw.GetTargetForceParameters(Name, 0.0, 0, 0.0, NoStop)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.GetTargetForceParameters falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a static nonlinear staged analysis case. If this function is
        called for an existing load case, all items for the case are reset to their default
        value. The function returns zero if the load case is successfully initialized;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified, otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetGeometricNonlinearity(self, Name: str, NLGeomType: int):
        """This function sets the geometric nonlinearity option for the specified load case. The
        function returns zero if the option is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        NLGeomType (input): This is 0, 1 or 2, indicating the geometric nonlinearity option
            selected for the load case. 0 = None 1 = P-delta 2 = P-delta plus large
            displacements
        """
        _r = self._raw.SetGeometricNonlinearity(Name, NLGeomType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.SetGeometricNonlinearity falhou (ret={_r})".format(_r=_r))
        return None

    def SetHingeUnloading(self, Name: str, UnloadType: int):
        """This function sets the hinge unloading option for the specified load case. The function
        returns zero if the option is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        UnloadType (input): This is 1, 2 or 3, indicating the hinge unloading option
            selected for the load case. 1 = Unload entire structure 2 = Apply local
            redistribution 3 = Restart using secant stiffness
        """
        _r = self._raw.SetHingeUnloading(Name, UnloadType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.SetHingeUnloading falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        InitialCase (input): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts from the state at the end of a
            nonlinear static or nonlinear direct integration time history load case. If the
            specified initial case is a nonlinear static or nonlinear direct integration
            time history load case, the state at the end of that case is used. If the
            initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetMassSource(self, Name: str, Source: str):
        """This function sets the mass source to be used for the specified load case. The function
        returns zero if the mass source is data is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        Source (input): This is the name of an existing mass source or a blank string. Blank
            indicates to use the mass source from the previous load case or the default mass
            source if the load case starts from zero initial conditions.
        """
        _r = self._raw.SetMassSource(Name, Source)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.SetMassSource falhou (ret={_r})".format(_r=_r))
        return None

    def SetMaterialNonlinearity(self, Name: str, TimeDepMatProp: bool):
        """This function sets the material nonlinearity options for the specified load case. The
        function returns zero if the options are successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        TimeDepMatProp (input): When this is True, any specified time dependent material
            properties are considered in the analysis.
        """
        _r = self._raw.SetMaterialNonlinearity(Name, TimeDepMatProp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.SetMaterialNonlinearity falhou (ret={_r})".format(_r=_r))
        return None

    def SetResultsSaved(self, Name: str, StagedSaveOption: int, StagedMinSteps: int = 1, StagedMinStepsTD: int = 1):
        """This function sets the results saved parameters for the specified load case. The function
        returns zero if the parameters are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        StagedSaveOption (input): This is 0, 1, 2 or 3, indicating the results saved option
            for the load case. 0 = End of final stage 1 = End of each stage 2 = Start and
            end of each stage 3 = Two or more times in each stage
        StagedMinSteps (input): The minimum number of steps for application of instantaneous
            load. This item applies only when StagedSaveOption = 3.
        StagedMinStepsTD (input): The minimum number of steps for analysis of time dependent
            items. This item applies only when StagedSaveOption = 3.
        """
        _r = self._raw.SetResultsSaved(Name, StagedSaveOption, StagedMinSteps, StagedMinStepsTD)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.SetResultsSaved falhou (ret={_r})".format(_r=_r))
        return None

    def SetSolControlParameters(self, Name: str, MaxTotalSteps: int, MaxFailedSubSteps: int, MaxIterCS: int, MaxIterNR: int, TolConvD: float, UseEventStepping: bool, TolEventD: float, MaxLineSearchPerIter: int, TolLineSearch: float, LineSearchStepFact: float):
        """This function sets the solution control parameters for the specified load case. The function
        returns zero if the parameters are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear load case.
        MaxTotalSteps (input): The maximum total steps per stage.
        MaxFailedSubSteps (input): The maximum null (zero) steps per stage.
        MaxIterCS (input): The maximum constant-stiffness iterations per step.
        MaxIterNR (input): The maximum Newton_Raphson iterations per step.
        TolConvD (input): The relative iteration convergence tolerance.
        UseEventStepping (input): This item is True if event-to-event stepping is used.
        TolEventD (input): The relative event lumping tolerance.
        MaxLineSearchPerIter (input): The maximum number of line searches per iteration.
        TolLineSearch (input): The relative line-search acceptance tolerance.
        LineSearchStepFact (input): The line-search step factor.
        """
        _r = self._raw.SetSolControlParameters(Name, MaxTotalSteps, MaxFailedSubSteps, MaxIterCS, MaxIterNR, TolConvD, UseEventStepping, TolEventD, MaxLineSearchPerIter, TolLineSearch, LineSearchStepFact)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.SetSolControlParameters falhou (ret={_r})".format(_r=_r))
        return None

    def SetTargetForceParameters(self, Name: str, TolConvF: float, MaxIter: int, AccelFact: float, NoStop: bool):
        """This function sets the target force iteration parameters for the specified load case. The
        function returns zero if the parameters are successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear staged analysis case.
        TolConvF (input): The relative convergence tolerance for target force iteration.
        MaxIter (input): The maximum iterations per stage for target force iteration.
        AccelFact (input): The acceleration factor.
        NoStop (input): If this item is True, the analysis is continued when there is no
            convergence in the target force iteration.
        """
        _r = self._raw.SetTargetForceParameters(Name, TolConvF, MaxIter, AccelFact, NoStop)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinearStaged.SetTargetForceParameters falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_StaticLinear:
    """Wrapper para SapModel.LoadCases.StaticLinear."""

    def __init__(self, raw):
        self._raw = raw

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing static linear load case.
        InitialCase (output): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinear.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing static linear load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinear.GetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetCase(self, Name: str):
        """This function initializes a static linear load case. If this function is called for an
        existing load case, all items for the case are reset to their default value. The
        function returns zero if the load case is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinear.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static linear load case.
        InitialCase (input): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else then zero initial conditions are
            assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinear.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing static linear load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinear.SetLoads falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_ModHistNonlinear:
    """Wrapper para SapModel.LoadCases.ModHistNonlinear."""

    def __init__(self, raw):
        self._raw = raw

    def GetDampConstant(self, Name: str):
        """This function retrieves the constant modal damping for all modes assigned to the specified
        load case. The function returns zero if the option is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case that has
            constant damping.
        Damp (output): The constant damping for all modes (0 <= Damp < 1).
        """
        _r = self._raw.GetDampConstant(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetDampConstant falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetDampInterpolated(self, Name: str):
        """This function retrieves the interpolated modal damping data assigned to the specified load
        case. The function returns zero if the option is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case that has
            interpolated damping.
        DampType (output): This is 5 or 6, indicating the interpolated modal damping type. 5
            = Interpolated damping by period 6 = Interpolated damping by frequency
        NumberItems (output): The number of Time and Damp pairs.
        Time (output): This is an array that includes the period or the frequency, depending
            on the value of the DampType item. [s] for DampType = 5 and [cyc/s] for DampType
            = 6
        Damp (output): This is an array that includes the damping for the specified period
            of frequency (0 <= Damp < 1).
        """
        _r = self._raw.GetDampInterpolated(Name, 0, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetDampInterpolated falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampOverrides(self, Name: str):
        """This function retrieves the modal damping overrides assigned to the specified load case. The
        function returns zero if the overrides are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        NumberItems (output): The number of Mode and Damp pairs.
        Mode (output): This is an array that includes a mode number.
        Damp (output): This is an array that includes the damping for the specified mode (0
            <= Damp < 1).
        """
        _r = self._raw.GetDampOverrides(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetDampInterpolated falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampProportional(self, Name: str):
        """This function retrieves the proportional modal damping data assigned to the specified load
        case. The function returns zero if the option is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case that has
            proportional damping.
        DampType (output): This is 1, 2 or 3, indicating the proportional modal damping
            type. 1 = Mass and stiffness proportional damping by direct specification 2 =
            Mass and stiffness proportional damping by period 3 = Mass and stiffness
            proportional damping by frequency
        Dampa (output): The mass proportional damping coefficient.
        Dampb (output): The stiffness proportional damping coefficient.
        Dampf1 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampd1 (output): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (output): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.GetDampProportional(Name, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetDampProportional falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampType(self, Name: str):
        """This function retrieves the modal damping type for the specified load case. The function
        returns zero if the type is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        DampType (output): This is 1, 2, 3, 4, 5 or 6, indicating the modal damping type for
            the load case. 1 = Mass and stiffness proportional damping by direct
            specification 2 = Mass and stiffness proportional damping by period 3 = Mass and
            stiffness proportional damping by frequency 4 = Constant damping for all modes 5
            = Interpolated damping by period 6 = Interpolated damping by frequency
        """
        _r = self._raw.GetDampType(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetDampType falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        InitialCase (output): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it continues from the end of another nonlinear
            modal time history load case. If the specified initial case is not a nonlinear
            modal time history load case, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float], TF: list[float], AT: list[float], CSys: list[str]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load or Accel, indicating the type
            of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (output): This is an array that includes the name of the time history function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        TF (input): This is an array that includes the time scale factor of each load
            assigned to the load case.
        AT (input): This is an array that includes the arrival time of each load assigned to
            the load case.
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (output): This is an array that includes the angle between the acceleration
            local 1 axis and the +X-axis of the coordinate system specified by the CSys
            item. The rotation is about the Z-axis of the specified coordinate system. [deg]
            This item applies only when the LoadType item is Accel.
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, [], SF, TF, AT, CSys, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetLoads falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetModalCase(self, Name: str):
        """This function retrieves the modal case assigned to the specified load case. The function
        returns zero if the modal case is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        ModalCase (output): This is None or the name of an existing modal analysis case. It
            specifies the modal load case on which any mode-type load assignments to the
            specified load case are based.
        """
        _r = self._raw.GetModalCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetModalCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSolControlParameters(self, Name: str):
        """This function retrieves the solution control parameters for the specified load case. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal time history analysis case.
        tstat (output): The static period.
        dtmax (output): The maximum substep size.
        dtmin (output): The minimum substep size.
        ftol (output): The relative force convergence tolerance.
        etol (output): The relative energy convergence tolerance.
        itmax (output): The maximum iteration limit.
        itmin (output): The minimum iteration limit.
        Cf (output): The convergence factor.
        """
        _r = self._raw.GetSolControlParameters(Name, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetSolControlParameters falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTimeStep(self, Name: str):
        """This function retrieves the time step data for the specified load case. The function returns
        zero if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        nstep (output): The number of output time steps.
        DT (output): The output time step size.
        """
        _r = self._raw.GetTimeStep(Name, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.GetTimeStep falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a nonlinear modal history analysis case. If this function is
        called for an existing load case, all items for the case are reset to their default
        values. The function returns zero if the load case is successfully initialized;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampConstant(self, Name: str, Damp: float):
        """This function sets constant modal damping for the specified load case. The function returns
        zero if the damping is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        Damp (input): The constant damping for all modes (0 <= Damp < 1).
        """
        _r = self._raw.SetDampConstant(Name, Damp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetDampConstant falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampInterpolated(self, Name: str, DampType: int, NumberItems: int, Time: list[float], Damp: list[float]):
        """This function sets interpolated modal damping data for the specified load case. The function
        returns zero if the damping is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        DampType (input): This is 5 or 6, indicating the interpolated modal damping type. 5
            = Interpolated damping by period 6 = Interpolated damping by frequency
        NumberItems (input): The number of Time and Damp pairs.
        Time (input): This is an array that includes the period or the frequency, depending
            on the value of the DampType item. [s] for DampType = 5 and [cyc/s] for DampType
            = 6
        Damp (input): This is an array that includes the damping for the specified period of
            frequency (0 <= Damp < 1).
        """
        _r = self._raw.SetDampInterpolated(Name, DampType, NumberItems, Time, Damp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetDampInterpolated falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampOverrides(self, Name: str, NumberItems: int, Mode: list[int], Damp: list[float]):
        """This function sets the modal damping overrides for the specified load case. The function
        returns zero if the overrides are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        NumberItems (input): The number of Mode and Damp pairs.
        Mode (input): This is an array that includes a mode number.
        Damp (input): This is an array that includes the damping for the specified mode (0
            <= Damp < 1).
        """
        _r = self._raw.SetDampOverrides(Name, NumberItems, Mode, Damp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetDampOverrides falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampProportional(self, Name: str, DampType: int, Dampa: float, Dampb: float, Dampf1: float, Dampf2: float, Dampd1: float, Dampd2: float):
        """This function sets proportional modal damping data for the specified load case. The function
        returns zero if the damping is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        DampType (input): This is 1, 2 or 3, indicating the proportional modal damping type.
            1 = Mass and stiffness proportional damping by direct specification 2 = Mass and
            stiffness proportional damping by period 3 = Mass and stiffness proportional
            damping by frequency
        Dampa (input): The mass proportional damping coefficient. This item applies only
            when DampType = 1.
        Dampb (input): The stiffness proportional damping coefficient. This item applies
            only when DampType = 1.
        Dampf1 (input): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (input): This is the period or the frequency (depending on the value of the
            DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampd1 (input): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (input): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.SetDampProportional(Name, DampType, Dampa, Dampb, Dampf1, Dampf2, Dampd1, Dampd2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetDampProportional falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        InitialCase (input): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it continues from the end of another nonlinear
            modal time history load case. If the specified initial case is not a nonlinear
            modal time history load case, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], Func: list[str], SF: list[float], TF: list[float], AT: list[float], CSys: list[str], Ang: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load or Accel, indicating the type
            of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (input): This is an array that includes the name of the time history function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        TF (input): This is an array that includes the time scale factor of each load
            assigned to the load case.
        AT (input): This is an array that includes the arrival time of each load assigned to
            the load case.
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (input): This is an array that includes the angle between the acceleration local
            1 axis and the +X-axis of the coordinate system specified by the CSys item. The
            rotation is about the Z-axis of the specified coordinate system. [deg] This item
            applies only when the LoadType item is Accel.
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, Func, SF, TF, AT, CSys, Ang)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetModalCase(self, Name: str, ModalCase: str):
        """This function sets the modal case for the specified analysis case. The function returns zero
        if the modal case is successfully set; otherwise it returns a nonzero value. If the
        specified modal case is not actually a modal case, the program automatically
        replaces it with the first modal case it can find. If no modal load cases exist, an
        error is returned.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        ModalCase (input): This is the name of an existing modal load case. It specifies the
            modal load case on which any mode-type load assignments to the specified load
            case are based.
        """
        _r = self._raw.SetModalCase(Name, ModalCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetModalCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetSolControlParameters(self, Name: str, tstat: float, dtmax: float, dtmin: float, ftol: float, etol: float, itmax: int, itmin: int, Cf: float):
        """This function sets the solution control parameters for the specified load case. The function
        returns zero if the parameters are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing nonlinear modal time history analysis case.
        tstat (input): The static period.
        dtmax (input): The maximum substep size.
        dtmin (input): The minimum substep size.
        ftol (input): The relative force convergence tolerance.
        etol (input): The relative energy convergence tolerance.
        itmax (input): The maximum iteration limit.
        itmin (input): The minimum iteration limit.
        Cf (input): The convergence factor.
        """
        _r = self._raw.SetSolControlParameters(Name, tstat, dtmax, dtmin, ftol, etol, itmax, itmin, Cf)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetSolControlParameters falhou (ret={_r})".format(_r=_r))
        return None

    def SetTimeStep(self, Name: str, nstep: int, DT: float):
        """This function sets the time step data for the specified load case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing nonlinear modal history analysis case.
        nstep (input): The number of output time steps.
        DT (input): The output time step size.
        """
        _r = self._raw.SetTimeStep(Name, nstep, DT)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistNonlinear.SetTimeStep falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_PSD:
    """Wrapper para SapModel.LoadCases.PSD."""

    def __init__(self, raw):
        self._raw = raw

    def GetDampConstant(self, Name: str):
        """This function retrieves the constant hysteretic damping for all frequencies assigned to the
        specified load case. The function returns zero if the damping is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case that has
            constant damping.
        HysConMassCoeff (output): The mass proportional damping coefficient.
        HysConStiffCoeff (output): The stiffness proportional damping coefficient.
        """
        _r = self._raw.GetDampConstant(Name, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.GetDampConstant falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampInterpolated(self, Name: str):
        """This function retrieves the interpolated hysteretic damping by frequency assigned to the
        specified load case. The function returns zero if the damping is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case that has
            interpolated damping.
        HysIntFreqUnits (output): This is 1 or 2, indicating the units for the frequency. 1
            = Hz [cyc/s] 2 = RPM
        HysIntNumFreqs (output): The number of sets of frequency, mass coefficient and
            stiffness coefficient data.
        HysIntFreq (output): This is an array of frequencies. The frequency is either in Hz
            or RPM depending on the value of HysIntFreqUnits.
        HysIntMassCoeff (output): This is an array that includes the mass proportional
            damping coefficient.
        HysIntStiffCoeff (output): This is an array that includes the stiffness proportional
            damping coefficient.
        """
        _r = self._raw.GetDampInterpolated(Name, 0, 0, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.GetDampInterpolated falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampType(self, Name: str):
        """This function retrieves the hysteretic damping type for the specified load case. The
        function returns zero if the type is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case.
        DampType (output): This is 1 or 2, indicating the hysteretic damping type for the
            load case. 1 = Constant hysteretic damping for all frequencies 2 = Interpolated
            hysteretic damping by frequency
        """
        _r = self._raw.GetDampType(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.GetDampType falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetFreqData(self, Name: str, FreqAddModal: bool, FreqAddModalDev: bool, FreqAddSpecified: bool):
        """This function retrieves the frequency data for the specified load case. The function returns
        zero if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case.
        FreqFirst (output): The first frequency. [cyc/s]
        FreqLast (output): The last frequency. [cyc/s]
        FreqNumIncs (output): The number of frequency increments.
        FreqAddModal (input): If this item is True, modal frequencies are added.
        FreqAddModalDev (input): If this item is True, signed fractional deviations from
            modal frequencies are added.
        FreqAddSpecified (input): If this item is True, specified frequencies are added.
        FreqNumModalDev (output): The number of signed fractional deviations from modal
            frequencies that are added. This item applies only when FreqAddModalDev = True.
        FreqModalDev (output): This is an array that includes the added signed fractional
            deviations from modal frequencies. This item applies only when FreqAddModalDev =
            True.
        FreqNumSpecified (output): The number of specified frequencies that are added. This
            item applies only when FreqAddSpecified = True.
        FreqSpecified (output): This is an array that includes the added specified
            frequencies. This item applies only when FreqAddModalDev = True.
        """
        _r = self._raw.GetFreqData(Name, 0.0, 0.0, 0, FreqAddModal, FreqAddModalDev, FreqAddSpecified, 0, [], 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.GetFreqData falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case.
        InitialCase (output): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float], CSys: list[str]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (output): This is an array that includes the name of the power spectral density
            function associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        PhaseAngle (output): This is an array that includes the phase angle. [deg]
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (output): This is an array that includes the angle between the acceleration
            local 1 axis and the +X-axis of the coordinate system specified by the CSys
            item. The rotation is about the Z-axis of the specified coordinate system. [deg]
            This item applies only when the LoadType item is Accel.
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, [], SF, [], CSys, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.GetLoads falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a power spectral density analysis case. If this function is called
        for an existing load case, all items for the case are reset to their default value.
        The function returns zero if the load case is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampConstant(self, Name: str, HysConMassCoeff: float, HysConStiffCoeff: float):
        """This function sets constant hysteretic damping for all frequencies for the specified load
        case. The function returns zero if the damping is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case.
        HysConMassCoeff (input): The mass proportional damping coefficient.
        HysConStiffCoeff (input): The stiffness proportional damping coefficient.
        """
        _r = self._raw.SetDampConstant(Name, HysConMassCoeff, HysConStiffCoeff)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.SetDampConstant falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampInterpolated(self, Name: str, HysIntFreqUnits: int, HysIntNumFreqs: int, HysIntFreq: list[float], HysIntMassCoeff: list[float], HysIntStiffCoeff: list[float]):
        """This function sets interpolated hysteretic damping by frequency for the specified load case.
        The function returns zero if the damping is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case.
        HysIntFreqUnits (input): This is either 1 or 2, indicating the units for the
            frequency. 1 = Hz [cyc/s] 2 = RPM
        HysIntNumFreqs (input): The number of sets of frequency, mass coefficient and
            stiffness coefficient data.
        HysIntFreq (input): This is an array of frequencies. The frequency is either in Hz
            or RPM depending on the value of HysIntFreqUnits.
        HysIntMassCoeff (input): This is an array that includes the mass proportional
            damping coefficient.
        HysIntStiffCoeff (input): This is an array that includes the stiffness proportional
            damping coefficient.
        """
        _r = self._raw.SetDampInterpolated(Name, HysIntFreqUnits, HysIntNumFreqs, HysIntFreq, HysIntMassCoeff, HysIntStiffCoeff)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.SetDampInterpolated falhou (ret={_r})".format(_r=_r))
        return None

    def SetFreqData(self, Name: str, FreqFirst: float, FreqLast: float, FreqNumIncs: int, FreqAddModal: bool, FreqAddModalDev: bool, FreqAddSpecified: bool, FreqNumModalDev: int, FreqModalDev: list[float], FreqNumSpecified: int, FreqSpecified: list[float]):
        """This function sets the frequency data for the specified load case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case.
        FreqFirst (input): The first frequency. [cyc/s]
        FreqLast (input): The last frequency. [cyc/s]
        FreqNumIncs (input): The number of frequency increments.
        FreqAddModal (input): If this item is True, modal frequencies are added.
        FreqAddModalDev (input): If this item is True, signed fractional deviations from
            modal frequencies are added.
        FreqAddSpecified (input): If this item is True, specified frequencies are added.
        FreqNumModalDev (input): The number of signed fractional deviations from modal
            frequencies that are added. This item applies only when FreqAddModalDev = True.
        FreqModalDev (input): This is an array that includes the added signed fractional
            deviations from modal frequencies. This item applies only when FreqAddModalDev =
            True.
        FreqNumSpecified (input): The number of specified frequencies that are added. This
            item applies only when FreqAddSpecified = True.
        FreqSpecified (input): This is an array that includes the added specified
            frequencies. This item applies only when FreqAddModalDev = True.
        """
        _r = self._raw.SetFreqData(Name, FreqFirst, FreqLast, FreqNumIncs, FreqAddModal, FreqAddModalDev, FreqAddSpecified, FreqNumModalDev, FreqModalDev, FreqNumSpecified, FreqSpecified)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.SetFreqData falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing power spectral density analysis case.
        InitialCase (input): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], Func: list[str], SF: list[float], PhaseAngle: list[float], CSys: list[str], Ang: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing power spectral density analysis case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (input): This is an array that includes the name of the power spectral density
            function associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        PhaseAngle (input): This is an array that includes the phase angle. [deg]
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies pnly when the LoadType item is Accel.
        Ang (input): This is an array that includes the angle between the acceleration local
            1 axis and the +X-axis of the coordinate system specified by the CSys item. The
            rotation is about the Z-axis of the specified coordinate system. [deg] This item
            applies only when the LoadType item is Accel.
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, Func, SF, PhaseAngle, CSys, Ang)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.PSD.SetLoads falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_ResponseSpectrum:
    """Wrapper para SapModel.LoadCases.ResponseSpectrum."""

    def __init__(self, raw):
        self._raw = raw

    def GetDampConstant(self, Name: str):
        """This function retrieves the constant modal damping for all modes assigned to the specified
        load case. The function returns zero if the option is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case that has constant
            damping.
        Damp (output): The constant damping for all modes (0 <= Damp < 1).
        """
        _r = self._raw.GetDampConstant(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetDampConstant falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetDampInterpolated(self, Name: str):
        """This function retrieves the interpolated modal damping data assigned to the specified load
        case. The function returns zero if the option is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case that has
            interpolated damping.
        DampType (output): This is either 5 or 6, indicating the interpolated modal damping
            type. 5 = Interpolated damping by period 6 = Interpolated damping by frequency
        NumberItems (output): The number of Time and Damp pairs.
        Time (output): This is an array that includes the period or the frequency depending
            on the value of the DampType item. [s] for DampType = 5 and [cyc/s] for DampType
            = 6
        Damp (output): This is an array that includes the damping for the specified period
            of frequency (0 <= Damp < 1).
        """
        _r = self._raw.GetDampInterpolated(Name, 0, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetDampInterpolated falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampOverrides(self, Name: str):
        """This function retrieves the modal damping overrides assigned to the specified load case. The
        function returns zero if the overrides are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        NumberItems (output): The number of Mode and Damp pairs.
        Mode (output): This is an array that includes a mode number.
        Damp (output): This is an array that includes the damping for the specified mode (0
            <= Damp < 1).
        """
        _r = self._raw.GetDampOverrides(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetDampInterpolated falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampProportional(self, Name: str):
        """This function retrieves the proportional modal damping data assigned to the specified load
        case. The function returns zero if the option is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case that has
            proportional damping.
        DampType (output): This is 1, 2 or 3, indicating the proportional modal damping
            type. 1 = Mass and stiffness proportional damping by direct specification 2 =
            Mass and stiffness proportional damping by period 3 = Mass and stiffness
            proportional damping by frequency
        Dampa (output): The mass proportional damping coefficient.
        Dampb (output): The stiffness proportional damping coefficient.
        Dampf1 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampd1 (output): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (output): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.GetDampProportional(Name, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetDampProportional falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampType(self, Name: str):
        """This function retrieves the modal damping type for the specified load case. The function
        returns zero if the type is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing response spectrum load case.
        DampType (output): This is 1, 2, 3, 4, 5 or 6, indicating the modal damping type for
            the load case. 1 = Mass and stiffness proportional damping by direct
            specification 2 = Mass and stiffness proportional damping by period 3 = Mass and
            stiffness proportional damping by frequency 4 = Constant damping for all modes 5
            = Interpolated damping by period 6 = Interpolated damping by frequency
        """
        _r = self._raw.GetDampType(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetDampType falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetDiaphragmEccentricityOverride(self, Name: str):
        """This function retrieves the diaphragm eccentricity overrides for a response spectrum load
        case. The function returns zero if the overrides are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        Num (output): The number of diaphragm eccentricity overrides for the specified load
            case.
        Diaph (output): This is an array that includes the names of the diaphragms that have
            eccentricity overrides.
        Eccen (output): This is an array that includes the eccentricity applied to each
            diaphragm. [L]
        """
        _r = self._raw.GetDiaphragmEccentricityOverride(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetDiaphragmEccentricityOverride falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDirComb(self, Name: str):
        """This function retrieves the directional combination option assigned to the specified load
        case. The function returns zero if the option is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        MyType (output): This is 1, 2, or 3, indicating the directional combination option.
            1 = SRSS 2 = ABS 3 = CQC3
        SF (output): This item applies only when MyType = 2. It is the ABS scale factor.
        """
        _r = self._raw.GetDirComb(Name, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetDirComb falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetEccentricity(self, Name: str):
        """This function retrieves the eccentricity ratio that applies to all diaphragms for the
        specified load case. The function returns zero if the ratio is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        Eccen (output): The eccentricity ratio that applies to all diaphragms.
        """
        _r = self._raw.GetEccentricity(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetEccentricity falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, SF: list[float], CSys: list[str]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadName (output): This is an array that includes U1, U2, U3, R1, R2 or R3,
            indicating the direction of the load.
        Func (output): This is an array that includes the name of the response spectrum
            function associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed.
        Ang (output): This is an array that includes the angle between the acceleration
            local 1 axis and the +X-axis of the coordinate system specified by the CSys
            item. The rotation is about the Z-axis of the specified coordinate system. [deg]
        """
        _r = self._raw.GetLoads(Name, NumberLoads, [], [], SF, CSys, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetLoads falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetModalCase(self, Name: str):
        """This function retrieves the modal case assigned to the specified load case. The function
        returns zero if the modal case is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        ModalCase (output): This is None or the name of an existing modal analysis case. It
            specifies the modal load case on which any mode-type load assignments to the
            specified load case are based.
        """
        _r = self._raw.GetModalCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetModalCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetModalComb_1(self, Name: str):
        """This function retrieves the modal combination option assigned to the specified load case.
        The function returns zero if the option is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        MyType (output): This is 1, 2, 3, 4, 5 or 6, indicating the modal combination
            option. 1 = CQC 2 = SRSS 3 = Absolute 4 = GMC 5 = NRC 10 percent 6 = Double sum
        F1 (output): The GMC f1 factor. This item does not apply when MyType = 3. [cyc/s]
        F2 (output): The GMC f2 factor. This item does not apply when MyType = 3. [cyc/s]
        PeriodicRigidCombType (output): This is 1 or 2, indicating the periodic plus rigid
            modal combination option. 1 = SRSS 2 = Absolute
        td (output): This item applies only when MyType = 6. It is the factor td. [s]
        """
        _r = self._raw.GetModalComb_1(Name, 0, 0.0, 0.0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.GetModalComb_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a response spectrum analysis case. If this function is called for
        an existing load case, all items for the case are reset to their default value. The
        function returns zero if the load case is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampConstant(self, Name: str, Damp: float):
        """This function sets constant modal damping for the specified load case. The function returns
        zero if the damping is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        Damp (input): The constant damping for all modes (0 <= Damp < 1).
        """
        _r = self._raw.SetDampConstant(Name, Damp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetDampConstant falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampInterpolated(self, Name: str, DampType: int, NumberItems: int, Time: list[float], Damp: list[float]):
        """This function sets interpolated modal damping data for the specified load case. The function
        returns zero if the damping is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing response spectrum load case.
        DampType (input): This is either 5 or 6, indicating the interpolated modal damping
            type. 5 = Interpolated damping by period 6 = Interpolated damping by frequency
        NumberItems (input): The number of Time and Damp pairs.
        Time (input): This is an array that includes the period or the frequency depending
            on the value of the DampType item. [s] for DampType = 5 and [cyc/s] for DampType
            = 6
        Damp (input): This is an array that includes the damping for the specified period of
            frequency (0 <= Damp < 1).
        """
        _r = self._raw.SetDampInterpolated(Name, DampType, NumberItems, Time, Damp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetDampInterpolated falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampOverrides(self, Name: str, NumberItems: int, Mode: list[int], Damp: list[float]):
        """This function sets the modal damping overrides for the specified load case. The function
        returns zero if the overrides are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing response spectrum load case.
        NumberItems (input): The number of Mode and Damp pairs.
        Mode (input): This is an array that includes a mode number.
        Damp (input): This is an array that includes the damping for the specified mode (0
            <= Damp < 1).
        """
        _r = self._raw.SetDampOverrides(Name, NumberItems, Mode, Damp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetDampOverrides falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampProportional(self, Name: str, DampType: int, Dampa: float, Dampb: float, Dampf1: float, Dampf2: float, Dampd1: float, Dampd2: float):
        """This function sets proportional modal damping data for the specified load case. The function
        returns zero if the damping is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing response spectrum load case.
        DampType (input): This is 1, 2 or 3, indicating the proportional modal damping type.
            1 = Mass and stiffness proportional damping by direct specification 2 = Mass and
            stiffness proportional damping by period 3 = Mass and stiffness proportional
            damping by frequency
        Dampa (input): The mass proportional damping coefficient. This item applies only
            when DampType = 1.
        Dampb (input): The stiffness proportional damping coefficient. This item applies
            only when DampType = 1.
        Dampf1 (input): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (input): This is the period or the frequency (depending on the value of the
            DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampd1 (input): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (input): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.SetDampProportional(Name, DampType, Dampa, Dampb, Dampf1, Dampf2, Dampd1, Dampd2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetDampProportional falhou (ret={_r})".format(_r=_r))
        return None

    def SetDiaphragmEccentricityOverride(self, Name: str, Diaph: str, Eccen: float, Delete: bool = False):
        """This function assigns diaphragm eccentricity overrides for response spectrum load cases. The
        function returns zero if the overrides are successfully assigned; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
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
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetDiaphragmEccentricityOverride falhou (ret={_r})".format(_r=_r))
        return None

    def SetDirComb(self, Name: str, MyType: int, SF: float):
        """This function sets the directional combination option for the specified load case. The
        function returns zero if the option is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        MyType (input): This is 1, 2, or 3, indicating the directional combination option. 1
            = SRSS 2 = ABS 3 = CQC3
        SF (input): This item applies only when MyType = 2. It is the ABS scale factor.
        """
        _r = self._raw.SetDirComb(Name, MyType, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetDirComb falhou (ret={_r})".format(_r=_r))
        return None

    def SetEccentricity(self, Name: str, Eccen: float):
        """This function sets the eccentricity ratio that applies to all diaphragms for the specified
        load case. The function returns zero if the ratio is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        Eccen (input): The eccentricity ratio that applies to all diaphragms.
        """
        _r = self._raw.SetEccentricity(Name, Eccen)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetEccentricity falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadName: list[str], Func: list[str], SF: list[float], CSys: list[str], Ang: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing response spectrum load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadName (input): This is an array that includes U1, U2, U3, R1, R2 or R3,
            indicating the direction of the load.
        Func (input): This is an array that includes the name of the response spectrum
            function associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed.
        Ang (input): This is an array that includes the angle between the acceleration local
            1 axis and the +X-axis of the coordinate system specified by the CSys item. The
            rotation is about the Z-axis of the specified coordinate system. [deg]
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadName, Func, SF, CSys, Ang)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetModalCase(self, Name: str, ModalCase: str):
        """This function sets the modal case for the specified analysis case. The function returns zero
        if the initial condition is successfully set; otherwise it returns a nonzero value.
        If the specified modal case is not actually a modal case, the program automatically
        replaces it with the first modal case it can find. If no modal load cases exist, an
        error is returned.
    
        Name (input): The name of an existing response spectrum load case.
        ModalCase (input): This is the name of an existing modal load case. It specifies the
            modal load case on which any mode-type load assignments to the specified load
            case are based.
        """
        _r = self._raw.SetModalCase(Name, ModalCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetModalCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetModalComb_1(self, Name: str, MyType: int, F1: float = 1, F2: float = 0, PeriodicRigidCombType: int = 1, td: float = 60):
        """This function sets the modal combination option for the specified load case. The function
        returns zero if the option is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing response spectrum load case.
        MyType (input): This is 1, 2, 3, 4, 5 or 6, indicating the modal combination option.
            1 = CQC 2 = SRSS 3 = Absolute 4 = GMC 5 = NRC 10 percent 6 = Double sum
        F1 (input): The GMC f1 factor. This item does not apply when MyType = 3. [cyc/s]
        F2 (input): The GMC f2 factor. This item does not apply when MyType = 3. [cyc/s]
        PeriodicRigidCombType (input): This is 1 or 2, indicating the periodic plus rigid
            modal combination option. 1 = SRSS 2 = Absolute
        """
        _r = self._raw.SetModalComb_1(Name, MyType, F1, F2, PeriodicRigidCombType, td)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ResponseSpectrum.SetModalComb_1 falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_StaticLinearMultistep:
    """Wrapper para SapModel.LoadCases.StaticLinearMultistep."""

    def __init__(self, raw):
        self._raw = raw

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise,
        it returns a nonzero value.
    
        Name (input): The name of an existing static linear multistep analysis case.
        InitialCase (output): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinearMultistep.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of an existing static linear multistep analysis case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinearMultistep.GetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetCase(self, Name: str):
        """This function initializes a static linear multistep analysis case. If this function is
        called for an existing load case, all items for the case are reset to their default
        value. The function returns zero if the load case is successfully initialized;
        otherwise, it returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinearMultistep.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static linear multistep analysis case.
        InitialCase (input): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinearMultistep.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing static linear multistep analysis case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticLinearMultistep.SetLoads falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_HyperStatic:
    """Wrapper para SapModel.LoadCases.HyperStatic."""

    def __init__(self, raw):
        self._raw = raw

    def GetBaseCase(self, Name: str):
        """This function retrieves the base case for the specified hyperstatic load case. The function
        returns zero if the base case is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing hyperstatic load case.
        BaseCase (output): The name of an existing static linear load case that is the base
            case for the specified hyperstatic load case.
        """
        _r = self._raw.GetBaseCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.HyperStatic.GetBaseCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetBaseCase(self, Name: str, BaseCase: str):
        """This function sets the base case for the specified hyperstatic load case. The function
        returns zero if the base case is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing hyperstatic load case.
        BaseCase (input): The name of an existing static linear load case that is the base
            case for the specified hyperstatic load case.
        """
        _r = self._raw.SetBaseCase(Name, BaseCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.HyperStatic.SetBaseCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetCase(self, Name: str):
        """This function initializes a hyperstatic load case. If this function is called for an
        existing load case, all items for the case are reset to their default value. The
        function returns zero if the load case is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.HyperStatic.SetCase falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_ModHistLinear:
    """Wrapper para SapModel.LoadCases.ModHistLinear."""

    def __init__(self, raw):
        self._raw = raw

    def GetDampConstant(self, Name: str):
        """This function retrieves the constant modal damping for all modes assigned to the specified
        load case. The function returns zero if the option is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case that has
            constant damping.
        Damp (output): The constant damping for all modes (0 <= Damp < 1).
        """
        _r = self._raw.GetDampConstant(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.GetDampConstant falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetDampInterpolated(self, Name: str):
        """This function retrieves the interpolated modal damping data assigned to the specified load
        case. The function returns zero if the option is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case that has
            interpolated damping.
        DampType (output): This is 5 or 6, indicating the interpolated modal damping type. 5
            = Interpolated damping by period 6 = Interpolated damping by frequency
        NumberItems (output): The number of Time and Damp pairs.
        Time (output): This is an array that includes the period or the frequency, depending
            on the value of the DampType item. [s] for DampType = 5 and [cyc/s] for DampType
            = 6
        Damp (output): This is an array that includes the damping for the specified period
            of frequency (0 <= Damp < 1).
        """
        _r = self._raw.GetDampInterpolated(Name, 0, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.GetDampInterpolated falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampOverrides(self, Name: str):
        """This function retrieves the modal damping overrides assigned to the specified load case. The
        function returns zero if the overrides are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case.
        NumberItems (output): The number of Mode and Damp pairs.
        Mode (output): This is an array that includes a mode number.
        Damp (output): This is an array that includes the damping for the specified mode (0
            <= Damp < 1).
        """
        _r = self._raw.GetDampOverrides(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.GetDampInterpolated falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampProportional(self, Name: str):
        """This function retrieves the proportional modal damping data assigned to the specified load
        case. The function returns zero if the option is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case that has
            proportional damping.
        DampType (output): This is 1, 2 or 3, indicating the proportional modal damping
            type. 1 = Mass and stiffness proportional damping by direct specification 2 =
            Mass and stiffness proportional damping by period 3 = Mass and stiffness
            proportional damping by frequency
        Dampa (output): The mass proportional damping coefficient.
        Dampb (output): The stiffness proportional damping coefficient.
        Dampf1 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (output): This is the period or the frequency (depending on the value of the
            DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampd1 (output): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (output): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.GetDampProportional(Name, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.GetDampProportional falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampType(self, Name: str):
        """This function retrieves the modal damping type for the specified load case. The function
        returns zero if the type is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing linear modal history analysis case.
        DampType (output): This is 1, 2, 3, 4, 5 or 6, indicating the modal damping type for
            the load case. 1 = Mass and stiffness proportional damping by direct
            specification 2 = Mass and stiffness proportional damping by period 3 = Mass and
            stiffness proportional damping by frequency 4 = Constant damping for all modes 5
            = Interpolated damping by period 6 = Interpolated damping by frequency
        """
        _r = self._raw.GetDampType(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.GetDampType falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float], TF: list[float], AT: list[float], CSys: list[str]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load or Accel, indicating the type
            of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (output): This is an array that includes the name of the time history function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        TF (input): This is an array that includes the time scale factor of each load
            assigned to the load case.
        AT (input): This is an array that includes the arrival time of each load assigned to
            the load case.
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (output): This is an array that includes the angle between the acceleration
            local 1 axis and the +X-axis of the coordinate system specified by the CSys
            item. The rotation is about the Z-axis of the specified coordinate system. [deg]
            This item applies only when the LoadType item is Accel.
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, [], SF, TF, AT, CSys, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.GetLoads falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetModalCase(self, Name: str):
        """This function retrieves the modal case assigned to the specified load case. The function
        returns zero if the modal case is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case.
        ModalCase (output): This is None or the name of an existing modal analysis case. It
            specifies the modal load case on which any mode-type load assignments to the
            specified load case are based.
        """
        _r = self._raw.GetModalCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.GetModalCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMotionType(self, Name: str):
        """This function retrieves the motion type for the specified load case. The function returns
        zero if the motion type is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing linear modal history analysis case.
        MotionType (output): This is 1 or 2, indicating the time history motion type. 1 =
            Transient 2 = Periodic
        """
        _r = self._raw.GetMotionType(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.GetMotionType falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetTimeStep(self, Name: str):
        """This function retrieves the time step data for the specified load case. The function returns
        zero if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case.
        nstep (output): The number of output time steps.
        DT (output): The output time step size.
        """
        _r = self._raw.GetTimeStep(Name, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.GetTimeStep falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a linear modal history analysis case. If this function is called
        for an existing load case then all items for the case are reset to their default
        value. The function returns zero if the load case is successfully initialized;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampConstant(self, Name: str, Damp: float):
        """This function sets constant modal damping for the specified load case. The function returns
        zero if the damping is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case.
        Damp (input): The constant damping for all modes (0 <= Damp < 1).
        """
        _r = self._raw.SetDampConstant(Name, Damp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.SetDampConstant falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampInterpolated(self, Name: str, DampType: int, NumberItems: int, Time: list[float], Damp: list[float]):
        """This function sets interpolated modal damping data for the specified load case. The function
        returns zero if the damping is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing linear modal history analysis case.
        DampType (input): This is 5 or 6, indicating the interpolated modal damping type. 5
            = Interpolated damping by period 6 = Interpolated damping by frequency
        NumberItems (input): The number of Time and Damp pairs.
        Time (input): This is an array that includes the period or the frequency, depending
            on the value of the DampType item. [s] for DampType = 5 and [cyc/s] for DampType
            = 6
        Damp (input): This is an array that includes the damping for the specified period of
            frequency (0 <= Damp < 1).
        """
        _r = self._raw.SetDampInterpolated(Name, DampType, NumberItems, Time, Damp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.SetDampInterpolated falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampOverrides(self, Name: str, NumberItems: int, Mode: list[int], Damp: list[float]):
        """This function sets the modal damping overrides for the specified load case. The function
        returns zero if the overrides are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing linear modal history analysis case.
        NumberItems (input): The number of Mode and Damp pairs.
        Mode (input): This is an array that includes a mode number.
        Damp (input): This is an array that includes the damping for the specified mode (0
            <= Damp < 1).
        """
        _r = self._raw.SetDampOverrides(Name, NumberItems, Mode, Damp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.SetDampOverrides falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampProportional(self, Name: str, DampType: int, Dampa: float, Dampb: float, Dampf1: float, Dampf2: float, Dampd1: float, Dampd2: float):
        """This function sets proportional modal damping data for the specified load case. The function
        returns zero if the damping is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing linear modal history analysis case.
        DampType (input): This is 1, 2 or 3, indicating the proportional modal damping type.
            1 = Mass and stiffness proportional damping by direct specification 2 = Mass and
            stiffness proportional damping by period 3 = Mass and stiffness proportional
            damping by frequency
        Dampa (input): The mass proportional damping coefficient. This item applies only
            when DampType = 1.
        Dampb (input): The stiffness proportional damping coefficient. This item applies
            only when DampType = 1.
        Dampf1 (input): This is the period or the frequency (depending on the value of the
            DampType item) for point 1. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampf2 (input): This is the period or the frequency (depending on the value of the
            DampType item) for point 2. [s] for DampType = 2 and [cyc/s] for DampType = 3
            This item applies only when DampType = 2 or 3.
        Dampd1 (input): This is the damping at point 1 (0 <= Dampd1 < 1). This item applies
            only when DampType = 2 or 3.
        Dampd2 (input): This is the damping at point 2 (0 <= Dampd2 < 1). This item applies
            only when DampType = 2 or 3.
        """
        _r = self._raw.SetDampProportional(Name, DampType, Dampa, Dampb, Dampf1, Dampf2, Dampd1, Dampd2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.SetDampProportional falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], Func: list[str], SF: list[float], TF: list[float], AT: list[float], CSys: list[str], Ang: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load or Accel, indicating the type
            of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (input): This is an array that includes the name of the time history function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        TF (input): This is an array that includes the time scale factor of each load
            assigned to the load case.
        AT (input): This is an array that includes the arrival time of each load assigned to
            the load case.
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (input): This is an array that includes the angle between the acceleration local
            1 axis and the +X-axis of the coordinate system specified by the CSys item. The
            rotation is about the Z-axis of the specified coordinate system. [deg] This item
            applies only when the LoadType item is Accel.
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, Func, SF, TF, AT, CSys, Ang)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetModalCase(self, Name: str, ModalCase: str):
        """This function sets the modal case for the specified analysis case. The function returns zero
        if the modal case is successfully set; otherwise it returns a nonzero value. If the
        specified modal case is not actually a modal case, the program automatically
        replaces it with the first modal case it can find. If no modal load cases exist, an
        error is returned.
    
        Name (input): The name of an existing linear modal history analysis case.
        ModalCase (input): This is the name of an existing modal load case. It specifies the
            modal load case on which any mode-type load assignments to the specified load
            case are based.
        """
        _r = self._raw.SetModalCase(Name, ModalCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.SetModalCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetMotionType(self, Name: str, MotionType: int):
        """This function sets the motion type for the specified analysis case. The function returns
        zero if the motion type is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case.
        MotionType (input): This is 1 or 2, indicating the time history motion type. 1 =
            Transient 2 = Periodic
        """
        _r = self._raw.SetMotionType(Name, MotionType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.SetMotionType falhou (ret={_r})".format(_r=_r))
        return None

    def SetTimeStep(self, Name: str, nstep: int, DT: float):
        """This function sets the time step data for the specified load case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear modal history analysis case.
        nstep (input): The number of output time steps.
        DT (input): The output time step size.
        """
        _r = self._raw.SetTimeStep(Name, nstep, DT)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModHistLinear.SetTimeStep falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_ModalEigen:
    """Wrapper para SapModel.LoadCases.ModalEigen."""

    def __init__(self, raw):
        self._raw = raw

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing modal eigen load case.
        InitialCase (output): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalEigen.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing modal eigen load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load, Accel or Link, indicating the
            type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load. If the LoadType item is Link, this
            item is not used.
        TargetPar (output): This is an array that includes the target mass participation
            ratio.
        StaticCorrect (output): This is an array that includes either 0 or 1, indicating if
            static correction modes are to be calculated.
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalEigen.GetLoads falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNumberModes(self, Name: str):
        """This function retrieves the number of modes requested for the specified load case. The
        function returns zero if the number of modes is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing modal eigen load case.
        MaxModes (output): The maximum number of modes requested.
        MinModes (output): The minimum number of modes requested.
        """
        _r = self._raw.GetNumberModes(Name, 0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalEigen.GetNumberModes falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetParameters(self, Name: str):
        """This function retrieves various parameters for the specified load case. The function returns
        zero if the parameters are successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing modal eigen load case.
        EigenShiftFreq (output): The eigenvalue shift frequency. [cyc/s]
        EigenCutOff (output): The eigencutoff frequency radius. [cyc/s]
        EigenTol (output): The relative convergence tolerance for eigenvalues.
        AllowAutoFreqShift (output): This is either 0 or 1, indicating if automatic
            frequency shifting is allowed. 0 = Automatic frequency shifting is NOT allowed 1
            = Automatic frequency shifting is allowed
        """
        _r = self._raw.GetParameters(Name, 0.0, 0.0, 0.0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalEigen.GetParameters falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a modal eigen load case. If this function is called for an
        existing load case, all items for the case are reset to their default value. The
        function returns zero if the load case is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalEigen.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing modal eigen load case.
        InitialCase (input): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalEigen.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], TargetPar: list[float], StaticCorrect: list[bool]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing modal eigen load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load, Accel or Link, indicating the
            type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load. If the LoadType item is Link, this
            item is not used.
        TargetPar (input): This is an array that includes the target mass participation
            ratio.
        StaticCorrect (input): This is an array that includes either 0 or 1, indicating if
            static correction modes are to be calculated.
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, TargetPar, StaticCorrect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalEigen.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetNumberModes(self, Name: str, MaxModes: int, MinModes: int):
        """This function sets the number of modes requested for the specified load case. The function
        returns zero if the number of modes is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing modal eigen load case.
        MaxModes (input): The maximum number of modes requested.
        MinModes (input): The minimum number of modes requested.
        """
        _r = self._raw.SetNumberModes(Name, MaxModes, MinModes)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalEigen.SetNumberModes falhou (ret={_r})".format(_r=_r))
        return None

    def SetParameters(self, Name: str, EigenShiftFreq: float, EigenCutOff: float, EigenTol: float, AllowAutoFreqShift: int):
        """This function sets various parameters for the specified modal eigen load case. The function
        returns zero if the parameters are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing modal eigen load case.
        EigenShiftFreq (input): The eigenvalue shift frequency. [cyc/s]
        EigenCutOff (input): The eigencutoff frequency radius. [cyc/s]
        EigenTol (input): The relative convergence tolerance for eigenvalues.
        AllowAutoFreqShift (input): This is either 0 or 1, indicating if automatic frequency
            shifting is allowed. 0 = Automatic frequency shifting is NOT allowed 1 =
            Automatic frequency shifting is allowed
        """
        _r = self._raw.SetParameters(Name, EigenShiftFreq, EigenCutOff, EigenTol, AllowAutoFreqShift)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalEigen.SetParameters falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_StaticNonlinear:
    """Wrapper para SapModel.LoadCases.StaticNonlinear."""

    def __init__(self, raw):
        self._raw = raw

    def GetStageData_2(self, Name: str, Stage: int, MyName: list[str], SF: list[float]):
        """This function retrieves stage data for the specified stage in the specified load case. The
        function returns zero if the data is successfully retrieved; otherwise, it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear staged load case.
        Stage (input): The stage in the specified load case for which data is requested.
            Stages are numbered sequentially starting from 1.
        NumberOperations (output): The number of operations in the specified stage.
        Operation (output): This is an array that includes 1, 2, 3, 4, 5, 6, 7, or 11,
            indicating an operation type. 1 = Add structure 2 = Remove structure 3 = Load
            objects if new 4 = Load objects 5 = Change section properties 6 = Change section
            property modifiers 7 = Change releases 11 = Change section properties and age
        ObjectType (output): This is an array that includes the object type associated with
            the specified operation. The object type may be one of the following: Group
            Frame Cable Tendon Area Solid Link Point The following list shows which object
            types are applicable to each operation type: Operation = 1 (Add structure): All
            object types Operation = 2 (Remove structure): All object types Operation = 3
            (Load objects if new): All object types Operation = 4 (Load objects): All object
            types Operation = 5 (Change section properties): All object types except Point
            Operation = 6 (Change section property modifiers): Group, Frame, Cable, Area
            Operation = 7 (Change releases): Group, Frame Operation = 11 (Change section
            properties and age): All object types except Point
        ObjectName (output): This is an array that includes the name of the object
            associated with the specified operation. This is the name of a Group, Frame
            object, Cable object, Tendon object, Area object, Solid object, Link object or
            Point object, depending on the ObjectType item.
        Age (output): This is an array that includes the age of the added structure, at the
            time it is added, in days. This item applies only to operations with Operation =
            1.
        MyType (output): This is an array that includes a load type or an object type,
            depending on what is specified for the Operation item. This item applies only to
            operations with Operation = 3, 4, 5, 6, 7, or 11. When Operation = 3 or 4, this
            is an array that includes Load or Accel, indicating the load type of an added
            load. When Operation = 5 or 11, and the ObjectType item is Group, this is an
            array that includes Frame, Cable, Tendon, Area, Solid or Link, indicating the
            object type for which the section property is changed. When Operation = 6 and
            the ObjectType item is Group, this is an array that includes Frame, Cable or
            Area, indicating the object type for which the section property modifiers are
            changed. When Operation = 7 and the ObjectType item is Group, this is an array
            that includes Frame, indicating the object type for which the releases are
            changed. When Operation = 5, 6, 7, or 11, and the ObjectType item is not Group
            and not Point, this item is ignored and the type is picked up from the
            ObjectType item.
        MyName (input): This is an array that includes a load assignment or an object name,
            depending on what is specified for the Operation item. This item applies only to
            operations with Operation = 3, 4, 5, 6, 7, or 11. When Operation = 3 or 4, this
            is an array that includes the name of the load assigned to the operation. If the
            associated LoadType item is Load, this item is the name of a defined load
            pattern. If the associated LoadType item is Accel , this item is UX, UY, UZ, RX,
            RY or RZ, indicating the direction of the load. When Operation = 5 or 11, this
            is the name of a Frame, Cable, Tendon, Area, Solid or Link object, depending on
            the object type specified. When Operation = 6, this is the name of a Frame,
            Cable or Area object, depending on the object type specified. When Operation =
            7, this is the name of a Frame object.
        SF (input): This is an array that includes the scale factor for the load assigned to
            the operation, if any. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless This
            item applies only to operations with Operation = 3 or 4.
        """
        _r = self._raw.GetStageData_2(Name, Stage, 0, [], [], [], [], [], MyName, SF)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetStageData_2 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetStageDefinitions_2(self, Name: str):
        """This function retrieves the stage definition data for the specified load case. The function
        returns zero if the data is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear staged load case.
        NumberStages (output): The number of stages defined for the specified load case.
        Duration (output): This is an array that includes the duration in days for each
            stage.
        Output (output): This is an array that includes True or False, indicating if
            analysis output is to be saved for each stage.
        OutputName (output): This is an array that includes a user-specified output name for
            each stage.
        Comment (output): This is an array that includes a comment for each stage. The
            comment may be a blank string.
        """
        _r = self._raw.GetStageDefinitions_2(Name, 0, [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetStageDefinitions_2 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetStageData_2(self, Name: str, Stage: int, NumberOperations: int, Operation: list[int], ObjectType: list[str], ObjectName: list[str], Age: list[float], MyType: list[str], MyName: list[str], SF: list[float]):
        """This function sets the stage data for the specified stage in the specified load case. All
        previous stage data for the specified stage is cleared when this function is called.
        The function returns zero if the data is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear staged load case.
        Stage (input): The stage in the specified load case to which the data applies.
            Stages are numbered sequentially starting from 1.
        NumberOperations (input): The number of operations in the specified stage.
        Operation (input): This is an array that includes 1, 2, 3, 4, 5, 6, 7, or 11,
            indicating an operation type. 1 = Add structure 2 = Remove structure 3 = Load
            objects if new 4 = Load objects 5 = Change section properties 6 = Change section
            property modifiers 7 = Change releases 11 = Change section properties and age
        ObjectType (input): This is an array that includes the object type associated with
            the specified operation. The object type may be one of the following: Group
            Frame Cable Tendon Area Solid Link Point The following list shows which object
            types are applicable to each operation type: Operation = 1 (Add structure): All
            object types Operation = 2 (Remove structure): All object types Operation = 3
            (Load objects if new): All object types Operation = 4 (Load objects): All object
            types Operation = 5 (Change section properties): All object types except Point
            Operation = 6 (Change section property modifiers): Group, Frame, Cable, Area
            Operation = 7 (Change releases): Group, Frame Operation = 11 (Change section
            properties and age): All object types except Point
        ObjectName (input): This is an array that includes the name of the object associated
            with the specified operation. This is the name of a Group, Frame object, Cable
            object, Tendon object, Area object, Solid object, Link object or Point object,
            depending on the ObjectType item.
        Age (input): This is an array that includes the age of the added structure, at the
            time it is added, in days. This item applies only to operations with Operation =
            1.
        MyType (input): This is an array that includes a load type or an object type,
            depending on what is specified for the Operation item. This item applies only to
            operations with Operation = 3, 4, 5, 6, 7, or 11. When Operation = 3 or 4, this
            is an array that includes Load or Accel, indicating the load type of an added
            load. When Operation = 5 or 11, and the ObjectType item is Group, this is an
            array that includes Frame, Cable, Tendon, Area, Solid or Link, indicating the
            object type for which the section property is changed. When Operation = 6 and
            the ObjectType item is Group, this is an array that includes Frame, Cable or
            Area, indicating the object type for which the section property modifiers are
            changed. When Operation = 7 and the ObjectType item is Group, this is an array
            that includes Frame, indicating the object type for which the releases are
            changed. When Operation = 5, 6, 7, or 11, and the ObjectType item is not Group
            and not Point, this item is ignored and the type is picked up from the
            ObjectType item.
        MyName (input): This is an array that includes a load assignment or an object name,
            depending on what is specified for the Operation item. This item applies only to
            operations with Operation = 3, 4, 5, 6, 7 or 11. When Operation = 3 or 4, this
            is an array that includes the name of the load assigned to the operation. If the
            associated LoadType item is Load, this item is the name of a defined load
            pattern. If the associated LoadType item is Accel, this item is UX, UY, UZ, RX,
            RY or RZ, indicating the direction of the load. When Operation = 5 or 11, this
            is the name of a Frame, Cable, Tendon, Area, Solid or Link object, depending on
            the object type specified. When Operation = 6, this is the name of a Frame,
            Cable or Area object, depending on the object type specified. When Operation =
            7, this is the name of a Frame object.
        SF (input): This is an array that includes the scale factor for the load assigned to
            the operation, if any. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless This
            item applies only to operations with Operation = 3 or 4.
        """
        _r = self._raw.SetStageData_2(Name, Stage, NumberOperations, Operation, ObjectType, ObjectName, Age, MyType, MyName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetStageData_2 falhou (ret={_r})".format(_r=_r))
        return None

    def SetStageDefinitions_2(self, Name: str, NumberStages: int, Duration: list[float], Output: list[bool], OutputName: list[str], Comment: list[str]):
        """This function initializes the stage definition data for the specified load case. All
        previous stage definition data for the case is cleared when this function is called.
        The function returns zero if the data is successfully initialized; otherwise, it
        returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear staged load case.
        NumberStages (input): The number of stages defined for the specified load case.
        Duration (input): This is an array that includes the duration in days for each
            stage.
        Output (input): This is an array that includes True or False, indicating if analysis
            output is to be saved for each stage.
        OutputName (input): This is an array that includes a user-specified output name for
            each stage.
        Comment (input): This is an array that includes a comment for each stage. The
            comment may be a blank string.
        """
        _r = self._raw.SetStageDefinitions_2(Name, NumberStages, Duration, Output, OutputName, Comment)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetStageDefinitions_2 falhou (ret={_r})".format(_r=_r))
        return None

    def GetGeometricNonlinearity(self, Name: str):
        """This function retrieves the geometric nonlinearity option for the specified load case. The
        function returns zero if the option is successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        NLGeomType (output): This is 0, 1 or 2, indicating the geometric nonlinearity option
            selected for the load case. 0 = None 1 = P-delta 2 = P-delta plus large
            displacements
        """
        _r = self._raw.GetGeometricNonlinearity(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetGeometricNonlinearity falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetHingeUnloading(self, Name: str):
        """This function retrieves the hinge unloading option for the specified load case. The function
        returns zero if the option is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear load case.
        UnloadType (output): This is 1, 2 or 3, indicating the hinge unloading option
            selected for the load case. 1 = Unload entire structure 2 = Apply local
            redistribution 3 = Restart using secant stiffness
        """
        _r = self._raw.GetHingeUnloading(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetHingeUnloading falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        InitialCase (output): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts from the state at the end of a
            nonlinear static or nonlinear direct integration time history load case. If the
            specified initial case is a nonlinear static or nonlinear direct integration
            time history load case, the state at the end of that case is used. If the
            initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoadApplication(self, Name: str):
        """This function retrieves the load application control parameters for the specified load case.
        The function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        LoadControl (output): This is either 1 or 2, indicating the load application control
            method. 1 = Full load 2 = Displacement control
        DispType (output): This is either 1 or 2, indicating the control displacement type.
            1 = Conjugate displacement 2 = Monitored displacement This item applies only
            when displacement control is used, that is, LoadControl = 2.
        Displ (output): This item applies only when displacement control is used, that is,
            LoadControl = 2. The structure is loaded to a monitored displacement of this
            magnitude. [L] when DOF = 1, 2 or 3 and [rad] when DOF = 4, 5 or 6
        Monitor (output): This is either 1 or 2, indicating the monitored displacement. 1 =
            Displacement at a specified point object 2 = Generalized displacement
        DOF (output): This is 1, 2, 3, 4, 5 or 6, indicating the degree of freedom for which
            the displacement at a point object is monitored. 1 = U1 2 = U2 3 = U3 4 = R1 5 =
            R2 6 = R3 This item applies only when Monitor = 1.
        PointName (output): The name of the point object at which the displacement is
            monitored. This item applies only when Monitor = 1.
        GDispl (output): The name of the generalized displacement for which the displacement
            is monitored. This item applies only when Monitor = 2.
        """
        _r = self._raw.GetLoadApplication(Name, 0, 0, 0.0, 0, 0, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetLoadApplication falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def GetModalCase(self, Name: str):
        """This function retrieves the modal case assigned to the specified load case. The function
        returns zero if the modal case is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        ModalCase (output): This is either None or the name of an existing modal analysis
            case. It specifies the modal load case on which any mode-type load assignments
            to the specified load case are based.
        """
        _r = self._raw.GetModalCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetModalCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetResultsSaved(self, Name: str, SaveMultipleSteps: bool, PositiveOnly: bool):
        """This function retrieves the results saved parameters for the specified load case. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        SaveMultipleSteps (input): This item is True if multiple states are saved for the
            nonlinear analysis. It is False only if the final state is saved.
        MinSavedStates (output): This item applies only when SaveMultipleSteps = True. It is
            the minimum number of saved steps.
        MaxSavedStates (output): This item applies only when SaveMultipleSteps = True. It is
            the maximum number of saved steps.
        PositiveOnly (input): If this item is True, only positive displacement increments
            are saved. If it is False, all displacement increments are saved.
        """
        _r = self._raw.GetResultsSaved(Name, SaveMultipleSteps, 0, 0, PositiveOnly)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetResultsSaved falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSolControlParameters(self, Name: str, UseEventStepping: bool):
        """This function retrieves the solution control parameters for the specified load case. The
        function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        MaxTotalSteps (output): The maximum total steps per stage.
        MaxFailedSubSteps (output): The maximum null (zero) steps per stage.
        MaxIterCS (output): The maximum constant-stiffness iterations per step.
        MaxIterNR (output): The maximum Newton_Raphson iterations per step.
        TolConvD (output): The relative iteration convergence tolerance.
        UseEventStepping (input): This item is True if event-to-event stepping is used.
        TolEventD (output): The relative event lumping tolerance.
        MaxLineSearchPerIter (output): The maximum number of line searches per iteration.
        TolLineSearch (output): The relative line-search acceptance tolerance.
        LineSearchStepFact (output): The line-search step factor.
        """
        _r = self._raw.GetSolControlParameters(Name, 0, 0, 0, 0, 0.0, UseEventStepping, 0.0, 0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetSolControlParameters falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTargetForceParameters(self, Name: str, NoStop: bool):
        """This function retrieves the target force iteration parameters for the specified load case.
        The function returns zero if the parameters are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        TolConvF (output): The relative convergence tolerance for target force iteration.
        MaxIter (output): The maximum iterations per stage for target force iteration.
        AccelFact (output): The acceleration factor.
        NoStop (input): If this item is True, the analysis is continued when there is no
            convergence in the target force iteration.
        """
        _r = self._raw.GetTargetForceParameters(Name, 0.0, 0, 0.0, NoStop)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.GetTargetForceParameters falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a static nonlinear analysis case. If this function is called for
        an existing load case, all items for the case are reset to their default value. The
        function returns zero if the load case is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetGeometricNonlinearity(self, Name: str, NLGeomType: int):
        """This function sets the geometric nonlinearity option for the specified load case. The
        function returns zero if the option is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        NLGeomType (input): This is 0, 1 or 2, indicating the geometric nonlinearity option
            selected for the load case. 0 = None 1 = P-delta 2 = P-delta plus large
            displacements
        """
        _r = self._raw.SetGeometricNonlinearity(Name, NLGeomType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetGeometricNonlinearity falhou (ret={_r})".format(_r=_r))
        return None

    def SetHingeUnloading(self, Name: str, UnloadType: int):
        """This function sets the hinge unloading option for the specified load case. The function
        returns zero if the option is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear load case.
        UnloadType (input): This is 1, 2 or 3, indicating the hinge unloading option
            selected for the load case. 1 = Unload entire structure 2 = Apply local
            redistribution 3 = Restart using secant stiffness
        """
        _r = self._raw.SetHingeUnloading(Name, UnloadType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetHingeUnloading falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear load case.
        InitialCase (input): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts from the state at the end of a
            nonlinear static or nonlinear direct integration time history load case. If the
            specified initial case is a nonlinear static or nonlinear direct integration
            time history load case, the state at the end of that case is used. If the
            initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadApplication(self, Name: str, LoadControl: int, DispType: int, Displ: float, Monitor: int, DOF: int, PointName: str, GDispl: str):
        """This function sets the load application control parameters for the specified load case. The
        function returns zero if the parameters are successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        LoadControl (input): This is either 1 or 2, indicating the load application control
            method. 1 = Full load 2 = Displacement control
        DispType (input): This is either 1 or 2 indicating the control displacement type. 1
            = Conjugate displacement 2 = Monitored displacement This item applies only when
            displacement control is used, that is, LoadControl = 2.
        Displ (input): This item applies only when displacement control is used, that is,
            LoadControl = 2. The structure is loaded to a monitored displacement of this
            magnitude. [L] when DOF = 1, 2 or 3 and [rad] when DOF = 4, 5 or 6
        Monitor (input): This is either 1 or 2, indicating the monitored displacement. 1 =
            Displacement at a specified point object 2 = Generalized displacement
        DOF (input): This is 1, 2, 3, 4, 5 or 6, indicating the degree of freedom for which
            the displacement at a point object is monitored. 1 = U1 2 = U2 3 = U3 4 = R1 5 =
            R2 6 = R3 This item applies only when Monitor = 1.
        PointName (input): The name of the point object at which the displacement is
            monitored. This item applies only when Monitor = 1.
        GDispl (input): The name of the generalized displacement for which the displacement
            is monitored. This item applies only when Monitor = 2.
        """
        _r = self._raw.SetLoadApplication(Name, LoadControl, DispType, Displ, Monitor, DOF, PointName, GDispl)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetLoadApplication falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ indicating the direction of the load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetMassSource(self, Name: str, Source: str):
        """This function sets the mass source to be used for the specified load case. The function
        returns zero if the mass source is data is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        Source (input): This is the name of an existing mass source or a blank string. Blank
            indicates to use the mass source from the previous load case or the default mass
            source if the load case starts from zero initial conditions.
        """
        _r = self._raw.SetMassSource(Name, Source)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetMassSource falhou (ret={_r})".format(_r=_r))
        return None

    def SetModalCase(self, Name: str, ModalCase: str):
        """This function sets the modal case for the specified analysis case. The function returns zero
        if the initial condition is successfully set; otherwise it returns a nonzero value.
        If the specified modal case is not actually a modal case, the program automatically
        replaces it with the first modal case it can find. If no modal load cases exist, an
        error is returned.
    
        Name (input): The name of an existing static nonlinear load case.
        ModalCase (input): This is the name of an existing modal load case. It specifies the
            modal load case on which any mode-type load assignments to the specified load
            case are based.
        """
        _r = self._raw.SetModalCase(Name, ModalCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetModalCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetResultsSaved(self, Name: str, SaveMultipleSteps: bool, MinSavedStates: int = 10, MaxSavedStates: int = 100, PositiveOnly: bool = True):
        """This function sets the results saved parameters for the specified load case. The function
        returns zero if the parameters are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear load case.
        SaveMultipleSteps (input): This item is True if multiple states are saved for the
            nonlinear analysis. It is False only if the final state is saved.
        MinSavedStates (input): This item only applies when SaveMultipleSteps = True. It is
            the minimum number of saved steps.
        MaxSavedStates (input): This item only applies when SaveMultipleSteps = True. It is
            the maximum number of saved steps.
        PositiveOnly (input): If this item is True, only positive displacement increments
            are saved. If it is False, all displacement increments are saved.
        """
        _r = self._raw.SetResultsSaved(Name, SaveMultipleSteps, MinSavedStates, MaxSavedStates, PositiveOnly)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetResultsSaved falhou (ret={_r})".format(_r=_r))
        return None

    def SetSolControlParameters(self, Name: str, MaxTotalSteps: int, MaxFailedSubSteps: int, MaxIterCS: int, MaxIterNR: int, TolConvD: float, UseEventStepping: bool, TolEventD: float, MaxLineSearchPerIter: int, TolLineSearch: float, LineSearchStepFact: float):
        """This function sets the solution control parameters for the specified load case. The function
        returns zero if the parameters are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing static nonlinear load case.
        MaxTotalSteps (input): The maximum total steps per stage.
        MaxFailedSubSteps (input): The maximum null (zero) steps per stage.
        MaxIterCS (input): The maximum constant-stiffness iterations per step.
        MaxIterNR (input): The maximum Newton_Raphson iterations per step.
        TolConvD (input): The relative iteration convergence tolerance.
        UseEventStepping (input): This item is True if event-to-event stepping is used.
        TolEventD (input): The relative event lumping tolerance.
        MaxLineSearchPerIter (input): The maximum number of line searches per iteration.
        TolLineSearch (input): The relative line-search acceptance tolerance.
        LineSearchStepFact (input): The line-search step factor.
        """
        _r = self._raw.SetSolControlParameters(Name, MaxTotalSteps, MaxFailedSubSteps, MaxIterCS, MaxIterNR, TolConvD, UseEventStepping, TolEventD, MaxLineSearchPerIter, TolLineSearch, LineSearchStepFact)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetSolControlParameters falhou (ret={_r})".format(_r=_r))
        return None

    def SetTargetForceParameters(self, Name: str, TolConvF: float, MaxIter: int, AccelFact: float, NoStop: bool):
        """This function sets the target force iteration parameters for the specified load case. The
        function returns zero if the parameters are successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        TolConvF (input): The relative convergence tolerance for target force iteration.
        MaxIter (input): The maximum iterations per stage for target force iteration.
        AccelFact (input): The acceleration factor.
        NoStop (input): If this item is True, the analysis is continued when there is no
            convergence in the target force iteration.
        """
        _r = self._raw.SetTargetForceParameters(Name, TolConvF, MaxIter, AccelFact, NoStop)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.StaticNonlinear.SetTargetForceParameters falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_SteadyState:
    """Wrapper para SapModel.LoadCases.SteadyState."""

    def __init__(self, raw):
        self._raw = raw

    def GetDampConstant(self, Name: str):
        """This function retrieves the constant hysteretic damping for all frequencies assigned to the
        specified load case. The function returns zero if the damping is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing steady state load case that has constant
            damping.
        HysConMassCoeff (output): The mass proportional damping coefficient.
        HysConStiffCoeff (output): The stiffness proportional damping coefficient.
        """
        _r = self._raw.GetDampConstant(Name, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.GetDampConstant falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampInterpolated(self, Name: str):
        """This function retrieves the interpolated hysteretic damping by frequency assigned to the
        specified load case. The function returns zero if the damping is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing steady state load case that has interpolated
            damping.
        HysIntFreqUnits (output): This is 1 or 2, indicating the units for the frequency. 1
            = Hz [cyc/s] 2 = RPM
        HysIntNumFreqs (output): The number of sets of frequency, mass coefficient and
            stiffness coefficient data.
        HysIntFreq (output): This is an array of frequencies. The frequency is in Hz or RPM,
            depending on the value of HysIntFreqUnits.
        HysIntMassCoeff (output): This is an array that includes the mass proportional
            damping coefficient.
        HysIntStiffCoeff (output): This is an array that includes the stiffness proportional
            damping coefficient.
        """
        _r = self._raw.GetDampInterpolated(Name, 0, 0, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.GetDampInterpolated falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDampType(self, Name: str):
        """This function retrieves the hysteretic damping type for the specified load case. The
        function returns zero if the type is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing steady state load case.
        DampType (output): This is 1 or 2, indicating the hysteretic damping type for the
            load case. 1 = Constant hysteretic damping for all frequencies 2 = Interpolated
            hysteretic damping by frequency
        """
        _r = self._raw.GetDampType(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.GetDampType falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetFreqData(self, Name: str, FreqAddModal: bool, FreqAddModalDev: bool, FreqAddSpecified: bool):
        """This function retrieves the frequency data for the specified load case. The function returns
        zero if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing steady state load case.
        FreqFirst (output): The first frequency. [cyc/s]
        FreqLast (output): The last frequency. [cyc/s]
        FreqNumIncs (output): The number of frequency increments.
        FreqAddModal (input): If this item is True then modal frequencies are added.
        FreqAddModalDev (input): If this item is True then signed fractional deviations from
            modal frequencies are added.
        FreqAddSpecified (input): If this item is True, specified frequencies are added.
        FreqNumModalDev (output): The number of signed fractional deviations from modal
            frequencies that are added. This item applies only when FreqAddModalDev = True.
        FreqModalDev (output): This is an array that includes the added signed fractional
            deviations from modal frequencies. This item applies only when FreqAddModalDev =
            True.
        FreqNumSpecified (output): The number of specified frequencies that are added. This
            item applies only when FreqAddSpecified = True.
        FreqSpecified (output): This is an array that includes the added specified
            frequencies. This item applies only when FreqAddModalDev = True.
        """
        _r = self._raw.GetFreqData(Name, 0.0, 0.0, 0, FreqAddModal, FreqAddModalDev, FreqAddSpecified, 0, [], 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.GetFreqData falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing steady state load case.
        InitialCase (output): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float], CSys: list[str]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing steady state load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (output): This is an array that includes the name of the steady state function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        PhaseAngle (output): This is an array that includes the phase angle. [deg]
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (output): This is an array that includes the angle between the acceleration
            local 1 axis and the +X-axis of the coordinate system specified by the CSys
            item. The rotation is about the Z-axis of the specified coordinate system. [deg]
            This item applies only when the LoadType item is Accel.
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, [], SF, [], CSys, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.GetLoads falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a steady state load case. If this function is called for an
        existing load case, all items for the case are reset to their default value. The
        function returns zero if the load case is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case
            then that case is modified, otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampConstant(self, Name: str, HysConMassCoeff: float, HysConStiffCoeff: float):
        """This function sets constant hysteretic damping for all frequencies for the specified load
        case. The function returns zero if the damping is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing steady state load case.
        HysConMassCoeff (input): The mass proportional damping coefficient.
        HysConStiffCoeff (input): The stiffness proportional damping coefficient.
        """
        _r = self._raw.SetDampConstant(Name, HysConMassCoeff, HysConStiffCoeff)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.SetDampConstant falhou (ret={_r})".format(_r=_r))
        return None

    def SetDampInterpolated(self, Name: str, HysIntFreqUnits: int, HysIntNumFreqs: int, HysIntFreq: list[float], HysIntMassCoeff: list[float], HysIntStiffCoeff: list[float]):
        """This function sets interpolated hysteretic damping by frequency for the specified load case.
        The function returns zero if the damping is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing steady state load case.
        HysIntFreqUnits (input): This is either 1 or 2, indicating the units for the
            frequency. 1 = Hz [cyc/s] 2 = RPM
        HysIntNumFreqs (input): The number of sets of frequency, mass coefficient and
            stiffness coefficient data.
        HysIntFreq (input): This is an array of frequencies. The frequency is either in Hz
            or RPM depending on the value of HysIntFreqUnits.
        HysIntMassCoeff (input): This is an array that includes the mass proportional
            damping coefficient.
        HysIntStiffCoeff (input): This is an array that includes the stiffness proportional
            damping coefficient.
        """
        _r = self._raw.SetDampInterpolated(Name, HysIntFreqUnits, HysIntNumFreqs, HysIntFreq, HysIntMassCoeff, HysIntStiffCoeff)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.SetDampInterpolated falhou (ret={_r})".format(_r=_r))
        return None

    def SetFreqData(self, Name: str, FreqFirst: float, FreqLast: float, FreqNumIncs: int, FreqAddModal: bool, FreqAddModalDev: bool, FreqAddSpecified: bool, FreqNumModalDev: int, FreqModalDev: list[float], FreqNumSpecified: int, FreqSpecified: list[float]):
        """This function sets the frequency data for the specified load case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing steady state load case.
        FreqFirst (input): The first frequency. [cyc/s]
        FreqLast (input): The last frequency. [cyc/s]
        FreqNumIncs (input): The number of frequency increments.
        FreqAddModal (input): If this item is True, modal frequencies are added.
        FreqAddModalDev (input): If this item is True, signed fractional deviations from
            modal frequencies are added.
        FreqAddSpecified (input): If this item is True, specified frequencies are added.
        FreqNumModalDev (input): The number of signed fractional deviations from modal
            frequencies that are added. This item applies only when FreqAddModalDev = True.
        FreqModalDev (input): This is an array that includes the added signed fractional
            deviations from modal frequencies. This item applies only when FreqAddModalDev =
            True.
        FreqNumSpecified (input): The number of specified frequencies that are added. This
            item applies only when FreqAddSpecified = True.
        FreqSpecified (input): This is an array that includes the added specified
            frequencies. This item applies only when FreqAddModalDev = True.
        """
        _r = self._raw.SetFreqData(Name, FreqFirst, FreqLast, FreqNumIncs, FreqAddModal, FreqAddModalDev, FreqAddSpecified, FreqNumModalDev, FreqModalDev, FreqNumSpecified, FreqSpecified)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.SetFreqData falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing steady state load case.
        InitialCase (input): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], Func: list[str], SF: list[float], PhaseAngle: list[float], CSys: list[str], Ang: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing steady state load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is U1, U2, U3, R1, R2 or
            R3, indicating the direction of the load.
        Func (input): This is an array that includes the name of the steady state function
            associated with each load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for U1 U2 and U3; otherwise unitless
        PhaseAngle (input): This is an array that includes the phase angle. [deg]
        CSys (input): This is an array that includes the name of the coordinate system
            associated with each load. If this item is a blank string, the Global coordinate
            system is assumed. This item applies only when the LoadType item is Accel.
        Ang (input): This is an array that includes the angle between the acceleration local
            1 axis and the +X-axis of the coordinate system specified by the CSys item. The
            rotation is about the Z-axis of the specified coordinate system. [deg] This item
            applies only when the LoadType item is Accel.
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, Func, SF, PhaseAngle, CSys, Ang)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.SteadyState.SetLoads falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_Buckling:
    """Wrapper para SapModel.LoadCases.Buckling."""

    def __init__(self, raw):
        self._raw = raw

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing buckling load case.
        InitialCase (output): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else then zero initial conditions are
            assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Buckling.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing buckling load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Buckling.GetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def GetParameters(self, Name: str):
        """This function retrieves various parameters for the specified load case. The function returns
        zero if the parameters are successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing buckling load case.
        NumBucklingModes (output): The number of buckling modes requested.
        EigenTol (output): The relative convergence tolerance for eigenvalues.
        """
        _r = self._raw.GetParameters(Name, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Buckling.GetParameters falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a buckling load case. If this function is called for an existing
        load case, all items for the case are reset to their default value. The function
        returns zero if the load case is successfully initialized; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case
            then that case is modified, otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Buckling.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing buckling load case.
        InitialCase (input): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Buckling.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], SF: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing buckling load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes either Load or Accel, indicating
            the type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Acce, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load.
        SF (input): This is an array that includes the scale factor of each load assigned to
            the load case. [L/s 2 ] for Accel UX UY and UZ; otherwise unitless
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, SF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Buckling.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetParameters(self, Name: str, NumBucklingModes: int, EigenTol: float):
        """This function sets various parameters for the specified buckling load case. The function
        returns zero if the parameters are successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing buckling load case.
        NumBucklingModes (input): The number of buckling modes requested.
        EigenTol (input): The relative convergence tolerance for eigenvalues.
        """
        _r = self._raw.SetParameters(Name, NumBucklingModes, EigenTol)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Buckling.SetParameters falhou (ret={_r})".format(_r=_r))
        return None


class N_LoadCases_Static_Nonlinear:
    """Wrapper para SapModel.LoadCases.Static Nonlinear."""

    def __init__(self, raw):
        self._raw = raw

    def GetMassSource(self, Name: str):
        """This function sets the mass source to be used for the specified load case. The function
        returns zero if the mass source is data is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing static nonlinear load case.
        Source (output): This is the name of an existing mass source or a blank string.
            Blank indicates to use the mass source from the previous load case or the
            default mass source if the load case starts from zero initial conditions.
        """
        _r = self._raw.GetMassSource(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.Static Nonlinear.GetMassSource falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_LoadCases_ModalRitz:
    """Wrapper para SapModel.LoadCases.ModalRitz."""

    def __init__(self, raw):
        self._raw = raw

    def GetInitialCase(self, Name: str):
        """This function retrieves the initial condition assumed for the specified load case. The
        function returns zero if the initial condition is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing modal ritz load case.
        InitialCase (output): This is blank, None or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.GetInitialCase(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalRitz.GetInitialCase falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str]):
        """This function retrieves the load data for the specified load case. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing modal ritz load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load, Accel or Link, indicating the
            type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load. If the LoadType item is Link, this
            item is not used.
        RitzMaxCyc (output): This is an array that includes the maximum number of generation
            cycles to be performed for the specified ritz starting vector. A value of 0
            means there is no limit on the number of cycles.
        TargetPar (output): This is an array that includes the target dynamic participation
            ratio.
        """
        _r = self._raw.GetLoads(Name, NumberLoads, LoadType, LoadName, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalRitz.GetLoads falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNumberModes(self, Name: str):
        """This function retrieves the number of modes requested for the specified load case. The
        function returns zero if the number of modes is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing modal ritz load case.
        MaxModes (output): The maximum number of modes requested.
        MinModes (output): The minimum number of modes requested.
        """
        _r = self._raw.GetNumberModes(Name, 0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalRitz.GetNumberModes falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCase(self, Name: str):
        """This function initializes a modal ritz load case. If this function is called for an existing
        load case, all items for the case are reset to their default value. The function
        returns zero if the load case is successfully initialized; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing or new load case. If this is an existing case,
            that case is modified; otherwise, a new case is added.
        """
        _r = self._raw.SetCase(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalRitz.SetCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetInitialCase(self, Name: str, InitialCase: str):
        """This function sets the initial condition for the specified load case. The function returns
        zero if the initial condition is successfully set; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing modal ritz load case.
        InitialCase (input): This is blank, None, or the name of an existing analysis case.
            This item specifies if the load case starts from zero initial conditions, that
            is, an unstressed state, or if it starts using the stiffness that occurs at the
            end of a nonlinear static or nonlinear direct integration time history load
            case. If the specified initial case is a nonlinear static or nonlinear direct
            integration time history load case, the stiffness at the end of that case is
            used. If the initial case is anything else, zero initial conditions are assumed.
        """
        _r = self._raw.SetInitialCase(Name, InitialCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalRitz.SetInitialCase falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoads(self, Name: str, NumberLoads: int, LoadType: list[str], LoadName: list[str], RitzMaxCyc: list[int], TargetPar: list[float]):
        """This function sets the load data for the specified analysis case. The function returns zero
        if the data is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing modal ritz load case.
        NumberLoads (input): The number of loads assigned to the specified analysis case.
        LoadType (input): This is an array that includes Load, Accel or Link, indicating the
            type of each load assigned to the load case.
        LoadName (input): This is an array that includes the name of each load assigned to
            the load case. If the LoadType item is Load, this item is the name of a defined
            load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or
            RZ, indicating the direction of the load. If the LoadType item is Link, this
            item is not used.
        RitzMaxCyc (input): This is an array that includes the maximum number of generation
            cycles to be performed for the specified ritz starting vector. A value of 0
            means there is no limit on the number of cycles.
        TargetPar (input): This is an array that includes the target dynamic participation
            ratio.
        """
        _r = self._raw.SetLoads(Name, NumberLoads, LoadType, LoadName, RitzMaxCyc, TargetPar)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalRitz.SetLoads falhou (ret={_r})".format(_r=_r))
        return None

    def SetNumberModes(self, Name: str, MaxModes: int, MinModes: int):
        """This function sets the number of modes requested for the specified load case. The function
        returns zero if the number of modes is successfully set; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing modal ritz load case.
        MaxModes (input): The maximum number of modes requested.
        MinModes (input): The minimum number of modes requested.
        """
        _r = self._raw.SetNumberModes(Name, MaxModes, MinModes)
        if _r != 0:
            raise Sap2000ApiError("SapModel.LoadCases.ModalRitz.SetNumberModes falhou (ret={_r})".format(_r=_r))
        return None


