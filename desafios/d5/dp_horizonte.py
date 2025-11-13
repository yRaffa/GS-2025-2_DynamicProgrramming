## IMPORTS ##
from __future__ import annotations
from typing import Dict, List, Tuple, Set

from .modelo_base import filtrarSkillsViaveis

# DP de horizonte finito para recomendação de habilidades
def dpHorizonte(
    perfil_atual: Set[str],
    prob_mercado: Dict[str, float],
    anos: int = 5
) -> Tuple[float, List[str]]:
    memo = {}

    # Função recursiva com memoização
    def solve(perfil: frozenset, ano: int) -> Tuple[float, List[str]]:
        if ano == anos:
            return 0.0, []

        chave = (perfil, ano)
        if chave in memo:
            return memo[chave]

        perfil_set = set(perfil)
        viaveis = filtrarSkillsViaveis(perfil_set)

        if not viaveis:
            return 0.0, []

        melhor_valor = -1
        melhor_plano: List[str] = []

        for sid, info in viaveis.items():
            valor = info['Valor']
            p = prob_mercado[sid]
            ganho_esperado = valor * p

            novo_perfil = frozenset(perfil_set | {sid})
            futuro_valor, futuro_plano = solve(novo_perfil, ano + 1)

            total = ganho_esperado + futuro_valor
            if total > melhor_valor:
                melhor_valor = total
                melhor_plano = [sid] + futuro_plano

        memo[chave] = (melhor_valor, melhor_plano)
        return memo[chave]

    return solve(frozenset(perfil_atual), 0)
