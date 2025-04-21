from enum import Enum

# Enum que representa todas las clases léxicas del lenguaje
class ClaseLexica(Enum):
    INT = 1              # 'int'
    FLOAT = 2            # 'float'

    IDENTIFICADOR = 3    # Nombres de variables
    NUMERO = 4           # Constantes numéricas (solo enteros por ahora)

    IGUAL = 5            # '='

    PUNTOYCOMA = 6       # ';'
    COMA = 7             # ','

    PARIZQ = 8           # '('
    PARDER = 9           # ')'

    IF = 10              # 'if'
    ELSE = 11            # 'else'
    WHILE = 12           # 'while'

    MAS = 13             # '+'
    MENOS = 14           # '-'
    POR = 15             # '*'
    DIV = 16             # '/'
