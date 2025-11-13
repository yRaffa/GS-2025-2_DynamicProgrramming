## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any, Set

from .dp_horizonte import dpHorizonte

# Recomendador principal usando DP de horizonte finito
def recomendarSkills(
    perfil_atual: Set[str],
    prob_mercado: Dict[str, float],
    anos: int = 5,
    k_recomendacoes: int = 3
) -> Dict[str, Any]:
    valor, plano = dpHorizonte(perfil_atual, prob_mercado, anos)

    return {
        'Valor_Esperado_Total': valor,
        'Plano_Completo_5_Anos': plano,
        'Recomendacoes': plano[:k_recomendacoes]
    }
