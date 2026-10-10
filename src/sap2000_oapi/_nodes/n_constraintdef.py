"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_ConstraintDef:
    """Wrapper para SapModel.ConstraintDef."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value.
    
        Name (input): The existing name of a defined constraint.
        NewName (input): The new name for the constraint.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self, ConstraintType: int = None):
        """If the ConstraintType item is specified, the function returns the number of defined
        constraints of the specified type. Otherwise it returns the total number of defined
        constraints without regard for type.
    
        ConstraintType (input): This optional value is one of the following items in the
            eConstraintType enumeration. CONSTRAINT_BODY = 1 CONSTRAINT_DIAPHRAGM = 2
            CONSTRAINT_PLATE = 3 CONSTRAINT_ROD = 4 CONSTRAINT_BEAM = 5 CONSTRAINT_EQUAL = 6
            CONSTRAINT_LOCAL = 7 CONSTRAINT_WELD = 8 CONSTRAINT_LINE = 13
        """
        _r = self._raw.Count(ConstraintType)
        return _r

    def Delete(self, Name: str):
        """The function deletes the specified constraint. All constraint assignments for that
        constraint are also deleted. The function returns zero if the constraint is
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing constraint.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetBeam(self, Name: str, Axis: int):
        """The function returns the definition for the specified constraint. The function returns zero
        if the constraint data is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Axis (input): This is one of the following items from the eConstraintAxis
            enumeration. It specifies the axis in the specified coordinate system that is
            parallel to the axis of the constraint. If AutoAxis is specified, the axis of
            the constraint is automatically determined from the joints assigned to the
            constraint. X = 1 Y = 2 Z = 3 AutoAxis = 4
        CSys (output): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.GetBeam(Name, Axis, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetBeam falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetBody(self, Name: str):
        """The function returns the definition for the specified constraint. The function returns zero
        if the constraint data is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Value (output): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are UX, UY, UZ, RX, RY and RZ.
        CSys (output): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.GetBody(Name, [], "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetBody falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetConstraintType(self, Name: str):
        """The function returns the constraint type for the specified constraint. The function returns
        zero if the constraint type is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        ConstraintType (output): This value is one of the following items in the
            eConstraintType enumeration. CONSTRAINT_BODY = 1 CONSTRAINT_DIAPHRAGM = 2
            CONSTRAINT_PLATE = 3 CONSTRAINT_ROD = 4 CONSTRAINT_BEAM = 5 CONSTRAINT_EQUAL = 6
            CONSTRAINT_LOCAL = 7 CONSTRAINT_WELD = 8 CONSTRAINT_LINE = 13
        """
        _r = self._raw.GetConstraintType(Name, None)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetConstraintType falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetDiaphragm(self, Name: str, Axis: int):
        """The function returns the definition for the specified constraint. The function returns zero
        if the constraint data is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Axis (input): This is one of the following items from the eConstraintAxis
            enumeration. It specifies the axis in the specified coordinate system that is
            perpendicular to the plane of the constraint. If AutoAxis is specified, the axis
            of the constraint is automatically determined from the joints assigned to the
            constraint. X = 1 Y = 2 Z = 3 AutoAxis = 4
        CSys (output): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.GetDiaphragm(Name, Axis, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetDiaphragm falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetEqual(self, Name: str):
        """The function returns the definition for the specified constraint. The function returns zero
        if the constraint data is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Value (output): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are UX, UY, UZ, RX, RY and RZ.
        CSys (output): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.GetEqual(Name, [], "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetEqual falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLine(self, Name: str):
        """The function returns the definition for the specified constraint. The function returns zero
        if the constraint data is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Value (output): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are UX, UY, UZ, RX, RY and RZ.
        CSys (output): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.GetLine(Name, [], "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetLine falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocal(self, Name: str):
        """The function returns the definition for the specified constraint. The function returns zero
        if the constraint data is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Value (output): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are U1, U2, U3, R1, R2 and R3.
        """
        _r = self._raw.GetLocal(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetLocal falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined joint constraints. The function returns
        zero if the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of joint constraint names retrieved by the program.
        MyName (output): This is a one-dimensional array of joint constraint names. The
            MyName array is created as a dynamic, zero-based, array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames 1) inside the
            Sap2000 program, filled with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPlate(self, Name: str, Axis: int):
        """The function returns the definition for the specified constraint. The function returns zero
        if the constraint data is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Axis (input): This is one of the following items from the eConstraintAxis
            enumeration. It specifies the axis in the specified coordinate system that is
            perpendicular to the plane of the constraint. If AutoAxis is specified, the axis
            of the constraint is automatically determined from the joints assigned to the
            constraint. X = 1 Y = 2 Z = 3 AutoAxis = 4
        CSys (output): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.GetPlate(Name, Axis, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetPlate falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetRod(self, Name: str, Axis: int):
        """The function returns the definition for the specified constraint. The function returns zero
        if the constraint data is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Axis (input): This is one of the following items from the eConstraintAxis
            enumeration. It specifies the axis in the specified coordinate system that is
            parallel to the axis of the constraint. If AutoAxis is specified, the axis of
            the constraint is automatically determined from the joints assigned to the
            constraint. X = 1 Y = 2 Z = 3 AutoAxis = 4
        CSys (output): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.GetRod(Name, Axis, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetRod falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSpecialRigidDiaphragmList(self):
        """This function retrieves the list of the names of each special rigid diaphragm constraint. A
        special rigid diaphragm constraint is required for assignment of auto seismic load
        diaphragm eccentricity overwrites. It is also required for calculation of auto wind
        loads whose exposure widths are determined from the extents of rigid diaphragms. A
        special rigid diaphragm constraint is a constraint with the following features: 1.
        The constraint type is CONSTRAINT_DIAPHRAGM = 2. 2. The constraint coordinate system
        is Global. 3. The constraint axis is Z. The function returns zero if the name list
        is successfully retrieved; otherwise it returns a nonzero value.
    
        Num (output): The number of special rigid diaphragm constraints.
        Diaph (output): This is an array that includes the name of each special rigid
            diaphragm constraint.
        """
        _r = self._raw.GetSpecialRigidDiaphragmList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetSpecialRigidDiaphragmList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetWeld(self, Name: str):
        """The function returns the definition for the specified constraint. The function returns zero
        if the constraint data is successfully obtained, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Value (output): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are UX, UY, UZ, RX, RY and RZ.
        Tolerance (output): Joints within this distance of each other are constrained
            together.
        CSys (output): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.GetWeld(Name, [], 0.0, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetWeld falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetBeam(self, Name: str, Axis: int = 4, CSys: str = 'Global'):
        """This function defines a Beam constraint. If the specified name is not used for a constraint,
        a new constraint is defined using the specified name. If the specified name is
        already used for another Beam constraint, the definition of that constraint is
        modified. If the specified name is already used for some constraint that is not a
        Beam constraint, an error is returned. The function returns zero if the constraint
        data is successfully added or modified, otherwise it returns a nonzero value.
    
        Name (input): The name of a constraint.
        Axis (input): This is one of the following items from the eConstraintAxis
            enumeration. It specifies the axis in the specified coordinate system that is
            parallel to the axis of the constraint. If AutoAxis is specified, the axis of
            the constraint is automatically determined from the joints assigned to the
            constraint. X = 1 Y = 2 Z = 3 AutoAxis = 4
        CSys (input): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.SetBeam(Name, Axis, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.SetBeam falhou (ret={_r})".format(_r=_r))
        return None

    def SetBody(self, Name: str, Value: list[bool], CSys: str = 'Global'):
        """This function defines a Body constraint. If the specified name is not used for a constraint,
        a new constraint is defined using the specified name. If the specified name is
        already used for another Body constraint, the definition of that constraint is
        modified. If the specified name is already used for some constraint that is not a
        Body constraint, an error is returned. The function returns zero if the constraint
        data is successfully added or modified, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing constraint.
        Value (input): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are UX, UY, UZ, RX, RY and RZ.
        CSys (input): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.SetBody(Name, Value, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.SetBody falhou (ret={_r})".format(_r=_r))
        return None

    def SetDiaphragm(self, Name: str, Axis: int = 4, CSys: str = 'Global'):
        """This function defines a Diaphragm constraint. If the specified name is not used for a
        constraint, a new constraint is defined using the specified name. If the specified
        name is already used for another Diaphragm constraint, the definition of that
        constraint is modified. If the specified name is already used for some constraint
        that is not a Diaphragm constraint, an error is returned. The function returns zero
        if the constraint data is successfully added or modified, otherwise it returns a
        nonzero value.
    
        Name (input): The name of a constraint.
        Axis (input): This is one of the following items from the eConstraintAxis
            enumeration. It specifies the axis in the specified coordinate system that is
            perpendicular to the plane of the constraint. If AutoAxis is specified, the axis
            of the constraint is automatically determined from the joints assigned to the
            constraint. X = 1 Y = 2 Z = 3 AutoAxis = 4
        CSys (input): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.SetDiaphragm(Name, Axis, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.SetDiaphragm falhou (ret={_r})".format(_r=_r))
        return None

    def SetEqual(self, Name: str, Value: list[bool], CSys: str = 'Global'):
        """This function defines an Equal constraint. If the specified name is not used for a
        constraint, a new constraint is defined using the specified name. If the specified
        name is already used for another Equal constraint, the definition of that constraint
        is modified. If the specified name is already used for some constraint that is not
        an Equal constraint, an error is returned. The function returns zero if the
        constraint data is successfully added or modified, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing constraint.
        Value (input): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are UX, UY, UZ, RX, RY and RZ.
        CSys (input): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.SetEqual(Name, Value, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.SetEqual falhou (ret={_r})".format(_r=_r))
        return None

    def SetLine(self, Name: str, Value: list[bool], CSys: str = 'Global'):
        """This function defines a Line constraint. If the specified name is not used for a constraint,
        a new constraint is defined using the specified name. If the specified name is
        already used for another Line constraint, the definition of that constraint is
        modified. If the specified name is already used for some constraint that is not a
        Line constraint, an error is returned. The function returns zero if the constraint
        data is successfully added or modified, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing constraint.
        Value (input): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are UX, UY, UZ, RX, RY and RZ.
        CSys (input): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.SetLine(Name, Value, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.SetLine falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocal(self, Name: str, Value: list[bool]):
        """This function defines a Local constraint. If the specified name is not used for a
        constraint, a new constraint is defined using the specified name. If the specified
        name is already used for another Local constraint, the definition of that constraint
        is modified. If the specified name is already used for some constraint that is not a
        Local constraint, an error is returned. The function returns zero if the constraint
        data is successfully added or modified, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing constraint.
        Value (input): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are U1, U2, U3, R1, R2 and R3.
        """
        _r = self._raw.SetLocal(Name, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.SetLocal falhou (ret={_r})".format(_r=_r))
        return None

    def SetPlate(self, Name: str, Axis: int = 4, CSys: str = 'Global'):
        """This function defines a Plate constraint. If the specified name is not used for a
        constraint, a new constraint is defined using the specified name. If the specified
        name is already used for another Plate constraint, the definition of that constraint
        is modified. If the specified name is already used for some constraint that is not a
        Plate constraint, an error is returned. The function returns zero if the constraint
        data is successfully added or modified, otherwise it returns a nonzero value.
    
        Name (input): The name of a constraint.
        Axis (input): This is one of the following items from the eConstraintAxis
            enumeration. It specifies the axis in the specified coordinate system that is
            perpendicular to the plane of the constraint. If AutoAxis is specified, the axis
            of the constraint is automatically determined from the joints assigned to the
            constraint. X = 1 Y = 2 Z = 3 AutoAxis = 4
        CSys (input): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.SetPlate(Name, Axis, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.SetPlate falhou (ret={_r})".format(_r=_r))
        return None

    def SetRod(self, Name: str, Axis: int = 4, CSys: str = 'Global'):
        """This function defines a Rod constraint. If the specified name is not used for a constraint,
        a new constraint is defined using the specified name. If the specified name is
        already used for another Rod constraint, the definition of that constraint is
        modified. If the specified name is already used for some constraint that is not a
        Rod constraint, an error is returned. The function returns zero if the constraint
        data is successfully added or modified, otherwise it returns a nonzero value.
    
        Name (input): The name of a constraint.
        Axis (input): This is one of the following items from the eConstraintAxis
            enumeration. It specifies the axis in the specified coordinate system that is
            parallel to the axis of the constraint. If AutoAxis is specified, the axis of
            the constraint is automatically determined from the joints assigned to the
            constraint. X = 1 Y = 2 Z = 3 AutoAxis = 4
        CSys (input): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.SetRod(Name, Axis, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.SetRod falhou (ret={_r})".format(_r=_r))
        return None

    def SetWeld(self, Name: str, Value: list[bool], Tolerance: float, CSys: str = 'Global'):
        """This function defines a Weld constraint. If the specified name is not used for a constraint,
        a new constraint is defined using the specified name. If the specified name is
        already used for another Weld constraint, the definition of that constraint is
        modified. If the specified name is already used for some constraint that is not a
        Weld constraint, an error is returned. The function returns zero if the constraint
        data is successfully added or modified, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing constraint.
        Value (input): Value is an array of six booleans that indicate which joint degrees
            of freedom are included in the constraint. In order, the degrees of freedom
            addressed in the array are UX, UY, UZ, RX, RY and RZ.
        Tolerance (input): Joints within this distance of each other are constrained
            together.
        CSys (input): The name of the coordinate system in which the constraint is defined.
        """
        _r = self._raw.SetWeld(Name, Value, Tolerance, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.SetWeld falhou (ret={_r})".format(_r=_r))
        return None

    def GetDList(self):
        """This function retrieves the list of the names of each special rigid diaphragm constraint. A
        special rigid diaphragm constraint is required for assignment of auto seismic load
        diaphragm eccentricity overwrites. It is also required for calculation of auto wind
        loads whose exposure widths are determined from the extents of rigid diaphragms. A
        special rigid diaphragm constraint is a constraint with the following features: 1.
        The constraint type is CONSTRAINT_DIAPHRAGM = 2. 2. The constraint coordinate system
        is Global. 3. The constraint axis is Z. The function returns zero if the name list
        is successfully retrieved; otherwise it returns a nonzero value.
    
        Num (output): The number of special rigid diaphragm constraints.
        Diaph (output): This is an array that includes the name of each special rigid
            diaphragm constraint.
        """
        _r = self._raw.GetDList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.ConstraintDef.GetSpecialRigidDiaphragmList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)


