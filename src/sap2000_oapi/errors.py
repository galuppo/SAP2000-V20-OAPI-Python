"""Exceções da biblioteca."""


class Sap2000ApiError(RuntimeError):
    """Uma chamada da OAPI retornou código de erro (ret != 0)."""

