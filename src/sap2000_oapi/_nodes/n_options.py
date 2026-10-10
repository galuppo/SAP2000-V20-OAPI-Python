"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_Options:
    """Wrapper para SapModel.Options."""

    def __init__(self, raw):
        self._raw = raw

    def GetDimensions(self):
        """This function retrieves the program dimension and tolerance items. The function returns zero
        if the items are successfully retrieved; otherwise it returns a nonzero value.
    
        CuttingPlaneTol (output): The tolerance for 2D view cutting planes. [L]
        WorldSpacing (output): The plan fine grid spacing. [L]
        NudgeValue (output): The plan nudge value. [L]
        PixelClickSize (output): The screen selection tolerance in pixels.
        PixelSnapSize (output): The screen snap tolerance in pixels.
        ScrLinThk (output): The screen line thickness in pixels.
        PrtLinThk (output): The printer line thickness in pixels.
        MaxFont (output): The maximum graphic font size in points.
        MinFont (output): The minimum graphic font size in points.
        ZoomStep (output): The auto zoom step size in percent (0 < ZoomStep < = 100).
        ShrinkFact (output): The shrink factor in percent (0 < ShrinkFact < = 100).
        TextFileMaxChar (output): The maximum line length in the text file (ShrinkFact > =
            80).
        """
        _r = self._raw.GetDimensions(0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Options.GetDimensions falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetDimensions(self, CuttingPlaneTol: float = 0, WorldSpacing: float = 0, NudgeValue: float = 0, PixelClickSize: int = 0, PixelSnapSize: int = 0, ScrLinThk: int = 0, PrtLinThk: int = 0, MaxFont: int = 0, MinFont: int = 0, ZoomStep: int = 0, ShrinkFact: int = 0, TextFileMaxChar: int = 0):
        """This function sets program dimension and tolerance items. Inputting 0 for any item means
        that the item will be ignored by the program; that is, its current value will not be
        changed. The function returns zero if the items are successfully set; otherwise it
        returns a nonzero value.
    
        CuttingPlaneTol (input): The tolerance for 2D view cutting planes. [L]
        WorldSpacing (input): The plan fine grid spacing. [L]
        NudgeValue (input): The plan nudge value. [L]
        PixelClickSize (input): The screen selection tolerance in pixels.
        PixelSnapSize (input): The screen snap tolerance in pixels.
        ScrLinThk (input): The screen line thickness in pixels.
        PrtLinThk (input): The printer line thickness in pixels.
        MaxFont (input): The maximum graphic font size in points.
        MinFont (input): The minimum graphic font size in points.
        ZoomStep (input): The auto zoom step size in percent (0 < ZoomStep <= 100).
        ShrinkFact (input): The shrink factor in percent (0 < ShrinkFact <= 100).
        TextFileMaxChar (input): The maximum line length in the text file (ShrinkFact >=
            80).
        """
        _r = self._raw.SetDimensions(CuttingPlaneTol, WorldSpacing, NudgeValue, PixelClickSize, PixelSnapSize, ScrLinThk, PrtLinThk, MaxFont, MinFont, ZoomStep, ShrinkFact, TextFileMaxChar)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Options.SetDimensions falhou (ret={_r})".format(_r=_r))
        return None


