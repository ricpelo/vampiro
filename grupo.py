class Grupo:
    def __init__(self, iterable=None):
        self._coleccion = set()
        self.meter_masivo(iterable)

    def __iter__(self):
        return iter(self.coleccion())

    def __repr__(self):
        return str(self.coleccion())

    def coleccion(self):
        return self._coleccion

    def meter(self, elem):
        self.coleccion().add(elem)

    def meter_masivo(self, iterable):
        if iterable is not None:
            for elem in iterable:
                self.meter(elem)