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
                self.meter(elem)

    def items(self):
        return self._items

    def meter(self, item):
        self.items().add(item)

    def sacar(self, item):
        self.items().discard(item)

    def esta_vacio(self):
        return len(self.items()) == 0

    def contiene(self, item):
        return item in self.items()

    def contiene_palabra(self, palabra):
        for item in self.items():
            if item.palabra() == palabra:
                return item
        return False

    def __iter__(self):
        return iter(self.items())
