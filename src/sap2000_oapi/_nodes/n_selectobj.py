"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_SelectObj:
    """Wrapper para SapModel.SelectObj."""

    def __init__(self, raw):
        self._raw = raw

    def All(self, DeSelect: bool = False):
        """This function selects or deselects all objects in the model. This function returns zero if
        the selection is successfully completed, otherwise it returns nonzero.
    
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.All(DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.All falhou (ret={_r})".format(_r=_r))
        return None

    def ClearSelection(self):
        """This function deselects all objects in the model. It returns zero if the selection status is
        successfully set, otherwise it returns nonzero.
        """
        _r = self._raw.ClearSelection()
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.ClearSelection falhou (ret={_r})".format(_r=_r))
        return None

    def Constraint(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all point objects to which the specified constraint has
        been assigned. The function returns zero if the selection is successfully completed,
        otherwise it returns nonzero.
    
        Name (input): The name of an existing joint constraint.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.Constraint(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.Constraint falhou (ret={_r})".format(_r=_r))
        return None

    def CoordinateRange(self, XMin: float, XMax: float, YMin: float, YMax: float, ZMin: float, ZMax: float, DeSelect: bool = False, CSys: str = 'Global', IncludeIntersections: bool = False, Point: bool = True, Line: bool = True, Area: bool = True, Solid: bool = True, Link: bool = True):
        """This function selects or deselects objects inside the box defined by the XMin, XMax, YMin,
        YMax, ZMin and ZMax coordinates. The function returns zero if the selection is
        successfully completed, otherwise it returns nonzero.
    
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        CSys (input): The name of the coordinate system in which XMin, XMax, YMin, YMax,
            ZMin and ZMax are specified.
        IncludeIntersections (input): When this item is True, objects that are inside the
            box or intersecting the sides and edges of the box are selected or deselected.
            When this item is False, only objects that are fully inside the box are selected
            or deselected.
        Point (input): Point objects that fall inside the box are only selected or
            deselected when this item is True.
        Line (input): Line objects that fall inside the box are only selected or deselected
            when this item is True.
        Area (input): Area objects that fall inside the box are only selected or deselected
            when this item is True.
        Solid (input): Solid objects that fall inside the box are only selected or
            deselected when this item is True.
        Link (input): Link objects that fall inside the box are only selected or deselected
            when this item is True.
        """
        _r = self._raw.CoordinateRange(XMin, XMax, YMin, YMax, ZMin, ZMax, DeSelect, CSys, IncludeIntersections, Point, Line, Area, Solid, Link)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.CoordinateRange falhou (ret={_r})".format(_r=_r))
        return None

    def GetSelected(self):
        """This function retrieves a list of selected objects. The function returns zero if the
        selection list is successfully retrieved, otherwise it returns a nonzero value.
    
        NumberItems (output): The number of selected objects.
        ObjectType (output): This is an array that includes the object type of each selected
            object. 1 = Point object 2 = Frame object 3 = Cable object 4 = Tendon object 5 =
            Area object 6 = Solid object 7 = Link object
        ObjectName (output): This is an array that includes the name of each selected
            object.
        """
        _r = self._raw.GetSelected(0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SelectObj.GetSelected falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def Group(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all objects in the specified group. The function returns
        zero if the selection is successfully completed, otherwise it returns nonzero.
    
        Name (input): The name of an existing group.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.Group(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.Group falhou (ret={_r})".format(_r=_r))
        return None

    def InvertSelection(self):
        """This function deselects all selected objects and selects all unselected objects; that is, it
        inverts the selection. The function returns zero if the selection is successfully
        inverted, otherwise it returns nonzero.
        """
        _r = self._raw.InvertSelection()
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.InvertSelection falhou (ret={_r})".format(_r=_r))
        return None

    def LinesParallelToCoordAxis(self, CSys: str = 'Global', Tolerance: float = 0.057, DeSelect: bool = False):
        """This function selects or deselects objects parallel to specified coordinate axes or planes.
        The function returns zero if the selection is successfully completed, otherwise it
        returns nonzero.
    
        ParallelTo (output): This is an array of six booleans representing three coordinate
            axes and three coordinate planes. Any combination of the six may be specified.
            ParallelTo(0) = X axis ParallelTo(1) = Y axis ParallelTo(2) = Z axis
            ParallelTo(3) = XY plane ParallelTo(4) = XZ plane ParallelTo(5) = YZ plane
        CSys (input): The name of the coordinate system to which the ParallelTo items apply.
        Tolerance (input): Line objects that are within this angle in degrees of being
            parallel to a specified coordinate axis or plane are selected or deselected.
            [deg]
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.LinesParallelToCoordAxis([], CSys, Tolerance, DeSelect)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SelectObj.LinesParallelToCoordAxis falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def PlaneXY(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all objects that are in the same XY plane (in the present
        coordinate system) as the specified point object. The function returns zero if the
        selection is successfully completed, otherwise it returns nonzero.
    
        Name (input): The name of a point object.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PlaneXY(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PlaneXY falhou (ret={_r})".format(_r=_r))
        return None

    def PlaneXZ(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all objects that are in the same XZ plane (in the present
        coordinate system) as the specified point object. The function returns zero if the
        selection is successfully completed, otherwise it returns nonzero.
    
        Name (input): The name of a point object.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PlaneXZ(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PlaneXZ falhou (ret={_r})".format(_r=_r))
        return None

    def PlaneYZ(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all objects that are in the same YZ plane (in the present
        coordinate system) as the specified point object. The function returns zero if the
        selection is successfully completed, otherwise it returns nonzero.
    
        Name (input): The name of a point object.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PlaneYZ(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PlaneYZ falhou (ret={_r})".format(_r=_r))
        return None

    def PreviousSelection(self):
        """This function restores the previous selection. The function returns zero if the selection is
        successfully restored, otherwise it returns nonzero.
        """
        _r = self._raw.PreviousSelection()
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PreviousSelection falhou (ret={_r})".format(_r=_r))
        return None

    def PropertyArea(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all area objects to which the specified section has been
        assigned. The function returns zero if the selection is successfully completed,
        otherwise it returns nonzero.
    
        Name (input): The name of an existing area section property.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PropertyArea(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PropertyArea falhou (ret={_r})".format(_r=_r))
        return None

    def PropertyCable(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all cable objects to which the specified section has been
        assigned. The function returns zero if the selection is successfully completed,
        otherwise it returns nonzero.
    
        Name (input): The name of an existing cable section property.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PropertyCable(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PropertyCable falhou (ret={_r})".format(_r=_r))
        return None

    def PropertyFrame(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all line objects to which the specified section has been
        assigned. The function returns zero if the selection is successfully completed,
        otherwise it returns nonzero.
    
        Name (input): The name of an existing frame section property.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PropertyFrame(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PropertyFrame falhou (ret={_r})".format(_r=_r))
        return None

    def PropertyLink(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all link objects to which the specified section property
        has been assigned. The function returns zero if the selection is successfully
        completed, otherwise it returns nonzero.
    
        Name (input): The name of an existing link property.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PropertyLink(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PropertyLink falhou (ret={_r})".format(_r=_r))
        return None

    def PropertyLinkFD(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all link objects to which the specified frequency
        dependent link property has been assigned. The function returns zero if the
        selection is successfully completed, otherwise it returns nonzero.
    
        Name (input): The name of an existing frequency dependent link property.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PropertyLinkFD(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PropertyLinkFD falhou (ret={_r})".format(_r=_r))
        return None

    def PropertyMaterial(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all objects to which the specified material property has
        been assigned. The function returns zero if the selection is successfully completed,
        otherwise it returns nonzero.
    
        Name (input): The name of an existing material property.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PropertyMaterial(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PropertyMaterial falhou (ret={_r})".format(_r=_r))
        return None

    def PropertySolid(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all solid objects to which the specified property has
        been assigned. The function returns zero if the selection is successfully completed,
        otherwise it returns nonzero.
    
        Name (input): The name of an existing solid property.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PropertySolid(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PropertySolid falhou (ret={_r})".format(_r=_r))
        return None

    def PropertyTendon(self, Name: str, DeSelect: bool = False):
        """This function selects or deselects all tendon objects to which the specified section has
        been assigned. The function returns zero if the selection is successfully completed,
        otherwise it returns nonzero.
    
        Name (input): The name of an existing tendon section property.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        """
        _r = self._raw.PropertyTendon(Name, DeSelect)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SelectObj.PropertyTendon falhou (ret={_r})".format(_r=_r))
        return None

    def SupportedPoints(self, CSys: str = 'Local', DeSelect: bool = False, SelectRestraints: bool = True, SelectJointSprings: bool = True, SelectLineSprings: bool = True, SelectAreaSprings: bool = True, SelectSolidSprings: bool = True, SelectOneJointLinks: bool = True):
        """This function selects or deselects point objects with support in the specified degrees of
        freedom. The function returns zero if the selection is successfully completed,
        otherwise it returns nonzero.
    
        DOF (output): This is an array of six booleans for the six degrees of freedom of a
            point object. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3 DOF(3) = R1 DOF(4) = R2 DOF(5)
            = R3
        CSys (input): The name of the coordinate system in which degrees of freedom (DOF)
            are specified. This is either Local or the name of a defined coordinate system.
            Local means the point local coordinate system.
        DeSelect (input): The item is False if objects are to be selected and True if they
            are to be deselected.
        SelectRestraints (input): If this item is True then points with restraint
            assignments in one of the specified degrees of freedom are selected or
            deselected.
        SelectJointSprings (input): If this item is True then points with joint spring
            assignments in one of the specified degrees of freedom are selected or
            deselected.
        SelectLineSprings (input): If this item is True, points with a contribution from
            line spring assignments in one of the specified degrees of freedom are selected
            or deselected.
        SelectAreaSprings (input): If this item is True, points with a contribution from
            area spring assignments in one of the specified degrees of freedom are selected
            or deselected.
        SelectSolidSprings (input): If this item is True, points with a contribution from
            solid surface spring assignments in one of the specified degrees of freedom are
            selected or deselected.
        SelectOneJointLinks (input): If this item is True, points with one joint link
            assignments in one of the specified degrees of freedom are selected or
            deselected.
        """
        _r = self._raw.SupportedPoints([True]*6, CSys, DeSelect, SelectRestraints, SelectJointSprings, SelectLineSprings, SelectAreaSprings, SelectSolidSprings, SelectOneJointLinks)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.SelectObj.SupportedPoints falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


