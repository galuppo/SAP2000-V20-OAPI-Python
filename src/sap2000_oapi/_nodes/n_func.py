"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_Func:
    """Wrapper para SapModel.Func."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing function. The function returns zero if the new
        name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined function.
        NewName (input): The new name for the function.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def ConvertToUser(self, Name: str):
        """This function converts an existing function to a user defined function. The function returns
        zero if the function definition is successfully converted; otherwise it returns a
        nonzero value. An error is returned if the specified function is already a user
        defined function.
    
        Name (input): The name of an existing function that is not a user defined function.
        """
        _r = self._raw.ConvertToUser(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.ConvertToUser falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self, FuncType: int = 0):
        """This function returns the total number of defined functions in the model of the specified
        type.
    
        FuncType (input): This optional value is one of the following numbers, indicating
            the type of function for which the count is desired. 0 = All function types 1 =
            Response spectrum 2 = Time history 3 = Power spectral density 4 = Steady state
        """
        _r = self._raw.Count(FuncType)
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified function. The function returns zero if the function is
        successfully deleted; otherwise it returns a nonzero value. It returns an error if
        the specified function can not be deleted if, for example, it is being used in an
        load case.
    
        Name (input): The name of an existing function.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetNameList(self, FuncType: int = 0):
        """This function retrieves the names of all defined functions of the specified type. The
        function returns zero if the names are successfully retrieved; otherwise it returns
        nonzero.
    
        NumberNames (output): The number of function names retrieved by the program.
        MyName (output): This is a one-dimensional array of function names. The MyName array
            is created as a dynamic, zero-based array by the API user: Dim MyName() as
            String The array is dimensioned to (NumberNames - 1) inside the SAP2000 program,
            filled with the names, and returned to the API user.
        FuncType (input): This is one of the following numbers, indicating the type of
            function for which the name list is desired. 0 = All function types 1 = Response
            spectrum 2 = Time history 3 = Power spectral density 4 = Steady state
        """
        _r = self._raw.GetNameList(0, [], FuncType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTypeOAPI(self, Name: str):
        """This function retrieves the function type for the specified function. The function returns
        zero if the type is successfully retrieved; otherwise it returns nonzero.
    
        Name (input): The name of an existing function.
        FuncType (output): This is one of the following numbers, indicating the type of
            function. 1 = Response spectrum 2 = Time history 3 = Power spectral density 4 =
            Steady state
        AddType (output): The is one of the following items, indicating the function
            subtype. Response Spectrum Functions 0 = From file 1 = User 2 = UBC 94 3 = UBC
            97 4 = BOCA 96 5 = NBCC 95 6 = IBC 2003 7 = NEHRP 97 8 = Eurocode 8-1998 9 =
            NZS4203 1992 10 = Chinese 2010 11 = Italian Ordinanza 3274 12 = IS1893:2002 13 =
            AASHTO LRFD 2006 14 = NCHRP Project 20-07 15 = IBC 2006 16 = NBCC 2005 17 =
            Eurocode 8-2004 18 = AS 1170.4-2007 19 = NZS 1170.5-2004 20 = AASHTO 2007 21 =
            Chinese JTG/T B02-2013 22 = Chinese GB 50111-2006 23 = IBC 2009 24 = NBCC 2010
            25 = NTC 2008 26 = AASHTO 2012 27 = IBC 2012 28 = TSC 2007 29 = SI 413(1995) 30
            = Argentina INPRES-CIRSOC 103 31 = Chile Norma NCh433+DS61 32 = Chile Norma
            NCh2369-2003 33 = Colombia NSR-10 34 = Ecuador NEC-11 Capitulo 2 35 = Guatemala
            AGIES NSE 2-10 36 = Mexico NTC 2004 37 = Peru Norma E.030 38 = Dominican
            Republic R-001 39 = Venezuela COVENIN 1756-2:2001 40 = KBC 2009 41 = Mexico
            CFE-93 42 = Peru NTE E.030 2014 43 = Mexico CFE-2008 44 = Ecuado Norma NEC-SE-DS
            2015 45 = Costa Rica Seismic Code 2010 46 = SP 14.13330.2014 47 = Chinese CJJ
            166-2011 Time History Functions 0 = From file 1 = User 2 = Sine 3 = Cosine 4 =
            Ramp 5 = Sawtooth 6 = Triangular 7 = User periodic Power Spectral Density
            Functions 0 = From file 1 = User Steady State Functions 0 = From file 1 = User
        """
        _r = self._raw.GetTypeOAPI(Name, 0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.GetTypeOAPI falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetValues(self, Name: str):
        """This function retrieves the time and function values for any defined function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing function.
        NumberItems (output): The number of time and function value pairs retrieved.
        MyTime (output): This is an array that includes the time value for each data point.
            [s] for response spectrum and time history functions, [cyc/s] for power spectral
            density and steady state functions
        Value (output): This is an array that includes the function value for each data
            point.
        """
        _r = self._raw.GetValues(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.GetValues falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    @cached_property
    def FuncPSD(self):
        return N_Func_FuncPSD(self._raw.FuncPSD)

    @cached_property
    def FuncRS(self):
        return N_Func_FuncRS(self._raw.FuncRS)

    @cached_property
    def FuncSS(self):
        return N_Func_FuncSS(self._raw.FuncSS)

    @cached_property
    def FuncTH(self):
        return N_Func_FuncTH(self._raw.FuncTH)


class N_Func_FuncTH:
    """Wrapper para SapModel.Func.FuncTH."""

    def __init__(self, raw):
        self._raw = raw

    def GetCosine(self, Name: str):
        """This function retrieves the definition of a cosine-type time history function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a cosine-type time history function.
        CosineP (output): The period of the cosine function. [s]
        CosineSteps (output): The number of steps in the cosine function. This item can not
            be less than 8.
        CosineCycles (output): The number of cycles in the cosine function.
        CosineAmp (output): The amplitude of the cosine function.
        """
        _r = self._raw.GetCosine(Name, 0.0, 0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.GetCosine falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetFromFile_1(self, Name: str, FreeFormat: bool):
        """This function retrieves the definition of a time history function from file. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a defined time history function specified to be from a
            text file.
        FileName (output): The full path of the text file containing the function data.
        HeadLines (output): The number of header lines in the text file to be skipped before
            starting to read function data.
        PreChars (output): The number of prefix characters to be skipped on each line in the
            text file.
        PointsPerLine (output): The number of function points included on each text file
            line.
        ValueType (output): This is 1 or 2, indicating value type. 1 = Values at equal time
            intervals 2 = Time and function values
        FreeFormat (input): This item is True if the data is provided in a free format. It
            is False if it is in a fixed format.
        NumberFixed (output): This item applies only when the FreeFormat item is False. It
            is the number of characters per item.
        DT (output): This item applies only when the ValueType item is 1 (equal time
            intervals). It is the time interval between function points.
        """
        _r = self._raw.GetFromFile_1(Name, "", 0, 0, 0, 0, FreeFormat, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.GetFromFile_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetRamp(self, Name: str):
        """This function retrieves the definition of a ramp-type time history function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a ramp-type time history function.
        RampTime (output): The time it takes for the ramp function to initially reach its
            maximum value. [s]
        RampAmp (output): The maximum amplitude of the ramp function.
        RampMaxTime (output): The time at the end of the ramp function. This time must be
            greater than the RampTime. [s]
        """
        _r = self._raw.GetRamp(Name, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.GetRamp falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSawtooth(self, Name: str):
        """This function retrieves the definition of a sawtooth-type time history function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a sawtooth-type time history function.
        SawP (output): The period of the sawtooth function. [s]
        SawTime (output): The time it takes for the sawtooth function to ramp up from a
            function value of zero to its maximum amplitude. [s]
        SawCycles (output): The number of cycles in the function.
        SawAmp (output): The maximum amplitude of the sawtooth function.
        """
        _r = self._raw.GetSawtooth(Name, 0.0, 0.0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.GetSawtooth falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSine(self, Name: str):
        """This function retrieves the definition of a sine-type time history function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a sine-type time history function.
        SineP (output): The period of the sine function. [s]
        SineSteps (output): The number of steps in the sine function. This item can not be
            less than 8.
        SineCycles (output): The number of cycles in the sine function.
        SineAmp (output): The amplitude of the sine function.
        """
        _r = self._raw.GetSine(Name, 0.0, 0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.GetSine falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTriangular(self, Name: str):
        """This function retrieves the definition of a triangular-type time history function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a triangular-type time history function.
        TriP (output): The period of the triangular function. [s]
        TriCycles (output): The number of cycles in the function.
        TriAmp (output): The maximum amplitude of the triangular function.
        """
        _r = self._raw.GetTriangular(Name, 0.0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.GetTriangular falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUserPeriodic(self, Name: str):
        """This function retrieves the definition of a user periodic time history function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a user periodic time history function.
        UPCycles (output): The number of cycles in the function.
        NumberItems (output): The number of frequency and value pairs defined.
        MyTime (output): This is an array that includes the time for each data point. [s]
        Value (output): This is an array that includes the function value for each data
            point.
        """
        _r = self._raw.GetUserPeriodic(Name, 0, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.GetUserPeriodic falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUser(self, Name: str):
        """This function retrieves the definition of a user defined time history function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a user defined time history function.
        NumberItems (output): The number of frequency and value pairs defined.
        MyTime (output): This is an array that includes the time for each data point. [s]
        Value (output): This is an array that includes the function value for each data
            point.
        """
        _r = self._raw.GetUser(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.GetUser falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetCosine(self, Name: str, CosineP: float, CosineSteps: int, CosineCycles: int, CosineAmp: float):
        """This function defines a cosine-type time history function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        CosineP (input): The period of the cosine function. [s]
        CosineSteps (input): The number of steps in the cosine function. This item can not
            be less than 8.
        CosineCycles (input): The number of cycles in the cosine function.
        CosineAmp (input): The amplitude of the cosine function.
        """
        _r = self._raw.SetCosine(Name, CosineP, CosineSteps, CosineCycles, CosineAmp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.SetCosine falhou (ret={_r})".format(_r=_r))
        return None

    def SetFromFile_1(self, Name: str, FileName: str, HeadLines: int, PreChars: int, PointsPerLine: int, ValueType: int, FreeFormat: bool, NumberFixed: int = 10, DT: float = 0.02):
        """This function defines a time history function from file. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        FileName (input): The full path of the text file containing the function data.
        HeadLines (input): The number of header lines in the text file to be skipped before
            starting to read function data.
        PreChars (input): The number of prefix characters to be skipped on each line in the
            text file.
        PointsPerLine (input): The number of function points included on each text file
            line.
        ValueType (input): This is 1 or 2, indicating value type. 1 = Values at equal time
            intervals 2 = Time and function values
        FreeFormat (input): This item is True if the data is provided in a free format. It
            is False if it is in a fixed format.
        NumberFixed (input): This item applies only when the FreeFormat item is False. It is
            the number of characters per item.
        DT (input): This item applies only when the ValueType item is 1 (equal time
            intervals). It is the time interval between function points.
        """
        _r = self._raw.SetFromFile_1(Name, FileName, HeadLines, PreChars, PointsPerLine, ValueType, FreeFormat, NumberFixed, DT)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.SetFromFile_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetRamp(self, Name: str, RampTime: float, RampAmp: float, RampMaxTime: float):
        """This function defines a ramp-type time history function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        RampTime (input): The time it takes for the ramp function to initially reach its
            maximum value. [s]
        RampAmp (input): The maximum amplitude of the ramp function.
        RampMaxTime (input): The time at the end of the ramp function. This time must be
            greater than the RampTime. [s]
        """
        _r = self._raw.SetRamp(Name, RampTime, RampAmp, RampMaxTime)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.SetRamp falhou (ret={_r})".format(_r=_r))
        return None

    def SetSawtooth(self, Name: str, SawP: float, SawTime: float, SawCycles: int, SawAmp: float):
        """This function defines a sawtooth-type time history function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        SawP (input): The period of the sawtooth function. [s]
        SawTime (input): The time it takes for the sawtooth function to ramp up from a
            function value of zero to its maximum amplitude. [s]
        SawCycles (input): The number of cycles in the function.
        SawAmp (input): The maximum amplitude of the sawtooth function.
        """
        _r = self._raw.SetSawtooth(Name, SawP, SawTime, SawCycles, SawAmp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.SetSawtooth falhou (ret={_r})".format(_r=_r))
        return None

    def SetSine(self, Name: str, SineP: float, SineSteps: int, SineCycles: int, SineAmp: float):
        """This function defines a sine-type time history function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        SineP (input): The period of the sine function. [s]
        SineSteps (input): The number of steps in the sine function. This item can not be
            less than 8.
        SineCycles (input): The number of cycles in the sine function.
        SineAmp (input): The amplitude of the sine function.
        """
        _r = self._raw.SetSine(Name, SineP, SineSteps, SineCycles, SineAmp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.SetSine falhou (ret={_r})".format(_r=_r))
        return None

    def SetTriangular(self, Name: str, TriP: float, TriCycles: int, TriAmp: float):
        """This function defines a triangular-type time history function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        TriP (input): The period of the triangular function. [s]
        TriCycles (input): The number of cycles in the function.
        TriAmp (input): The maximum amplitude of the triangular function.
        """
        _r = self._raw.SetTriangular(Name, TriP, TriCycles, TriAmp)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.SetTriangular falhou (ret={_r})".format(_r=_r))
        return None

    def SetUserPeriodic(self, Name: str, UPCycles: int, NumberItems: int, MyTime: list[float], Value: list[float]):
        """This function defines a user periodic time history function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        UPCycles (input): The number of cycles in the function.
        NumberItems (input): The number of time and value pairs defined.
        MyTime (input): This is an array that includes the time for each data point. [s]
        Value (input): This is an array that includes the function value for each data
            point.
        """
        _r = self._raw.SetUserPeriodic(Name, UPCycles, NumberItems, MyTime, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.SetUserPeriodic falhou (ret={_r})".format(_r=_r))
        return None

    def SetUser(self, Name: str, NumberItems: int, MyTime: list[float], Value: list[float]):
        """This function defines a user time history function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        NumberItems (input): The number of time and value pairs defined.
        MyTime (input): This is an array that includes the time for each data point. [s]
        Value (input): This is an array that includes the function value for each data
            point.
        """
        _r = self._raw.SetUser(Name, NumberItems, MyTime, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncTH.SetUser falhou (ret={_r})".format(_r=_r))
        return None


class N_Func_FuncPSD:
    """Wrapper para SapModel.Func.FuncPSD."""

    def __init__(self, raw):
        self._raw = raw

    def GetFromFile(self, Name: str, FreeFormat: bool):
        """This function retrieves the definition of a power spectral density function from file. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a defined power spectral density function specified to be
            from a text file.
        FileName (output): The full path of the text file containing the function data.
        HeadLines (output): The number of header lines in the text file to be skipped before
            starting to read function data.
        PreChars (output): The number of prefix characters to be skipped on each line in the
            text file.
        PointsPerLine (output): The number of function points included on each text file
            line.
        ValueType (output): This is either 1 or 2, indicating value type. 1 = Values at
            equal time intervals 2 = Time and function values
        FreeFormat (input): This item is True if the data is provided in a free format. It
            is False if it is in a fixed format.
        NumberFixed (output): This item applies only when the FreeFormat item is False. It
            is the number of characters per item.
        FreqTypeInFile (output): This is either 1 or 2, indicating frequency type. 1 = Hz 2
            = RPM
        """
        _r = self._raw.GetFromFile(Name, "", 0, 0, 0, 0, FreeFormat, 0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncPSD.GetFromFile falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUser(self, Name: str):
        """This function retrieves the definition of a user defined power spectral density function.
        The function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a user defined power spectral density function.
        NumberItems (output): The number of frequency and value pairs defined.
        Frequency (output): This is an array that includes the frequency in Hz for each data
            point. [cyc/s]
        Value (output): This is an array that includes the function value for each data
            point.
        """
        _r = self._raw.GetUser(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncPSD.GetUser falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetFromFile(self, Name: str, FileName: str, HeadLines: int, PreChars: int, PointsPerLine: int, ValueType: int, FreeFormat: bool, NumberFixed: int = 10, FreqTypeInFile: int = 1):
        """This function defines a power spectral density function from file. The function returns zero
        if the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        FileName (input): The full path of the text file containing the function data.
        HeadLines (input): The number of header lines in the text file to be skipped before
            starting to read function data.
        PreChars (input): The number of prefix characters to be skipped on each line in the
            text file.
        PointsPerLine (input): The number of function points included on each text file
            line.
        ValueType (input): This is either 1 or 2, indicating value type. 1 = Values at equal
            time intervals 2 = Time and function values
        FreeFormat (input): This item is True if the data is provided in a free format. It
            is False if it is in a fixed format.
        NumberFixed (input): This item only applies when the FreeFormat item is False. It is
            the number of characters per item.
        FreqTypeInFile (input): This is either 1 or 2, indicating frequency type. 1 = Hz 2 =
            RPM
        """
        _r = self._raw.SetFromFile(Name, FileName, HeadLines, PreChars, PointsPerLine, ValueType, FreeFormat, NumberFixed, FreqTypeInFile)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncPSD.SetFromFile falhou (ret={_r})".format(_r=_r))
        return None

    def SetUser(self, Name: str, NumberItems: int, Frequency: list[float], Value: list[float]):
        """This function defines a user power spectral density function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        NumberItems (input): The number of frequency and value pairs defined.
        Frequency (input): This is an array that includes the frequency in Hz for each data
            point. [cyc/s]
        Value (input): This is an array that includes the function value for each data
            point.
        """
        _r = self._raw.SetUser(Name, NumberItems, Frequency, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncPSD.SetUser falhou (ret={_r})".format(_r=_r))
        return None


class N_Func_FuncRS:
    """Wrapper para SapModel.Func.FuncRS."""

    def __init__(self, raw):
        self._raw = raw

    def GetAASHTO2006(self, Name: str):
        """This function retrieves the definition of an AASHTO2006 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an AASHTO2006 response spectrum function.
        AASHTO2006A (output): The acceleration coefficient, A.
        AASHTO2006SoilProfileType (output): This is 1, 2, 3 or 4, indicating the soil
            profile type. 1 = I 2 = II 3 = III 4 = IV
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetAASHTO2006(Name, 0.0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetAASHTO2006 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetAASHTO2007(self, Name: str):
        """This function retrieves the definition of a AASHTO 20-07 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an AASHTO 20-07 response spectrum function.
        AASHTO2007Option (output): This is 0, 1, or 2, indicating the seismic coefficient
            option. 0 = Ss and S1 from USGS by latitude and longitude 1 = Ss and S1 from
            USGS by zip code 2 = Ss and S1 are user defined
        AASHTO2007ZipCode (output): The zip code for which the seismic coefficients are
            obtained. This item is used only when AASHTO2007Option = 1.
        AASHTO2007SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class.
            1 = A 2 = B 3 = C 4 = D 5 = E 6 = F
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetAASHTO2007(Name, 0, 0.0, 0.0, "", 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetAASHTO2007 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetAS11702007(self, Name: str):
        """This function retrieves the definition of an AS 1170 2007 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a AS 1170 2007 response spectrum function.
        AS2007SiteClass (output): This is 1, 2, 3, 4 or 5, indicating the site class. 1 = A
            2 = B 3 = C 4 = D 5 = E
        AS2007kp (output): The probability factor, kp.
        AS2007Z (output): The hazard factor, Z.
        AS2007Sp (output): The structural performance factor, Sp.
        AS2007Mu (output): The structural ductility factor, u.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetAS11702007(Name, 0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetAS11702007 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetBOCA96(self, Name: str):
        """This function retrieves the definition of a BOCA96 response spectrum function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a BOCA96 response spectrum function.
        BOCA96Aa (output): The effective peak acceleration, Aa.
        BOCA96Av (output): The effective peak velocity, Av.
        BOCA96S (output): The soil profile coefficient, S.
        BOCA96R (output): The response modification factor, R.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetBOCA96(Name, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetBOCA96 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCJJ1662011(self, Name: str):
        """This function retrieves the definition of a CJJ 166-2011 response spectrum function. The
        function returns zero if the function is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a CJJ 166-2011 response spectrum function.
        Direction (output): This is 1 or 2, indicating the response spectrum direction. 1 =
            Horizontal 2 = Vertical
        PeakAccel (output): The peak acceleration, A.
        Tg (output): The characteristic ground period , Tg > 0.1. [s]
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetCJJ1662011(Name, None, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetCJJ1662011 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetChinese2010(self, Name: str):
        """This function retrieves the definition of a Chinese 2010 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a Chinese 2010 response spectrum function.
        JGJ32010AlphaMax (output): The maximum influence factor.
        JGJ32010SI (output): This is 1, 2, 3, 4, 5 or 6, indicating the seismic intensity. 1
            = 6 (0.05g) 2 = 7 (0.10g) 3 = 7 (0.15g) 4 = 8 (0.20g) 5 = 8 (0.30g) 6 = 9
            (0.40g)
        JGJ32010Tg (output): The characteristic ground period, Tg > 0.1. [s]
        JGJ32010PTDF (output): The period time discount factor.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetChinese2010(Name, 0.0, 0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetChinese2010 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetEuroCode8(self, Name: str):
        """This function retrieves the definition of a EuroCode8 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a EuroCode8 response spectrum function.
        EuroCode8AG (output): The design ground acceleration, Ag.
        EuroCode8S (output): This is 1, 2 or 3, indicating the subsoil class. 1 = A 2 = B 3
            = C
        EuroCode8n (output): The damping correction factor, n, where n >= 0.7.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetEuroCode8(Name, 0.0, 0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetEuroCode8 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetEurocode82004_1(self, Name: str):
        """This function retrieves the definition of a Eurocode 8 2004 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a Eurocode 8 2004 response spectrum function.
        EURO2004Country (output): This is 0, 1, 5, 6, or 10 indicating the country for which
            the Nationally Determined Parameters (NDPs) are specified. 0 = Other (NDPs are
            user specified) 1 = CEN Default 5 = Norway 6 = Singapore 10 = Portugal
        EURO2004Direction (output): This is 1 or 2, indicating the ground motion direction.
            1 = Horizontal 2 = Vertical (Does not apply when EURO2004Country = 6)
        EURO2004SpectrumType (output): This is 1 or 2, indicating the spectrum type. 1 =
            Type 1 2 = Type 2 (Does not apply when EURO2004Country = 5 or 6)
        EURO2004GroundType (output): This is 1, 2, 3, 4, 5 or 6, indicating the ground type.
            This item only applies when the EURO2004Direction item is 1 (horizontal). 1 = A
            (Does not apply when EURO2004Country = 6) 2 = B (Does not apply when
            EURO2004Country = 6) 3 = C 4 = D 5 = E (Does not apply when EURO2004Country = 6)
            6 = S1 (Only applies when EURO2004Country = 6)
        EURO2004ag (output): The design ground acceleration in g, ag.
        EURO2004S (output): The soil factor, S. This item only applies when the
            EURO2004Direction item is 1 (horizontal).
        EURO2004AvgoverAg (output): The vertical ground acceleration divided by the
            horizontal ground acceleration, Avg/Ag. This item only applies when the
            EURO2004Direction item is 2 (vertical).
        EURO2004Tb (output): The lower limit of period of the constant spectral acceleration
            branch, Tb.
        EURO2004Tc (output): The upper limit of period of the constant spectral acceleration
            branch, Tc.
        EURO2004Td (output): The period defining the start of the constant displacement
            range, Td.
        EURO2004Beta (output): The lower bound factor, Beta.
        EURO2004q (output): The behavior factor, q.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetEurocode82004_1(Name, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetEurocode82004_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetFromFile(self, Name: str):
        """This function retrieves the definition of a response spectrum function from file. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a defined response spectrum function specified to be from
            a text file.
        FileName (output): The full path of the text file containing the function data.
        HeadLines (output): The number of header lines in the text file to be skipped before
            starting to read function data.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        ValueType (output): This is either 1 or 2, indicating time value type. 1 = Frequency
            2 = Period
        """
        _r = self._raw.GetFromFile(Name, "", 0, 0.0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetFromFile falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIBC2003(self, Name: str):
        """This function retrieves the definition of a IBC2003 response spectrum function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a IBC2003 response spectrum function.
        IBC2003SS (output): The design spectral acceleration at short periods, Sds.
        IBC2003S1 (output): The design spectral acceleration at a one second period, Sd1.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetIBC2003(Name, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetIBC2003 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIBC2006(self, Name: str):
        """This function retrieves the definition of a IBC2006 response spectrum function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a IBC2006 response spectrum function.
        IBC2006Option (output): This is 0, 1 or 2, indicating the seismic coefficient
            option. 0 = Ss and S1 from USGS by latitiude and longitude 1 = Ss and S1 from
            USGS by zip code 2 = Ss and S1 are user defined
        IBC2006ZipCode (output): The zip code for which the seismic coefficients are
            obtained. This item is used only when IBC2006Option = 1.
        IBC2006TL (output): The long-period transition period. [s]
        IBC2006SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1
            = A 2 = B 3 = C 4 = D 5 = E 6 = F
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetIBC2006(Name, 0, 0.0, 0.0, "", 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetIBC2006 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetIS18932002(self, Name: str):
        """This function retrieves the definition of a IS1893-2002 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a IS1893-2002 response spectrum function.
        INZ (output): The seismic zone factor, Z.
        INS (output): This is 1, 2 or 3, indicating the soil type. 1 = I 2 = II 3 = III
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetIS18932002(Name, 0.0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetIS18932002 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetItalian3274(self, Name: str):
        """This function retrieves the definition of a Italian 3274 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a Italian 3274 response spectrum function.
        Italag (output): The peak ground acceleration.
        ItalSoilType (output): This is 1, 2, 3, 4 or 5, indicating the seismic intensity. 1
            = A 2 = B 3 = C 4 = E 5 = D
        Italq (output): The structure factor.
        ItalLevel (output): This is 0, 1, 2, 3, 4, 5, 6 or 7, indicating the spectral level,
            direction and building type. 0 = SLU/H/Building 1 = SLU/H/Bridge 2 =
            SLU/V/Building 3 = SLU/V/Bridge 4 = EL/H/Building 5 = EL/H/Bridge 6 =
            EL/V/Building 7 = EL/V/Bridge SLU refers to ultimate strength design and EL
            refers to elastic design. H and V are horizontal and vertical, respectively.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetItalian3274(Name, 0.0, 0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetItalian3274 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetJTGB022013(self, Name: str):
        """This function retrieves the definition of a JTG B02-2013 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a JTG B02-2013 response spectrum function.
        Direction (output): This is 1, 2 or 3, indicating the response spectrum direction. 1
            = Horizontal 2 = Vertical-Rock 3 = Vertical-Soil
        PeakAccel (output): The peak acceleration, A.
        Tg (output): The characteristic ground period, Tg > 0.1. [s]
        Ci (output): The importance coefficient.
        Cs (output): The site soil coefficient.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetJTGB022013(Name, None, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetJTGB022013 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC2005(self, Name: str):
        """This function retrieves the definition of a NBCC2005 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a NBCC2005 response spectrum function.
        NBCC2005PGA (output): The peak ground acceleration.
        NBCC2005S02 (output): The spectral acceleration at a 0.2 second period.
        NBCC2005S05 (output): The spectral acceleration at a 0.52 second period.
        NBCC2005S1 (output): The spectral acceleration at a 1 second period.
        NBCC2005S2 (output): The spectral acceleration at a 2 second period.
        NBCC2005SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1
            = A 2 = B 3 = C 4 = D 5 = E 6 = F
        NBCC2005Fa (output): The site coefficient, Fa. This item is read when the site class
            is F only.
        NBCC2005Fv (output): The site coefficient, Fv. This item is read when the site class
            is F only.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetNBCC2005(Name, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNBCC2005 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC2010(self, Name: str):
        """This function retrieves the definition of a NBCC2010 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a NBCC2010 response spectrum function.
        PGA (output): The peak ground acceleration.
        S02 (output): The spectral acceleration at a 0.2 second period.
        S05 (output): The spectral acceleration at a 0.5 second period.
        S1 (output): The spectral acceleration at a 1 second period.
        S2 (output): The spectral acceleration at a 2 second period.
        SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        Fa (output): The site coefficient, Fa. This item is read when the site class is F
            only.
        Fv (output): The site coefficient, Fv. This item is read when the site class is F
            only.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetNBCC2010(Name, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNBCC2010 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC2015(self, Name: str):
        """This function retrieves the definition of a NBCC2015 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a NBCC2015 response spectrum function.
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
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetNBCC2015(Name, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNBCC2015 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNBCC95(self, Name: str):
        """This function retrieves the definition of a NBCC95 response spectrum function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a NBCC95 response spectrum function.
        NBCC95ZVR (output): The zonal velocity ratio.
        NBCC95ZA (output): The acceleration-related seismic zone.
        NBCC95ZV (output): The velocity-related seismic zone.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetNBCC95(Name, 0.0, 0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNBCC95 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNCHRP2007(self, Name: str):
        """This function retrieves the definition of a NCHRP 20-07 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a NCHRP 20-07 response spectrum function.
        NCHRP2007Option (output): This is 0, 1 or 2, indicating the seismic coefficient
            option. 0 = Ss and S1 from USGS by latitiude and longitude 1 = Ss and S1 from
            USGS by zip code 2 = Ss and S1 are user defined
        NCHRP2007ZipCode (output): The zip code for which the seismic coefficients are
            obtained. This item is used only when NCHRP2007Option = 1.
        NCHRP2007SiteClass (output): This is 1, 2, 3, 4, 5 or 6, indicating the site class.
            1 = A 2 = B 3 = C 4 = D 5 = E 6 = F
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetNCHRP2007(Name, 0, 0.0, 0.0, "", 0.0, 0.0, 0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNCHRP2007 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNEHRP97(self, Name: str):
        """This function retrieves the definition of a NEHRP97 response spectrum function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a NEHRP97 response spectrum function.
        NEHRP97SS (output): The design spectral acceleration at short periods, Sds.
        NEHRP97S1 (output): The design spectral acceleration at a one second period, Sd1.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetNEHRP97(Name, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNEHRP97 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNTC2008(self, Name: str):
        """This function retrieves the definition of a NTC2008 response spectrum function. The function
        returns zero if the function is successfully defined; otherwise it returns a nonzero
        value.
    
        Name (input): The name of a NTC2008 response spectrum function.
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
        """
        _r = self._raw.GetNTC2008(Name, 0, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNTC2008 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNTC2018(self, Name: str):
        """This function retrieves the definition of a NTC2018 response spectrum function. The function
        returns zero if the function is successfully defined; otherwise it returns a nonzero
        value.
    
        Name (input): The name of a NTC2018 response spectrum function.
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
        """
        _r = self._raw.GetNTC2018(Name, 0, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNTC2018 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNZS11702004(self, Name: str, NZS2004SiteClass: int, NZS2004Z: float, NZS2004R: float, NZS2004DIST: float):
        """This function retrieves the definition of an NZS 1170 2004 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a NZS 1170 2004 response spectrum function.
        NZS2004SiteClass (input): This is 1, 2, 3, 4 or 5, indicating the site class. 1 = A
            2 = B 3 = C 4 = D 5 = E
        NZS2004Z (input): The hazard factor, Z.
        NZS2004R (input): The return period factor, R.
        NZS2004DIST (input): Distance to the fault in km, used to calculate the near fault
            factor.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetNZS11702004(Name, NZS2004SiteClass, NZS2004Z, NZS2004R, NZS2004DIST, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNZS11702004 falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNZS42031992(self, Name: str):
        """This function retrieves the definition of a NZS4203-1992 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a NZS4203-1992 response spectrum function.
        NZS4203SF (output): The scaling factor (Sm * Sp * R * Z * L).
        NZS4203S (output): This is 1, 2 or 3, indicating the site subsoil category. 1 = A 2
            = B 3 = C
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetNZS42031992(Name, 0.0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetNZS42031992 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSP14133302014(self, Name: str, NonlinSoil: bool):
        """This function retrieves the definition of a SP 14.13330.2014 response spectrum function. The
        function returns zero if the function is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a SP 14.13330.2014 response spectrum function.
        Direction (output): This is 1, 2, 3, or 4, indicating the direction and structure
            type for which the response spectrum is generated. 1 = Building Horizontal 2 =
            Building Vertical 3 = Bridge Horizontal 4 = Bridge Vertical
        Seismicity (output): This is 1, 2, 3, or 4, indicating the region seismicity of the
            construction site. 1 = 6 2 = 7 3 = 8 4 = 9
        SoilCat (output): This is 1, 2, 3, or 4, indicating the soil category. 1 = I 2 = II
            3 = III 4 = IV
        K0Factor (output): The K0Factor, 0 < K0 <= 2.0. This is only applicable when the
            Direction parameter is 1 or 3 for horizontal spectra.
        K1Factor (output): The K1Factor, 0 < K1 <= 1.0.
        KPsiFactor (output): The KPsiFactor, 0.5 < KPsi <= 1.5. This is only applicable when
            the Direction parameter is 1 or 3 for horizontal spectra.
        NonlinSoil (input): This item is True if nonlinear soil deformation should be
            accounted for. This is only applicable when the Direction parameter is 1 or 2
            for buildings and the SoilCat parameter is 3 or 4.
        ASoil (output): The nonlinear soil deformation factor, 0 > a_soil <= 1.0. This is
            only applicable when the NonlinSoil parameter is True, the Direction parameter
            is 1 or 2 buildings, and the SoilCat parameter is 3 or 4.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetSP14133302014(Name, 0, 0, 0, 0.0, 0.0, 0.0, NonlinSoil, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetSP14133302014 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUBC94(self, Name: str):
        """This function retrieves the definition of a UBC94 response spectrum function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a UBC94 response spectrum function.
        UBC94Z (output): The seismic zone factor, Z.
        UBC94S (output): This is 1, 2 or 3, indicating the soil type.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetUBC94(Name, 0.0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetUBC94 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUBC97(self, Name: str):
        """This function retrieves the definition of a UBC97 response spectrum function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a UBC97 response spectrum function.
        UBC97Ca (output): The seismic coefficient, Ca.
        UBC97Cv (output): The seismic coefficient, Cv.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetUBC97(Name, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetUBC97 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUser(self, Name: str):
        """This function retrieves the definition of a user defined response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of a user defined response spectrum function.
        NumberItems (output): The number of frequency and value pairs defined.
        Period (output): This is an array that includes the time for each data point. [s]
        Value (output): This is an array that includes the function value for each data
            point.
        DampRatio (output): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.GetUser(Name, 0, [], [], 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.GetUser falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetAASHTO2006(self, Name: str, AASHTO2006A: float, AASHTO2006SoilProfileType: int, DampRatio: float):
        """This function defines an AASHTO2006 response spectrum function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function then that function is modified, otherwise, a new function is added.
        AASHTO2006A (input): The acceleration coefficient, A.
        AASHTO2006SoilProfileType (input): This is 1, 2, 3 or 4, indicating the soil profile
            type. 1 = I 2 = II 3 = III 4 = IV
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetAASHTO2006(Name, AASHTO2006A, AASHTO2006SoilProfileType, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetAASHTO2006 falhou (ret={_r})".format(_r=_r))
        return None

    def SetAASHTO2007(self, Name: str, AASHTO2007Option: int, AASHTO2007Latitude: float, AASHTO2007Longitude: float, AASHTO2007ZipCode: str, AASHTO2007SS: float, AASHTO2007S1: float, AASHTO2007PGA: float, AASHTO2007SiteClass: int, AASHTO2007Fa: float, AASHTO2007Fv: float, AASHTO2007Fpga: float, DampRatio: float):
        """This function defines a AASHTO 2007 response spectrum function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        AASHTO2007Option (input): This is 0, 1 or 2, indicating the seismic coefficient
            option. 0 = Ss and S1 from USGS by latitude and longitude 1 = Ss and S1 from
            USGS by zip code 2 = Ss and S1 are user defined
        AASHTO2007ZipCode (input): The zip code for which the seismic coefficients are
            obtained. This item is used only when AASHTO2007Option = 1.
        AASHTO2007SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class.
            1 = A 2 = B 3 = C 4 = D 5 = E 6 = F
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetAASHTO2007(Name, AASHTO2007Option, AASHTO2007Latitude, AASHTO2007Longitude, AASHTO2007ZipCode, AASHTO2007SS, AASHTO2007S1, AASHTO2007PGA, AASHTO2007SiteClass, AASHTO2007Fa, AASHTO2007Fv, AASHTO2007Fpga, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetAASHTO2007 falhou (ret={_r})".format(_r=_r))
        return None

    def SetAS11702007(self, Name: str, AS2007SiteClass: int, AS2007kp: float, AS2007Z: float, AS2007Sp: float, AS2007Mu: float, DampRatio: float):
        """This function defines an AS 1170.4 2007 response spectrum function. The function returns
        zero if the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function then that function is modified, otherwise, a new function is added.
        AS2007SiteClass (input): This is 1, 2, 3, 4 or 5, indicating the site class. 1 = A 2
            = B 3 = C 4 = D 5 = E
        AS2007kp (input): The probability factor, kp.
        AS2007Z (input): The hazard factor, Z.
        AS2007Sp (input): The structural performance factor, Sp.
        AS2007Mu (input): The structural ductility factor, u.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetAS11702007(Name, AS2007SiteClass, AS2007kp, AS2007Z, AS2007Sp, AS2007Mu, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetAS11702007 falhou (ret={_r})".format(_r=_r))
        return None

    def SetBOCA96(self, Name: str, BOCA96Aa: float, BOCA96Av: float, BOCA96S: float, BOCA96R: float, DampRatio: float):
        """This function defines a BOCA96 response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        BOCA96Aa (input): The effective peak acceleration, Aa.
        BOCA96Av (input): The effective peak velocity, Av.
        BOCA96S (input): The soil profile coefficient, S.
        BOCA96R (input): The response modification factor, R.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetBOCA96(Name, BOCA96Aa, BOCA96Av, BOCA96S, BOCA96R, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetBOCA96 falhou (ret={_r})".format(_r=_r))
        return None

    def SetCJJ1662011(self, Name: str, Direction: int, PeakAccel: float, Tg: float, DampRatio: float):
        """This function defines a CJJ 166-2011 response spectrum function. The function returns zero
        if the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        Direction (input): This is 1 or 2, indicating the response spectrum direction. 1 =
            Horizontal 2 = Vertical
        PeakAccel (input): The peak acceleration, A.
        Tg (input): The characteristic ground period, Tg > 0.1. [s]
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetCJJ1662011(Name, Direction, PeakAccel, Tg, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetCJJ1662011 falhou (ret={_r})".format(_r=_r))
        return None

    def SetChinese2010(self, Name: str, JGJ32010AlphaMax: float, JGJ32010SI: int, JGJ32010Tg: float, JGJ32010PTDF: float, DampRatio: float):
        """This function defines a Chinese 2010 response spectrum function. The function returns zero
        if the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        JGJ32010AlphaMax (input): The maximum influence factor.
        JGJ32010SI (input): This is 1, 2, 3, 4, 5 or 6, indicating the seismic intensity. 1
            = 6 (0.05g) 2 = 7 (0.10g) 3 = 7 (0.15g) 4 = 8 (0.20g) 5 = 8 (0.30g) 6 = 9
            (0.40g)
        JGJ32010Tg (input): The characteristic ground period, Tg > 0.1. [s]
        JGJ32010PTDF (input): The period time discount factor.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetChinese2010(Name, JGJ32010AlphaMax, JGJ32010SI, JGJ32010Tg, JGJ32010PTDF, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetChinese2010 falhou (ret={_r})".format(_r=_r))
        return None

    def SetEuroCode8(self, Name: str, EuroCode8AG: float, EuroCode8S: int, EuroCode8n: float, DampRatio: float):
        """This function defines a EuroCode8 response spectrum function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        EuroCode8AG (input): The design ground acceleration, Ag.
        EuroCode8S (input): This is 1, 2 or 3, indicating the subsoil class. 1 = A 2 = B 3 =
            C
        EuroCode8n (input): The damping correction factor, n, where n >= 0.7.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetEuroCode8(Name, EuroCode8AG, EuroCode8S, EuroCode8n, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetEuroCode8 falhou (ret={_r})".format(_r=_r))
        return None

    def SetEurocode82004_1(self, Name: str, EURO2004Country: int, EURO2004Direction: int, EURO2004SpectrumType: int, EURO2004GroundType: int, EURO2004ag: float, EURO2004S: float, EURO2004AvgoverAg: float, EURO2004Tb: float, EURO2004Tc: float, EURO2004Td: float, EURO2004Beta: float, EURO2004q: float, DampRatio: float):
        """This function defines a Eurocode 8 2004 response spectrum function. The function returns
        zero if the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function,n that function is modified; otherwise, a new function is added.
        EURO2004Country (input): This is 0, 1, 5, 6, or 10 indicating the country for which
            the Nationally Determined Parameters (NDPs) are specified. 0 = Other (NDPs are
            user specified) 1 = CEN Default 5 = Norway 6 = Singapore 10 = Portugal
        EURO2004Direction (input): This is 1 or 2, indicating the ground motion direction. 1
            = Horizontal 2 = Vertical (Does not apply when EURO2004Country = 6)
        EURO2004SpectrumType (input): This is 1 or 2, indicating the spectrum type. 1 = Type
            1 2 = Type 2 (Does not apply when EURO2004Country = 5 or 6)
        EURO2004GroundType (input): This is 1, 2, 3, 4, 5 or 6, indicating the ground type.
            This item only applies when the EURO2004Direction item is 1 (horizontal). 1 = A
            (Does not apply when EURO2004Country = 6) 2 = B (Does not apply when
            EURO2004Country = 6) 3 = C 4 = D 5 = E (Does not apply when EURO2004Country = 6)
            6 = S1 (Only applies when EURO2004Country = 6)
        EURO2004ag (input): The design ground acceleration in g, ag.
        EURO2004S (input): The soil factor, S. This item only applies when the
            EURO2004Direction item is 1 (horizontal). If the EURO2004Country item is not 0,
            then the input value for this item is ignored.
        EURO2004AvgoverAg (input): The vertical ground acceleration divided by the
            horizontal ground acceleration, Avg/Ag. This item only applies when the
            EURO2004Direction item is 2 (vertical). If the EURO2004Country item is not 0,
            then the input value for this item is ignored.
        EURO2004Tb (input): The lower limit of period of the constant spectral acceleration
            branch, Tb. If the EURO2004Country item is not 0, then the input value for this
            item is ignored.
        EURO2004Tc (input): The upper limit of period of the constant spectral acceleration
            branch, Tc. If the EURO2004Country item is not 0, then the input value for this
            item is ignored.
        EURO2004Td (input): The period defining the start of the constant displacement
            range, Td. If the EURO2004Country item is not 0, then the input value for this
            item is ignored.
        EURO2004Beta (input): The lower bound factor, Beta. If the EURO2004Country item is
            not 0, then the input value for this item is ignored.
        EURO2004q (input): The behavior factor, q.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetEurocode82004_1(Name, EURO2004Country, EURO2004Direction, EURO2004SpectrumType, EURO2004GroundType, EURO2004ag, EURO2004S, EURO2004AvgoverAg, EURO2004Tb, EURO2004Tc, EURO2004Td, EURO2004Beta, EURO2004q, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetEurocode82004_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetFromFile(self, Name: str, FileName: str, HeadLines: int, DampRatio: float, ValueType: int = 2):
        """This function defines a response spectrum function from file. The function returns zero if
        the function is successfully defined, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function. that function is modified; otherwise, a new function is added.
        FileName (input): The full path of the text file containing the function data.
        HeadLines (input): The number of header lines in the text file to be skipped before
            starting to read function data.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        ValueType (input): This is either 1 or 2, indicating time value type. 1 = Frequency
            2 = Period
        """
        _r = self._raw.SetFromFile(Name, FileName, HeadLines, DampRatio, ValueType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetFromFile falhou (ret={_r})".format(_r=_r))
        return None

    def SetIBC2003(self, Name: str, IBC2003SS: float, IBC2003S1: float, DampRatio: float):
        """This function defines a IBC2003 response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function then that function is modified, otherwise, a new function is added.
        IBC2003SS (input): The design spectral acceleration at short periods, Sds.
        IBC2003S1 (input): The design spectral acceleration at a one second period, Sd1.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetIBC2003(Name, IBC2003SS, IBC2003S1, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetIBC2003 falhou (ret={_r})".format(_r=_r))
        return None

    def SetIBC2006(self, Name: str, IBC2006Option: int, IBC2006Latitude: float, IBC2006Longitude: float, IBC2006ZipCode: str, IBC2006SS: float, IBC2006S1: float, IBC2006TL: float, IBC2006SiteClass: int, IBC2006Fa: float, IBC2006Fv: float, DampRatio: float):
        """This function defines a IBC2006 response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function then that function is modified; otherwise, a new function is added.
        IBC2006Option (input): This is 0, 1 or 2, indicating the seismic coefficient option.
            0 = Ss and S1 from USGS by latitiude and longitude 1 = Ss and S1 from USGS by
            zip code 2 = Ss and S1 are user defined
        IBC2006ZipCode (input): The zip code for which the seismic coefficients are
            obtained. This item is used only when IBC2006Option = 1.
        IBC2006TL (input): The long-period transition period. [s]
        IBC2006SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 =
            A 2 = B 3 = C 4 = D 5 = E 6 = F
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetIBC2006(Name, IBC2006Option, IBC2006Latitude, IBC2006Longitude, IBC2006ZipCode, IBC2006SS, IBC2006S1, IBC2006TL, IBC2006SiteClass, IBC2006Fa, IBC2006Fv, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetIBC2006 falhou (ret={_r})".format(_r=_r))
        return None

    def SetIS18932002(self, Name: str, INZ: float, INS: int, DampRatio: float):
        """This function defines a IS1893-2002 response spectrum function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        INZ (input): The seismic zone factor, Z.
        INS (input): This is 1, 2 or 3, indicating the soil type. 1 = I 2 = II 3 = III
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetIS18932002(Name, INZ, INS, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetIS18932002 falhou (ret={_r})".format(_r=_r))
        return None

    def SetItalian3274(self, Name: str, Italag: float, ItalSoilType: int, Italq: float, ItalLevel: float, DampRatio: float):
        """This function defines a Italian 3274 response spectrum function. The function returns zero
        if the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        Italag (input): The peak ground acceleration.
        ItalSoilType (input): This is 1, 2, 3, 4 or 5, indicating the seismic intensity. 1 =
            A 2 = B 3 = C 4 = E 5 = D
        Italq (input): The structure factor.
        ItalLevel (input): This is 0, 1, 2, 3, 4, 5, 6 or 7, indicating the spectral level,
            direction and building type. 0 = SLU/H/Building 1 = SLU/H/Bridge 2 =
            SLU/V/Building 3 = SLU/V/Bridge 4 = EL/H/Building 5 = EL/H/Bridge 6 =
            EL/V/Building 7 = EL/V/Bridge SLU refers to ultimate strength design and EL
            refers to elastic design. H and V are horizontal and vertical, respectively.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetItalian3274(Name, Italag, ItalSoilType, Italq, ItalLevel, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetItalian3274 falhou (ret={_r})".format(_r=_r))
        return None

    def SetJTGB022013(self, Name: str, Direction: int, PeakAccel: float, Tg: float, Ci: float, Cs: float, DampRatio: float):
        """This function defines a JTG B02-2013 response spectrum function. The function returns zero
        if the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        Direction (input): This is 1, 2 or 3, indicating the response spectrum direction. 1
            = Horizontal 2 = Vertical-Rock 3 = Vertical-Soil
        PeakAccel (input): The peak acceleration, A.
        Tg (input): The characteristic ground period, Tg > 0.1. [s]
        Ci (input): The importance coefficient.
        Cs (input): The site soil coefficient.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetJTGB022013(Name, Direction, PeakAccel, Tg, Ci, Cs, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetJTGB022013 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC2005(self, Name: str, NBCC2005PGA: float, NBCC2005S02: float, NBCC2005S05: float, NBCC2005S1: float, NBCC2005S2: float, NBCC2005SiteClass: int, NBCC2005Fa: float, NBCC2005Fv: float, DampRatio: float):
        """This function defines a NBCC2005 response spectrum function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
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
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetNBCC2005(Name, NBCC2005PGA, NBCC2005S02, NBCC2005S05, NBCC2005S1, NBCC2005S2, NBCC2005SiteClass, NBCC2005Fa, NBCC2005Fv, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNBCC2005 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC2010(self, Name: str, PGA: float, S02: float, S05: float, S1: float, S2: float, SiteClass: int, Fa: float, Fv: float, DampRatio: float):
        """This function defines a NBCC2010 response spectrum function. The function returns zero if
        the function definition is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        PGA (input): The peak ground acceleration.
        S02 (input): The spectral acceleration at a 0.2 second period.
        S05 (input): The spectral acceleration at a 0.5 second period.
        S1 (input): The spectral acceleration at a 1 second period.
        S2 (input): The spectral acceleration at a 2 second period.
        SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1 = A 2 =
            B 3 = C 4 = D 5 = E 6 = F
        Fa (input): The site coefficient, Fa. This item is read when the site class is F
            only.
        Fv (input): The site coefficient, Fv. This item is read when the site class is F
            only.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetNBCC2010(Name, PGA, S02, S05, S1, S2, SiteClass, Fa, Fv, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNBCC2010 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC2015(self, Name: str, PGA: float, S02: float, S05: float, S1: float, S2: float, S5: float, S10: float, SiteClass: int, F02: float, F05: float, F1: float, F2: float, F5: float, F10: float, DampRatio: float):
        """This function retrieves the definition of a NBCC2015 response spectrum function. The
        function returns zero if the function definition is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
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
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetNBCC2015(Name, PGA, S02, S05, S1, S2, S5, S10, SiteClass, F02, F05, F1, F2, F5, F10, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNBCC2015 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNBCC95(self, Name: str, NBCC95ZVR: float, NBCC95ZA: int, NBCC95ZV: int, DampRatio: float):
        """This function defines a NBCC95 response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function then that function is modified; otherwise, a new function is added.
        NBCC95ZVR (input): The zonal velocity ratio.
        NBCC95ZA (input): The acceleration-related seismic zone.
        NBCC95ZV (input): The velocity-related seismic zone.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetNBCC95(Name, NBCC95ZVR, NBCC95ZA, NBCC95ZV, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNBCC95 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNCHRP2007(self, Name: str, NCHRP2007Option: int, NCHRP2007Latitude: float, NCHRP2007Longitude: float, NCHRP2007ZipCode: str, NCHRP2007SS: float, NCHRP2007S1: float, NCHRP2007SiteClass: int, NCHRP2007Fa: float, NCHRP2007Fv: float, DampRatio: float):
        """This function defines a NCHRP 20-07 response spectrum function. The function returns zero if
        the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        NCHRP2007Option (input): This is 0, 1 or 2, indicating the seismic coefficient
            option. 0 = Ss and S1 from USGS by latitiude and longitude 1 = Ss and S1 from
            USGS by zip code 2 = Ss and S1 are user defined
        NCHRP2007ZipCode (input): The zip code for which the seismic coefficients are
            obtained. This item is used only when NCHRP2007Option = 1.
        NCHRP2007SiteClass (input): This is 1, 2, 3, 4, 5 or 6, indicating the site class. 1
            = A 2 = B 3 = C 4 = D 5 = E 6 = F
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetNCHRP2007(Name, NCHRP2007Option, NCHRP2007Latitude, NCHRP2007Longitude, NCHRP2007ZipCode, NCHRP2007SS, NCHRP2007S1, NCHRP2007SiteClass, NCHRP2007Fa, NCHRP2007Fv, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNCHRP2007 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNEHRP97(self, Name: str, NEHRP97SS: float, NEHRP97S1: float, DampRatio: float):
        """This function defines a NEHRP97 response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function then that function is modified; otherwise, a new function is added.
        NEHRP97SS (input): The design spectral acceleration at short periods, Sds.
        NEHRP97S1 (input): The design spectral acceleration at a one second period, Sd1.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetNEHRP97(Name, NEHRP97SS, NEHRP97S1, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNEHRP97 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNTC2008(self, Name: str, ParamsOption: int, Latitude: float, Longitude: float, Island: int, LimitState: int, UsageClass: int, NomLife: float, PeakAccel: float, F0: float, Tcs: float, SpecType: int, SoilType: int, Topography: int, hRatio: float, Damping: float, q: float):
        """This function defines a NTC2008 response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
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
        """
        _r = self._raw.SetNTC2008(Name, ParamsOption, Latitude, Longitude, Island, LimitState, UsageClass, NomLife, PeakAccel, F0, Tcs, SpecType, SoilType, Topography, hRatio, Damping, q)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNTC2008 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNTC2018(self, Name: str, ParamsOption: int, Latitude: float, Longitude: float, Island: int, LimitState: int, UsageClass: int, NomLife: float, PeakAccel: float, F0: float, Tcs: float, SpecType: int, SoilType: int, Topography: int, hRatio: float, Damping: float, q: float):
        """This function defines a NTC2018 response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
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
        """
        _r = self._raw.SetNTC2018(Name, ParamsOption, Latitude, Longitude, Island, LimitState, UsageClass, NomLife, PeakAccel, F0, Tcs, SpecType, SoilType, Topography, hRatio, Damping, q)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNTC2018 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNZS11702004(self, Name: str, NZS2004SiteClass: int, NZS2004Z: float, NZS2004R: float, NZS2004DIST: float, DampRatio: float):
        """This function defines an NZS 1170.5 2004 response spectrum function. The function returns
        zero if the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        NZS2004SiteClass (input): This is 1, 2, 3, 4 or 5, indicating the site class. 1 = A
            2 = B 3 = C 4 = D 5 = E
        NZS2004Z (input): The hazard factor, Z.
        NZS2004R (input): The return period factor, R.
        NZS2004DIST (input): Distance to the fault in kim, used to calculate the near fault
            factor.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetNZS11702004(Name, NZS2004SiteClass, NZS2004Z, NZS2004R, NZS2004DIST, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNZS11702004 falhou (ret={_r})".format(_r=_r))
        return None

    def SetNZS42031992(self, Name: str, NZS4203SF: float, NZS4203S: int, DampRatio: float):
        """This function defines a NZS4203-1992 response spectrum function. The function returns zero
        if the function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        NZS4203SF (input): The scaling factor (Sm * Sp * R * Z * L).
        NZS4203S (input): This is 1, 2 or 3, indicating the site subsoil category. 1 = A 2 =
            B 3 = C
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetNZS42031992(Name, NZS4203SF, NZS4203S, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetNZS42031992 falhou (ret={_r})".format(_r=_r))
        return None

    def SetSP14133302014(self, Name: str, Direction: int, Seismicity: int, SoilCat: int, K0Factor: float, K1Factor: float, KPsiFactor: float, NonlinSoil: bool, ASoil: float, DampRatio: float):
        """This function retrieves the definition of a SP 14.13330.2014 response spectrum function. The
        function returns zero if the function is successfully defined; otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        Direction (input): This is 1, 2, 3, or 4, indicating the direction and structure
            type for which the response spectrum is generated. 1 = Building Horizontal 2 =
            Building Vertical 3 = Bridge Horizontal 4 = Bridge Vertical
        Seismicity (input): This is 1, 2, 3, or 4, indicating the region seismicity of the
            construction site. 1 = 6 2 = 7 3 = 8 4 = 9
        SoilCat (input): This is 1, 2, 3, or 4, indicating the soil category. 1 = I 2 = II 3
            = III 4 = IV
        K0Factor (input): The K0Factor, 0 < K0 <= 2.0. This is only applicable when the
            Direction parameter is 1 or 3 for horizontal spectra.
        K1Factor (input): The K1Factor, 0 < K1 <= 1.0.
        KPsiFactor (input): The KPsiFactor, 0.5 < KPsi <= 1.5. This is only applicable when
            the Direction parameter is 1 or 3 for horizontal spectra.
        NonlinSoil (input): This item is True if nonlinear soil deformation should be
            accounted for. This is only applicable when the Direction parameter is 1 or 2
            for buildings and the SoilCat parameter is 3 or 4.
        ASoil (input): The nonlinear soil deformation factor, 0 > a_soil <= 1.0. This is
            only applicable when the NonlinSoil parameter is True, the Direction parameter
            is 1 or 2 buildings, and the SoilCat parameter is 3 or 4.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetSP14133302014(Name, Direction, Seismicity, SoilCat, K0Factor, K1Factor, KPsiFactor, NonlinSoil, ASoil, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetSP14133302014 falhou (ret={_r})".format(_r=_r))
        return None

    def SetUBC94(self, Name: str, UBC94Z: float, UBC94S: int, DampRatio: float):
        """This function defines a UBC94 response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        UBC94Z (input): The seismic zone factor, Z.
        UBC94S (input): This is 1, 2 or 3, indicating the soil type.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetUBC94(Name, UBC94Z, UBC94S, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetUBC94 falhou (ret={_r})".format(_r=_r))
        return None

    def SetUBC97(self, Name: str, UBC97Ca: float, UBC97Cv: float, DampRatio: float):
        """This function defines a UBC97 response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        UBC97Ca (input): The seismic coefficient, Ca.
        UBC97Cv (input): The seismic coefficient, Cv.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetUBC97(Name, UBC97Ca, UBC97Cv, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetUBC97 falhou (ret={_r})".format(_r=_r))
        return None

    def SetUser(self, Name: str, NumberItems: int, Period: list[float], Value: list[float], DampRatio: float):
        """This function defines a user response spectrum function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        NumberItems (input): The number of period and value pairs defined.
        Period (input): This is an array that includes the period for each data point. [s]
        Value (input): This is an array that includes the function value for each data
            point.
        DampRatio (input): The damping ratio for the function, 0 <= DampRatio < 1.
        """
        _r = self._raw.SetUser(Name, NumberItems, Period, Value, DampRatio)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncRS.SetUser falhou (ret={_r})".format(_r=_r))
        return None


class N_Func_FuncSS:
    """Wrapper para SapModel.Func.FuncSS."""

    def __init__(self, raw):
        self._raw = raw

    def GetFromFile(self, Name: str, FreeFormat: bool):
        """This function retrieves the definition of a steady state function from file. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a defined steady state function specified to be from a
            text file.
        FileName (output): The full path of the text file containing the function data.
        HeadLines (output): The number of header lines in the text file to be skipped before
            starting to read function data.
        PreChars (output): The number of prefix characters to be skipped on each line in the
            text file.
        PointsPerLine (output): The number of function points included on each text file
            line.
        ValueType (output): This is either 1 or 2, indicating value type. 1 = Values at
            equal time intervals 2 = Time and function values
        FreeFormat (input): This item is True if the data is provided in a free format. It
            is False if it is in a fixed format.
        NumberFixed (output): This item only applies when the FreeFormat item is False. It
            is the number of characters per item.
        FreqTypeInFile (output): This is either 1 or 2, indicating frequency type. 1 = Hz 2
            = RPM
        """
        _r = self._raw.GetFromFile(Name, "", 0, 0, 0, 0, FreeFormat, 0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncSS.GetFromFile falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetUser(self, Name: str):
        """This function retrieves the definition of a user defined steady state function. The function
        returns zero if the function definition is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a user defined steady state function.
        NumberItems (output): The number of frequency and value pairs defined.
        Frequency (output): This is an array that includes the frequency in Hz for each data
            point. [cyc/s]
        Value (output): This is an array that includes the function value for each data
            point.
        """
        _r = self._raw.GetUser(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Func.FuncSS.GetUser falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetFromFile(self, Name: str, FileName: str, HeadLines: int, PreChars: int, PointsPerLine: int, ValueType: int, FreeFormat: bool, NumberFixed: int = 10, FreqTypeInFile: int = 1):
        """This function defines a steady state function from file. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        FileName (input): The full path of the text file containing the function data.
        HeadLines (input): The number of header lines in the text file to be skipped before
            starting to read function data.
        PreChars (input): The number of prefix characters to be skipped on each line in the
            text file.
        PointsPerLine (input): The number of function points included on each text file
            line.
        ValueType (input): This is either 1 or 2, indicating value type. 1 = Values at equal
            time intervals 2 = Time and function values
        FreeFormat (input): This item is True if the data is provided in a free format. It
            is False if it is in a fixed format.
        NumberFixed (input): This item only applies when the FreeFormat item is False. It is
            the number of characters per item.
        FreqTypeInFile (input): This is either 1 or 2, indicating frequency type. 1 = Hz 2 =
            RPM
        """
        _r = self._raw.SetFromFile(Name, FileName, HeadLines, PreChars, PointsPerLine, ValueType, FreeFormat, NumberFixed, FreqTypeInFile)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncSS.SetFromFile falhou (ret={_r})".format(_r=_r))
        return None

    def SetUser(self, Name: str, NumberItems: int, Frequency: list[float], Value: list[float]):
        """This function defines a user steady state function. The function returns zero if the
        function is successfully defined; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new function. If this is an existing
            function, that function is modified; otherwise, a new function is added.
        NumberItems (input): The number of frequency and value pairs defined.
        Frequency (input): This is an array that includes the frequency in Hz for each data
            point. [cyc/s]
        Value (input): This is an array that includes the function value for each data
            point.
        """
        _r = self._raw.SetUser(Name, NumberItems, Frequency, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Func.FuncSS.SetUser falhou (ret={_r})".format(_r=_r))
        return None


