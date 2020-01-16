import parser
import mapeado as mapa
import items

mapa.actual = mapa.vestibulo
mapa.describir()

while True:
    entrada = input('\n¿Qué vas a hacer ahora?\n> ').strip().upper()
    parser.interpretar(entrada)
    # print('El verbo es', parser.verbo)
    # print('El nombre es', parser.nombre)
    if parser.verbo == parser.ABRIR and \
       parser.nombre == parser.PUERTA and \
       mapa.actual == mapa.vestibulo:
        print('No puedes salir sin haber acabado tu misión.')
    elif parser.verbo == parser.MIRAR:
        mapa.describir()
    elif parser.verbo == parser.COGER and \
         parser.nombre == parser.PALANCA and \
         mapa.actual == mapa.biblioteca:
        mapa.actual[mapa.ITEMS].remove(items.palanca)
        print('Has cogido la palanca.')
    else:
        destino = mapa.conecta_con(mapa.actual, parser.verbo)
        if destino != mapa.localidad_nula:
            mapa.actual = destino
            mapa.describir()
        else:
            print('No puedes hacer eso.')
