import sys
from analisis.sintactico import Parser
from analisis.lexico import Lexer

def main():
    # Verifica si se pasó un archivo como argumento
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            # Intenta abrir el archivo y leer su contenido
            with open(filename, 'r') as file:
                data = file.read()
                print(f"Archivo cargado: {filename}")
        except FileNotFoundError:
            print(f"Error: el archivo '{filename}' no existe.")
            return
    else:
        # Si no se pasa archivo, usa una cadena por defecto
        data = "42"
        print("Cadena directa")

    # Construir el analizador léxico (scanner)
    scanner = Lexer()
    scanner.build()
    scanner.lexer.input(data)

    # Crear el parser y comenzar el análisis sintáctico
    parser = Parser(scanner)
    parser.parse()

if __name__ == "__main__":
    main()
