import numpy
"""
https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?h_r=next-challenge&h_v=zen

Mean: calcula la media aritmética a lo largo del eje especificado.
Var: calcula la varianza aritmética a lo largo del eje especificado.
Std: calcula la desviación estándar aritmética a lo largo del eje especificado.

Tarea:
Se le da una matriz 2-D de tamaño NxM.
Tu tarea es encontrar:
La mean a lo largo del axis 1
La var a lo largo del axis 0
El std a lo largo del axis None

Formato de entrada:
La primera línea contiene los valores 
separados por espacios de N y M.
Las siguientes N líneas contienen M enteros
separados por espacios.

Formato de salida:
Primero, imprima el mean.
En segundo lugar, imprima la var.
En tercer lugar, imprima el std.

"""
def mean_var_std(data2):
    ARRAY = numpy.array(data2)
    for i in range(3):
        if i == 0:
            yield numpy.mean(ARRAY, axis = 1)
        elif i == 1:
            yield numpy.var(ARRAY, axis = 0)
        elif i == 2:
            yield round(numpy.std(ARRAY, axis = None), 11)

if __name__ == '__main__':
    lista = list()
    filas, colum = list(map(int, input().split()))
    for i in range(filas):
        lista.append([])
        lista[i].extend(list(map(int, input().split())))

    for i in mean_var_std(lista):
        print(i)

# Test input:
# 2 2
# 1 2
# 3 4

# Output
# [ 1.5  3.5]
# [ 1.  1.]
# 1.11803398875