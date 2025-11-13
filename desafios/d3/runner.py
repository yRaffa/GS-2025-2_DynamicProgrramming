## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any
from pprint import pprint

from .modelo_basico import skillsBasicas
from .selecao_greedy import selecionarGreedy
from .otimo_exaustivo import selecionarOtimoExaustivo
from .analise_resultados import compararGreedyOtimo, contraexemploGreedy

# Executa todas as etapas do desafio 03 e retorna um dicionário com os resultados
def executarDesafio3(threshold_valor: int = 15) -> Dict[str, Any]:
    basicas = skillsBasicas()
    greedy_real = selecionarGreedy(threshold_valor=threshold_valor)
    otimo_real = selecionarOtimoExaustivo(threshold_valor=threshold_valor)
    comparacao = compararGreedyOtimo(threshold_valor=threshold_valor)
    contraex = contraexemploGreedy(threshold_valor=threshold_valor)

    return {
        'Threshold_Valor': threshold_valor,
        'Skills_Basicas': basicas,
        'Greedy_Real': greedy_real,
        'Otimo_Real': otimo_real,
        'Comparacao_Real': comparacao,
        'Contraexemplo_Greedy': contraex,
    }

if __name__ == '__main__':
    pprint(executarDesafio3())
