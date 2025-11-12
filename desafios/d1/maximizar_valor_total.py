## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any

from d1.solucao_deterministica import solucaoDeterministica
from d1.calcular_incerteza import monteCarlo

# Resumo comparativo entre solução determinística e simulação de Monte Carlo
def resumoComparativo(runs: int = 1000, seed: int = 42) -> Dict[str, Any]:
    det = solucaoDeterministica()
    mc = monteCarlo(runs=runs, seed=seed)
    summary = {
        'Deterministico': det, 
        'Monte_Carlo': mc
    }
    if not det.get('Viavel', False) and 'Base_Deterministica' in mc:
        det_val = det['Melhor_Sem_Alvo']['Valor']
        summary['Comparacao'] = {
            'Deterministico_Valor': det_val,
            'E_Valor_Simulado': mc['E_Valor'],
            'Desvio_Padrao': mc['Desvio_Padrao'],
            'Observacao': 'Como a média do ruído uniforme é o valor original, E[Valor] tende a ficar próximo do determinístico.'
        }
    return summary
