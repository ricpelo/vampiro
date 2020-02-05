class Token:
    def __init__(self, token):
        self.set_token(token)

    def __repr__(self):
        return self.token()

    def token(self):
        return self._token

    def set_token(self, token):
        self._token = token

token_nulo = Token('NULO')

class Vocabulario:
    verbo = token_nulo
    nombre = token_nulo

    def __init__(self, diccionario=None):
        self._vocabulario = {}
        if diccionario is not None:
            for token, lexemas in diccionario.items():
                self.meter(token, lexemas)

    def __contains__(self, key):
        return key in self._vocabulario

    def meter(self, token, lexemas):
        for lexema in lexemas:
            self._vocabulario[lexema] = token

    def token(self, lexema, default=None):
        return self._vocabulario.get(lexema, default)

    @staticmethod
    def interpretar(entrada, verbos, nombres):
        import re
        Vocabulario.verbo = token_nulo
        Vocabulario.nombre = token_nulo
        patron = re.compile(r'^\w+( +\w+)?$')
        if patron.match(entrada) is not None:
            palabras = entrada.split()
            Vocabulario.verbo = verbos.token(palabras[0])
            if len(palabras) > 1:
                Vocabulario.nombre = nombres.token(palabras[1])
