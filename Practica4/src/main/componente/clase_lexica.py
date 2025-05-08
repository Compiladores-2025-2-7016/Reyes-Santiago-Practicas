from enum import Enum

class ClaseLexica(Enum):
    EOF = 0
    NUMERO = 1 
    PLUS = 2
    ESPACIO = 5

class NoTerminal(Enum):
    epsilon = ''
    s = "s"
    sprim = "sprim"
