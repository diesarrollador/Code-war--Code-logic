from random import randint
""" Genera numeros aleatorios que sean de la longitud ingresada"""
def random_int(lenght = 1):
    num_final = ''
    if lenght <= 0: 
        return 0
    for i in range(lenght):
        aleatoreo = randint(1, 9)
        num_final += str(aleatorio)
    return int(num_final)
print(random_int(46))  