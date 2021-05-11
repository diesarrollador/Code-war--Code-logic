""" Su tarea es ordenar una cadena determinada.
Cada palabra de la cadena contendrá un solo número.
Este número es la posición que debería tener la palabra en el resultado.

Nota: Los números pueden ser del 1 al 9. Por lo tanto, 
1 será la primera palabra (no 0).
Si la cadena de entrada está vacía, devuelve una cadena vacía. 
Las palabras en la cadena de entrada solo 
contendrán números consecutivos válidos. """

def order(sentence):
    z = []
    for i in range(1,10):
        for j in list(sentence.split()):
            if str(i) in j:
                z.append(j)
    return " ".join(z)

print(order("4of Fo1r pe6ople g3ood th5e the2"))