verbo = None
nombre = None

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

# NOMBRES

LLAVE = 'LLAVE'
PUERTA = 'PUERTA'

verbos = {
    'ABRIR': ABRIR,
    'ABRE': ABRIR,
    'NORTE': NORTE,
    'N': NORTE,
    'S': SUR,
    'E': ESTE,
    'O': OESTE,
    'ARRIBA': ARRIBA,
    'SUBIR': ARRIBA,
    'SUBE': ARRIBA,
    'ABAJO': ABAJO,
    'BAJAR': ABAJO,
    'BAJA': ABAJO,
    'CERRAR': CERRAR,
    'CIERRA': CERRAR,
    'MIRAR': MIRAR,
    'M': MIRAR
}

nombres = {
    'LLAVE': LLAVE,
    'LLAVECITA': LLAVE,
    'PUERTA': PUERTA,
    'PORTON': PUERTA
}

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
    patron = re.compile(r'^\w+( +\w+)?$')
    if patron.match(entrada) is None:
        verbo = None
        nombre = None
    else:
        tokens = entrada.split()
        verbo = verbos.get(tokens[0])
        if len(tokens) > 1:
            nombre = nombres.get(tokens[1])
        else:
            nombre = None

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
