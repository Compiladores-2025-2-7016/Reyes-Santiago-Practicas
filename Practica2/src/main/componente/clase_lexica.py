from enum import Enum

class ClaseLexica(Enum):
    """
    Enumeración de los tokens reconocidos en el lenguaje.
    """
    INT = 1
    FLOAT = 2
    IF = 3
    ELSE = 4
    WHILE = 5
    NUMERO = 6
    ID = 7
    PYC = 8
    COMA = 9
    LPAR = 10
    RPAR = 11
