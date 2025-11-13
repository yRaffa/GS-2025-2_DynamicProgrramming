## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any, List

from .modelo_basico import *

# Seleção greedy baseada na razão Valor/Tempo
def selecionarGreedy(threshold_valor: int = 15) -> Dict[str, Any]:
    basicas = skillsBasicas()
    detalhes_razao = []
    for sid, info in basicas.items():
        v = info['Valor']
        t = info['Tempo']
        razao = v / t if t > 0 else 0
        detalhes_razao.append((sid, v, t, razao))

    detalhes_razao.sort(key=lambda x: x[3], reverse=True)
    escolhidas: List[str] = []
    valor_acum = 0
    tempo_acum = 0
    for sid, v, t, r in detalhes_razao:
        if valor_acum >= threshold_valor:
            break
        escolhidas.append(sid)
        valor_acum += v
        tempo_acum += t

    threshold_alcancado = valor_acum >= threshold_valor
    return {
        'Escolhidas': escolhidas,
        'Valor_Total': valor_acum,
        'Tempo_Total': tempo_acum,
        'Threshold_Valor': threshold_valor,
        'Threshold_Alcancado': threshold_alcancado,
        'Detalhes_Razao': detalhes_razao,
    }
