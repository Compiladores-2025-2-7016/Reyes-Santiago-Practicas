import sys
from lexer.scanner import Lexer

def main():
    """
    Función principal que ejecuta el analizador léxico.
    """
    archivo = sys.argv[1] if len(sys.argv) > 1 else None

    if archivo:
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
        except Exception as e:
            print(f"No se pudo leer el archivo {archivo}: {e}")
            return
    else:
        contenido = "3 y 4"  # Entrada predeterminada

    lexer = Lexer()
    lexer.build()
    lexer.scan(contenido)

if __name__ == '__main__':
    main()
