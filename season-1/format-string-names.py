""" Dado: una matriz que contiene hashes de nombres

Retorno: una cadena formateada como una lista de 
nombres separados por comas, excepto los dos últimos 
nombres, que deben estar separados por un ampersand. """
from loguru import logger
@logger.catch
def nameList(names):
    if not names: return ''
    cadena = [''.join(names[i].values()) for i in range(len(names))]
    names2 = ', '.join(cadena)
    strg = str(names2[::-1].replace(',', '& ', 1))
    return strg[::-1]


print(nameList([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
