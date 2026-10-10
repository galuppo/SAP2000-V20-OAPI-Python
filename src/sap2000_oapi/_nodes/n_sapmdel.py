"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_SapMdel:
    """Wrapper para SapModel.SapMdel."""

    def __init__(self, raw):
        self._raw = raw

    @cached_property
    def PointObj(self):
        return N_SapMdel_PointObj(self._raw.PointObj)


class N_SapMdel_PointObj:
    """Wrapper para SapModel.SapMdel.PointObj."""

    def __init__(self, raw):
        self._raw = raw

    def SetPanelZone(self, Name: str, PropType: int, Thickness: float, K1: float, K2: float, LinkProp: str, Connectivity: int, LocalAxisFrom: int, LocalAxisAngle: float, ItemType: int = 0):
        """This function makes panel zone assignments to point objects. Any existing panel zone
        assignments are replaced by the new assignments. The function returns zero if the
        panel zone data is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing point object.
        PropType (input): This is 0, 1, 2, or 3. 0 = Properties are elastic from column 1 =
            Properties are elastic from column and doubler plate 2 = Properties are from
            specified spring stiffnesses 3 = Properties are from a specified link property
        Thickness (input): The thickness of the doubler plate. This item applies only when
            PropType = 1. [L]
        K1 (input): The spring stiffness for major axis bending (about the local 3 axis of
            the column and panel zone). This item applies only when PropType = 2. [FL/rad]
        K2 (input): The spring stiffness for minor axis bending (about the local 2 axis of
            the column and panel zone). This item applies only when PropType = 2. [FL/rad]
        LinkProp (input): The name of the link property used to define the panel zone. This
            item applies only when PropType = 3.
        Connectivity (input): This is 0 or 1. 0 = Panel zone connects beams to other objects
            1 = Panel zone connects braces to other objects
        LocalAxisFrom (input): This is 0 or 1. 0 = Panel zone local axis angle is from
            column 1 = Panel zone local axis angle is user defined The LocalAxisFrom item
            can be 1 only when the PropType item is 3.
        LocalAxisAngle (input): This item applies only when PropType = 3 and LocalAxisFrom =
            1. It is the angle measured counter clockwise from the positive global X-axis to
            the local 2-axis of the panel zone. [deg]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the panel zone
            assignment is made to the point object specified by the Name item. If this item
            is Group, the panel zone assignment is made to all point objects in the group
            specified by the Name item. If this item is SelectedObjects, the panel zone
            assignment is made to all selected point objects and the Name item is ignored.
        """
        _r = self._raw.SetPanelZone(Name, PropType, Thickness, K1, K2, LinkProp, Connectivity, LocalAxisFrom, LocalAxisAngle, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.SapMdel.PointObj.SetPanelZone falhou (ret={_r})".format(_r=_r))
        return None


