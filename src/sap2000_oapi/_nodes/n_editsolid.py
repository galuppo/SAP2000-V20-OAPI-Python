"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_EditSolid:
    """Wrapper para SapModel.EditSolid."""

    def __init__(self, raw):
        self._raw = raw

    def Divide(self, Name: str, n1: int, n2: int, n3: int):
        """This function meshes solid objects. The function returns zero if the meshing is successful;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing solid object.
        n1 (input): This is the number of objects created between faces 2 and 4 of the solid
            object.
        n2 (input): This is the number of objects created between faces 1 and 3 of the solid
            object.
        n3 (input): This is the number of objects created between faces 5 and 6 of the solid
            object.
        NumberSolids (output): The number of solid objects created when the specified solid
            object is divided.
        SolidName (output): This is an array of the name of each solid object created when
            the specified solid object is divided.
        """
        _r = self._raw.Divide(Name, n1, n2, n3, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.Divide falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ExtrudeAreaToSolidLinearNormal(self, Name: str, PropName: str, nPlus3: int, tPlus3: float, nMinus3: int, tMinus3: float, Remove: bool = True):
        """This function creates new solid objects by linearly extruding a specified area object, in
        the local 3-axis direction of the area object, into solid objects. The function
        returns zero if the extrusion is successful; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object to be extruded.
        PropName (input): This is either Default or the name of a defined solid property to
            be used for the new extruded solid objects.
        nPlus3 (input): The number of solid objects created in the positive local 3-axis
            direction of the specified area object.
        tPlus3 (input): The thickness of the solid objects created in the positive local
            3-axis direction of the specified area object.
        nMinus3 (input): The number of solid objects created in the negative local 3-axis
            direction of the specified area object.
        tMinus3 (input): The thickness of the solid objects created in the negative local
            3-axis direction of the specified area object.
        NumberSolids (output): The number of solid objects created when the specified area
            object is extruded.
        SolidName (output): This is an array of the name of each solid object created when
            the specified area object is extruded.
        Remove (input): If this item is True, the area object indicated by the Name item is
            deleted after the extrusion is complete.
        """
        _r = self._raw.ExtrudeAreaToSolidLinearNormal(Name, PropName, nPlus3, tPlus3, nMinus3, tMinus3, 0, [], Remove)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ExtrudeAreaToSolidLinearNormal falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ExtrudeAreaToSolidLinearUser(self, Name: str, PropName: str, dx: float, dy: float, dz: float, Number: int, Remove: bool = True):
        """This function creates new solid objects by linearly extruding a specified area object, in a
        user specified direction, into solid objects. The function returns zero if the
        extrusion is successful; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing area object to be extruded.
        PropName (input): This is either Default or the name of a defined solid property to
            be used for the new extruded solid objects.
        Number (input): The number of increments for the extrusion.
        NumberSolids (output): The number of solid objects created when the specified area
            object is extruded. Usually this item is returned the same as the Number item.
            However, in some cases, such as when an area object with more than four sides is
            extruded, this item will be larger than the Number item.
        SolidName (output): This is an array of the name of each solid object created when
            the specified area object is extruded.
        Remove (input): If this item is True, the area object indicated by the Name item is
            deleted after the extrusion is complete.
        """
        _r = self._raw.ExtrudeAreaToSolidLinearUser(Name, PropName, dx, dy, dz, Number, 0, [], Remove)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ExtrudeAreaToSolidLinearUser falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ExtrudeAreaToSolidRadial(self, Name: str, PropName: str, RotateAxis: int, x: float, y: float, z: float, IncrementAng: float, TotalRise: float, Number: int, Remove: bool = True):
        """This function creates new solid objects by radially extruding a specified area object into
        solid objects. The function returns zero if the extrusion is successful; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing area object to be extruded.
        PropName (input): This is either Default or the name of a defined solid property to
            be used for the new extruded solid objects.
        RotateAxis (input): This is 0, 1 or 2, indicating the axis that the radial extrusion
            is around. 0 = X axis 1 = Y axis 2 = Z axis
        IncrementAng (input): The angle is rotated by this amount for each added solid
            object. [deg]
        TotalRise (input): The total rise over the full length of the extrusion. [L]
        Number (input): The number of angle increments for the extrusion.
        NumberSolids (output): The number of solid objects created when the specified area
            object is extruded. Usually this item is returned the same as the Number item.
            However, in some cases, such as when an area object with more than four sides is
            extruded, this item will be larger than the Number item.
        SolidName (output): This is an array of the name of each solid object created when
            the specified area object is extruded.
        Remove (input): If this item is True, the area object indicated by the Name item is
            deleted after the extrusion is complete.
        """
        _r = self._raw.ExtrudeAreaToSolidRadial(Name, PropName, RotateAxis, x, y, z, IncrementAng, TotalRise, Number, 0, [], Remove)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ExtrudeAreaToSolidRadial falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ExtrudeFrameToAreaLinear(self, Name: str, PropName: str, dx: float, dy: float, dz: float, NumberAreas: int, Remove: bool = True):
        """This function creates new area objects by linearly extruding a specified straight frame
        object into area objects. The function returns zero if the extrusion is successful;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing straight frame object to be extruded.
        PropName (input): This is Default, None or the name of a defined area property to be
            used for the new extruded area objects.
        NumberAreas (input): The number of area objects created when the specified line
            object is extruded.
        AreaName (output): This is an array of the name of each area object created when the
            specified line object is extruded.
        Remove (input): If this item is True, the straight frame object indicated by the
            Name item is deleted after the extrusion is complete.
        """
        _r = self._raw.ExtrudeFrameToAreaLinear(Name, PropName, dx, dy, dz, NumberAreas, [], Remove)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ExtrudeFrameToAreaLinear falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ExtrudeFrameToAreaRadial(self, Name: str, PropName: str, RotateAxis: int, x: float, y: float, z: float, IncrementAng: float, TotalRise: float, NumberAreas: int, Remove: bool = True):
        """This function creates new area objects by radially extruding a specified straight frame
        object into area objects. The function returns zero if the extrusion is successful;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing line object to be extruded.
        PropName (input): This is Default, None or the name of a defined area property to be
            used for the new extruded area objects.
        RotateAxis (input): This is 0, 1 or 2, indicating the axis that the radial extrusion
            is around. 0 = X axis 1 = Y axis 2 = Z axis
        IncrementAng (input): The angle is rotated by this amount for each added area
            object. [deg]
        TotalRise (input): The total rise over the full length of the extrusion. [L]
        NumberAreas (input): The number of area objects created when the specified line
            object is extruded.
        AreaName (output): This is an array of the name of each area object created when the
            specified line object is extruded.
        Remove (input): If this item is True, the straight frame object indicated by the
            Name item is deleted after the extrusion is complete.
        """
        _r = self._raw.ExtrudeFrameToAreaRadial(Name, PropName, RotateAxis, x, y, z, IncrementAng, TotalRise, NumberAreas, [], Remove)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ExtrudeFrameToAreaRadial falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ExtrudePointToFrameLinear(self, Name: str, PropName: str, dx: float, dy: float, dz: float, NumberFrames: int):
        """This function creates new frame objects by linearly extruding a specified point object into
        frame objects. The function returns zero if the extrusion is successful; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing point object to be extruded.
        PropName (input): This is Default, None or the name of a defined frame section
            property to be used for the new extruded frame objects.
        NumberFrames (input): The number of frame objects created when the specified point
            object is extruded.
        FrameName (output): This is an array of the name of each frame object created when
            the specified point object is extruded.
        """
        _r = self._raw.ExtrudePointToFrameLinear(Name, PropName, dx, dy, dz, NumberFrames, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ExtrudePointToFrameLinear falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ExtrudePointToFrameRadial(self, Name: str, PropName: str, RotateAxis: int, x: float, y: float, z: float, IncrementAng: float, TotalRise: float, NumberFrames: int):
        """This function creates new frame objects by radially extruding a specified point object into
        frame objects. The function returns zero if the extrusion is successful; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing point object to be extruded.
        PropName (input): This is Default, None or the name of a defined frame section
            property to be used for the new extruded frame objects.
        RotateAxis (input): This is 0, 1 or 2, indicating the axis that the radial extrusion
            is around. 0 = X axis 1 = Y axis 2 = Z axis
        IncrementAng (input): The angle is rotated by this amount for each added frame
            object. [deg]
        TotalRise (input): The total rise over the full length of the extrusion. [L]
        NumberFrames (input): The number of frame objects created when the specified point
            object is extruded.
        FrameName (output): This is an array of the name of each frame object created when
            the specified point object is extruded.
        """
        _r = self._raw.ExtrudePointToFrameRadial(Name, PropName, RotateAxis, x, y, z, IncrementAng, TotalRise, NumberFrames, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ExtrudePointToFrameRadial falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ReplicateLinear(self, dx: float, dy: float, dz: float, Number: int, Remove: bool = False):
        """This function linearly replicates selected objects. The function returns zero if the
        replication is successful; otherwise it returns a nonzero value.
    
        Number (input): The number of times the selected objects are to be replicated.
        NumberObjects (output): The number of new objects created by the replication
            process.
        ObjectName (output): This is an array of the name of each object created by the
            replication process.
        ObjectType (output): This is an array of the type of each object created by the
            replication process. 1 = Point object 2 = Frame object 3 = Cable object 4 =
            Tendon object 5 = Area object 6 = Solid object 7 = Link object
        Remove (input): If this item is True, the originally selected objects are deleted
            after the replication is complete.
        """
        _r = self._raw.ReplicateLinear(dx, dy, dz, Number, 0, [], [], Remove)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ReplicateLinear falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ReplicateMirror(self, Plane: int, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, Remove: bool = False):
        """This function mirror replicates selected objects. The function returns zero if the
        replication is successful; otherwise it returns a nonzero value.
    
        Plane (input): This is 1, 2, 3 or 4, indicating the mirror plane type. 1 = Parallel
            to Z 2 = Parallel to X 3 = Parallel to Y 4 = 3D plane
        NumberObjects (output): The number of new objects created by the replication
            process.
        ObjectName (output): This is an array of the name of each object created by the
            replication process.
        ObjectType (output): This is an array of the type of each object created by the
            replication process. 1 = Point object 2 = Frame object 3 = Cable object 4 =
            Tendon object 5 = Area object 6 = Solid object 7 = Link object
        Remove (input): If this item is True, the originally selected objects are deleted
            after the replication is complete.
        """
        _r = self._raw.ReplicateMirror(Plane, x1, y1, z1, x2, y2, z2, x3, y3, z3, 0, [], [], Remove)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ReplicateMirror falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ReplicateRadial(self, RotateAxis: int, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, Number: int, Ang: float, Remove: bool = False):
        """This function radially replicates selected objects. The function returns zero if the
        replication is successful; otherwise it returns a nonzero value.
    
        RotateAxis (input): This is 1, 2, 3 or 4, indicating the rotation axis. 1 = Parallel
            to X axis 2 = Parallel to Y axis 3 = Parallel to Z axis 4 = 3D line
        Number (input): The increment angle for each replication.
        Ang (input): The number of times the selected objects are to be replicated.
        NumberObjects (output): The number of new objects created by the replication
            process.
        ObjectName (output): This is an array of the name of each object created by the
            replication process.
        ObjectType (output): This is an array of the type of each object created by the
            replication process. 1 = Point object 2 = Frame object 3 = Cable object 4 =
            Tendon object 5 = Area object 6 = Solid object 7 = Link object
        Remove (input): If this item is True, the originally selected objects are deleted
            after the replication is complete.
        """
        _r = self._raw.ReplicateRadial(RotateAxis, x1, y1, z1, x2, y2, z2, Number, Ang, 0, [], [], Remove)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.EditSolid.ReplicateRadial falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)


