import parser
import mapeado
import items

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
        item = mapeado.actual.items().contiene_palabra(parser.nombre)
        if item:
            mapeado.actual.items().sacar(item)
            print(f'Has cogido {item.nombre()}.')
    else:
        destino = mapeado.actual.conecta_al(parser.verbo)
        if destino != mapeado.localidad_nula:
            mapeado.actual = destino
            mapeado.actual.describir()
        else:
            print('No puedes hacer eso.')
