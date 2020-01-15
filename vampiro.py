import parser
import mapeado as mapa

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
    else:
        destino = mapa.conecta_con(mapa.actual, parser.verbo)
        if destino != mapa.localidad_nula:
            mapa.actual = destino
            mapa.describir()
        else:
            print('No puedes hacer eso.')
