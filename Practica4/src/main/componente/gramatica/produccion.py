from typing import List
from ..gramatica.simbolo import Simbolo

class Produccion:
    def __init__(self, cabeza: Simbolo = None, cuerpo: List[Simbolo] = None):
        self.cabeza = cabeza
        self.cuerpo = cuerpo if cuerpo is not None else []

    def __str__(self):
        cuerpo_str = ' '.join(
            s.sim.name if hasattr(s.sim, 'name') else str(s.sim)
            for s in self.cuerpo if s.sim != ''
        )
        return f"{self.cabeza.sim.name} -> {cuerpo_str or 'ε'}"