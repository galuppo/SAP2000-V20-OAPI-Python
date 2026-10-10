"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_Group:
    """Wrapper para SapModel.Group."""

    def __init__(self, raw):
        self._raw = raw

    def Clear(self, Name: str):
        """This function clears (removes) all assignments from the specified group. The function
        returns zero if the group assignment is successfully cleared, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing group.
        """
        _r = self._raw.Clear(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Group.Clear falhou (ret={_r})".format(_r=_r))
        return None

    def GetAssignments(self, Name: str):
        """This function retrieves the assignments to a specified group. The function returns zero if
        the group assignment is successfully retrieved, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing group.
        NumberItems (output): The number of assignments made to the specified group.
        ObjectType (output): This is an array that includes the object type of each item in
            the group. 1 = Point object 2 = Frame object 3 = Cable object 4 = Tendon object
            5 = Area object 6 = Solid object 7 = Link object
        ObjectName (output): This is an array that includes the name of each item in the
            group.
        """
        _r = self._raw.GetAssignments(Name, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Group.GetAssignments falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)


