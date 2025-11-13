## IMPORTS ##
from __future__ import annotations
from typing import Dict, List, Tuple
import time

from .modelo_trilhas import listarTrilhaSkills
from .ordenacoes import quickSort

# Replica a lista de 12 habilidades X vezes para aumentar o tamanho da entrada e permitir comparação de tempo mais visível.
def _replicarDados(mult: int = 1000) -> List[Tuple[str, Dict]]:
    base = listarTrilhaSkills()
    dados = base * mult
    return dados

# Mede o tempo médio de execução do Quick Sort vs Sort nativo para uma lista replicada de tamanho 12 * mult.
def medirTempos(mult: int = 1000, repeticoes: int = 5) -> Dict[str, float]:
    dados_base = _replicarDados(mult=mult)
    tempos_qs = []
    for _ in range(repeticoes):
        dados = list(dados_base)
        ini = time.perf_counter()
        quickSort(dados, key=lambda item: item[1]['Complexidade'], reverse=False)
        fim = time.perf_counter()
        tempos_qs.append(fim - ini)
    tempo_qs_medio = sum(tempos_qs) / len(tempos_qs)
    tempos_native = []
    for _ in range(repeticoes):
        dados = list(dados_base)
        ini = time.perf_counter()
        sorted(dados, key=lambda item: item[1]['Complexidade'])
        fim = time.perf_counter()
        tempos_native.append(fim - ini)
    tempo_native_medio = sum(tempos_native) / len(tempos_native)
    razao = tempo_qs_medio / tempo_native_medio if tempo_native_medio > 0 else None
    return {
        'Tamanho_Lista': len(dados_base),
        'Repeticoes': repeticoes,
        'Tempo_QuickSort': tempo_qs_medio,
        'Tempo_Sort_Nativo': tempo_native_medio,
        'Razao_Quick_vs_Nativo': razao,
    }
