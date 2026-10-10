"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_EditPoint:
    """Wrapper para SapModel.EditPoint."""

    def __init__(self, raw):
        self._raw = raw

    def Align(self, MyType: int, Ordinate: float):
        """This function aligns selected point objects. The function returns zero if the alignment is
        successful; otherwise it returns a nonzero value.
    
        MyType (input): This is 1, 2, 3 or 4, indicating the alignment option. 1 = Align
            points to X-ordinate in present coordinate system 2 = Align points to Y-ordinate
            in present coordinate system 3 = Align points to Z-ordinate in present
            coordinate system 4 = Align points to nearest selected line object, area object
            edge or solid object edge
        Ordinate (input): The X, Y or Z ordinate that applies if MyType is 1, 2 or 3,
            respectively. [L]
        NumberPoints (output): The number of point objects that are in a new location after
            the alignment is complete.
        PointName (output): This is an array of the name of each point object that is in a
            new location after the alignment is complete.
        """
        _r = self._raw.Align(MyType, Ordinate, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditPoint.Align falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ChangeCoordinates_1(self, Name: str, x: float, y: float, z: float, NoRefresh: bool = False):
        """This function changes the coordinates of a specified point object. The function returns zero
        if the coordinate change is successful; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object.
        NoRefresh (input): If this item is True, the model display window is not refreshed
            after the point object is moved.
        """
        _r = self._raw.ChangeCoordinates_1(Name, x, y, z, NoRefresh)
        if _r != 0:
            raise Sap2000ApiError("SapModel.EditPoint.ChangeCoordinates_1 falhou (ret={_r})".format(_r=_r))
        return None

    def Connect(self):
        """This function connects objects that have been disconnected using the Disconnect function. If
        two or more objects have different end points objects that are at the same location,
        all of those objects can be connected together by selecting the objects, and
        selecting their end points, and calling the Connect function. The result will be
        that all of the objects are connected at a single point. The function returns zero
        if the connect is successful; otherwise it returns a nonzero value.
    
        NumberPoints (output): The number of the point objects that remain at locations
            where connections were made.
        PointName (output): This is an array of the name of each point object that remains
            at locations where connections were made.
        """
        _r = self._raw.Connect(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditPoint.Connect falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def Disconnect(self):
        """This function disconnects selected point objects. Disconnect creates a separate point for
        each object that frames into the selected point object. The function returns zero if
        the disconnect is successful; otherwise it returns a nonzero value.
    
        NumberPoints (output): The number of the point objects (including the original
            selected point objects) that are created by the disconnect action.
        PointName (output): This is an array of the name of each point object (including the
            original selected point objects) that is created by the disconnect action.
        """
        _r = self._raw.Disconnect(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditPoint.Disconnect falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def Merge(self, MergeTol: float):
        """This function merges selected point objects that are within a specified distance of one
        another. The function returns zero if the merge is successful; otherwise it returns
        a nonzero value.
    
        MergeTol (input): Point objects within this distance of one another are merged into
            one point object. [L]
        NumberPoints (output): The number of the selected point objects that still exist
            after the merge is complete.
        PointName (output): This is an array of the name of each selected point object that
            still exists after the merge is complete.
        """
        _r = self._raw.Merge(MergeTol, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditPoint.Merge falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)


