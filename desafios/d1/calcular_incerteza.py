## IMPORTS ##
from __future__ import annotations
from typing import Dict, List, Tuple, Set
import random, statistics

from data.dados import dic_skills as SKILLS
from .modelo_dp import valorTotal, T_MAX, C_MAX, TARGET
from .solucao_deterministica import solucaoDeterministica

# Gera valores de skill para uma amostra (V-10%, V+10%)
def valoresAmostra() -> Dict[str, float]:
    return {sid: random.uniform(0.9*meta['Valor'], 1.1*meta['Valor']) for sid, meta in SKILLS.items()}

# Simula o valor total de um conjunto de skills em múltiplas amostras
def simularConjunto(chosen: Set[str], runs: int = 1000, seed: int = 42) -> Tuple[float, float, List[float]]:
    random.seed(seed)
    values: List[float] = []
    for _ in range(runs):
        v_over = valoresAmostra()
        _, _, v = valorTotal(set(chosen), v_over)
        values.append(v)
    mean = statistics.mean(values)
    stdev = statistics.pstdev(values) if len(values) > 1 else 0.0
    return mean, stdev, values

# Realiza a simulação de Monte Carlo conforme o desafio (Se o alvo for inviável, simula a distribuição do melhor conjunto determinístico sem o alvo)
def monteCarlo(runs: int = 1000, seed: int = 42):
    det = solucaoDeterministica()
    if not det.get('Viavel', False):
        base = det['Melhor_Sem_Alvo']['Conjunto']
        mean, stdev, vals = simularConjunto(set(base), runs, seed)
        return {
            'Alvo_Viavel': False,
            'Motivo': det['Motivo'],
            'Base_Deterministica': det['Melhor_Sem_Alvo'],
            'E_Valor': mean,
            'Desvio_Padrao': stdev,
            'Amostras': vals[:50]  # Retorna apenas as primeiras 50 amostras para evitar excesso de dados
        }
    return {
        'Alvo_Viavel': True, 
        'Nota': 'Implementação de cenário por cenário disponível se necessário.'
    }
