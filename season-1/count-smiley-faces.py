""" Dada una matriz(arr) como argumento,
complete la función countSmileys que
debería devolver el número total de caras sonrientes.
Reglas para una cara sonriente:
Cada cara sonriente debe contener un par de ojos válido.
Los ojos se pueden marcar como : o ;
Una carita sonriente puede tener nariz, pero no es necesario.
Los caracteres válidos para una nariz son - o ~
Cada rostro sonriente debe tener una boca sonriente
que debe estar marcada con ) o D
No se permiten caracteres adicionales excepto los mencionados.
Ejemplos de caritas sonrientes válidas:
:) :D ;-D :~)
Caritas sonrientes no válidas:; (:>:}:] """
from loguru import logger


@logger.catch
def count_smileys(arr):
    cont = 0
    for item in arr:
        item = ''.join(x for x in item if x not in '-~')
        if item in [':)', ':D', ';D', ';)']:
            cont += 1
    return cont


print(count_smileys([':)', ';(', ';}', ':-D']))
print(count_smileys([';D', ':-(', ':-)', ';~)']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
