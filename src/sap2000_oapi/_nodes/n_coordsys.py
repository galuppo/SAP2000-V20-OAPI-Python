"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_CoordSys:
    """Wrapper para SapModel.CoordSys."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value. Changing the name of the Global coordinate system will fail and
        return an error.
    
        Name (input): The existing name of a defined coordinate system.
        NewName (input): The new name for the coordinate system.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CoordSys.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """The function returns the number of defined coordinate systems.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes the specified coordinate system. Attempting to delete the Global
        coordinate system will fail and return an error. The function returns zero if the
        coordinate system is successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing coordinate system.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CoordSys.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetCoordSys(self, Name: str):
        """The function returns zero if the coordinate system data is successfully retrieved, otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing coordinate system.
        x (output): The global X coordinate of the origin of the coordinate system. [L]
        y (output): The global Y coordinate of the origin of the coordinate system. [L]
        z (output): The global Z coordinate of the origin of the coordinate system. [L]
        """
        _r = self._raw.GetCoordSys(Name, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CoordSys.GetCoordSys falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNameList(self):
        """This function retrieves the names of all defined coordinate systems. The function returns
        zero if the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of coordinate system names retrieved by the
            program.
        MyName (output): This is a one-dimensional array of coordinate system names. The
            MyName array is created as a dynamic, zero-based, array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames 1) inside the
            Sap2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CoordSys.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTransformationMatrix(self, Name: str):
        """The function returns zero if the coordinate system transformation matrix is successfully
        returned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing coordinate system.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix from the specified global coordinate system to the global
            coordinate system. The following matrix equation shows how the transformation
            matrix is used to convert coordinates from a coordinate system to the global
            coordinate system. In the equation, c0 through c8 are the nine values from the
            transformation array; (x, y, z) are the coordinates of a point in the CSys
            coordinate system; (ux, uy, uz) are the offset of the origin of the CSys
            coordinate system from the global coordinate system; and (gx, gy, gz) are the
            global coordinates of the point.
        """
        _r = self._raw.GetTransformationMatrix(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.CoordSys.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetCoordSys(self, Name: str, x: float, y: float, z: float, RZ: float, RY: float, RX: float):
        """The function returns zero if the coordinate system is successfully added or modified,
        otherwise it returns a nonzero value. Modifying the Global coordinate system will
        fail and return an error.
    
        Name (input): This is the name of a coordinate system. If this is the name of an
            existing coordinate system, that coordinate system is modified, otherwise a new
            coordinate system is added.
        x (input): The global X coordinate of the origin of the coordinate system. [L]
        y (input): The global Y coordinate of the origin of the coordinate system. [L]
        z (input): The global Z coordinate of the origin of the coordinate system. [L]
        """
        _r = self._raw.SetCoordSys(Name, x, y, z, RZ, RY, RX)
        if _r != 0:
            raise Sap2000ApiError("SapModel.CoordSys.SetCoordSys falhou (ret={_r})".format(_r=_r))
        return None


