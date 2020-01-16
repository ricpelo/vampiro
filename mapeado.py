import parser as d
import items

NOMBRE = 'nombre'
DESCR = 'descr'
ITEMS = 'items'
CONEX = 'conex'

vestibulo = {
    NOMBRE: 'VESTÍBULO',
    DESCR: 'Estás en el vestíbulo del castillo...',
    ITEMS: []
}

pasillo = {
    NOMBRE: 'PASILLO',
    DESCR: 'Te encuentras en medio del pasillo principal...',
    ITEMS: []
}

cocina = {
    NOMBRE: 'COCINA',
    DESCR: 'Estás en la cocina del castillo...',
    ITEMS: [items.cuchillo]
}

biblioteca = {
    NOMBRE: 'BIBLIOTECA',
    DESCR: 'Te hallas en la biblioteca del castillo...',
    ITEMS: [items.palanca, items.crucifijo]
}

localidad_nula = {}

vestibulo[CONEX] = {d.NORTE: pasillo}
pasillo[CONEX] = {d.SUR: vestibulo, d.ESTE: biblioteca, d.OESTE: cocina}
biblioteca[CONEX] = {d.OESTE: pasillo}
cocina[CONEX] = {d.ESTE: pasillo}

actual = localidad_nula

def describir():
    print(actual[NOMBRE])
    print(actual[DESCR])
    if actual[ITEMS] != []:
        # Visualiza la lista de ítems que hay en la localidad actual
        print('También puedes ver:')
        for item in actual[ITEMS]:
            print(item[0])

def conecta_con(localidad, direccion):
    if direccion in localidad[CONEX]:
        return localidad[CONEX][direccion]
    else:
        return localidad_nula
