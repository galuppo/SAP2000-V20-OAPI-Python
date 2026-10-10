"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_GenRefLine:
    """Wrapper para SapModel.GenRefLine."""

    def __init__(self, raw):
        self._raw = raw

    def ConvertLineToBLL(self, Name: str, FirstStation: float = 0, CSys: str = 'Global', OffsetX: float = 0, OffsetY: float = 0, OffsetZ: float = None):
        """This function converts an existing general reference line to a new bridge layout line, with
        the ability to specify offset values. The function returns zero if the bridge layout
        line is successfully created; otherwise it returns a nonzero value.
    
        Name (input): This is the name of an existing general reference line.
        FirstStation (input): The first station value on the bridge layout line. [L]
        CSys (input): The name of the coordinate system in which the general reference line
            is offset to create the bridge layout line.
        OffsetX (input): The distance to offset the general reference line in the
            x-direction of the specified CSys, to the location of the new bridge layout
            line. OffsetY The distance to offset the general reference line in the
            y-direction of the specified CSys, to the location of the new bridge layout
            line.
        """
        _r = self._raw.ConvertLineToBLL(Name, FirstStation, CSys, OffsetX, OffsetY, OffsetZ)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GenRefLine.ConvertLineToBLL falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """The function returns the number of defined general reference lines.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes the specified general reference line. The function returns zero if the
        general reference line is successfully deleted; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing general reference line.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GenRefLine.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetLineElevPoints(self, Name: str, CSys: str = 'Global'):
        """This function retrieves the general reference line elevation points and the associated
        parameters. The function returns zero if the general reference line parameters are
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing general reference line.
        NumberPoints (output): The number of points used to define the general reference
            line elevation layout.
        CurveType (output): This is an array of values indicating the general reference line
            elevation layout curve type for each point. 0 = None 1 = Circular Curve 2 =
            Highway Curve 3 = Parabolic Curve 4 = Bezier Curve 5 = BSpline Curve 6 = Bezier
            Curve Child Point 7 = BSpline Curve Child Point
        Value1 (output): This is the value of a parameter used to define the general
            reference line layout. The item that Value1 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Curve Radius [L] CurveType = 2:
            Curve Radius [L] CurveType = 3: Angle measured from the horizontal, up station
            axis, to the axis of symmetry of the parabolic curve. [deg] CurveType = 4:
            Number of control points. This is currently hard-wired internally to 4.
            CurveType = 5: Number of control points. CurveType = 6: Not Used CurveType = 7:
            Not Used Value2 This is the value of a parameter used to define the general
            reference line layout. The item that Value2 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Not Used CurveType = 2: Curve
            length, including length of spirals on either end. [L] CurveType = 3: Rate at
            which the slope of a parabolic curve is changing in percent. [1/L] CurveType =
            4: Number of discretization points. CurveType = 5: Number of discretization
            points. CurveType = 6: Not Used CurveType = 7: Not Used
        Value3 (output): This is the value of a parameter used to define the general
            reference line layout. The item that Value3 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Not Used CurveType = 2: Not Used
            CurveType = 3: Not Used CurveType = 4: Not Used CurveType = 5: Curve order.
            CurveType = 6: Not Used CurveType = 7: Not Used
        s (output): This is an array of the station coordinate of each point in the
            coordinate system specified for the general reference line. [L]
        z (output): This is an array of the Z coordinate of each point in the coordinate
            system specified for the general reference line. [L]
        """
        _r = self._raw.GetLineElevPoints(Name, 0, [], [], [], [], [], [], CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GenRefLine.GetLineElevPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLinePlanPoints(self, Name: str, CSys: str = 'Global'):
        """This function retrieves the general reference line plan points and the associated
        parameters. The function returns zero if the general reference line parameters are
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing general reference line.
        NumberPoints (output): The number of points used to define the general reference
            line plan layout.
        CurveType (output): This is an array of values indicating the general reference line
            plan layout curve type for each point. 0 = None 1 = Circular Curve 2 = Highway
            Curve 3 = Parabolic Curve 4 = Bezier Curve 5 = BSpline Curve 6 = Bezier Curve
            Child Point 7 = BSpline Curve Child Point
        Value1 (output): This is the value of a parameter used to define the general
            reference line layout. The item that Value1 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Curve Radius [L] CurveType = 2:
            Curve Radius [L] CurveType = 3: Angle measured from the X-axis of the coordinate
            system in which the general reference line is defined, to the axis of symmetry
            of the parabolic curve. [deg] CurveType = 4: Number of control points. This is
            currently hard-wired internally to 4. CurveType = 5: Number of control points.
            CurveType = 6: Not Used CurveType = 7: Not Used
        Value2 (output): This is the value of a parameter used to define the general
            reference line layout. The item that Value2 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Not Used CurveType = 2: Curve
            length, including length of spirals on either end. [L] CurveType = 3: Rate at
            which the slope of a parabolic curve is changing in percent. [1/L] CurveType =
            4: Number of discretization points. CurveType = 5: Number of discretization
            points. CurveType = 6: Not Used CurveType = 7: Not Used
        Value3 (output): This is the value of a parameter used to define the general
            reference line layout. The item that Value3 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Not Used CurveType = 2: Not Used
            CurveType = 3: Not Used CurveType = 4: Not Used CurveType = 5: Curve order.
            CurveType = 6: Not Used CurveType = 7: Not Used
        x (output): This is an array of the X coordinate of each point in the coordinate
            system specified for the general reference line. [L]
        y (output): This is an array of the Y coordinate of each point in the coordinate
            system specified for the general reference line. [L]
        """
        _r = self._raw.GetLinePlanPoints(Name, 0, [], [], [], [], [], [], CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GenRefLine.GetLinePlanPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLine(self, Name: str, Color: int):
        """The function returns zero if the general reference line data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing general reference line.
        DiscLength (output): The maximum segment discretization length of the segments used
            to define curves in the general reference line. [L]
        DiscAngle (output): The maximum discretization angle in degrees for the general
            reference line. [deg]
        Color (input): The display color assigned to the general reference line.
        Visible (output): Specifies whether the general reference line will be displayed in
            windows displaying the model.
        """
        _r = self._raw.GetLine(Name, 0.0, 0.0, Color, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GenRefLine.GetLine falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNameList(self):
        """This function retrieves the names of all defined general reference lines. The function
        returns the names; otherwise it returns a nonzero value.
    
        NumberNames (output): The number of general reference line names retrieved by the
            program.
        MyName (output): This is a one-dimensional array of general reference line names.
            The MyName array is created as a dynamic, zero-based array by the API user: Dim
            MyName() As String The array is dimensioned to (NumberNames 1) inside the
            SAP2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        return (*_outs, _ret)

    def SetLineElevPoints(self, Name: str, NumberPoints: int, CurveType: list[int], Value1: list[float], Value2: list[float], Value3: list[float], s: list[float], z: list[float]):
        """This function assigns the general reference line elevation layout parameters. A minimum of
        three points is required for the Circular, Highway, and Parabolic curves. The Bezier
        curve requires a minimum of four points. The BSpline curve requires a minimum of two
        points. The Bezier and BSpline curve types require additional control points as
        specified by Value2. These control points are considered to be defined directly
        after the point specifying the Bezier or BSpline curve. Any Value1, Value2, or
        Value3 parameters defined on these control points are ignored. The function returns
        zero if the general reference line parameters are successfully defined; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a defined general reference line.
        NumberPoints (input): The number of points used to define the general reference line
            elevation layout.
        CurveType (input): This is an array of values indicating the general reference line
            elevation layout curve type for each point. 0 = None 1 = Circular Curve 2 =
            Highway Curve 3 = Parabolic Curve 4 = Bezier Curve 5 = BSpline Curve 6 = Bezier
            Curve Child Point 7 = BSpline Curve Child Point
        Value1 (input): This is the value of a parameter used to define the general
            reference line layout. The item that Value1 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Curve Radius [L] CurveType = 2:
            Curve Radius [L] CurveType = 3: Angle measured from the horizontal, up station
            axis, to the axis of symmetry of the parabolic curve. [deg] CurveType = 4:
            Number of control points. This is currently hard-wired internally to 4.
            CurveType = 5: Number of control points. CurveType = 6: Not Used CurveType = 7:
            Not Used
        Value2 (input): This is the value of a parameter used to define the general
            reference line layout. The item that Value2 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Not Used CurveType = 2: Curve
            length, including length of spirals on either end. [L] CurveType = 3: Rate at
            which the slope of a parabolic curve is changing in percent. [1/L] CurveType =
            4: Number of discretization points. CurveType = 5: Number of discretization
            points. CurveType = 6: Not Used CurveType = 7: Not Used
        Value3 (input): This is the value of a parameter used to define the general
            reference line layout. The item that Value3 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Not Used CurveType = 2: Not Used
            CurveType = 3: Not Used CurveType = 4: Not Used CurveType = 5: Curve order.
            CurveType = 6: Not Used CurveType = 7: Not Used
        """
        _r = self._raw.SetLineElevPoints(Name, NumberPoints, CurveType, Value1, Value2, Value3, s, z)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GenRefLine.SetLineElevPoints falhou (ret={_r})".format(_r=_r))
        return None

    def SetLinePlanPoints(self, Name: str, NumberPoints: int, CurveType: list[int], Value1: list[float], Value2: list[float], Value3: list[float], x: list[float], y: list[float]):
        """This function assigns the general reference line plan layout parameters. A minimum of three
        points is required for the Circular, Highway, and Parabolic curves. The Bezier curve
        requires a minimum of four points. The BSpline curve requires a minimum of two
        points. The Bezier and BSpline curve types require additional control points as
        specified by Value2. These control points are considered to be defined directly
        after the point specifying the Bezier or BSpline curve. Any Value1, Value2, or
        Value3 parameters defined on these control points are ignored. The function returns
        zero if the general reference line parameters are successfully defined; otherwise it
        returns a nonzero value.
    
        Name (input): The name of a defined general reference line.
        NumberPoints (input): The number of points used to define the general reference line
            plan layout.
        CurveType (input): This is an array of values indicating the general reference line
            plan layout curve type for each point. 0 = None 1 = Circular Curve 2 = Highway
            Curve 3 = Parabolic Curve 4 = Bezier Curve 5 = BSpline Curve 6 = Bezier Curve
            Child Point 7 = BSpline Curve Child Point
        Value1 (input): This is the value of a parameter used to define the general
            reference line layout. The item that Value1 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Curve Radius [L] CurveType = 2:
            Curve Radius [L] CurveType = 3: Angle measured from the X-axis of the coordinate
            system in which the general reference line is defined, to the axis of symmetry
            of the parabolic curve. [deg] CurveType = 4: Number of control points. This is
            currently hard-wired internally to 4. CurveType = 5: Number of control points.
            CurveType = 6: Not Used CurveType = 7: Not Used
        Value2 (input): This is the value of a parameter used to define the general
            reference line layout. The item that Value2 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Not Used CurveType = 2: Curve
            length, including length of spirals on either end. [L] CurveType = 3: Rate at
            which the slope of a parabolic curve is changing in percent. [1/L] CurveType =
            4: Number of discretization points. CurveType = 5: Number of discretization
            points. CurveType = 6: Not Used CurveType = 7: Not Used
        Value3 (input): This is the value of a parameter used to define the general
            reference line layout. The item that Value3 represents depends on the CurveType
            item. CurveType = 0: Not Used CurveType = 1: Not Used CurveType = 2: Not Used
            CurveType = 3: Not Used CurveType = 4: Not Used CurveType = 5: Curve order.
            CurveType = 6: Not Used CurveType = 7: Not Used
        x (input): This is an array of the X coordinate of each point in the coordinate
            system specified for the general reference line. [L]
        y (input): This is an array of the Y coordinate of each point in the coordinate
            system specified for the general reference line. [L]
        """
        _r = self._raw.SetLinePlanPoints(Name, NumberPoints, CurveType, Value1, Value2, Value3, x, y)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GenRefLine.SetLinePlanPoints falhou (ret={_r})".format(_r=_r))
        return None

    def SetLine(self, Name: str, DiscLength: float, DiscAngle: float, CSys: str = 'Global', Color: int = -1, Visible: bool = True):
        """The function returns zero if the general reference line is successfully added or modified;
        otherwise it returns a nonzero value.
    
        Name (input): This is the name of a general reference line. If this is the name of
            an existing general reference line, that general reference line is modified;
            otherwise a new general reference line is added.
        DiscLength (input): The maximum segment discretization length of the segments used
            to define curves in the general reference line. [L]
        DiscAngle (input): The maximum discretization angle in degrees for the general
            reference line. [deg]
        CSys (input): The name of the coordinate system in which the general reference line
            is defined.
        Color (input): The display color assigned to the general reference line. If Color is
            specified as - 1, the program will automatically assign a color.
        Visible (input): The item is True if the general reference line should be displayed
            in windows displaying the model.
        """
        _r = self._raw.SetLine(Name, DiscLength, DiscAngle, CSys, Color, Visible)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GenRefLine.SetLine falhou (ret={_r})".format(_r=_r))
        return None


