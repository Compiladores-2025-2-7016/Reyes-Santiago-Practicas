import os
from analisis.sintactico import ParserLL
from analisis.lexico import Lexer

ruta = os.path.join(os.path.dirname(__file__), "../../tst/valido1.txt")
with open(ruta) as f:
    data = f.read()

scanner = Lexer()
scanner.build()
scanner.lexer.input(data)

parser = ParserLL(scanner)
parser.parse()
