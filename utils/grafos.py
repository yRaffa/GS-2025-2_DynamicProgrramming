## IMPORTS ##
from __future__ import annotations
from typing import Dict, List, Set, Tuple
from collections import deque

# Monta o grafo de pré-requisitos e o grau de entrada de cada nó
def montarGrafo(sk: Dict[str, dict]) -> Tuple[Dict[str, List[str]], Dict[str, int]]:
    g = {k: [] for k in sk.keys()}
    indeg = {k: 0 for k in sk.keys()}
    for sid, meta in sk.items():
        for pre in meta.get('PreRequisito', []):
            g.setdefault(pre, []).append(sid)
            indeg[sid] = indeg.get(sid, 0) + 1
            indeg.setdefault(pre, 0)
    return g, indeg

# Valida o grafo de pré-requisitos: órfãos e ciclos
def validarGrafo(sk: Dict[str, dict]) -> Tuple[bool, List[str]]:
    errors: List[str] = []
    ids = set(sk.keys())
    for sid, meta in sk.items():
        for pre in meta.get('PreRequisito', []):
            if pre not in ids:
                errors.append(f'Pré-requisito inexistente: {sid} -> {pre}')
    g, indeg = montarGrafo(sk)
    q = deque([v for v, d in indeg.items() if d == 0])
    seen = 0
    while q:
        v = q.popleft()
        seen += 1
        for nb in g.get(v, []):
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)
    if seen != len(indeg):
        errors.append('Ciclo detectado no grafo de pré-requisitos.')
    return (len(errors) == 0), errors

# Retorna o conjunto de pré-requisitos (diretos e indiretos) de uma skill
def checaPreReq(sk: Dict[str, dict], sid: str) -> Set[str]:
    res: Set[str] = set()
    def dfs(u: str):
        if u in res: return
        res.add(u)
        for pre in sk[u].get('PreRequisito', []):
            dfs(pre)
    dfs(sid)
    return res

# Valida se o conjunto escolhido de skills respeita os pré-requisitos
def validaPreReq(chosen: Set[str], sk: Dict[str, dict]) -> bool:
    for s in chosen:
        for pre in sk[s].get('PreRequisito', []):
            if pre not in chosen:
                return False
    return True
