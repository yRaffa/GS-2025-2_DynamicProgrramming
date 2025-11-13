## IMPORTS ##
from __future__ import annotations
from typing import Dict
import numpy as np

from data.dados import dic_skills as SKILLS

# Cria um vetor de probabilidades representando a demanda de mercado
def gerarDemandaMercado(seed: int = 42) -> Dict[str, float]:
    np.random.seed(seed)
    probs = {}
    for sid, info in SKILLS.items():
        base = info['Valor'] + info['Complexidade']
        ruido = np.random.uniform(0.8, 1.2)
        score = base * ruido
        probs[sid] = score

    soma = sum(probs.values())
    for sid in probs:
        probs[sid] = probs[sid] / soma

    return probs
