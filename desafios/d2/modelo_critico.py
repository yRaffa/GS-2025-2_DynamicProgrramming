## IMPORTS ##
from __future__ import annotations
from typing import Dict, List, Set, Tuple
import itertools

from data.dados import dic_skills as SKILLS
from utils.grafos import validarGrafo, checaPreReq

CRITICAS: List[str] = ['S3', 'S5', 'S7', 'S8', 'S9']

# Verifica se o grafo de pré-requisitos da base é válido
def verificaGrafoCritico() -> Dict[str, object]:
    ok, erros = validarGrafo(SKILLS)
    return {
        'OK': ok,
        'Erros': erros
    }

# Retorna os pré-requisitos faltantes (diretos e indiretos) de uma skill, dado o conjunto atual de habilidades já adquiridas.
def prereqsFaltantes(skill_id: str, adquiridas: Set[str]) -> Set[str]:
    needed = checaPreReq(SKILLS, skill_id) - {skill_id}
    return {s for s in needed if s not in adquiridas}

# Calcula o custo total (Tempo de Aquisição + Espera por pré-reqs) para uma ordem específica das habilidades críticas.
def custoOrdemCritica(ordem: List[str]) -> int:
    adquiridas: Set[str] = set()
    custo_total = 0
    for sid in ordem:
        faltantes = prereqsFaltantes(sid, adquiridas)
        custo_total += sum(SKILLS[x]['Tempo'] for x in faltantes)
        adquiridas |= faltantes
        custo_total += SKILLS[sid]['Tempo']
        adquiridas.add(sid)
    return custo_total
