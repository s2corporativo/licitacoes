from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Proposta:
    fornecedor: str
    valor_total: float
    prazo_entrega_dias: int
    habilitada: bool = True


def selecionar_vencedor(propostas: list[Proposta]) -> Proposta:
    """Seleciona a proposta vencedora pelo menor valor total.

    Regras de desempate:
    1) Menor prazo de entrega.
    2) Ordem alfabética do nome do fornecedor.

    Levanta ValueError quando não há propostas habilitadas.
    """

    habilitadas = [p for p in propostas if p.habilitada]
    if not habilitadas:
        raise ValueError("Nenhuma proposta habilitada para julgamento.")

    return min(
        habilitadas,
        key=lambda p: (p.valor_total, p.prazo_entrega_dias, p.fornecedor.lower()),
    )
