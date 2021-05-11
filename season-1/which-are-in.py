""" Dadas dos matrices de cadenas a1 y a2 devuelven una 
matriz ordenada r en orden lexicográfico de las cadenas 
de a1 que son subcadenas de cadenas de a2. 
Ejemplo 1: 
a1 = ["arp", "live", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"] 
devuelve ["arp", "live ","strong"] 
Ejemplo 2: 
a1 = ["tarp","mice","bull"] 
a2 = ["lively","alive","harp","sharp","armstrong"] 
devuelve [] 
Notas: Las matrices se escriben en notación "general". 
Consulte "Sus casos de prueba" para ver ejemplos en su idioma. 
En Shell bash a1 y a2 son cadenas. El retorno es una
cadena donde las palabras están separadas por comas. 
Atención: r debe estar sin duplicados. No mutes las entradas. """
from loguru import logger
@logger.catch
def in_array(array1, array2):
    lst=[]
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] in array2[j]:
                lst.append(array1[i])

    return sorted(list(set(lst)))

print(in_array(["arp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))
