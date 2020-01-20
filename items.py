import parser

"""
cuchillo = (
    'un cuchillo',
    parser.CUCHILLO
)

palanca = (
    'una palanca',
    parser.PALANCA
)

crucifijo = (
    'un crucifijo',
    parser.CRUCIFIJO
)
"""

def vacia():
    return []

def meter(it, li):
    li.append(it)
    return li

def sacar(it, li):
    li.remove(it)
    return li

def es_vacia(li):
    return li == []

def esta_en(it, li):
    return it in li
