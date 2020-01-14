import parser
import mapeado

mapeado.actual = mapeado.vestibulo
print(mapeado.actual[0])
print(mapeado.actual[1])

while True:
    entrada = input('\n¿Qué vas a hacer ahora?\n> ').strip().upper()
    parser.interpretar(entrada)
    # print('El verbo es', parser.verbo)
    # print('El nombre es', parser.nombre)
    if parser.verbo == parser.ABRIR and \
       parser.nombre == parser.PUERTA and \
       mapeado.actual == mapeado.vestibulo:
        print('No puedes salir sin haber acabado tu misión.')
    elif parser.verbo == parser.MIRAR:
        print(mapeado.actual[0])
        print(mapeado.actual[1])
    else:
        c = mapeado.conexiones.get(mapeado.actual)
        if c is not None and parser.verbo in c:
            mapeado.actual = c[parser.verbo]
            print(mapeado.actual[0])
            print(mapeado.actual[1])
        else:
            print('No puedes hacer eso.')
