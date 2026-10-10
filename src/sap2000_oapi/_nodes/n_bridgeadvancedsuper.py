"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_BridgeAdvancedSuper:
    """Wrapper para SapModel.BridgeAdvancedSuper."""

    def __init__(self, raw):
        self._raw = raw

    def CountSuperCut(self, Name: str):
        """This function returns the number of superstructure section cuts that are available for
        getting analysis results and performing design. The function returns zero if the
        count is successfully retrieved, otherwise it returns a nonzero value. If the bridge
        object is not currently linked to existing objects in the model, an error is
        returned.
    
        Name (input): The name of an existing bridge object.
        Count (output): The number of section cuts in this bridge object. They will be
            identified in subsequent API functions using the indices 0 to Count-1. There may
            be one or two section cuts at each output station along the length of the
            superstructure.
        """
        _r = self._raw.CountSuperCut(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.CountSuperCut falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def CountSuperCutStressPoint(self, Name: str, CutIndex: int):
        """This function returns the number of stress points at the specified superstructure section
        cut. The function returns zero if the count is successfully retrieved, otherwise it
        returns a nonzero value. If the bridge object is not currently linked to existing
        objects in the model, an error is returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of section cut in this bridge object. This must
            be from 0 to Count-1, where Count is the value returned by function
            CountSuperCut.
        Count (output): The number of stress points for this section cut in this bridge
            object. They will be identified in subsequent API functions using the indices 0
            to Count-1.
        """
        _r = self._raw.CountSuperCutStressPoint(Name, CutIndex, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.CountSuperCutStressPoint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSuperCutLocation(self, Name: str, CutIndex: int):
        """This function returns location and orientation information about a single superstructure
        section cut in a bridge object. The function returns zero if the information is
        successfully retrieved, otherwise it returns a nonzero value. If the bridge object
        is not currently linked to existing objects in the model, an error is returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of section cut in this bridge object. This must
            be from 0 to Count-1, where Count is the value returned by function
            CountSuperCut. Section cuts will be in order of increasing Station and
            increasing SuperCutType.
        Location (output): This is 1 or 2, indicating whether the CutIndex section cut
            occurs before or after the associated station. 1 = Before the specified station.
            2 = After the specified station.
        Station (output): The station ordinate of the CutIndex section cut at the reference
            line of the superstructure. [L]
        Skew (output): The skew angle, in degrees, of the section cut, measured from the
            horizontal normal to the superstructure reference line, with positive being
            about the upward vertical axis.
        Grade (output): The grade, as a slope (abs(Grade) < 1.0), giving the vertical rise
            per distance along the superstructure reference line.
        SuperElev (output): The superelevation, as a slope (abs(SuperElev) < 1.0), giving
            the vertical rise per distance along the transverse normal to the superstructure
            reference line.
        """
        _r = self._raw.GetSuperCutLocation(Name, CutIndex, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.GetSuperCutLocation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSuperCutStressPoint(self, Name: str, CutIndex: int, PointIndex: int):
        """This function returns location and material information about a single stress point at a
        superstructure section cut in a bridge object. The function returns zero if the
        information is successfully retrieved, otherwise it returns a nonzero value. If the
        bridge object is not currently linked to existing objects in the model, an error is
        returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of section cut in this bridge object. This must
            be from 0 to Count-1, where Count is the value returned by function
            CountSuperCut.
        PointIndex (input): The index number of the stress point in this section cut in this
            bridge object. This must be from 0 to Count-1, where Count is the value returned
            by function CountSuperCutStressPoint.
        MatProp (output): The name of the material property at this stress point.
        Note (output): A description of the stress point that may be used for
            identification. Points that are pre-defined by the program will have prescribed
            notes.
        """
        _r = self._raw.GetSuperCutStressPoint(Name, CutIndex, PointIndex, 0.0, 0.0, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.GetSuperCutStressPoint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    @cached_property
    def BASConcBox(self):
        return N_BridgeAdvancedSuper_BASConcBox(self._raw.BASConcBox)


class N_BridgeAdvancedSuper_BASConcBox:
    """Wrapper para SapModel.BridgeAdvancedSuper.BASConcBox."""

    def __init__(self, raw):
        self._raw = raw

    def CountSuperCutWebStressPoint(self, Name: str, CutIndex: int, WebIndex: int):
        """This function returns the number of stress points at the specified web of the specified
        superstructure section cut. The function returns zero if the count is successfully
        retrieved; otherwise it returns a nonzero value. If the bridge object is not
        currently linked to existing objects in the model, an error is returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of section cut in this bridge object. This must
            be from 0 to Count-1, where Count is the value returned by function
            CountSuperCut.
        WebIndex (input): The index number of the web in this section cut in this bridge
            object. This must be from 0 to Count-1, where Count is the value returned by
            function GetSuperCutSectionValues.
        Count (output): The number of stress points in this web for this section cut in this
            bridge object. They will be identified in subsequent API functions using the
            indices 0 to Count-1.
        """
        _r = self._raw.CountSuperCutWebStressPoint(Name, CutIndex, WebIndex, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.BASConcBox.CountSuperCutWebStressPoint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSuperCutSectionPropsAtY(self, Name: str, CutIndex: int, Y: float, AboveY: bool):
        """This function returns section properties for the region above or below a given Y coordinate
        value at a single superstructure section cut in a bridge object. These properties
        are calculated for the section before skew, grade, and superelevation are applied.
        Coordinate values are measured from the lower-left corner of the section bounding-
        box. X is positive to the right when looking upstation, and Y is positive upward.
        The function returns zero if the information is successfully retrieved; otherwise it
        returns a nonzero value. If the bridge object is not currently linked to existing
        objects in the model, an error is returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of the section cut in this bridge object. This
            must be from 0 to Count-1, where Count is the value returned by the function
            CountSuperCut. Section cuts will be in order of increasing Station and
            increasing SuperCutType.
        Y (input): The Y coordinate in the section local coordinate system above or below
            which the section properties are calculated.
        AboveY (input): Boolean indicating whether properties are to be computed for the
            region above (if true) or below (if false) the specified coordinate Y.
        Ycg (output): Y coordinate of the centroid of the region above/below specified
            coordinate Y. [L]
        Area (output): Area of the region above/below specified coordinate Y. [L 2 ]
        Inertia (output): Moment of inertia of the region above/below specified coordinate
            Y, taken about a horizontal axis at Ycg. [L 4 ]
        """
        _r = self._raw.GetSuperCutSectionPropsAtY(Name, CutIndex, Y, AboveY, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionPropsAtY falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSuperCutSectionValues(self, Name: str, CutIndex: int, Item: int):
        """This function returns an individual section property at a single superstructure section cut
        in a bridge object. These properties are calculated for the section before skew,
        grade, and superelevation are applied. Coordinate values are measured from the
        lower-left corner of the section bounding-box. X is positive to the right when
        looking upstation, and Y is positive upward. The function returns zero if the
        information is successfully retrieved; otherwise it returns a nonzero value. If the
        bridge object is not currently linked to existing objects in the model, an error is
        returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of the section cut in this bridge object. This
            must be from 0 to Count-1, where Count is the value returned by the function
            CountSuperCut. Section cuts will be in order of increasing Station and
            increasing SuperCutType.
        Item (input): This is an integer from 1 to 12, inclusive, indicating the type of
            property value to be gotten: 1 = Number of girders or webs 2 = Design area of
            top slab, ASlabTop 3 = Design area of bottom slab, ASlabBot 4 = Width of top
            slab, BSlabTop 5 = Width of bottom slab, BSlabBot 6 = X coordinate of top slab
            centroid, XSlabTop 7 = X coordinate of bottom slab centroid, XSlabBot 8 = Y
            coordinate of top slab centroid, YSlabTop 9 = Y coordinate of bottom slab
            centroid, YSlabBot 10 = Area inside torsion circuit, ATorsion 11 = Length of
            torsion circuit, LTorsion 12 = Number of tendons 13 = Top outside width of
            torsion circuit, BTorsionTop 14 = Bottom outside width of torsion circuit,
            BTorsionBot 15 = Left outside length of torsion circuit (along slope),
            HTorsionLeft 16 = Right outside length of torsion circuit (along slope),
            HTorsionRight
        Value (output): The value of the requested item: 1 = Number of girders or webs Value
            >= 0, integral. 2 = Design area of top slab, ASlabTop Value > 0. [L 2 ] 3 =
            Design area of bottom slab, ASlabBot Value >= 0. [L 2 ] 4 = Width of top slab,
            BSlabTop Value > 0. [L] 5 = Width of bottom slab, BSlabBot Value >= 0. [L] 6 = X
            coordinate of top slab centroid, XSlabTop Any value is valid. [L] 7 = X
            coordinate of bottom slab centroid, XSlabBot Any value is valid. [L] 8 = Y
            coordinate of top slab centroid, YSlabTop Value >= 0. [L] 9 = Y coordinate of
            bottom slab centroid, YSlabBot Value <= 0. [L] 10 = Area inside torsion circuit,
            ATorsion Value >= 0. [L 2 ] 11 = Length of torsion circuit, LTorsion Value >= 0.
            [L] 12 = Number of tendons Value >= 0. 13 = Top outside width of torsion
            circuit, BTorsionTop Value > 0. [L] 14 = Bottom outside width of torsion
            circuit, BTorsionBot Value > 0. [L] 15 = Left outside length of torsion circuit
            (along slope), HTorsionLeft Value > 0. [L] 16 = Right outside length of torsion
            circuit (along slope), HTorsionRight Value > 0. [L]
        """
        _r = self._raw.GetSuperCutSectionValues(Name, CutIndex, Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionValues falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSuperCutSlabCoordsAtX(self, Name: str, CutIndex: int, X: float):
        """This function returns information about the box girder slab thicknesses at a given
        horizontal location across the box girder section. The function returns zero if the
        information is successfully retrieved; otherwise it returns a nonzero value. If the
        bridge object is not currently linked to existing objects in the model, an error is
        returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of the section cut in this bridge object. This
            must be from 0 to Count-1, where Count is the value returned by function
            CountSuperCut. Section cuts will be in order of increasing Station and
            increasing SuperCutType.
        X (input): The X coordinate in the section local coordinate system at which a
            vertical line is passed through the section and the slab coordinates are
            returned.
        Status (output): This is 0, 1, or 2. 0 = No portion of the section is cut. 1 = Only
            the section is cut; no interior cell is cut. 2 = The section and an interior
            cell are cut.
        y1 (output): The topmost Y coordinate where the vertical line cuts the section. This
            item is returned as zero when Status < 1.
        y2 (output): The bottommost Y coordinate where the vertical line cuts the section.
            This item is returned as zero when Status < 1.
        y3 (output): The topmost Y coordinate where the vertical line cuts an interior cell.
            This item is returned as zero when Status < 2.
        y4 (output): The bottommost Y coordinate where the vertical line cuts an interior
            cell. This item is returned as zero when Status < 2.
        """
        _r = self._raw.GetSuperCutSlabCoordsAtX(Name, CutIndex, X, 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSlabCoordsAtX falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSuperCutTendonNames(self, Name: str, CutIndex: int, TendonIndex: int):
        """This function returns the name of a single tendon object, giving access to tendon
        assignments, tendon section, and material property. The function returns zero if the
        information is successfully retrieved; otherwise it returns a nonzero value. If the
        bridge object is not currently linked to existing objects in the model, an error is
        returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of the section cut in this bridge object. This
            must be from 0 to Count-1, where Count is the value returned by the function
            CountSuperCut. Section cuts will be in order of increasing Station and
            increasing SuperCutType.
        TendonIndex (input): The index number of a tendon in this section cut of this bridge
            object. This must be from 0 to CountTendon-1, where CountTendon is the number of
            tendons returned by function GetSuperCutSectionValues using Item = 12.
        BridgeTendon (output): The name of the tendon inside of the bridge object
            corresponding to TendonIndex.
        TendonObj (output): The name of the tendon object created by the program from the
            bridge object tendon corresponding to TendonIndex.
        """
        _r = self._raw.GetSuperCutTendonNames(Name, CutIndex, TendonIndex, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutTendonNames falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSuperCutTendonValues(self, Name: str, CutIndex: int, TendonIndex: int, Item: int):
        """This function returns an individual section property for a single tendon at a single
        superstructure section cut in a bridge object. These properties are calculated for
        the section before skew, grade, and superelevation are applied. Coordinate values
        are measured from the lower-left corner of the section bounding-box. X is positive
        to the right when looking upstation, and Y is positive upward. The function returns
        zero if the information is successfully retrieved; otherwise it returns a nonzero
        value. If the bridge object is not currently linked to existing objects in the
        model, an error is returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of the section cut in this bridge object. This
            must be from 0 to Count-1, where Count is the value returned by the function
            CountSuperCut. Section cuts will be in order of increasing Station and
            increasing SuperCutType.
        TendonIndex (input): The index number of a tendon in this section cut of this bridge
            object. This must be from 0 to CountTendon-1, where CountTendon is the number of
            tendons returned by the function GetSuperCutSectionValues using Item = 12.
        Item (input): This is an integer from 1 to 4, inclusive, indicating the type of
            property value to be gotten: 1 = X coordinate of tendon centroid, Xcg 2 = Y
            coordinate of tendon centroid, Ycg 3 = Duct diameter for tendon 4 = Bonding type
            for tendon 5 = Tendon slope
        Value (output): The value of the requested item: 1 = X coordinate of tendon
            centroid, Xcg Any value OK. [L] 2 = Y coordinate of tendon centroid, Ycg Any
            value OK. [L] 3 = Duct diameter for tendon Value >= 0. [L] 4 = Bonding type for
            tendon 1 = Bonded 2 = Unbonded 5 = Tendon slope Any value OK. [L/L]
        """
        _r = self._raw.GetSuperCutTendonValues(Name, CutIndex, TendonIndex, Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutTendonValues falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSuperCutWebCoordsAtY(self, Name: str, CutIndex: int, Y: float):
        """This function returns information about the box girder web thicknesses at a given elevation
        in the box girder section. The function returns zero if the information is
        successfully retrieved; otherwise it returns a nonzero value. If the bridge object
        is not currently linked to existing objects in the model, an error is returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of the section cut in this bridge object. This
            must be from 0 to Count-1, where Count is the value returned by the function
            CountSuperCut. Section cuts will be in order of increasing Station and
            increasing SuperCutType.
        Y (input): The Y coordinate in the section local coordinate system at which the web
            coordinates are returned.
        NumberWebs (output): The number of webs in the section.
        WebIsCut (output): This is a array of booleans indicating if each web is cut by a
            horizontal line at the specified Y coordinate.
        WebLeft (output): This is a array of X coordinates of the left side of each web. If
            the web is not cut by a horizontal line at the specified Y coordinate, this
            value is returned as zero.
        WebRight (output): This is a array of X coordinates of the right side of each web.
            If the web is not cut by a horizontal line at the specified Y coordinate, this
            value is returned as zero.
        """
        _r = self._raw.GetSuperCutWebCoordsAtY(Name, CutIndex, Y, 0, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutWebCoordsAtY falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSuperCutWebStressPoint(self, Name: str, CutIndex: int, WebIndex: int, PointIndex: int):
        """This function returns location and material information about a single stress point in a web
        at a superstructure section cut in a bridge object. The function returns zero if the
        information is successfully retrieved; otherwise it returns a nonzero value. If the
        bridge object is not currently linked to existing objects in the model, an error is
        returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of section cut in this bridge object. This must
            be from 0 to Count-1, where Count is the value returned by function
            CountSuperCut.
        WebIndex (input): The index number of the web in this section cut in this bridge
            object. This must be from 0 to Count-1, where Count is the value returned by
            function GetSuperCutSectionValues.
        PointIndex (input): The index number of the stress point in this web of this section
            cut in this bridge object. This must be from 0 to Count-1, where Count is the
            value returned by function CountSuperCutWebStressPoint.
        MatProp (output): The name of the material property at this stress point.
        Note (output): A description of the stress point that may be used for
            identification. Points that are pre-defined by the program will have prescribed
            notes.
        """
        _r = self._raw.GetSuperCutWebStressPoint(Name, CutIndex, WebIndex, PointIndex, 0.0, 0.0, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutWebStressPoint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSuperCutWebValues(self, Name: str, CutIndex: int, WebIndex: int, Item: int):
        """This function returns an individual section property for a single web at a single
        superstructure section cut in a bridge object. These properties are calculated for
        the section before skew, grade, and superelevation are applied. Coordinate values
        are measured from the lower-left corner of the section bounding-box. X is positive
        to the right when looking upstation, and Y is positive upward The function returns
        zero if the information is successfully retrieved; otherwise it returns a nonzero
        value. An error is returned for items 3, 4, 5 and 6 if the WebIndex is specified as
        0. If the bridge object is not currently linked to existing objects in the model, an
        error is returned.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of the section cut in this bridge object. This
            must be from 0 to Count-1, where Count is the value returned by the function
            CountSuperCut. Section cuts will be in order of increasing Station and
            increasing SuperCutType.
        WebIndex (input): The index number of a web in this section cut of this bridge
            object. This must be from 0 to CountWeb-1, where CountWeb is the number of webs
            returned by thenfunction GetSuperCutSectionValues using Item = 1. Webs count
            from left to right when looking upstation.
        Item (input): This is an integer from 1 to 6, inclusive, indicating the type of
            property value to be gotten: 1 = Angle from vertical (Y) axis, clockwise is
            positive 2 = Minimum horizontal (X) web thickness 3 = Minimum top slab thickness
            above cell to left of web 4 = Minimum bottom slab thickness above cell to left
            of web 5 = Top width of cell to left of web measured from centerline of girders
            on each side of cell 6 = Bottom width of cell to left of web measured from
            centerline of girders on each side of cell.
        Value (output): The value of the requested item: 1 = Angle from vertical (Y) axis,
            clockwise is positive Abs(Value) < 90. [deg] 2 = Minimum horizontal (X) web
            thickness Value > 0. [L] 3 = Minimum top slab thickness Value < 0. [L] 4 =
            Minimum bottom slab thickness Value > 0. [L] 5 = Top width of cell Value >= 0.
            [L] 6 = Bottom width of cell Value >= 0. [L]
        """
        _r = self._raw.GetSuperCutWebValues(Name, CutIndex, WebIndex, Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutWebValues falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


