"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_Analyze:
    """Wrapper para SapModel.Analyze."""

    def __init__(self, raw):
        self._raw = raw

    def CreateAnalysisModel(self):
        """This function creates the analysis model. If the analysis model is already created and
        current, nothing is done. The function returns zero if the analysis model is
        successfully created or it already exists and is current, otherwise it returns a
        nonzero value. It is not necessary to call this function before running an analysis.
        The analysis model is automatically created, if necessary, when the model is run.
        """
        _r = self._raw.CreateAnalysisModel()
        if _r != 0:
            raise Sap2000ApiError("SapModel.Analyze.CreateAnalysisModel falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteResults(self, Name: str, All: bool = False):
        """This function deletes results for load cases. The function returns zero if the results are
        successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load case that is to have its results deleted.
            This item is ignored when the All item is True.
        All (input): If this item is True, the results are deleted for all load cases, and
            the Name item is ignored.
        """
        _r = self._raw.DeleteResults(Name, All)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Analyze.DeleteResults falhou (ret={_r})".format(_r=_r))
        return None

    def GetActiveDOF(self):
        """This function retrieves the model global degrees of freedom. The function returns zero if
        the degrees of freedom are successfully retrieved; otherwise it returns a nonzero
        value.
    
        DOF (output): This is an array of 6 boolean values, indicating if the specified
            model global degree of freedom is active. DOF(0) = UX DOF(1) = UY DOF(2) = UZ
            DOF(3) = RX DOF(4) = RY DOF(5) = RZ
        """
        _r = self._raw.GetActiveDOF([])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Analyze.GetActiveDOF falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetCaseStatus(self):
        """This function retrieves the status for all load cases. The function returns zero if the
        status is successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of load cases for which the status is reported.
        CaseName (output): This is an array that includes the name of each analysis case for
            which the status is reported.
        Status (output): This is an array of that includes 1, 2, 3 or 4, indicating the load
            case status. 1 = Not run 2 = Could not start 3 = Not finished 4 = Finished
        """
        _r = self._raw.GetCaseStatus(0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Analyze.GetCaseStatus falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetRunCaseFlag(self):
        """This function retrieves the run flags for all analysis cases. The function returns zero if
        the flags are successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of load cases for which the run flag is reported.
        CaseName (output): This is an array that includes the name of each analysis case for
            which the run flag is reported.
        Run (output): This is an array of boolean values indicating if the specified load
            case is to be run.
        """
        _r = self._raw.GetRunCaseFlag(0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Analyze.GetRunCaseFlag falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSolverOption(self, StiffCase: str):
        """This function retrieves the model solver options. The function returns zero if the options
        are successfully retrieved; otherwise it returns a nonzero value.
    
        SolverType (output): This is 0, 1 or 2, indicating the solver type. 0 = Standard
            solver 1 = Advanced solver 2 = Multi-threaded solver
        SolverProcessType (output): This is 0, 1 or 2, indicating the process the analysis
            is run. 0 = Auto (program determined) 1 = GUI process 2 = Separate process
        Force32BitSolver (output): This is True if the analysis is always run using 32-bit,
            even on 64-bit computers.
        StiffCase (input): The name of the load case used when outputting the mass and
            stiffness matrices to text files. If this item is blank, no matrices are output.
        """
        _r = self._raw.GetSolverOption(0, 0, False, StiffCase)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Analyze.GetSolverOption falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ModifyUnDeformedGeometry(self, CaseName: str, SF: float, Stage: int = -1, Original: bool = False):
        """This function modifies the undeformed geometry based on displacements obtained from a
        specified load case. The function returns zero if it is successful; otherwise it
        returns a nonzero value.
    
        CaseName (input): The name of the static load case from which displacements are
            obtained.
        SF (input): The scale factor applied to the displacements.
        Stage (input): This item applies only when the specified load case is a staged
            construction load case. It is the stage number from which the displacements are
            obtained. Specifying a -1 for this item means to use the last run stage.
        Original (input): If this item is True, all other input items in this function are
            ignored and the original undeformed geometry data is reinstated.
        """
        _r = self._raw.ModifyUnDeformedGeometry(CaseName, SF, Stage, Original)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Analyze.ModifyUnDeformedGeometry falhou (ret={_r})".format(_r=_r))
        return None

    def ModifyUnDeformedGeometryModeShape(self, CaseName: str, Mode: object, MaxDisp: float, Direction: object, Original: bool = False):
        """This function modifies the undeformed geometry based on the shape of a specified mode from a
        specified modal or buckling load case. The function returns zero if it is
        successful; otherwise it returns a nonzero value.
    
        CaseName (input): The name of a modal or buckling load case.
        Mode (input): The mode shape to consider.
        MaxDisp (input): The maximum displacement to which the mode shape will be scaled.
        Direction (input): The direction in which to apply the geometry modification.
        Original (input): If this item is True, all other input items in this function are
            ignored and the original undeformed geometry data is reinstated.
        """
        _r = self._raw.ModifyUnDeformedGeometryModeShape(CaseName, Mode, MaxDisp, Direction, Original)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Analyze.ModifyUnDeformedGeometryModeShape falhou (ret={_r})".format(_r=_r))
        return None

    def RunAnalysis(self):
        """This function runs the analysis. The analysis model is automatically created as part of this
        function. The function returns zero if the analysis model is successfully run,
        otherwise it returns a nonzero value. IMPORTANT NOTE: Your model must have a file
        path defined before running the analysis. If the model is opened from an existing
        file, a file path is defined. If the model is created from scratch, the File.Save
        function must be called with a file name before running the analysis. Saving the
        file creates the file path.
        """
        _r = self._raw.RunAnalysis()
        if _r != 0:
            raise Sap2000ApiError("SapModel.Analyze.RunAnalysis falhou (ret={_r})".format(_r=_r))
        return None

    def SetActiveDOF(self, DOF: list[bool]):
        """This function sets the model global degrees of freedom. The function returns zero if the
        degrees of freedom are successfully set; otherwise it returns a nonzero value.
    
        DOF (input): This is an array of 6 boolean values, indicating if the specified model
            global degree of freedom is active. DOF(0) = UX DOF(1) = UY DOF(2) = UZ DOF(3) =
            RX DOF(4) = RY DOF(5) = RZ
        """
        _r = self._raw.SetActiveDOF(DOF)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Analyze.SetActiveDOF falhou (ret={_r})".format(_r=_r))
        return None

    def SetRunCaseFlag(self, Name: str, Run: bool, All: bool = False):
        """This function sets the run flag for load cases. The function returns zero if the flag is
        successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing load case that is to have its run flag set.
            This item is ignored when the All item is True.
        Run (input): If this item is True, the specified load case is to be run.
        All (input): If this item is True, the run flag is set as specified by the Run item
            for all load cases, and the Name item is ignored.
        """
        _r = self._raw.SetRunCaseFlag(Name, Run, All)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Analyze.SetRunCaseFlag falhou (ret={_r})".format(_r=_r))
        return None

    def SetSolverOption_1(self, SolverType: int, SolverProcessType: int, Force32BitSolver: bool, StiffCase: str = ''):
        """This function sets the model solver options. The function returns zero if the options are
        successfully set; otherwise it returns a nonzero value.
    
        SolverType (input): This is 0, 1 or 2, indicating the solver type. 0 = Standard
            solver 1 = Advanced solver 2 = Multi-threaded solver
        SolverProcessType (input): This is 0, 1 or 2, indicating the process the analysis is
            run. 0 = Auto (program determined) 1 = GUI process 2 = Separate process
        Force32BitSolver (input): This is True if the analysis is always run using 32-bit,
            even on 64-bit computers.
        StiffCase (input): The name of the load case used when outputting the mass and
            stiffness matrices to text files If this item is blank, no matrices are output.
        """
        _r = self._raw.SetSolverOption_1(SolverType, SolverProcessType, Force32BitSolver, StiffCase)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Analyze.SetSolverOption_1 falhou (ret={_r})".format(_r=_r))
        return None


