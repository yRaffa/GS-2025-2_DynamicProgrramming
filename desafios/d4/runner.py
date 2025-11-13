## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any
from pprint import pprint

from .modelo_trilhas import trilhaSkills
from .ordenacoes import ordenarComplexidade, dividirSprints
from .benchmark import medirTempos

# Executa todas as etapas do desafio 04 e retorna um dicionário com os resultados
def executarDesafio4(
    reverse: bool = False,
    mult_benchmark: int = 1000,
    repeticoes_benchmark: int = 5,
) -> Dict[str, Any]:
    skills = trilhaSkills()
    ordenadas = ordenarComplexidade(reverse=reverse)
    sprints = dividirSprints(ordenadas)
    bench = medirTempos(mult=mult_benchmark, repeticoes=repeticoes_benchmark)

    return {
        'Skills_Trilha': skills,
        'Ordenadas_Por_Complexidade': ordenadas,
        'Sprints': sprints,
        'Benchmark': bench,
    }

if __name__ == '__main__':
    pprint(executarDesafio4())
