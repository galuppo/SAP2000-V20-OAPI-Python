"""Abertura da conexão com o SAP2000 via OAPI (comtypes), devolvendo um
SapModelWrapper tipado em vez do objeto COM cru.
"""

from __future__ import annotations

import comtypes.client

from .enums import eUnits
from .model import SapModelWrapper


class Sap2000Connection:
    """Uso:

        with Sap2000Connection(visible=True) as sap:
            sap.PropMaterial.SetMaterial("C30", eMatType.MATERIAL_CONCRETE)
            sap.FrameObj.AddByCoord(...)
            ...

    `sap` é um SapModelWrapper: navega a árvore de objetos exatamente como
    a OAPI documenta (sap.LoadPatterns.AutoSeismic.GetNBCC95(...) etc.),
    mas com métodos tipados, docstrings e exceções em vez de códigos de
    retorno.
    """

    def __init__(self, program_path: str, visible: bool = True, units: eUnits = eUnits.kgf_m_C):
        self._program_path = program_path
        self.visible = visible
        self.units = units
        self._helper = None
        self._sap_object = None
        self.raw_sap_model = None
        self.sap_model: SapModelWrapper | None = None

    def open(self) -> SapModelWrapper:
        self._helper = comtypes.client.CreateObject("SAP2000v20.Helper")
        self._helper = self._helper.QueryInterface(getattr(comtypes.gen, "SAP2000v20").cHelper) # type: ignore
        self._sap_object = self._helper.CreateObject(self._program_path)
        self._sap_object.ApplicationStart()
        self._sap_object.Visible = self.visible
        self.raw_sap_model = self._sap_object.SapModel
        self.raw_sap_model.InitializeNewModel()
        self.raw_sap_model.File.NewBlank()
        self.raw_sap_model.SetPresentUnits(int(self.units))
        self.sap_model = SapModelWrapper(self.raw_sap_model)
        return self.sap_model

    def close(self, save: bool = True) -> None:
        if self._sap_object is not None:
            self._sap_object.ApplicationExit(save)
        self._sap_object = None
        self.raw_sap_model = None
        self.sap_model = None

    def __enter__(self) -> SapModelWrapper:
        return self.open()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close(save=exc_type is None)
