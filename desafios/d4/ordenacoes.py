## IMPORTS ##
from __future__ import annotations
from typing import List, Tuple, Dict, Callable

from .modelo_trilhas import listarTrilhaSkills

# Quick Sort para uma lista de tuplas (ID, dict).
def quickSort(
    dados: List[Tuple[str, Dict]],
    key: Callable[[Tuple[str, Dict]], int],
    reverse: bool = False
) -> List[Tuple[str, Dict]]:
    if len(dados) <= 1:
        return dados

    pivot = dados[len(dados) // 2]
    k_p = key(pivot)

    if reverse:
        menores = [x for x in dados if key(x) > k_p]
        iguais  = [x for x in dados if key(x) == k_p]
        maiores = [x for x in dados if key(x) < k_p]
    else:
        menores = [x for x in dados if key(x) < k_p]
        iguais  = [x for x in dados if key(x) == k_p]
        maiores = [x for x in dados if key(x) > k_p]

    return quickSort(menores, key, reverse) + iguais + quickSort(maiores, key, reverse)

# Ordena as 12 habilidades por Complexidade usando Quick Sort.
def ordenarComplexidade(reverse: bool = False) -> List[Tuple[str, Dict]]:
    skills = listarTrilhaSkills()
    return quickSort(
        skills,
        key=lambda item: item[1]['Complexidade'],
        reverse=reverse
    )

# Divide a lista ordenada em duas sprints de 6 habilidades cada.
def dividirSprints(
    ordenadas: List[Tuple[str, Dict]]
) -> Dict[str, List[Tuple[str, Dict]]]:
    sprint_a = ordenadas[:6]
    sprint_b = ordenadas[6:12]
    return {
        'Sprint_A': sprint_a,
        'Sprint_B': sprint_b,
    }
