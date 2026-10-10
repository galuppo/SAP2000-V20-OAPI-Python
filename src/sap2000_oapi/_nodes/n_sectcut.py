"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_SectCut:
    """Wrapper para SapModel.SectCut."""

    def __init__(self, raw):
        self._raw = raw

    def AddQuad(self, Name: str, X: list[float], Y: list[float], Z: list[float]):
        """This function adds a new quadrilateral to a section cut defined by quadrilaterals. The
        function returns zero if the quadrilateral is successfully, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing section cut.
        X (input): This is an array of four X coordinates, one for each of the four points
            defining the quadrilateral.
        Y (input): This is an array of four Y coordinates, one for each of the four points
            defining the quadrilateral.
        Z (input): This is an array of four Z coordinates, one for each of the four points
            defining the quadrilateral.
        """
        _r = self._raw.AddQuad(Name, X, Y, Z)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.AddQuad falhou (ret={_r})".format(_r=_r))
        return None

    def GetCutInfo(self, Name: str, Num: int):
        """This function gets basic information about an existing section cut. The function returns
        zero if the section cut information is successfully obtained, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing section cut.
        GroupName (output): The name of the group associated with the section cut.
        MyType (output): This is either 1, 2, 3 or 4 indicating the result type of the
            section cut. 1 = Analysis 2 = Design Wall 3 = Design Spandrel 4 = Design Slab
        Num (input): The number of quadrilateral cutting planes defined for the section cut.
            If this number is zero then the section cut is defined by the associated group.
        """
        _r = self._raw.GetCutInfo(Name, "", 0, Num)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SectCut.GetCutInfo falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxesAnalysis(self, Name: str):
        """This function gets the local axes angles for an existing section cut whose result type is
        Analysis. The function returns zero if the angles are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing section cut.
        Z (output): The Rotation about the Z axis.
        Y (output): The rotation about the Y' axis where Y' is the orientation of the Y axis
            after rotation about the Z axis.
        X (output): The rotation about the X'' axis where X'' is the orientation of the X
            axis after rotation about the Z axis and about the Y' axis.
        IsAdvanced (output): Indicates if advanced local axes are specified.
        """
        _r = self._raw.GetLocalAxesAnalysis(Name, 0.0, 0.0, 0.0, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SectCut.GetLocalAxesAnalysis falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxesAngleDesign(self, Name: str):
        """This function gets the local axes angle for section cuts whose result type is Design (Wall,
        Spandrel or Slab). The function returns zero if the angle is successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing section cut.
        Angle (output): For design local axes orientation type wall this is the angle from
            the global X to the local 2 axis. For orientation types spandrel and slab it is
            the angle from the global X to the local 1 axis.
        """
        _r = self._raw.GetLocalAxesAngleDesign(Name, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SectCut.GetLocalAxesAngleDesign falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetLocalAxesAdvancedAnalysis(self, Name: str):
        """This function gets the advanced local axes data for an existing section cut whose result
        type is Analysis. The function returns zero if the data is successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing section cut.
        Active (output): This is True if advanced local axes exist.
        Plane2 (output): This is 12, 13, 21, 23, 31 or 32, indicating that the local plane
            determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, 0r 3-2
            plane. This item applies only when the Active item is True.
        """
        _r = self._raw.GetLocalAxesAdvancedAnalysis(Name, False, 0, "", [], [], [], 0, 0, "", [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SectCut.GetLocalAxesAdvancedAnalysis falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNameList(self):
        """This function retrieves the names of all defined section cuts. The function returns zero if
        the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of section cut names retrieved by the program.
        MyName (output): This is a one-dimensional array of section cut names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames 1) inside the Sap2000
            program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SectCut.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetQuad(self, Name: str, Num: int, X: list[float], Y: list[float], Z: list[float]):
        """This function returns the coordinates of a quadrilateral cutting plane in a section cut
        defined by quadrilaterals. The function returns zero if the coordinates are
        successfully returned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing section cut defined using quadrilateral
            cutting planes.
        Num (input): The number of a quadirilateral cutting plane in the section cut.
        X (input): This is an array of four X coordinates, one for each of the four points
            defining the quadrilateral.
        Y (input): This is an array of four Y coordinates, one for each of the four points
            defining the quadrilateral.
        Z (input): This is an array of four Z coordinates, one for each of the four points
            defining the quadrilateral.
        """
        _r = self._raw.GetQuad(Name, Num, X, Y, Z)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.GetQuad falhou (ret={_r})".format(_r=_r))
        return None

    def GetResultLocation(self, Name: str):
        """This function gets the results location for an existing section cut. The function returns
        zero if the result location is successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing section cut.
        IsDefault (output): Indicates if the section cut results are reported at the default
            location. If so, the X, Y and Z items are ignored.
        X (output): The X coordinate of the section cut result location when it is not
            default
        Y (output): The Y coordinate of the section cut result location when it is not
            default
        Z (output): The Z coordinate of the section cut result location when it is not
            default
        """
        _r = self._raw.GetResultLocation(Name, False, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SectCut.GetResultLocation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetResultsSide(self, Name: str, Side: int):
        """This function gets the side of the elements from which results are obtained. The function
        returns zero if the side is successfully retrieved, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing section cut.
        Side (input): This item is either 1 or 2 and indicates the side of the elements from
            which section cut results are obtained. For section cuts defined from
            quadrilaterals with an Analysis result type: 1 = Positive 3-axis side of
            quadrilateral 2 = Negative 3-axis side of quadrilateral For section cuts with a
            Design Wall result type: 1 = Top 2 = Bottom For section cuts with a Design
            Spandrel or Design Slab result type: 1 = Right 2 = Left
        """
        _r = self._raw.GetResultsSide(Name, Side)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.GetResultsSide falhou (ret={_r})".format(_r=_r))
        return None

    def SetByGroup(self, Name: str, GroupName: str, MyType: int):
        """This function adds a new section cut defined by a group to the model or reinitializes an
        existing section cut to be defined by a group. The function returns zero if the
        section cut is successfully added or initialized, otherwise it returns a nonzero
        value.
    
        Name (input): The section cut name. If a section cut with this name already exists
            then the section cut is reinitialized with the new data. All previous data
            assigned to the section cut is lost. If a section cut with this name does not
            exist then a new section cut is added.
        GroupName (input): The name of the group on which the section cut is based.
        MyType (input): This is either 1, 2, 3 or 4 indicating the result type of the
            section cut. 1 = Analysis 2 = Design Wall 3 = Design Spandrel 4 = Design Slab
        """
        _r = self._raw.SetByGroup(Name, GroupName, MyType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.SetByGroup falhou (ret={_r})".format(_r=_r))
        return None

    def SetByQuad(self, Name: str, GroupName: str, MyType: int, X: list[float], Y: list[float], Z: list[float]):
        """This function adds a new section cut defined by a quadrilateral to the model or
        reinitializes an existing section cut to be defined by a quadrilateral. The function
        returns zero if the section cut is successfully added or initialized, otherwise it
        returns a nonzero value.
    
        Name (input): The section cut name. If a section cut with this name already exists
            then the section cut is reinitialized with the new data. All previous data
            assigned to the section cut is lost. If a section cut with this name does not
            exist then a new section cut is added.
        GroupName (input): The name of the group associated with the section cut.
        MyType (input): This is either 1, 2, 3 or 4 indicating the result type of the
            section cut. 1 = Analysis 2 = Design Wall 3 = Design Spandrel 4 = Design Slab
        X (input): This is an array of four X coordinates, one for each of the four points
            defining the quadrilateral.
        Y (input): This is an array of four Y coordinates, one for each of the four points
            defining the quadrilateral.
        Z (input): This is an array of four Z coordinates, one for each of the four points
            defining the quadrilateral.
        """
        _r = self._raw.SetByQuad(Name, GroupName, MyType, X, Y, Z)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.SetByQuad falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxesAnalysis(self, Name: str, Z: float, Y: float, X: float):
        """This function sets the local axes angles for an existing section cut whose result type is
        Analysis. The function returns zero if the angles are successfully set, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing section cut.
        Z (input): The Rotation about the Z axis.
        Y (input): The rotation about the Y' axis where Y' is the orientation of the Y axis
            after rotation about the Z axis.
        X (input): The rotation about the X'' axis where X'' is the orientation of the X
            axis after rotation about the Z axis and about the Y' axis.
        """
        _r = self._raw.SetLocalAxesAnalysis(Name, Z, Y, X)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.SetLocalAxesAnalysis falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxesAdvancedAnalysis(self, Name: str, Active: bool, AxVectOpt: int, AxCSys: str, axdir: list[int], AxPt: list[str], AxVect: list[float], Plane2: int, PlVectOpt: int, PlCSys: str, PlDir: list[int], PlPt: list[str], PlVect: list[float]):
        """This function sets the advanced local axes data for an existing section cut whose result
        type is Analysis. The function returns zero if the data is successfully set,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing section cut.
        Active (input): This is True if advanced local axes exist.
        Plane2 (input): This is 12, 13, 21, 23, 31 or 32, indicating that the local plane
            determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, 0r 3-2
            plane. This item applies only when the Active item is True.
        """
        _r = self._raw.SetLocalAxesAdvancedAnalysis(Name, Active, AxVectOpt, AxCSys, axdir, AxPt, AxVect, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.SetLocalAxesAdvancedAnalysis falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxesAngleDesign(self, Name: str, Angle: float):
        """This function sets the local axes angle for section cuts whose result type is Design (Wall,
        Spandrel or Slab). The function returns zero if the angle is successfully set,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing section cut.
        Angle (input): For design local axes orientation type wall this is the angle from
            the global X to the local 2 axis. For orientation types spandrel and slab it is
            the angle from the global X to the local 1 axis.
        """
        _r = self._raw.SetLocalAxesAngleDesign(Name, Angle)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.SetLocalAxesAngleDesign falhou (ret={_r})".format(_r=_r))
        return None

    def SetResultLocation(self, Name: str, IsDefault: bool, X: float = 0, Y: float = 0, Z: float = 0):
        """This function sets the results location for an existing section cut. The function returns
        zero if the result location is successfully set, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing section cut.
        IsDefault (input): Indicates if the section cut results are reported at the default
            location. If so, the X, Y and Z items are ignored.
        X (input): The X coordinate of the section cut result location when it is not
            default
        Y (input): The Y coordinate of the section cut result location when it is not
            default
        Z (input): The Z coordinate of the section cut result location when it is not
            default
        """
        _r = self._raw.SetResultLocation(Name, IsDefault, X, Y, Z)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.SetResultLocation falhou (ret={_r})".format(_r=_r))
        return None

    def SetResultsSide(self, Name: str, Side: int):
        """This function sets the side of the elements from which results are obtained. The function
        returns zero if the side is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing section cut.
        Side (input): This item is either 1 or 2 and indicates the side of the elements from
            which section cut results are obtained. For section cuts defined from
            quadrilaterals with an Analysis result type: 1 = Positive 3-axis side of
            quadrilateral 2 = Negative 3-axis side of quadrilateral For section cuts with a
            Design Wall result type: 1 = Top 2 = Bottom For section cuts with a Design
            Spandrel or Design Slab result type: 1 = Right 2 = Left
        """
        _r = self._raw.SetResultsSide(Name, Side)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SectCut.SetResultsSide falhou (ret={_r})".format(_r=_r))
        return None


