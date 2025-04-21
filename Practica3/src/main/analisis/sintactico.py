from analisis.lexico import Lexer
from componente.clase_lexica import ClaseLexica

class Parser:

    def __init__(self, lexer: Lexer):
        # Guarda el analizador léxico y el token actual
        self.an_lexico = lexer
        self.token_actual = 0

    # Función que consume un token si es el esperado
    def eat(self, clase_lexica: int):
        if self.token_actual == clase_lexica:
            try:
                tok = self.an_lexico.lexer.token()
                if not tok:  # Fin de entrada
                    self.token_actual = 0
                else:
                    self.token_actual = ClaseLexica[tok.type].value
            except Exception as e:
                print(f"No fue posible leer el siguiente token. {e}")
        else:
            # Error si el token actual no es el esperado
            self.error(f"Se esperaba el token con clase léxica: {clase_lexica}, pero se recibió: {self.token_actual}")

    # Mensaje de error genérico
    def error(self, msg: str):
        print(f"ERROR DE SINTAXIS: {msg}. En la línea {self.an_lexico.lexer.lineno}")
        exit(1)

    # Inicia el análisis sintáctico desde el símbolo inicial
    def parse(self):
        try:
            tok = self.an_lexico.lexer.token()
            self.token_actual = ClaseLexica[tok.type].value
        except Exception as e:
            print(f"No fue posible obtener el primer token de la entrada: {e}")
            exit(1)

        self.programa()
        if self.token_actual == 0:
            print("La cadena es aceptada")
        else:
            print("La cadena no pertenece al lenguaje generado por la gramática")

    ###############################
    # Funciones por cada No Terminal
    ###############################

    # programa → declaraciones sentencias
    def programa(self):
        self.declaraciones()
        self.sentencias()

    # declaraciones → declaracion declaraciones'
    def declaraciones(self):
        self.declaracion()
        self.declaraciones_rest()

    # declaraciones' → declaracion declaraciones' | ε
    def declaraciones_rest(self):
        if self.token_actual in [ClaseLexica.INT.value, ClaseLexica.FLOAT.value]:
            self.declaracion()
            self.declaraciones_rest()

    # declaracion → tipo lista_var ;
    def declaracion(self):
        self.tipo()
        self.lista_var()
        self.eat(ClaseLexica.PUNTOYCOMA.value)

    # tipo → int | float
    def tipo(self):
        if self.token_actual == ClaseLexica.INT.value:
            self.eat(ClaseLexica.INT.value)
        elif self.token_actual == ClaseLexica.FLOAT.value:
            self.eat(ClaseLexica.FLOAT.value)
        else:
            self.error("Se esperaba 'int' o 'float'")

    # lista_var → IDENTIFICADOR lista_var'
    def lista_var(self):
        self.eat(ClaseLexica.IDENTIFICADOR.value)
        self.lista_var_rest()

    # lista_var' → , IDENTIFICADOR lista_var' | ε
    def lista_var_rest(self):
        if self.token_actual == ClaseLexica.COMA.value:
            self.eat(ClaseLexica.COMA.value)
            self.eat(ClaseLexica.IDENTIFICADOR.value)
            self.lista_var_rest()

    # sentencias → sentencia sentencias'
    def sentencias(self):
        self.sentencia()
        self.sentencias_rest()

    # sentencias' → sentencia sentencias' | ε
    def sentencias_rest(self):
        if self.token_actual == ClaseLexica.IDENTIFICADOR.value:
            self.sentencia()
            self.sentencias_rest()

    # sentencia → IDENTIFICADOR = expresion ;
    def sentencia(self):
        self.eat(ClaseLexica.IDENTIFICADOR.value)
        self.eat(ClaseLexica.IGUAL.value)
        self.expresion()
        self.eat(ClaseLexica.PUNTOYCOMA.value)

    # expresión → termino expresión'
    def expresion(self):
        self.termino()
        self.expresion_rest()

    # expresión' → + termino expresión' | - termino expresión' | ε
    def expresion_rest(self):
        if self.token_actual == ClaseLexica.MAS.value:
            self.eat(ClaseLexica.MAS.value)
            self.termino()
            self.expresion_rest()
        elif self.token_actual == ClaseLexica.MENOS.value:
            self.eat(ClaseLexica.MENOS.value)
            self.termino()
            self.expresion_rest()

    # termino → factor termino'
    def termino(self):
        self.factor()
        self.termino_rest()

    # termino' → * factor termino' | / factor termino' | ε
    def termino_rest(self):
        if self.token_actual == ClaseLexica.POR.value:
            self.eat(ClaseLexica.POR.value)
            self.factor()
            self.termino_rest()
        elif self.token_actual == ClaseLexica.DIV.value:
            self.eat(ClaseLexica.DIV.value)
            self.factor()
            self.termino_rest()

    # factor → NUMERO | IDENTIFICADOR | ( expresion )
    def factor(self):
        if self.token_actual == ClaseLexica.NUMERO.value:
            self.eat(ClaseLexica.NUMERO.value)
        elif self.token_actual == ClaseLexica.IDENTIFICADOR.value:
            self.eat(ClaseLexica.IDENTIFICADOR.value)
        elif self.token_actual == ClaseLexica.PARIZQ.value:
            self.eat(ClaseLexica.PARIZQ.value)
            self.expresion()
            self.eat(ClaseLexica.PARDER.value)
        else:
            self.error("Se esperaba un número, identificador o paréntesis")
