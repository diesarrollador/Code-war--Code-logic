"""
creará una función que toma una lista de enteros
no negativos y cadenas y devuelve una nueva lista 
con las cadenas filtradas.
"""
def filter_list(l=[]):
    n=[]
    for value in l:
        if not isinstance(value, str):
            n.append(value)
    return n

filter_list([1,2,'aasf','1','123',123])