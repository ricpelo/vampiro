import mapeado
import items

class Jugador:
    def __init__(self, iterable=None):
        self._inventario = items.GrupoItems(iterable)

    def inventario(self):
        return self._inventario

    def coger(self, item):
        if item in mapeado.actual.items():
            mapeado.actual.items().sacar(item)
            self.inventario().meter(item)
            print(f'Has cogido {item.nombre()}.')
        else:
            print('No veo eso que dices.')

    def dejar(self, item):
        if item in self.inventario():
            self.inventario().sacar(item)
            mapeado.actual.items().meter(item)
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

jugador = Jugador()
