## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any, List, Iterable
import itertools

from .modelo_basico import *

# Busca exaustiva em todos os subconjuntos de skills básicas (Entre todos os subconjuntos com Valor_Total >= threshold_valor, escolhe aquele com MENOR Tempo_Total).
def selecionarOtimoExaustivo(threshold_valor: int = 15) -> Dict[str, Any]:
    basicas = skillsBasicas()
    ids = list(basicas.keys())
    melhor_subconjunto: List[str] = []
    melhor_valor = 0
    melhor_tempo = float('inf')

    for r in range(1, len(ids) + 1):
        for comb in itertools.combinations(ids, r):
            valor, tempo = calcularValorTempo(comb)
            if valor >= threshold_valor:
                if tempo < melhor_tempo:
                    melhor_tempo = tempo
                    melhor_valor = valor
                    melhor_subconjunto = list(comb)
                elif tempo == melhor_tempo and valor > melhor_valor:
                    melhor_valor = valor
                    melhor_subconjunto = list(comb)

    threshold_alcancado = len(melhor_subconjunto) > 0
    return {
        'Melhor_Subconjunto': melhor_subconjunto,
        'Valor_Total': melhor_valor if threshold_alcancado else 0,
        'Tempo_Total': melhor_tempo if threshold_alcancado else 0,
        'Threshold_Valor': threshold_valor,
        'Threshold_Alcancado': threshold_alcancado,
    }
