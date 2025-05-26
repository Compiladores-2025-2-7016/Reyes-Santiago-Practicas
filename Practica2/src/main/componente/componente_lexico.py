from componente.clase_lexica import ClaseLexica

class ComponenteLexico:
    """
    Representa un token léxico en el proceso de análisis sintáctico.
    """
    def __init__(self, clase: ClaseLexica, lexema: str):
        """
        Constructor de la clase ComponenteLexico.
        """
        self.clase = clase
        self.lexema = lexema

    def __str__(self):
        return f"<{self.clase.name}, {self.lexema}>"
