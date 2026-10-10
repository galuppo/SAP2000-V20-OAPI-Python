"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_BridgeObj:
    """Wrapper para SapModel.BridgeObj."""

    def __init__(self, raw):
        self._raw = raw

    def GetBridgeUpdateData(self, Name: str, LinkedModelExists: bool):
        """This function returns a flag indicating if the specified bridge object is currently linked
        to existing objects in the model. If the bridge object is linked, it returns the
        model type (spine, area or solid) and meshing data used when the linked bridge model
        was updated. The function returns zero if the information is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing bridge object.
        LinkedModelExists (input): This item is True if a linked bridge model exists for the
            specified bridge object.
        ModelType (output): This is 1, 2 or 3, indicating the linked bridge model type. This
            item applies only when the LinkedModelExists item is True. 1 = Spine model
            (frame). 2 = Area model. 3 = Solid model.
        MaxDeckSegLength (output): The maximum length for the deck objects in the linked
            bridge model. This item applies only when the LinkedModelExists item is True.
            [L]
        MaxCapSegLength (output): The maximum length for the cap beam objects in the linked
            bridge model. This item applies only when the LinkedModelExists item is True.
            [L]
        MaxColSegLength (output): The maximum length for the column objects in the linked
            bridge model. This item applies only when the LinkedModelExists item is True.
            [L]
        SubMeshSize (output): The maximum submesh size for area and solid objects in the
            linked bridge model. This item applies only when the LinkedModelExists item is
            True and the ModelType item is 2 or 3 (area or solid model). [L]
        """
        _r = self._raw.GetBridgeUpdateData(Name, LinkedModelExists, 0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.BridgeObj.GetBridgeUpdateData falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetBridgeUpdateForAnalysisFlag(self):
        """When this flag is True, the program automatically updates bridge objects before running an
        analysis if it detects anything has been changed that might affect the bridge
        analysis. This flag is by default set to True for each new Sap2000 Object.
        """
        _r = self._raw.GetBridgeUpdateForAnalysisFlag()
        return _r

    def SetBridgeUpdateData(self, Name: str, Action: int, ModelType: int, MaxDeckSegLength: float, MaxCapSegLength: float, MaxColSegLength: float, SubMeshSize: float):
        """This function updates a linked bridge model, clears all objects from a linked bridge model,
        or converts a linked bridge model to an unlinked model. The function returns zero if
        it is successful.
    
        Name (input): The name of an existing bridge object.
        Action (input): This is 1, 2 or 3, indicating the action to be taken. 1 = Update
            linked model. 2 = Clear all from linked model. 3 = Convert to unlinked model.
        ModelType (input): This is 1, 2 or 3, indicating the linked bridge model type. This
            item applies only when the Action item is 1 (update linked model). 1 = Spine
            model (frame). 2 = Area model. 3 = Solid model.
        MaxDeckSegLength (input): The maximum length for the deck objects in the linked
            bridge model. This item applies only when the Action item is 1 (update linked
            model). [L]
        MaxCapSegLength (input): The maximum length for the cap beam objects in the linked
            bridge model. This item applies only when the Action item is 1 (update linked
            model). [L]
        MaxColSegLength (input): The maximum length for the column objects in the linked
            bridge model. This item applies only when the Action item is 1 (update linked
            model). [L]
        SubMeshSize (input): The maximum submesh size for area and solid objects in the
            linked bridge model. This item applies only when the Action item is 1 (update
            linked model) and the ModelType item is 2 or 3 (area or solid model). [L]
        """
        _r = self._raw.SetBridgeUpdateData(Name, Action, ModelType, MaxDeckSegLength, MaxCapSegLength, MaxColSegLength, SubMeshSize)
        if _r != 0:
            raise Sap2000ApiError("SapModel.BridgeObj.SetBridgeUpdateData falhou (ret={_r})".format(_r=_r))
        return None

    def SetBridgeUpdateForAnalysisFlag(self, Value: bool):
        """This function returns zero if the flag is successfully set, otherwise it returns a nonzero
        value. This flag is by default set to True for each new Sap2000 Object.
    
        Value (input): A boolean (True or False) value. When this item is True the program
            automatically updates bridge objects before running an analysis if it detects
            anything has been changed that might affect the bridge analysis.
        """
        _r = self._raw.SetBridgeUpdateForAnalysisFlag(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.BridgeObj.SetBridgeUpdateForAnalysisFlag falhou (ret={_r})".format(_r=_r))
        return None


