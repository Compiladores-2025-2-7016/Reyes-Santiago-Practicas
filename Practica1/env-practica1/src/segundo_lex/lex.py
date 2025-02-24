import sys
import ply.lex as lex
from ply.lex import TOKEN

# Definiciones de expresiones regulares auxiliares
digito = r'[0-9]'
letra = r'[a-zA-Z]'
hexadecimal = r'0[xX][0-9a-fA-F]+'
numero = r'(' + digito + r')+'
identificador_java = r'[a-zA-Z_][a-zA-Z0-9_]{0,31}'
espacio_en_blanco = r'[ \t]+'

# Lista de palabras reservadas de Python
reservadas_python = {
    "def", "class", "return", "if", "else"
}

# Lista de tokens. Siempre REQUERIDO
tokens = (
    "PALABRA",
    "NUMERO",
    "PARIZQ",
    "PARDER",
    "HEX",
    "RESERVADA_PYTHON",
    "ID_JAVA",
    "ESPACIO"
)

# Definición de reglas en una sola línea sin acción léxica
t_PALABRA = r'(' + letra + r'+)'
t_PARIZQ = r'\('
t_PARDER = r'\)'

# Definición de reglas con acción léxica
@TOKEN(hexadecimal)
def t_HEX(t):
    print('')
    print("Encontré un número hexadecimal:", t.value)
    return t

@TOKEN(numero)
def t_NUMERO(t):
    print('')
    print("Encontré un número:", t.value)
    return t

@TOKEN(identificador_java)
def t_ID_JAVA(t):
    if t.value in reservadas_python:
        t.type = "RESERVADA_PYTHON"
        print('')
        print("Palabra reservada de Python detectada:", t.value)
    else:
        print('')
        print("Identificador válido de Java:", t.value)
    return t

@TOKEN(espacio_en_blanco)
def t_ESPACIO(t):
    print('')
    print("Espacio en blanco detectado:", repr(t.value))
    return t

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar otros caracteres no especificados
t_ignore = ""

# Manejo de errores léxicos
def t_error(t):
    print('')
    print(f"Error léxico en línea {t.lexer.lineno}, columna {t.lexpos}: '{t.value[0]}'")
    t.lexer.skip(1)

###### Instanciación y uso del Analizador Léxico ######

# Construcción del Scanner
lexer = lex.lex()

# Código fuente de prueba
data = '''
def funcion():
    variable = 0xAB12
    class ClaseEjemplo:
        return 42
    _identificadorValidoJava32chars_abcdefghijklmno
    if else
    
'''

# En caso de que estemos leyendo un archivo señalado desde la línea de argumentos
if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as file:
        data = file.read()

lexer.input(data)

# Tokenización
while True:
    tok = lexer.token()
    if not tok:
        break  # Termina el análisis
    print(tok)
