## IMPORTS ##
from __future__ import annotations
from typing import Dict, List, Tuple

from data.dados import dic_skills as SKILLS

# IDs das 12 skills da base original do enunciado
IDS_ORIGINAIS: List[str] = [
    'S1', 'S2', 'S3', 'S4', 'S5', 'S6',
    'S7', 'S8', 'S9', 'H10', 'H11', 'H12'
]

# Retorna apenas as 12 skills originais, preservando os metadados da base mestre.
def trilhaSkills() -> Dict[str, Dict]:
    skills = {
        sid: SKILLS[sid]
        for sid in IDS_ORIGINAIS
        if sid in SKILLS
    }
    return skills

# Retorna uma lista de tuplas (ID, dados) das 12 skills, útil para ser passada para os algoritmos de ordenação.
def listarTrilhaSkills() -> List[Tuple[str, Dict]]:
    skills = trilhaSkills()
    return list(skills.items())
