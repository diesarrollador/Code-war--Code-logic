""" En este kata se requiere que, dada una cadena, 
reemplace cada letra con su posición en el alfabeto. 

Si algo en el texto no es una letra, ignórelo y no lo devuelva. 

"a" = 1, "b" = 2, etc. """
from string import ascii_lowercase
from loguru import logger

@logger.catch
def alphabet_position(text):
    position, position2 = [], []
    for i in (text.replace(" ", "").lower()):
        position.append((ascii_lowercase).find(i))
    position2 = [item + 1 for item in position if item != -1]
    return " ".join([str(value) for value in position2])

print(alphabet_position("The sunset sets at twelve o' clock."))
