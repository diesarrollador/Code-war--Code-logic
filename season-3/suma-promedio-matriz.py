"""Ingresar dos números enteros positivos entre 3 y 6, ambos inclusive,
luego esos números serán las dimensiones de un arreglo bidimensional.
Posteriormente, poblar la matriz con números reales. Finalmente, muestre:
La suma por filas
El promedio por columnas"""

f = int(input("Filas: "))
c = int(input("Columnas: "))
matriz = list()

for i in range(f):
    matriz.append([])
    for j in range(c):
        matriz[i].append(n := int(input("Ingrese número: ")))

print("\n".join(f"Suma de la fila {i + 1}: {str(sum(matriz[i]))}" for i in range(len(matriz))))

print("\n".join([f"Promedio de la columna {i + 1}: {sum([fila[i] for fila in matriz]) / f}" for i in range(c)]))