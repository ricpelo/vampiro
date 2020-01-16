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

def make_items(seq):
    return list(seq)

def es_vacia(li):
    return li == []

def primer_item(li):
    return li[0]

def resto_items(li):
    return li[1:]

def item_iesimo(li, i):
    return li[i]

def existe_item_iesimo(li, i):
    return i >= 0 and i < len(li)

def meter_item(li, i):
    li.append(i)
    return li

def sacar_item(li, i):
    li.remove(i)
    return li
