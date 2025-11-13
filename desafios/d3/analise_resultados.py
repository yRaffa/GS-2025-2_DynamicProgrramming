## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any, List, Tuple
import itertools

from .selecao_greedy import selecionarGreedy
from .otimo_exaustivo import selecionarOtimoExaustivo

# Compara o resultado do algoritmo greedy com a solução ótima exaustiva
def compararGreedyOtimo(threshold_valor: int = 15) -> Dict[str, Any]:
    greedy = selecionarGreedy(threshold_valor=threshold_valor)
    otimo = selecionarOtimoExaustivo(threshold_valor=threshold_valor)
    conj_greedy = set(greedy['Escolhidas'])
    conj_otimo = set(otimo['Melhor_Subconjunto'])
    greedy_eh_otimo = conj_greedy == conj_otimo
    tempo_g = greedy['Tempo_Total']
    tempo_o = otimo['Tempo_Total'] if otimo['Threshold_Alcancado'] else None

    delta_tempo = None
    if tempo_o is not None and tempo_o > 0:
        delta_tempo = (tempo_g - tempo_o) / tempo_o

    return {
        'Greedy': greedy,
        'Otimo_Exaustivo': otimo,
        'Greedy_Eh_Otimo': greedy_eh_otimo,
        'Delta_Tempo_Relativo': delta_tempo,
    }

# Constroi um pequeno conjunto artificial de skills básicas onde a estratégia greedy (por V/T) NÃO produz a solução ótima.
def contraexemploGreedy(threshold_valor: int = 15) -> Dict[str, Any]:
    skills_artificiais = {
        'A': {'Valor': 10, 'Tempo': 6},
        'B': {'Valor': 10, 'Tempo': 6},
        'C': {'Valor': 16, 'Tempo': 10},
    }

    detalhes = []
    for sid, info in skills_artificiais.items():
        v, t = info['Valor'], info['Tempo']
        r = v / t if t > 0 else 0
        detalhes.append((sid, v, t, r))
    detalhes.sort(key=lambda x: x[3], reverse=True)
    escolhidas_g: List[str] = []
    valor_g = 0
    tempo_g = 0
    for sid, v, t, r in detalhes:
        if valor_g >= threshold_valor:
            break
        escolhidas_g.append(sid)
        valor_g += v
        tempo_g += t

    melhor_subset: List[str] = []
    melhor_valor = 0
    melhor_tempo = float('inf')

    ids = list(skills_artificiais.keys())
    for r in range(1, len(ids) + 1):
        for comb in itertools.combinations(ids, r):
            valor = sum(skills_artificiais[s]['Valor'] for s in comb)
            tempo = sum(skills_artificiais[s]['Tempo'] for s in comb)
            if valor >= threshold_valor:
                if tempo < melhor_tempo:
                    melhor_tempo = tempo
                    melhor_valor = valor
                    melhor_subset = list(comb)
                elif tempo == melhor_tempo and valor > melhor_valor:
                    melhor_valor = valor
                    melhor_subset = list(comb)

    return {
        'Skills_Artificiais': skills_artificiais,
        'Greedy': {
            'Escolhidas': escolhidas_g,
            'Valor_Total': valor_g,
            'Tempo_Total': tempo_g,
        },
        'Otimo': {
            'Escolhidas': melhor_subset,
            'Valor_Total': melhor_valor,
            'Tempo_Total': melhor_tempo,
        },
    }
