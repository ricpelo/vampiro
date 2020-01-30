verbo = None
nombre = None

class Vocabulario:
    def __init__(self):
        self._vocabulario = {}

    def insertar(self, token, lexemas):
        for lexema in lexemas:
            self._vocabulario[lexema] = token

    def insertar_masivo(self, diccionario):
        for token, lexema in diccionario.items():
            self.insertar(token, lexema)

    def __contains__(self, key):
        return key in self._vocabulario

    def token(self, lexema, default=None):
        return self._vocabulario.get(lexema, default)

def interpretar(entrada):
    """
    >>> interpretar("ABRIR PUERTA")
    >>> print(verbo)
    ABRIR
    >>> print(nombre)
    PUERTA
    """
    global verbo
    global nombre
    import re
    verbo = None
    nombre = None
    patron = re.compile(r'^\w+( +\w+)?$')
    if patron.match(entrada) is not None:
        palabras = entrada.split()
        verbo = verbos.token(palabras[0])
        if len(palabras) > 1:
            nombre = nombres.token(palabras[1])

# VERBOS

ABRIR = 'ABRIR'
NORTE = 'NORTE'
SUR = 'SUR'
ESTE = 'ESTE'
OESTE = 'OESTE'
ARRIBA = 'ARRIBA'
ABAJO = 'ABAJO'
CERRAR = 'CERRAR'
MIRAR = 'MIRAR'
COGER = 'COGER'
DEJAR = 'DEJAR'

verbos = Vocabulario()
verbos.insertar_masivo({
    ABRIR: ['ABRIR', 'ABRE'],
    NORTE: ['NORTE', 'N'],
    SUR: ['SUR', 'S'],
    ESTE: ['ESTE', 'E'],
    OESTE: ['OESTE', 'O'],
    ARRIBA: ['ARRIBA', 'SUBIR', 'SUBE'],
    ABAJO: ['ABAJO', 'BAJAR', 'BAJA'],
    ABRIR: ['ABRIR', 'ABRE'],
    CERRAR: ['CERRAR', 'CIERRA'],
    MIRAR: ['MIRAR', 'MIRA', 'M'],
    COGER: ['COGER', 'COGE', 'TOMA'],
    DEJAR: ['DEJAR', 'DEJA']
})

# NOMBRES

LLAVE = 'LLAVE'
PUERTA = 'PUERTA'
CUCHILLO = 'CUCHILLO'
PALANCA = 'PALANCA'
CRUCIFIJO = 'CRUCIFIJO'

nombres = Vocabulario()
nombres.insertar_masivo({
    LLAVE: ['LLAVE', 'LLAVECITA'],
    PUERTA: ['PUERTA', 'PORTON'],
    CUCHILLO: ['CUCHILLO'],
    PALANCA: ['PALANCA'],
    CRUCIFIJO: ['CRUCIFIJO', 'CRUZ'],
})

if __name__ == "__main__":
    print("ABRIR PUERTA")
    interpretar("ABRIR PUERTA")
    print(verbo, verbo == ABRIR)
    print(nombre, nombre == PUERTA)

    print("ABRE PUERTA")
    interpretar("ABRIR PUERTA")
    print(verbo)
    print(nombre)

    print("ABRIR")
    interpretar("ABRIR")
    print(verbo)
    print(nombre)
