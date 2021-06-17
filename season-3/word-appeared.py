""" En este desafío, se le darán 2 números enteros,
n y m. Hay n palabras, que pueden repetirse,
en el grupo de palabras A. Hay m palabras que
pertenecen al grupo de palabras B. Para cada m
palabras, verifique si la palabra ha aparecido 
en el grupo A o no. Imprima los índices de cada 
aparición de m en el grupo A. Si no aparece,
imprima -1. 

Input Format
1- La primera línea contiene números enteros, 
n y m separados por un espacio.
2- Las siguientes n líneas contienen las palabras 
que pertenecen al grupo A.
3- Las siguientes m líneas contienen las palabras 
que pertenecen al grupo B.
"""
def word_appeared(group_a: list, group_b: list) -> str:
    out = list()
    for i in range(len(group_b)):
        if group_b[i] not in group_a:
            out.append([-1])
        else: out.append([])
        for j in enumerate(group_a):
            if group_b[i] == j[1]: 
                out[i].append(j[0] + 1)
    return "\n".join([" ".join([str(j) for j in i]) for i in out])

if __name__ == "__main__":
    group_a, group_b = list(), list()
    n, m = map(int, input().split())
    for _ in range(n):
        dato = input()
        group_a.append(dato)
    for _ in range(m):
        dato = input()
        group_b.append(dato)
    print(word_appeared(group_a, group_b))

# Input test:
# 5 2
# a
# a
# b
# a
# b
# a
# b

# Output
# 1 2 4
# 3 5