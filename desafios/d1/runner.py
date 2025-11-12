## IMPORTS ##
from __future__ import annotations
from typing import Dict, Any
from pprint import pprint

from d1.modelo_dp import T_MAX, C_MAX, TARGET, checaViabilidadeAlvo
from d1.solucao_deterministica import solucaoDeterministica
from d1.calcular_incerteza import monteCarlo
from d1.maximizar_valor_total import resumoComparativo

def executarDesafio1(runs: int = 1000, seed: int = 42) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    out["Modelo_DP"] = {
        "limites": {"T_MAX": T_MAX, "C_MAX": C_MAX, "TARGET": TARGET},
        "validacao/viabilidade": checaViabilidadeAlvo()
    }
    out["Solucao_Deterministica"] = solucaoDeterministica()
    out["Calcular_Incerteza"] = monteCarlo(runs=runs, seed=seed)
    out["Maximizar_Valor_Total"] = resumoComparativo(runs=runs, seed=seed)
    return out

if __name__ == "__main__":
    pprint(executarDesafio1())
