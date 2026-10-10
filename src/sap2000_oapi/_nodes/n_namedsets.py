"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_NamedSets:
    """Wrapper para SapModel.NamedSets."""

    def __init__(self, raw):
        self._raw = raw

    def GetJointRespSpec(self, Name: str, DefaultFreq: bool, StructuralFreq: bool):
        """This function gets a joint response spectrum named set definition. The function returns zero
        if the named set is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing joint response spectrum named set..
        NumberJoints (output): The number of joints for which to generate response spectra.
        JointNames (output): This is an array of joint names for which to generate response
            spectra.
        CoordSys (output): The name of a coordinate system in which the direction for
            results is defined. This can be Global, Local, or any other user-defined
            coordinate system.
        Direction (output): This specifies the direction, in the specified coordinate
            system, in which the results are to be retrieved. Valid values for the direction
            are: 1 = Local 1, Global X, or user-defined coordinate system X 2 = Local 2,
            Global Y, or user-defined coordinate system Y 3 = Local 3, Global Z, or user-
            defined coordinate system Z
        Abscissa (output): This is one of the following, specifying the abscissa data type.
            1 = Frequency 2 = Period
        Ordinate (output): This is one of the following, specifying the ordinate data type.
            1 = Spectral displacement 2 = Spectral velocity 3 = Pseudo-spectral velocity 4 =
            Spectral acceleration 5 = Pseudo-spectral acceleration
        DefaultFreq (input): If this item is True, the default frequencies are used for
            output.
        StructuralFreq (input): If this item is True, the structural frequencies are used
            for output.
        NumberUserFreq (output): The number of user-defined frequencies, which may be 0.
        UserFreqValues (output): This is an array that includes the user-defined
            frequencies. Values are returned using indices 0 to NumberUserFreq-1 if
            NumberUserFreq > 0. [1/s]
        NumberDampValues (output): The number of critical damping ratio values.
        OrdinatePlotType (output): This is one of the following, specifying the ordinate
            axis scale type. 1 = Arithmetic 2 = Log
        OrdinateScaleFactor (output): This is the scale factor used to linearly scale the
            response spectrum ordinate values.
        """
        _r = self._raw.GetJointRespSpec(Name, "", 0, [], "", 0, 0, 0, DefaultFreq, StructuralFreq, 0, [], 0, [], 0, 0.0, 0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.NamedSets.GetJointRespSpec falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetJointRespSpec(self, Name: str, LoadCase: str, NumberJoints: int, JointNames: list[str], CoordSys: str, Direction: int, Abscissa: int, Ordinate: int, DefaultFreq: bool, StructuralFreq: bool, NumberUserFreq: int, UserFreqValues: list[float], NumberDampValues: int, DampingValues: list[float], AbscissaPlotType: int = 2, SpectrumWidening: float = 0, OrdinatePlotType: int = 1, OrdinateScaleFactor: float = 1):
        """This function defines a joint response spectrum named set. The function returns zero if the
        named set is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a new or existing joint response spectrum named set. If
            the named set already exists, it will be modified, otherwise a new named set
            will be created.
        NumberJoints (input): The number of joints for which to generate response spectra.
        JointNames (input): This is an array of joint names for which to generate response
            spectra.
        CoordSys (input): The name of a coordinate system in which the direction for results
            is defined. This can be Global, Local, or any other user-defined coordinate
            system.
        Direction (input): This is a value specifying the direction, in the specified
            coordinate system, in which the results are to be retrieved. Valid values for
            the direction are: 1 = Local 1, Global X, or user-defined coordinate system X 2
            = Local 2, Global Y, or user-defined coordinate system Y 3 = Local 3, Global Z,
            or user-defined coordinate system Z
        Abscissa (input): This is one of the following, specifying the abscissa data type. 1
            = Frequency 2 = Period
        Ordinate (input): This is one of the following, specifying the ordinate data type. 1
            = Spectral displacement 2 = Spectral velocity 3 = Pseudo-spectral velocity 4 =
            Spectral acceleration 5 = Pseudo-spectral acceleration
        DefaultFreq (input): If this item is True, the default frequencies are used for
            output.
        StructuralFreq (input): If this item is True, the structural frequencies are used
            for output.
        NumberUserFreq (input): The number of user-defined frequencies, which may be 0.
        UserFreqValues (input): This is an array that includes the user-defined frequencies.
            Values are returned using indices 0 to NumberUserFreq-1 if NumberUserFreq > 0.
            [1/s]
        NumberDampValues (input): The number of critical damping ratio values, which must be
            at least 1..
        OrdinatePlotType (input): This is one of the following, specifying the ordinate axis
            scale type. 1 = Arithmetic 2 = Log
        OrdinateScaleFactor (input): This is the scale factor used to linearly scale the
            response spectrum ordinate values.
        """
        _r = self._raw.SetJointRespSpec(Name, LoadCase, NumberJoints, JointNames, CoordSys, Direction, Abscissa, Ordinate, DefaultFreq, StructuralFreq, NumberUserFreq, UserFreqValues, NumberDampValues, DampingValues, AbscissaPlotType, SpectrumWidening, OrdinatePlotType, OrdinateScaleFactor)
        if _r != 0:
            raise Sap2000ApiError("SapModel.NamedSets.SetJointRespSpec falhou (ret={_r})".format(_r=_r))
        return None


