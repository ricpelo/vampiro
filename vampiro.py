import parser
import mapeado as mapa
import items

mapa.actual = mapa.vestibulo
mapa.actual.describir()

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
        mapa.actual.describir()
#     elif parser.verbo == parser.COGER and \
#          parser.nombre == parser.PALANCA and \
#          mapa.actual == mapa.biblioteca:
#          items.sacar(items.palanca, mapa.actual[mapa.ITEMS])
# #        mapa.actual[mapa.ITEMS].remove(items.palanca)
#         print('Has cogido la palanca.')
    else:
        destino = mapa.actual.conecta_con(parser.verbo)
        if destino != mapa.localidad_nula:
            mapa.actual = destino
            mapa.actual.describir()
        else:
            print('No puedes hacer eso.')
