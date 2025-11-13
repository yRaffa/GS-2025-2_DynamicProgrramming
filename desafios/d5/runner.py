## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any, Set

from .transicoes import gerarDemandaMercado
from .recomendador import recomendarSkills

# Executa todas as etapas do desafio 05 e retorna um dicionário com os resultados
def executarDesafio5(
    perfil_atual: Set[str],
    anos: int = 5,
    k_recomendacoes: int = 3,
    seed: int = 42
) -> Dict[str, Any]:
    prob = gerarDemandaMercado(seed=seed)
    resultado = recomendarSkills(
        perfil_atual=perfil_atual,
        prob_mercado=prob,
        anos=anos,
        k_recomendacoes=k_recomendacoes
    )

    return {
        'Probabilidades_Mercado': prob,
        'Resultado_DP': resultado
    }

if __name__ == '__main__':
    perfil_exemplo = {'S1', 'S2'}
    print(executarDesafio5(perfil_exemplo))
