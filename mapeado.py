import items
import grupo

class Conexion:
    def __init__(self, direccion, destino):
        self.set_direccion(direccion)
        self.set_destino(destino)

    def __repr__(self):
        return str(self.direccion()) + ' => ' + str(self.destino())

    def direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def destino(self):
        return self._destino

    def set_destino(self, destino):
        self._destino = destino

class GrupoConexiones(grupo.Grupo):
    def conexiones(self):
        return self.coleccion()

    def conecta_al(self, direccion):
        for conexion in self.conexiones():
            if conexion.direccion() == direccion:
                return conexion.destino()
        return localidad_nula

class Localidad:
    def __init__(self, nombre, descripcion, conexiones=None, contiene=None):
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)
        self._conexiones = GrupoConexiones(conexiones)
        self._grupo_items = items.GrupoItems(contiene)

    def __repr__(self):
        return self.nombre()

    def nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def conexiones(self):
        return self._conexiones

    def items(self):
        return self._grupo_items

    def describir(self):
        print(self.nombre())
        print(self.descripcion())
        if not self.items().esta_vacio():
            print('También puedes ver:')
            for item in self.items():
                print('-', item.nombre())

    def conecta_con(self, iterable):
        self.conexiones().meter_masivo(iterable)

    def conecta_al(self, direccion):
        return self.conexiones().conecta_al(direccion)

    def meter_conexion(self, conexion):
        self.conexiones().meter(conexion)

    def contiene_token(self, token):
        return self.items().contiene_token(token)

    # def meter_item(self, item):
    #     self._grupo_items.meter(item)

    # def sacar_item(self, item):
    #     self._grupo_items.sacar(item)

    # def contiene_item(self, item):
    #     return self._grupo_items.contiene(item)

    # def tiene_items(self):
    #     return self._grupo_items.esta_vacio()

localidad_nula = Localidad('NULA', 'Localidad nula.')
