## IMPORTS ##
from __future__ import annotations
from typing import Dict, Set, Tuple, Iterable
import itertools

from data.dados import dic_skills as SKILLS
from utils.grafos import *  # validarGrafo, validaPreReq, checaPreReq

TARGET = 'S6'
T_MAX = 350
C_MAX = 30

# Calcula tempo, complexidade e valor total de um conjunto de skills
def valorTotal(chosen: Set[str], v_override: Dict[str, float] | None = None) -> Tuple[int, int, float]:
    t = sum(SKILLS[s]['Tempo'] for s in chosen)
    c = sum(SKILLS[s]['Complexidade'] for s in chosen)
    if v_override is None:
        v = sum(SKILLS[s]['Valor'] for s in chosen)
    else:
        v = sum(v_override.get(s, SKILLS[s]['Valor']) for s in chosen)
    return t, c, v

# Gera conjuntos válidos de skills dentro dos limites de tempo e complexidade
def conjuntosValidos(ids: Iterable[str], v_override: Dict[str, float] | None = None):
    for r in range(1, len(ids)+1):
        for comb in itertools.combinations(ids, r):
            chosen = set(comb)
            if not validaPreReq(chosen, SKILLS):
                continue
            t, c, v = valorTotal(chosen, v_override)
            if t <= T_MAX and c <= C_MAX:
                yield chosen, t, c, v

# Checa viabilidade do alvo dada as restrições
def checaViabilidadeAlvo():
    ok, errs = validarGrafo(SKILLS)
    if not ok:
        return {
            'OK': False, 
            'ERRO': errs
        }
    base = checaPreReq(SKILLS, TARGET)
    t0, c0, _ = valorTotal(base)
    return {
        'OK': True,
        'Pre_Requisitos': (t0 <= T_MAX and c0 <= C_MAX),
        'Skills': sorted(base),
        'Tempo': t0,
        'Complexidade': c0,
    }
