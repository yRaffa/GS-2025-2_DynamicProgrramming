## IMPORTS ##
from __future__ import annotations
from typing import Dict, List, Iterable, Tuple

from data.dados import dic_skills as SKILLS

# Retorna apenas as habilidades de nível básico, definidas como aquelas que NÃO possuem pré-requisitos
def skillsBasicas() -> Dict[str, Dict]:
    basicas = {
        sid: attrs
        for sid, attrs in SKILLS.items()
        if not attrs.get('PreRequisito')
    }
    return basicas

# Dado um subconjunto de skills, retorna (valor_total, tempo_total)
def calcularValorTempo(ids: Iterable[str]) -> Tuple[int, int]:
    valor_total = 0
    tempo_total = 0
    for sid in ids:
        info = SKILLS[sid]
        valor_total += info['Valor']
        tempo_total += info['Tempo']
    return valor_total, tempo_total
