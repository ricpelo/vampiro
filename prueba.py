class Persona:
    def __init__(self, nombre, apellidos):
        self._nombre = nombre
        self._apellidos = apellidos

    def nombre(self):
        return self._nombre

    def apellidos(self):
        return self._apellidos

    def visualizar(self):
        print(self.nombre(), self.apellidos())

class Cliente(Persona):
    def __init__(self, nombre, apellidos, numero):
        super().__init__(nombre, apellidos)
        self._numero = numero

    def numero(self):
        return self._numero

    def visualizar(self):
        super().visualizar()
        print(self.numero())

    @staticmethod
    def crear_desde_persona(per, num):
        return Cliente(per.nombre(), per.apellidos(), num)
