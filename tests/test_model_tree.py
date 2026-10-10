"""Testes que não dependem de um SAP2000 real: só a mecânica de geração
(árvore de objetos, desempacotamento de saídas, levantamento de exceção)."""

import pytest

from sap2000_oapi.model import SapModelWrapper
from sap2000_oapi.errors import Sap2000ApiError


class _FakeRaw:
    """Objeto raiz falso — qualquer atributo acessado devolve outro _FakeRaw,
    permitindo navegar árvores profundas sem precisar declarar cada nó."""

    def __getattr__(self, name):
        return _FakeRaw()


def test_arvore_de_objetos_navega_como_a_oapi():
    sap = SapModelWrapper(_FakeRaw())
    assert hasattr(sap.PropMaterial, "SetMaterial")
    assert hasattr(sap.LoadPatterns.AutoSeismic, "GetNBCC95")
    assert hasattr(sap.Results.Setup, "SetComboSelectedForOutput")


def test_funcao_status_puro_levanta_excecao_em_erro():
    class FailRaw:
        class PropMaterial:
            @staticmethod
            def SetMaterial(Name, MatType, Color, Notes, GUID):
                return 1  # não-zero = falha

    sap = SapModelWrapper(FailRaw())
    with pytest.raises(Sap2000ApiError):
        sap.PropMaterial.SetMaterial("X", 2)


def test_funcao_com_uma_saida_retorna_valor_direto():
    class OkRaw:
        class FrameObj:
            @staticmethod
            def AddByCoord(XI, YI, ZI, XJ, YJ, ZJ, Name, PropName, UserName, CSys):
                return ("NOME_ATRIBUIDO", 0)

    sap = SapModelWrapper(OkRaw())
    nome = sap.FrameObj.AddByCoord(0, 0, 0, 0, 0, 6)
    assert nome == "NOME_ATRIBUIDO"


def test_funcao_com_duas_saidas_retorna_tupla():
    class OkRaw:
        class FrameObj:
            @staticmethod
            def GetPoints(Name, Point1, Point2):
                return ("PT_BASE", "PT_TOPO", 0)

    sap = SapModelWrapper(OkRaw())
    p1, p2 = sap.FrameObj.GetPoints("P1")
    assert (p1, p2) == ("PT_BASE", "PT_TOPO")
