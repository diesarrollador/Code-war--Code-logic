""" Dada una matriz de números enteros, 
encuentre las veces que aparece un número impar.
Siempre habrá un solo número entero que aparezca un número impar de veces. """
def find_it(seq):
    odd_list = [r for r in seq if seq.count(r) % 2 != 0]
    if len(seq) == 1:
        return seq.pop(0)
    return odd_list.pop(0)

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))