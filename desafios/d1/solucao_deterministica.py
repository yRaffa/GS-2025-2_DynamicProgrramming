## IMPORTS ##
from __future__ import annotations
from typing import Dict, Set

from data.dados import dic_skills as SKILLS
from .modelo_dp import *  # T_MAX, C_MAX, TARGET, valorTotal, conjuntosValidos, checaViabilidadeAlvo

# Retorna a melhor solução viável sem o alvo
def melhorSemAlvo():
    ids = list(SKILLS.keys())
    best = {
        'Valor': float('-inf'), 
        'Conjunto': [], 
        'Tempo': 0, 
        'Complexidade': 0
    }
    for chosen, t, c, v in conjuntosValidos(ids):
        if v > best['Valor']:
            best = {
                'Valor': v, 
                'Conjunto': sorted(chosen), 
                'Tempo': t, 
                'Complexidade': c
            }
    return best

# Retorna a melhor solução viável com o alvo
def melhorComAlvo():
    ids = list(SKILLS.keys())
    best = {
        'Valor': float('-inf'), 
        'Conjunto': [], 
        'Tempo': 0, 
        'Complexidade': 0
    }
    for chosen, t, c, v in conjuntosValidos(ids):
        if TARGET in chosen and v > best['Valor']:
            best = {
                'Valor': v, 
                'Conjunto': sorted(chosen), 
                'Tempo': t, 
                'Complexidade': c
            }
    return best if best['Conjunto'] else None

# Solução determinística do DESAFIO 01
def solucaoDeterministica():
    feas = checaViabilidadeAlvo()
    if not feas['OK']:
        return {
            'Viavel': False, 
            'Erros': feas['ERRO']
        }
    if not feas['Pre_Requisitos']:
        motivo = (
            f"Para incluir {TARGET} é necessário ao menos {feas['Skills']} "
            f"(Tempo={feas['Tempo']}, Complexidade={feas['Complexidade']}), "
            f"o que viola T≤{T_MAX}, C≤{C_MAX}."
        )
        return {
            'Viavel': False,
            'Motivo': motivo,
            'Melhor_Sem_Alvo': melhorSemAlvo()
        }
    com_alvo = melhorComAlvo()
    if com_alvo is None:
        return {
            'Viavel': False,
            'Motivo': 'Nenhum subconjunto com o alvo atende às restrições.',
            'Melhor_Sem_Alvo': melhorSemAlvo()
        }
    return {
        'Viavel': True,
        'Melhor_Com_Alvo': com_alvo
    }
