""" Haga que la función FindIntersection (strArr)
lea la matriz de cadenas almacenada en strArr
que contendrá 2 elementos: 
el primer elemento representará una lista 
de números separados por comas ordenados 
en orden ascendente, el segundo elemento representará
una segunda lista de números separados por comas números
(también ordenados). Su objetivo es devolver una cadena
separada por comas que contenga los números que
aparecen en los elementos de strArr en orden ordenado.
Si no hay intersección, devuelve la cadena falsa """


def FindIntersection(strArr):
    resul = []
    for i in strArr[0].replace(' ', '').split(','):
        if i in strArr[1].replace(' ', '').split(','):
            resul.append(i)
    return ','.join(resul) if len(resul) > 0 else False


print(FindIntersection(["3, 17, 18", "1, 4, 9, 10"]))
