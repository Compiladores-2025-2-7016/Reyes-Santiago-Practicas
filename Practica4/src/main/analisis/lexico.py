import ply.lex as lex
from ply.lex import TOKEN
from componente.clase_lexica import ClaseLexica

class Lexer:
    digito = r'[0-9]'
    tokens = list(ClaseLexica._member_names_)

    @TOKEN(r'\+')
    def t_PLUS(self, t):
        t.type = 'PLUS'
        return t

    @TOKEN(r'(' + digito + r')+')
    def t_NUMERO(self, t):
        t.type = 'NUMERO'
        return t

    t_ignore = " \t"

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print("Error léxico:", t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def scan(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
