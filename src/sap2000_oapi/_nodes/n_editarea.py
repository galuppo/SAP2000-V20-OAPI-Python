"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_EditArea:
    """Wrapper para SapModel.EditArea."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeConnectivity(self, Name: str, NumberPoints: int):
        """This function modifies the connectivity of an area object. The function returns zero if the
        area object connectivity is successfully modified; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing area object.
        NumberPoints (input): The number of points in the area abject.
        Point (output): This is an array containing the names of the point objects that
            define the added area object. The point object names should be ordered to run
            clockwise or counter-clockwise around the area object.
        """
        _r = self._raw.ChangeConnectivity(Name, NumberPoints, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditArea.ChangeConnectivity falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def Divide(self, Name: str, MeshType: int, n1: int = 2, n2: int = 2, MaxSize1: float = 0, MaxSize2: float = 0, PointOnEdgeFromGrid: bool = False, PointOnEdgeFromLine: bool = False, PointOnEdgeFromPoint: bool = False, ExtendCookieCutLines: bool = False, Rotation: float = 0, MaxSizeGeneral: float = 0, LocalAxesOnEdge: bool = False, LocalAxesOnFace: bool = False, RestraintsOnEdge: bool = False, RestraintsOnFace: bool = False):
        """This function meshes area objects. The function returns zero if the meshing is successful;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object.
        MeshType (input): This item is 1, 2, 3, 4, 5 or 6, indicating the mesh type for the
            area object. 1 = Mesh area into a specified number of objects 2 = Mesh area into
            objects of a specified maximum size 3 = Mesh area based on points on area edges
            4 = Cookie cut mesh area based on lines intersecting edges 5 = Cookie cut mesh
            area based on points 6 = Mesh area using General Divide Tool Mesh options 1, 2
            and 3 apply to quadrilaterals and triangles only.
        NumberAreas (output): The number of area objects created when the specified area
            object is divided.
        AreaName (output): This is an array of the name of each area object created when the
            specified area object is divided.
        n1 (input): This item applies when MeshType = 1. It is the number of objects created
            along the edge of the meshed area object that runs from point 1 to point 2.
        n2 (input): This item applies when MeshType = 1. It is the number of objects created
            along the edge of the meshed area object that runs from point 1 to point 3.
        MaxSize1 (input): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed area object that runs from point 1
            to point 2. [L] If this item is input as 0, the default value is used. The
            default value is 48 inches if the database units are English or 120 centimeters
            if the database units are metric.
        MaxSize2 (input): This item applies when MeshType = 2. It is the maximum size of
            objects created along the edge of the meshed area object that runs from point 1
            to point 3. [L] If this item is input as 0, the default value is used. The
            default value is 48 inches if the database units are English or 120 centimeters
            if the database units are metric.
        PointOnEdgeFromGrid (input): This item applies when MeshType = 3. If it is True,
            points on the area object edges are determined from intersections of visible
            grid lines with the area object edges.
        PointOnEdgeFromLine (input): This item applies when MeshType = 3. If it is True,
            points on the area object edges are determined from intersections of selected
            straight line objects with the area object edges.
        PointOnEdgeFromPoint (input): This item applies when MeshType = 3. If it is True,
            points on the area object edges are determined from selected point objects that
            lie on the area object edges.
        ExtendCookieCutLines (input): This item applies when MeshType = 4. MeshType = 4
            provides cookie cut meshing based on selected straight line objects that
            intersect the area object edges. If the ExtendCookieCutLines item is True, all
            selected straight line objects are extended to intersect the area object edges
            for the purpose of meshing the area object.
        Rotation (input): This item applies when MeshType = 5. MeshType = 5 provides cookie
            cut meshing based on two perpendicular lines passing through selected point
            objects. By default these lines align with the area object local 1 and 2 axes.
            The Rotation item is an angle in degrees that the meshing lines are rotated from
            their default orientation. [deg]
        MaxSizeGeneral (input): This item applies when MeshType = 6. It is the maximum size
            of objects created by the General Divide Tool. If this item is input as 0, the
            default value is used. The default value is 48 inches if the database units are
            English or 120 centimeters if the database units are metric.
        LocalAxesOnEdge (input): If this item is True, and if both points along an edge of
            the original area object have the same local axes, the program makes the local
            axes for added points along the edge the same as the edge end points.
        LocalAxesOnFace (input): If this item is True, and if all points around the
            perimeter of the original area object have the same local axes, the program
            makes the local axes for all added points the same as the perimeter points.
        RestraintsOnEdge (input): If this item is True, and if both points along an edge of
            the original area object have the same restraint/constraint, then, if the added
            point and the adjacent corner points have the same local axes definition, the
            program includes the restraint/constraint for added points along the edge.
        RestraintsOnFace (input): If this item is True, and if all points around the
            perimeter of the original area object have the same restraint/constraint, then,
            if an added point and the perimeter points have the same local axes definition,
            the program includes the restraint/constraint for the added point.
        """
        _r = self._raw.Divide(Name, MeshType, 0, [], n1, n2, MaxSize1, MaxSize2, PointOnEdgeFromGrid, PointOnEdgeFromLine, PointOnEdgeFromPoint, ExtendCookieCutLines, Rotation, MaxSizeGeneral, LocalAxesOnEdge, LocalAxesOnFace, RestraintsOnEdge, RestraintsOnFace)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditArea.Divide falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ExpandShrink(self, OffsetType: int, Offset: float):
        """This function expands or shrinks selected area objects. The function returns zero if it is
        successful; otherwise it returns a nonzero value.
    
        OffsetType (input): This item is 0, 1 or 2, indicating the offset type for the
            selected area objects. 0 = Offset all area edges 1 = Offset selected area edges
            only 2 = Offset selected points of selected areas only
        Offset (input): The area edge offset distance. Positive distances expand the object
            and negative distances shrink the object.[L]
        """
        _r = self._raw.ExpandShrink(OffsetType, Offset)
        if _r != 0:
            raise Sap2000ApiError("SapModel.EditArea.ExpandShrink falhou (ret={_r})".format(_r=_r))
        return None

    def Merge(self):
        """This function merges selected area objects. The function returns zero if it is successful;
        otherwise it returns a nonzero value.
    
        NumberAreas (output): The number of originally selected area objects that remain
            when the merge is successfully completed.
        AreaName (output): This is an array that includes the names of the selected area
            objects that remain when the merge is successfully completed.
        """
        _r = self._raw.Merge(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditArea.Merge falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def PointAdd(self):
        """This function adds a point object at the midpoint of selected area object edges. The
        function returns zero if it is successful; otherwise it returns a nonzero value.
        """
        _r = self._raw.PointAdd()
        if _r != 0:
            raise Sap2000ApiError("SapModel.EditArea.PointAdd falhou (ret={_r})".format(_r=_r))
        return None

    def PointRemove(self):
        """This function removes selected point objects from selected area objects. Note that in some
        cases this command can cause the area object to be deleted. The function returns
        zero if it is successful; otherwise it returns a nonzero value.
        """
        _r = self._raw.PointRemove()
        if _r != 0:
            raise Sap2000ApiError("SapModel.EditArea.PointRemove falhou (ret={_r})".format(_r=_r))
        return None


