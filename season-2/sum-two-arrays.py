""" Su tarea es crear una función llamada,
que toma dos matrices que constan de
enteros y devuelve la suma de esas dos matrices. """
def sum_arrays(array1,array2):
    if not array1 and not array2:return []
    if not array1 or not array2:
        if not array1: return array2
        if not array2: return array1
    else:
        out=int(''.join(list(map(str,array1))))+int(''.join(list(map(str,array2))))
        if out<0:
            out2=list(map(int,str(abs(out))))
            f=0-out2[0]
            out2.pop(0)
            out2.insert(0,f)
        return out2 if out<0 else list(map(int,str(out)))

print(sum_arrays([],[]))
print(sum_arrays([0],[]))
print(sum_arrays([],[1,2]))
print(sum_arrays([3,2,9],[1,2]))
print(sum_arrays([-3,4,2],[3,4,4]))
print(sum_arrays([3,2,6,6],[-7,2,2,8]))