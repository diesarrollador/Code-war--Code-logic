"""
Complete la funcion / metodo (segun el lenguaje) para devolver verdadero
cuando su argumento es una matriz que tiene las mismas estructuras de 
anidamiento y la misma longitud correspondiente de matrices anidadas que la primera matriz.
"""
def same_structure_as(original, other):
    corchetes1=''.join([i for i in str(original) if i=='[' or i==']'])
    corchetes2=''.join([i for i in str(other) if i=='[' or i==']'])
    count=0
    if corchetes1==corchetes2:
        for i in range(len(original)):
            if type(original[i])==type(other[i]):
                for x in original:
                    if isinstance(x,list):
                        count+=1
                if count==0:
                    return len(original)==len(other)
                else:
                    for j in range(len(original)):
                        if isinstance(original[j],list) and isinstance(other[j],list):
                            return len(original[j])==len(other[j])
    return False

print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ]))
print(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
print(same_structure_as([1,'[',']'], ['[',']',1]))
print()
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ))
print(same_structure_as([1,[1,1]], [2,[2]]))

