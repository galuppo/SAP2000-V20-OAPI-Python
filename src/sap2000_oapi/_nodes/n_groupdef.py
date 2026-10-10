"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_GroupDef:
    """Wrapper para SapModel.GroupDef."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value. Changing the name of group ALL will fail and return an error.
    
        Name (input): The existing name of a defined group.
        NewName (input): The new name for the group.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GroupDef.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self):
        """The function returns the number of defined groups.
        """
        _r = self._raw.Count()
        return _r

    def Delete(self, Name: str):
        """The function deletes the specified group. It will return an error if an attempt is made to
        delete the Group named ALL. The function returns zero if the group is successfully
        deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing group.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GroupDef.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetGroup(self, Name: str, SpecifiedForSelection: bool, SpecifiedForSectionCutDefinition: bool, SpecifiedForSteelDesign: bool, SpecifiedForConcreteDesign: bool, SpecifiedForAluminumDesign: bool, SpecifiedForColdFormedDesign: bool, SpecifiedForStaticNLActiveStage: bool, SpecifiedForBridgeResponseOutput: bool, SpecifiedForAutoSeismicOutput: bool, SpecifiedForAutoWindOutput: bool, SpecifiedForMassAndWeight: bool):
        """The function returns zero if the group data is successfully retrieved, otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing group.
        color (output): The display color for the group specified as a Long.
        SpecifiedForSelection (input): This item is True if the group is specified to be
            used for selection; otherwise it is False.
        SpecifiedForSectionCutDefinition (input): This item is True if the group is
            specified to be used for defining section cuts; otherwise it is False.
        SpecifiedForSteelDesign (input): This item is True if the group is specified to be
            used for defining steel frame design groups; otherwise it is False.
        SpecifiedForConcreteDesign (input): This item is True if the group is specified to
            be used for defining concrete frame design groups; otherwise it is False.
        SpecifiedForAluminumDesign (input): This item is True if the group is specified to
            be used for defining aluminum frame design groups; otherwise it is False.
        SpecifiedForColdFormedDesign (input): This item is True if the group is specified to
            be used for defining cold formed frame design groups; otherwise it is False.
        SpecifiedForStaticNLActiveStage (input): This item is True if the group is specified
            to be used for defining stages for nonlinear static analysis; otherwise it is
            False.
        SpecifiedForBridgeResponseOutput (input): This item is True if the group is
            specified to be used for reporting bridge response output; otherwise it is
            False.
        SpecifiedForAutoSeismicOutput (input): This item is True if the group is specified
            to be used for reporting auto seismic loads; otherwise it is False.
        SpecifiedForAutoWindOutput (input): This item is True if the group is specified to
            be used for reporting auto wind loads; otherwise it is False.
        SpecifiedForMassAndWeight (input): This item is True if the group is specified to be
            used for reporting group masses and weight; otherwise it is False.
        """
        _r = self._raw.GetGroup(Name, 0, SpecifiedForSelection, SpecifiedForSectionCutDefinition, SpecifiedForSteelDesign, SpecifiedForConcreteDesign, SpecifiedForAluminumDesign, SpecifiedForColdFormedDesign, SpecifiedForStaticNLActiveStage, SpecifiedForBridgeResponseOutput, SpecifiedForAutoSeismicOutput, SpecifiedForAutoWindOutput, SpecifiedForMassAndWeight)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GroupDef.GetGroup falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

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
            raise Sap2000ApiError("SapModel.GroupDef.GetAssignments falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNameList(self):
        """This function retrieves the names of all defined groups. The function returns zero if the
        names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of group names retrieved by the program.
        MyName (output): This is a one-dimensional array of group names. The MyName array is
            created as a dynamic, zero-based, array by the API user: Dim MyName() as String
            The array is dimensioned to (NumberNames 1) inside the Sap2000 program, filled
            with the names, and returned to the API user.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.GroupDef.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetGroup(self, Name: str, color: int = -1, SpecifiedForSelection: bool = True, SpecifiedForSectionCutDefinition: bool = True, SpecifiedForSteelDesign: bool = True, SpecifiedForConcreteDesign: bool = True, SpecifiedForAluminumDesign: bool = True, SpecifiedForColdFormedDesign: bool = True, SpecifiedForStaticNLActiveStage: bool = True, SpecifiedForBridgeResponseOutput: bool = True, SpecifiedForAutoSeismicOutput: bool = False, SpecifiedForAutoWindOutput: bool = False, SpecifiedForMassAndWeight: bool = True):
        """The function returns zero if the group data is successfully set, otherwise it returns a
        nonzero value.
    
        Name (input): This is the name of a group. If this is the name of an existing group,
            that group is modified, otherwise a new group is added.
        color (input): The display color for the group specified as a Long. If this value is
            input as 1, the program automatically selects a display color for the group.
        SpecifiedForSelection (input): This item is True if the group is specified to be
            used for selection; otherwise it is False.
        SpecifiedForSectionCutDefinition (input): This item is True if the group is
            specified to be used for defining section cuts; otherwise it is False.
        SpecifiedForSteelDesign (input): This item is True if the group is specified to be
            used for defining steel frame design groups; otherwise it is False.
        SpecifiedForConcreteDesign (input): This item is True if the group is specified to
            be used for defining concrete frame design groups; otherwise it is False.
        SpecifiedForAluminumDesign (input): This item is True if the group is specified to
            be used for defining aluminum frame design groups; otherwise it is False.
        SpecifiedForColdFormedDesign (input): This item is True if the group is specified to
            be used for defining cold formed frame design groups; otherwise it is False.
        SpecifiedForStaticNLActiveStage (input): This item is True if the group is specified
            to be used for defining stages for nonlinear static analysis; otherwise it is
            False.
        SpecifiedForBridgeResponseOutput (input): This item is True if the group is
            specified to be used for reporting bridge response output; otherwise it is
            False.
        SpecifiedForAutoSeismicOutput (input): This item is True if the group is specified
            to be used for reporting auto seismic loads; otherwise it is False.
        SpecifiedForAutoWindOutput (input): This item is True if the group is specified to
            be used for reporting auto wind loads; otherwise it is False.
        SpecifiedForMassAndWeight (input): This item is True if the group is specified to be
            used for reporting group masses and weight; otherwise it is False.
        """
        _r = self._raw.SetGroup(Name, color, SpecifiedForSelection, SpecifiedForSectionCutDefinition, SpecifiedForSteelDesign, SpecifiedForConcreteDesign, SpecifiedForAluminumDesign, SpecifiedForColdFormedDesign, SpecifiedForStaticNLActiveStage, SpecifiedForBridgeResponseOutput, SpecifiedForAutoSeismicOutput, SpecifiedForAutoWindOutput, SpecifiedForMassAndWeight)
        if _r != 0:
            raise Sap2000ApiError("SapModel.GroupDef.SetGroup falhou (ret={_r})".format(_r=_r))
        return None


