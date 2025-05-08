from typing import Dict, List
from analisis.lexico import Lexer
from componente.gramatica.produccion import Produccion
from componente.gramatica.simbolo import Simbolo
from componente.clase_lexica import ClaseLexica, NoTerminal
from componente.gramatica.gramatica import Gramatica


class ParserLL:

    def __init__(self, lexer: Lexer):
        self.an_lexico = lexer
        self.token_actual = 0
        self.gramatica = Gramatica()
        self.tabla: Dict[Simbolo, Dict[Simbolo, Produccion]] = {} # self.tabla[S_inicial][NUMERO] -> Produccion

    def eat(self):
        # hint: ip++ == self.eat()
        try:
            tok = self.an_lexico.lexer.token()
            if not tok: # No hay mas entrada
                self.token_actual = 0
            else:
                self.token_actual = ClaseLexica[tok.type].value
        except Exception as e:
            print("No fue posible leer el siguiente token. {excp}".format(excp=str(e)))


    def error(self, msg: str):
        print("ERROR DE SINTAXIS: {mensaje}. En la línea {linea}".format(mensaje=msg, 
                                                                         linea=self.an_lexico.lexer.lineno))
        exit(1)



    ########################################################################
    ##                                                                    ##
    ##                    TODO: Hardcodeo de la gramática                 ##
    ##                                                                    ##
    ########################################################################

    def load_syms(self):
        from componente.clase_lexica import ClaseLexica, NoTerminal
        from componente.gramatica.simbolo import Simbolo

        self.gramatica.simbolos.extend([
            Simbolo(ClaseLexica.NUMERO, Simbolo.SimTipo.TERMINAL),
            Simbolo(ClaseLexica.PLUS, Simbolo.SimTipo.TERMINAL),
            Simbolo(ClaseLexica.EOF, Simbolo.SimTipo.TERMINAL),
            Simbolo(NoTerminal.s, Simbolo.SimTipo.NO_TERMINAL),
            Simbolo(NoTerminal.sprim, Simbolo.SimTipo.NO_TERMINAL),
            Simbolo(NoTerminal.epsilon, Simbolo.SimTipo.NO_TERMINAL),
    ])

    def load_prods(self):
        g = self.gramatica
        S = g.get_sim("s")
        S_ = g.get_sim("sprim")
        NUM = g.get_sim(1)
        PLUS = g.get_sim(2)
        EPS = g.get_sim("")

        g.producciones.extend([
            Produccion(S, [NUM, S_]),
            Produccion(S_, [PLUS, NUM, S_]),
            Produccion(S_, [EPS])
        ])

    def load_table(self):
        g = self.gramatica
        S = g.get_sim("s")
        S_ = g.get_sim("sprim")
        NUM = g.get_sim(1)
        PLUS = g.get_sim(2)
        EOF = g.get_sim(0)

        self.tabla[S] = { NUM: g.get_prod(0) }
        self.tabla[S_] = {
            PLUS: g.get_prod(1),
            EOF: g.get_prod(2)
        }

    def parse(self):
        self.load_syms()
        self.load_prods()
        self.load_table()

        stack = [
            self.gramatica.get_sim(ClaseLexica.EOF.value),   # $
            self.gramatica.get_sim(NoTerminal.s.value)       # símbolo inicial
        ]

        self.an_lexico.lexer.input(self.an_lexico.lexer.lexdata)
        tok = self.an_lexico.lexer.token()
        derivaciones = []

        while stack:
            top = stack.pop()

            if top.sim == NoTerminal.epsilon:
                continue  # ε no se procesa, solo se omite

            if top.tipo == Simbolo.SimTipo.TERMINAL:
                if not tok:
                    self.error(f"Entrada insuficiente, falta: {top.sim.name}")
                if ClaseLexica[tok.type] == top.sim:
                    tok = self.an_lexico.lexer.token()
                else:
                    self.error(f"Token inesperado: '{tok.value}' (esperado: {top.sim.name})")

            elif top.tipo == Simbolo.SimTipo.NO_TERMINAL:
                
                if not tok:
                    class DummyTok:
                        type = "EOF"
                        value = "$"
                    tok = DummyTok()



                actual = ClaseLexica[tok.type] if tok else ClaseLexica.EOF
                terminal = self.gramatica.get_sim(actual.value)

                if top not in self.tabla or terminal not in self.tabla[top]:
                    self.error(f"Sin regla para ({top.sim.name}, {actual.name})")

                produccion = self.tabla[top][terminal]
                derivaciones.append(str(produccion))
                for simbolo in reversed(produccion.cuerpo):
                    if simbolo.sim != '':
                        stack.append(simbolo)

        print("\nCadena aceptada. Derivación:")
        for paso in derivaciones:
            print(paso)

    