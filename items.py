class Item:
    def __init__(self, nombre, token):
        self.set_nombre(nombre)
        self.set_token(token)

    def nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def token(self):
        return self._token

    def set_token(self, token):
        self._token = token

class GrupoItems:
    def __init__(self, iterable=None):
        self._items = set()
        self.meter_masivo(iterable)

    def __iter__(self):
        return iter(self.items())

    def items(self):
        return self._items

    def meter(self, item):
        self.items().add(item)

    def meter_masivo(self, iterable):
        if iterable is not None:
            for elem in iterable:
                self.meter(elem)

    def sacar(self, item):
        self.items().discard(item)

    def esta_vacio(self):
        return len(self.items()) == 0

    def contiene(self, item):
        return item in self.items()

    def contiene_token(self, token):
        for item in self.items():
            if item.token() == token:
                return item
        return False
