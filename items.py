import parser

class Item:
    def __init__(self, nombre, palabra):
        self.set_nombre(nombre)
        self.set_palabra(palabra)

    def nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def palabra(self):
        return self._palabra

    def set_palabra(self, palabra):
        self._palabra = palabra

cuchillo = Item(
    'un cuchillo',
    parser.CUCHILLO
)

palanca = Item(
    'una palanca',
    parser.PALANCA
)

crucifijo = Item(
    'un crucifijo',
    parser.CRUCIFIJO
)

class GrupoItems:
    def __init__(self, iterable = None):
        self._items = set()
        if iterable is not None:
            for elem in iterable:
                self.insertar(elem)

    def insertar(self, item):
        self._items.add(item)

    def sacar(self, item):
        self._items.discard(item)

    def esta_vacio(self):
        return len(self._items) == 0

    def contiene(self, item):
        return item in self._items

grupo_items_vacio = GrupoItems()
