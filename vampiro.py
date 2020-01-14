import parser

while True:
    entrada = input('¿Qué vas a hacer ahora?\n> ').strip().upper()
    parser.interpretar(entrada)
    print('El verbo es', parser.verbo)
    print('El nombre es', parser.nombre)
