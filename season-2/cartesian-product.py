""" Calcula el producto cartesiano """
from itertools import product
a = input()
b = input()
solucion = lambda a, b : print(*product(list(map(int, a.split())), list(map(int, b.split()))))
solucion(a, b)