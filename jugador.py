import mapeado
import items

class Jugador:
    def __init__(self, localidad=mapeado.localidad_nula, iterable=None):
        self.set_localidad(localidad)
        self._inventario = items.GrupoItems(iterable)

    def inventario(self):
        return self._inventario

    def localidad(self):
        return self._localidad

    def set_localidad(self, localidad):
        self._localidad = localidad

    def coger(self, item):
        if item in self.localidad().items():
            self.localidad().items().sacar(item)
            self.inventario().meter(item)
            print(f'Has cogido {item.nombre()}.')
        else:
            print('No veo eso que dices.')

    def dejar(self, item):
        if item in self.inventario():
            self.inventario().sacar(item)
            self.localidad().items().meter(item)
            print(f'Has dejado {item.nombre()}.')
        else:
            print('No llevas eso.')

    def mostrar_inventario(self):
        if self.inventario().esta_vacio():
            print('No llevas nada.')
        else:
            print('Llevas:')
            for item in self.inventario():
                print('-', item.nombre())

    def mover(self, destino):
        self.set_localidad(destino)
        destino.describir()

    def contiene_token(self, token):
        return self.inventario().contiene_token(token)