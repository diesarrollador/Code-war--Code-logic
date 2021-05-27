""" La función 'fibonacci' debería devolver una matriz de números de fibonacci.
La función toma un número como argumento para decidir cuántos no.
de elementos a producir. Si el argumento es menor o igual a 0, devuelve una matriz vacía """
def fibonacci(n):
    lista=[0,1]
    if n<=0:return []
    if n==1:return [0]
    for i in range(2,n):
        lista.append(lista[i-1]+lista[i-2])
    return lista

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(8))
print(fibonacci(4))
print(fibonacci(10))
print(fibonacci(-14))