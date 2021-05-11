""" Si enumeramos todos los números naturales 
por debajo de 10 que son múltiplos de 3 o 5, 
obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.
Termina la solución para que devuelva la suma de todos 
los múltiplos de 3 o 5 por debajo del número pasado. 
Nota: Si el número es un múltiplo de 3 y 5, solo cuéntelo 
una vez. Además, si un número es negativo, devuelve 0 
(para los idiomas que los tienen) """
solution = lambda number : 0 if number < 1 else sum([(i) for i in range(number) if (i) % 3 == 0 or (i) % 5 == 0])

print(solution(100))
