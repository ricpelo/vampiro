import parser
import mapeado
import items
import jugador

Voc = parser.Vocabulario
Tok = parser.Token

# VERBOS

ABRIR = Tok('ABRIR')
NORTE = Tok('NORTE')
SUR = Tok('SUR')
ESTE = Tok('ESTE')
OESTE = Tok('OESTE')
ARRIBA = Tok('ARRIBA')
ABAJO = Tok('ABAJO')
CERRAR = Tok('CERRAR')
MIRAR = Tok('MIRAR')
COGER = Tok('COGER')
DEJAR = Tok('DEJAR')
INVENTARIO = Tok('INVENTARIO')
FIN = Tok('FIN')

verbos = Voc({
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

LLAVE = Tok('LLAVE')
PUERTA = Tok('PUERTA')
CUCHILLO = Tok('CUCHILLO')
PALANCA = Tok('PALANCA')
CRUCIFIJO = Tok('CRUCIFIJO')

nombres = Voc({
    LLAVE: ['LLAVE', 'LLAVECITA'],
    PUERTA: ['PUERTA', 'PORTON'],
    CUCHILLO: ['CUCHILLO', 'NAVAJA'],
    PALANCA: ['PALANCA'],
    CRUCIFIJO: ['CRUCIFIJO', 'CRUZ'],
})

# ÍTEMS

cuchillo = items.Item(
    'un cuchillo',
    CUCHILLO
)

palanca = items.Item(
    'una palanca',
    PALANCA
)

crucifijo = items.Item(
    'un crucifijo',
    CRUCIFIJO
)

# LOCALIDADES

vestibulo = mapeado.Localidad(
    'VESTIBULO',
    'Estás en el vestíbulo del castillo...'
)

pasillo = mapeado.Localidad(
    'PASILLO',
    'Te encuentras en medio del pasillo principal...'
)

cocina = mapeado.Localidad(
    'COCINA',
    'Estás en la cocina del castillo...'
)

biblioteca = mapeado.Localidad(
    'BIBLIOTECA',
    'Te hallas en la biblioteca del castillo...',
    contiene=[palanca]
)

# CONEXIONES

vestibulo.conecta_con([
    mapeado.Conexion(NORTE, pasillo)
])

pasillo.conecta_con([
    mapeado.Conexion(SUR, vestibulo),
    mapeado.Conexion(ESTE, biblioteca),
    mapeado.Conexion(OESTE, cocina)
])

biblioteca.conecta_con([
    mapeado.Conexion(OESTE, pasillo)
])

cocina.conecta_con([
    mapeado.Conexion(ESTE, pasillo)
])

# Sitúa al jugador en la localidad inicial

aventurero = jugador.Jugador(localidad=vestibulo)
aventurero.localidad().describir()

# Empieza el bucle principal del juego

while True:
    entrada = input('\n¿Qué vas a hacer ahora?\n> ').strip().upper()
    Voc.interpretar(entrada, verbos, nombres)
    if Voc.verbo == ABRIR and \
       Voc.nombre == PUERTA and \
       aventurero.localidad() == vestibulo:
        print('No puedes salir sin haber acabado tu misión.')
    elif Voc.verbo == MIRAR:
        aventurero.localidad().describir()
    elif Voc.verbo == COGER:
        item = aventurero.localidad().items().contiene_token(Voc.nombre)
        aventurero.coger(item)
    elif Voc.verbo == DEJAR:
        item = aventurero.inventario().contiene_token(Voc.nombre)
        aventurero.dejar(item)
    elif Voc.verbo == INVENTARIO:
        aventurero.mostrar_inventario()
    elif Voc.verbo == FIN:
        print('Gracias por jugar.')
        break
    else:
        destino = aventurero.localidad().conecta_al(Voc.verbo)
        if destino != mapeado.localidad_nula:
            aventurero.mover(destino)
        else:
            print('No puedes hacer eso.')
