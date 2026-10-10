"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_ExternalAnalysisResults:
    """Wrapper para SapModel.ExternalAnalysisResults."""

    def __init__(self, raw):
        self._raw = raw

    def DeleteAllFrameForces(self):
        """This function deletes all the external results previously provided for all frame objects.
        The function returns zero if the results are successfully deleted, otherwise it
        returns a nonzero value.
        """
        _r = self._raw.DeleteAllFrameForces()
        if _r != 0:
            raise Sap2000ApiError("SapModel.ExternalAnalysisResults.DeleteAllFrameForces falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteFrameForces(self, Name: str):
        """This function deletes all the external results previously provided for a given frame object.
        This function returns zero if the external results are successfully deleted,
        otherwise it returns a nonzero value.
        """
        _r = self._raw.DeleteFrameForces(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ExternalAnalysisResults.DeleteFrameForces falhou (ret={_r})".format(_r=_r))
        return None

    def PresetFrameCases(self, Count: int):
        """Calling this function is optional, but it can speed up subsequent assignment of external
        analysis results which are available for more than one load case. The first time
        this function is called for a particular frame object, it sets the list of names of
        external result load cases for which results relevant to the object are available.
        Subsequent calls to this function for the same object reset the results for load
        cases already in the list, and add load cases not already in. This function returns
        zero if the stations are successfully set, otherwise it returns a nonzero value.
        """
        _r = self._raw.PresetFrameCases("", Count, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ExternalAnalysisResults.PresetFrameCases falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetFrameForce(self, Name: str, InitialCase: str, NumStep: int):
        """This function reports the external result forces for a given step of a given external
        results load case on a given object. The function returns zero if the external
        result forces are successfully recovered, otherwise it returns a nonzero value.
        """
        _r = self._raw.GetFrameForce(Name, InitialCase, NumStep, 0, [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ExternalAnalysisResults.GetFrameForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetFrameStations(self):
        """This function gets the frame stations on a frame object for which user-supplied external
        analysis results are available. The function returns zero if the stations are
        successfully get, otherwise it returns a nonzero value.
        """
        _r = self._raw.GetFrameStations("", 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ExternalAnalysisResults.GetFrameStations falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetFrameStations(self, Name: str, ObjSta: list[float]):
        """This function sets the frame stations on a frame object for which user-supplied external
        analysis results are available. The function returns zero if the stations are
        successfully set, otherwise it returns a nonzero value.
        """
        _r = self._raw.SetFrameStations(Name, ObjSta)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ExternalAnalysisResults.SetFrameStations falhou (ret={_r})".format(_r=_r))
        return None

    def SetFrameForceMultiple(self, NumberFrameNames: int, FrameName: list[str], NumberLoadCases: int, LoadCase: list[str], FirstStep: list[int], LastStep: list[int], P: list[float], M2: list[float], M3: list[float]):
        """This function sets the external result forces for all input frames and load cases. The P,
        V2, V3, T, M2, M3 arrays should be of length: (Sum of all steps for all input Load
        Cases) * (Sum of all stations for all input Frames) As an example, consider setting
        results for two Frames, each with two defined Stations, for two Load Cases, each
        Load Case containing three steps, eg First Step = 1, Last step = 3. The values of
        this array will be iterated over in the following order: The P[0] value will be the
        axial force for FrameName[0], LoadCase[0], FirstStep[0], 1st Station The P[1] value
        will be the axial force for FrameName[0], LoadCase[0], FirstStep[0], 2nd Station The
        P[2] value will be the axial force for FrameName[0], LoadCase[0], FirstStep[0]+1,
        1st Station The P[3] value will be the axial force for FrameName[0], LoadCase[0],
        FirstStep[0]+1, 2nd Station The P[4] value will be the axial force for FrameName[0],
        LoadCase[0], LastStep[0], 1st Station The P[5] value will be the axial force for
        FrameName[0], LoadCase[0], LastStep[0], 2nd Station The P[6] value will be the axial
        force for FrameName[0], LoadCase[1], FirstStep[1], 1st Station The P[7] value will
        be the axial force for FrameName[0], LoadCase[1], FirstStep[1], 2nd Station The P[8]
        value will be the axial force for FrameName[0], LoadCase[1], FirstStep[1]+1, 1st
        Station The P[9] value will be the axial force for FrameName[0], LoadCase[1],
        FirstStep[1]+1, 2nd Station The P[10] value will be the axial force for
        FrameName[0], LoadCase[1], LastStep[1], 1st Station The P[11] value will be the
        axial force for FrameName[0], LoadCase[1], LastStep[1], 2nd Station The P[12] value
        will be the axial force for FrameName[1], LoadCase[0], FirstStep[0], 1st Station And
        so on The number of stations must be previously declared using SetFrameStations
        Enter 0 for any unneeded values in these arrays The function returns zero if the
        forces are successfully set, otherwise it returns a nonzero value.
        """
        _r = self._raw.SetFrameForceMultiple(NumberFrameNames, FrameName, NumberLoadCases, LoadCase, FirstStep, LastStep, P, M2, M3)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ExternalAnalysisResults.SetFrameForceMultiple falhou (ret={_r})".format(_r=_r))
        return None

    def SetFrameForce(self, Name: str, InitialCase: str, StepNum: int, P: list[float], V2: list[float], V3: list[float], T: list[float], M2: list[float], M3: list[float]):
        """This function sets the external result forces for a given step of a given external results
        load case on a frame object. The function returns zero if the forces are
        successfully set, otherwise it returns a nonzero value.
        """
        _r = self._raw.SetFrameForce(Name, InitialCase, StepNum, P, V2, V3, T, M2, M3)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ExternalAnalysisResults.SetFrameForce falhou (ret={_r})".format(_r=_r))
        return None


