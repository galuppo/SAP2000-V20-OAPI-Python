"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_EditFrame:
    """Wrapper para SapModel.EditFrame."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeConnectivity(self, Name: str, Point1: str, Point2: str):
        """This function modifies the connectivity of a frame object. The function returns zero if the
        frame object connectivity is successfully modified; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing frame object.
        Point1 (input): The name of the point object at the I-End of the frame object.
        Point2 (input): The name of the point object at the J-End of the frame object.
        """
        _r = self._raw.ChangeConnectivity(Name, Point1, Point2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.EditFrame.ChangeConnectivity falhou (ret={_r})".format(_r=_r))
        return None

    def DivideAtDistance(self, Name: str, Dist: float, IEnd: bool):
        """This function divides straight frame objects into two objects at a location defined by the
        Dist and IEnd items. Curved frame objects are not divided. The function returns zero
        if the frame objects are successfully divided; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing straight frame object.
        Dist (input): The frame object is divided at this distance from the end specified by
            the IEnd item.[L]
        IEnd (input): If this item is True, the Dist item is measured from the I-end of the
            frame object. Otherwise it is measured from the J-end of the frame object.
        NewName (output): This is an array that includes the names of the two new frame
            objects.
        """
        _r = self._raw.DivideAtDistance(Name, Dist, IEnd, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditFrame.DivideAtDistance falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def DivideAtIntersections(self, Name: str):
        """This function divides straight frame objects at intersections with selected point objects,
        line objects, area edges and solid edges. Curved frame objects are not divided. The
        function returns zero if the frame objects are successfully divided; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing straight frame object.
        Num (output): This is the number of frame objects into which the specified frame
            object is divided.
        NewName (output): This is an array that includes the names of the new frame objects.
        """
        _r = self._raw.DivideAtIntersections(Name, 0.0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditFrame.DivideAtIntersections falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def DivideByRatio(self, Name: str, Num: int, Ratio: float):
        """This function divides straight frame objects based on a specified Last/First length ratio.
        Curved frame objects are not divided. The function returns zero if the frame objects
        are successfully divided; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing straight frame object.
        Num (input): The frame object is divided into this number of new objects.
        Ratio (input): The Last/First length ratio for the new frame objects.
        NewName (output): This is an array that includes the names of the new frame objects.
        """
        _r = self._raw.DivideByRatio(Name, Num, Ratio, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditFrame.DivideByRatio falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def Extend(self, Name: str, IEnd: bool, JEnd: bool, Item1: str, Item2: str = ''):
        """This function extends straight frame objects. Curved frame objects are not extended. The
        function returns zero if the frame objects are successfully extended; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing straight frame object to be extended.
        IEnd (input): This item is True if the I-End of the frame object specified by the
            Name item is to be extended.
        JEnd (input): This item is True if the J-End of the frame object specified by the
            Name item is to be extended.
        Item1 (input): The name of an existing straight frame object used as a extension
            line.
        Item2 (input): The name of an existing straight frame object used as a extension
            line.
        """
        _r = self._raw.Extend(Name, IEnd, JEnd, Item1, Item2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.EditFrame.Extend falhou (ret={_r})".format(_r=_r))
        return None

    def Join(self, Name: str, Item2: str):
        """This function joins two straight frame objects that have a common end point and are
        colinear. The function returns zero if the frame objects are successfully joined;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object to be joined. The new, joined
            frame object keeps this name.
        Item2 (input): The name of an existing frame object to be joined.
        """
        _r = self._raw.Join(Name, Item2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.EditFrame.Join falhou (ret={_r})".format(_r=_r))
        return None

    def Trim(self, Name: str, IEnd: bool, JEnd: bool, Item1: str, Item2: str = ''):
        """This function trims straight frame objects. Curved frame objects are not trimmed. The
        function returns zero if the frame objects are successfully trimmed; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing straight frame object to be trimmed.
        IEnd (input): This item is True if the I-End of the frame object specified by the
            Name item is to be trimmed.
        JEnd (input): This item is True if the J-End of the frame object specified by the
            Name item is to be trimmed.
        Item1 (input): The name of an existing straight frame object used as a trim line.
        Item2 (input): The name of an existing straight frame object used as a trim line.
        """
        _r = self._raw.Trim(Name, IEnd, JEnd, Item1, Item2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.EditFrame.Trim falhou (ret={_r})".format(_r=_r))
        return None


