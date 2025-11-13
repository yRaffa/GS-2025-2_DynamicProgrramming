## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any
from pprint import pprint

from .modelo_critico import CRITICAS, verificaGrafoCritico
from .calcular_permutacoes import listarPermutacoesComCusto
from .analisar_ordens import resumoOrdensCriticas

def executarDesafio2() -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    out['Modelo_Critico'] = {
        'Habilidades_Criticas': CRITICAS,
        'Validacao_Grafo': verificaGrafoCritico()
    }
    perms_info = listarPermutacoesComCusto()
    out['Permutacoes_e_Custos'] = perms_info
    out['Analise_Ordens'] = resumoOrdensCriticas()
    return out

if __name__ == '__main__':
    pprint(executarDesafio2())
