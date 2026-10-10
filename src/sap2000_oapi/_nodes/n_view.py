"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_View:
    """Wrapper para SapModel.View."""

    def __init__(self, raw):
        self._raw = raw

    def RefreshView(self, Window: int = 0, Zoom: bool = True):
        """This function refreshes the view for the specified window(s). It returns zero if the window
        views are successfully refreshed, otherwise it returns a nonzero value. See
        RefreshWindow and RefreshView for more information.
    
        Window (input): This is 0 meaning all windows or an existing window number. It
            indicates the window(s) to have its view refreshed.
        Zoom (input): If this item is True, the window zoom is maintained when the view is
            refreshed. If it is False, the zoom returns to a default zoom.
        """
        _r = self._raw.RefreshView(Window, Zoom)
        if _r != 0:
            raise Sap2000ApiError("SapModel.View.RefreshView falhou (ret={_r})".format(_r=_r))
        return None

    def RefreshWindow(self, Window: int = 0):
        """This function refreshes the specified window(s). It returns zero if the windows are
        successfully refreshed, otherwise it returns a nonzero value. See RefreshWindow and
        RefreshView for more information.
    
        Window (input): This is 0 meaning all windows or an existing window number. It
            indicates the window(s) to be refreshed.
        """
        _r = self._raw.RefreshWindow(Window)
        if _r != 0:
            raise Sap2000ApiError("SapModel.View.RefreshWindow falhou (ret={_r})".format(_r=_r))
        return None


