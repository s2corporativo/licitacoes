import pytest

from licitacoes.ranking import Proposta, selecionar_vencedor


def test_seleciona_menor_valor_total():
    propostas = [
        Proposta("Fornecedor A", 1500.0, 10),
        Proposta("Fornecedor B", 1200.0, 15),
        Proposta("Fornecedor C", 1300.0, 7),
    ]

    vencedor = selecionar_vencedor(propostas)

    assert vencedor.fornecedor == "Fornecedor B"


def test_desempate_por_prazo_e_nome():
    propostas = [
        Proposta("Zulu", 1000.0, 8),
        Proposta("Alfa", 1000.0, 8),
        Proposta("Beta", 1000.0, 6),
    ]

    vencedor = selecionar_vencedor(propostas)

    assert vencedor.fornecedor == "Beta"


def test_ignora_inabilitadas():
    propostas = [
        Proposta("Menor mas inabilitada", 900.0, 5, habilitada=False),
        Proposta("Habilitada", 1000.0, 10, habilitada=True),
    ]

    vencedor = selecionar_vencedor(propostas)

    assert vencedor.fornecedor == "Habilitada"


def test_erro_sem_habilitadas():
    propostas = [
        Proposta("A", 1000.0, 10, habilitada=False),
    ]

    with pytest.raises(ValueError, match="Nenhuma proposta habilitada"):
        selecionar_vencedor(propostas)
