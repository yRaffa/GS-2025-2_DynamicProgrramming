## IMPORTS ##
from __future__ import annotations
from typing import List, Dict, Any
import itertools

from data.dados import dic_skills as SKILLS
from .modelo_critico import CRITICAS, custoOrdemCritica, verificaGrafoCritico

# Gera todas as 120 permutações das habilidades críticas, e calcula o custo total de cada ordem e devolve ordenado por custo crescente.
def listarPermutacoesComCusto() -> Dict[str, Any]:
    validacao = verificaGrafoCritico()
    if not validacao['OK']:
        return {
            'OK': False,
            'Erros': validacao['Erros'],
            'Permutacoes': []
        }
    resultados: List[Dict[str, object]] = []
    for perm in itertools.permutations(CRITICAS):
        ordem = list(perm)
        custo = custoOrdemCritica(ordem)
        resultados.append({
            'Ordem': ordem,
            'Custo': custo
        })
    resultados.sort(key=lambda x: x['Custo'])
    return {
        'OK': True,
        'Erros': [],
        'Permutacoes': resultados
    }
