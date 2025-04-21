import ply.lex as lex
from ply.lex import TOKEN
from componente.clase_lexica import ClaseLexica

# Clase principal del analizador léxico
class Lexer(object):
    # Expresiones auxiliares para construir patrones más adelante
    digito = r'[0-9]'
    letra = r'[a-zA-Z_]'
    letra_o_digito = r'[a-zA-Z_0-9]'

    # Lista de nombres de tokens que se generan desde el enum ClaseLexica
    tokens = [token.name for token in ClaseLexica]

    # Palabras reservadas del lenguaje, se reconocerán como tokens especiales
    reserved = {
        'int': 'INT',
        'float': 'FLOAT',
        'if': 'IF',
        'else': 'ELSE',
        'while': 'WHILE'
    }

    # ----------------------------------
    # Tokens definidos con funciones
    # ----------------------------------

    def t_MAS(self, t):
        r'\+'
        print(f"Token MAS: {t.value}")
        return t

    def t_MENOS(self, t):
        r'-'
        print(f"Token MENOS: {t.value}")
        return t

    def t_POR(self, t):
        r'\*'
        print(f"Token POR: {t.value}")
        return t

    def t_DIV(self, t):
        r'/'
        print(f"Token DIV: {t.value}")
        return t

    def t_PARIZQ(self, t):
        r'\('
        print(f"Token PARIZQ: {t.value}")
        return t

    def t_PARDER(self, t):
        r'\)'
        print(f"Token PARDER: {t.value}")
        return t

    def t_IGUAL(self, t):
        r'='
        print(f"Token IGUAL: {t.value}")
        return t

    def t_PUNTOYCOMA(self, t):
        r';'
        print(f"Token PUNTOYCOMA: {t.value}")
        return t

    def t_COMA(self, t):
        r','
        print(f"Token COMA: {t.value}")
        return t

    # ----------------------------------
    # Tokens con acciones léxicas
    # ----------------------------------

    # Números enteros
    @TOKEN(r'[0-9]+')
    def t_NUMERO(self, t):
        print(f"Token NUMERO: {t.value}")
        return t

    # Identificadores o palabras clave
    @TOKEN(r'[a-zA-Z_][a-zA-Z_0-9]*')
    def t_IDENTIFICADOR(self, t):
        if t.value in self.reserved:
            t.type = self.reserved[t.value]  # Cambia el tipo si es palabra clave
        print(f"Token {t.type}: {t.value}")
        return t

    # Contar líneas para mensajes de error
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Ignorar espacios y tabulaciones
    t_ignore = ' \t'

    # Manejo de errores: ignora y avisa del carácter no reconocido
    def t_error(self, t):
        print(f"Error léxico. Caracter no reconocido: '{t.value[0]}'")
        t.lexer.skip(1)

    # Construcción del analizador léxico
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # imprime todos los tokens
    def scan(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
