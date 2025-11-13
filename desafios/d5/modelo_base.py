## IMPORTS ##
from __future__ import annotations
from typing import Dict, List, Set

from data.dados import dic_skills as SKILLS

# Retorna apenas as habilidades que o usuário ainda NÃO possui.
def skillsDisponiveis(perfil_atual: Set[str]) -> Dict[str, Dict]:
    return {
        sid: info
        for sid, info in SKILLS.items()
        if sid not in perfil_atual
    }

# Filtra as habilidades cujos pré-requisitos já foram atendidos.
def filtrarSkillsViaveis(perfil_atual: Set[str]) -> Dict[str, Dict]:
    viaveis = {}
    for sid, info in SKILLS.items():
        if sid in perfil_atual:
            continue
        prereqs = set(info['PreRequisito'])
        if prereqs.issubset(perfil_atual):
            viaveis[sid] = info
    return viaveis
