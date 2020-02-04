import parser
import mapeado
import items
import jugador

mapeado.actual = mapeado.vestibulo
mapeado.actual.describir()

while True:
    entrada = input('\n¿Qué vas a hacer ahora?\n> ').strip().upper()
    parser.interpretar(entrada)
    if parser.verbo == parser.ABRIR and \
       parser.nombre == parser.PUERTA and \
       mapeado.actual == mapeado.vestibulo:
        print('No puedes salir sin haber acabado tu misión.')
    elif parser.verbo == parser.MIRAR:
        mapeado.actual.describir()
    elif parser.verbo == parser.COGER:
        item = mapeado.actual.items().contiene_token(parser.nombre)
        jugador.jugador.coger(item)
    elif parser.verbo == parser.DEJAR:
        item = jugador.jugador.inventario().contiene_token(parser.nombre)
        jugador.jugador.dejar(item)
    elif parser.verbo == parser.INVENTARIO:
        jugador.jugador.mostrar_inventario()
    elif parser.verbo == parser.FIN:
        print('Gracias por jugar.')
        break
    else:
        destino = mapeado.actual.conecta_al(parser.verbo)
        if destino != mapeado.localidad_nula:
            mapeado.actual = destino
            mapeado.actual.describir()
        else:
            print('No puedes hacer eso.')
