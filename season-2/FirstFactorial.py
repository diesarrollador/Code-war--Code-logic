""" Haga que la función que tome el parámetro num 
que se está pasando y devuelva el factorial del mismo.
Por ejemplo: si num = 4,
entonces su programa debería 
devolver (4 * 3 * 2 * 1) = 24.
Para los casos de prueba,
el rango estará entre 1 y 18 y
la entrada siempre será un número entero. """
from math import factorial
FirstFactorial = lambda num: 1 if num<=1 else factorial(num)


print(FirstFactorial(8))
