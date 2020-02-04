class Token:
    def __init__(self, token):
        self.set_token(token)

    def __repr__(self):
        return self.token()

    def token(self):
        return self._token

    def set_token(self, token):
        self._token = token

token_nulo = Token('NULO')

class Vocabulario:
    def __init__(self, diccionario=None):
        self._vocabulario = {}
        if diccionario is not None:
            for token, lexemas in diccionario.items():
                self.meter(token, lexemas)

    def __contains__(self, key):
        return key in self._vocabulario

    def meter(self, token, lexemas):
        for lexema in lexemas:
            self._vocabulario[lexema] = token

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
    import re
    global verbo
    global nombre
    verbo = token_nulo
    nombre = token_nulo
    patron = re.compile(r'^\w+( +\w+)?$')
    if patron.match(entrada) is not None:
        palabras = entrada.split()
        verbo = verbos.token(palabras[0])
        if len(palabras) > 1:
            nombre = nombres.token(palabras[1])

# VERBOS

ABRIR = Token('ABRIR')
NORTE = Token('NORTE')
SUR = Token('SUR')
ESTE = Token('ESTE')
OESTE = Token('OESTE')
ARRIBA = Token('ARRIBA')
ABAJO = Token('ABAJO')
CERRAR = Token('CERRAR')
MIRAR = Token('MIRAR')
COGER = Token('COGER')
DEJAR = Token('DEJAR')
INVENTARIO = Token('INVENTARIO')
FIN = Token('FIN')

verbos = Vocabulario({
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
    DEJAR: ['DEJAR', 'DEJA'],
    INVENTARIO: ['INVENTARIO', 'I'],
    FIN: ['FIN', 'TERMINAR', 'ACABAR', 'FINALIZAR']
})

# NOMBRES

LLAVE = Token('LLAVE')
PUERTA = Token('PUERTA')
CUCHILLO = Token('CUCHILLO')
PALANCA = Token('PALANCA')
CRUCIFIJO = Token('CRUCIFIJO')

nombres = Vocabulario({
    LLAVE: ['LLAVE', 'LLAVECITA'],
    PUERTA: ['PUERTA', 'PORTON'],
    CUCHILLO: ['CUCHILLO', 'NAVAJA'],
    PALANCA: ['PALANCA'],
    CRUCIFIJO: ['CRUCIFIJO', 'CRUZ'],
})

verbo = token_nulo
nombre = token_nulo

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
