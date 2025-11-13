## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any, List
from collections import Counter

from .calcular_permutacoes import listarPermutacoesComCusto

# Analisa as permutações das habilidades críticas (3 ordens com menor custo, custo médio das 3 melhores, pior ordem)
def resumoOrdensCriticas() -> Dict[str, Any]:
    dados = listarPermutacoesComCusto()
    if not dados['OK']:
        return {
            'OK': False,
            'Erros': dados['Erros']
        }
    perms = dados['Permutacoes']
    if not perms:
        return {
            'OK': False,
            'Erros': ['Nenhuma permutação encontrada.']
        }
    top3 = perms[:3]
    pior = perms[-1]
    media_top3 = sum(p['Custo'] for p in top3) / 3.0
    primeiros = [p['Ordem'][0] for p in top3]
    cont = Counter(primeiros)
    habilidade_mais_frequente = cont.most_common(1)[0][0]
    conclusao = (
        f"Nas 3 melhores ordens, a habilidade {habilidade_mais_frequente} "
        f"aparece com maior frequência na primeira posição, sugerindo que "
        f"iniciar a trilha crítica por ela reduz o tempo de espera acumulado "
        f"por pré-requisitos das demais habilidades críticas."
    )
    return {
        'OK': True,
        'Top3': top3,
        'Media_Custo_Top3': media_top3,
        'Pior': pior,
        'Conclusao': conclusao
    }
