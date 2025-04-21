from componente.clase_lexica import ClaseLexica

# Clase que representa un token (componente léxico)
class ComponenteLexico:
    clase: ClaseLexica
    lexema: str

    def __init__(self, clase, lexema):
        self.clase = clase
        self.lexema = lexema

    def __str__(self):
        return f"<{self.clase.name}, '{self.lexema}'>"
