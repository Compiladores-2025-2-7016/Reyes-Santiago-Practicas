import ply.lex as lex
from ply.lex import TOKEN
from componente.clase_lexica import ClaseLexica
from componente.componente_lexico import ComponenteLexico

class Lexer:
    """
    Clase Lexer que implementa el analizador léxico.
    """

    # Expresiones regulares auxiliares.
    digito = r'[0-9]'
    numero = rf'{digito}+(\.{digito}+)?([eE][+-]?{digito}+)?'
    letra = r'[a-zA-Z]'
    identificador = rf'[_a-zA-Z][_a-zA-Z0-9]*'

    # Lista de tokens reconocidos.
    tokens = [
        'NUMERO', 'ID', 'PYC', 'COMA', 'LPAR', 'RPAR',
        'INT', 'FLOAT', 'IF', 'ELSE', 'WHILE'
    ]

    # Diccionario de palabras reservadas.
    reservadas = {
        'int': 'INT',
        'float': 'FLOAT',
        'if': 'IF',
        'else': 'ELSE',
        'while': 'WHILE',
    }

    @TOKEN(numero)
    def t_NUMERO(self, t):
        """
        Regla para reconocer números enteros y flotantes.
        """
        print(ComponenteLexico(ClaseLexica.NUMERO, t.value))
        return t

    @TOKEN(identificador)
    def t_ID(self, t):
        """
        Regla para reconocer identificadores y palabras reservadas.
        """
        t.type = self.reservadas.get(t.value, 'ID')
        print(ComponenteLexico(getattr(ClaseLexica, t.type), t.value))
        return t

    def t_PYC(self, t):
        r";"
        print(ComponenteLexico(ClaseLexica.PYC, t.value))
        return t

    def t_COMA(self, t):
        r","
        print(ComponenteLexico(ClaseLexica.COMA, t.value))
        return t

    def t_LPAR(self, t):
        r"\("
        print(ComponenteLexico(ClaseLexica.LPAR, t.value))
        return t

    def t_RPAR(self, t):
        r"\)"
        print(ComponenteLexico(ClaseLexica.RPAR, t.value))
        return t

    # Ignorar espacios y tabulaciones.
    t_ignore = " \t"

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        """
        Manejo de errores léxicos.
        """
        print(f"Error léxico: '{t.value[0]}' no reconocido.")
        t.lexer.skip(1)

    def build(self, **kwargs):
        """
        Construye el lexer con las reglas definidas.
        """
        self.lexer = lex.lex(module=self, **kwargs)

    def scan(self, data):
        """
        Ejecuta el análisis léxico sobre una cadena de entrada.
        """
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
