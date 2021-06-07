""" Dados los nombres y calificaciones de cada estudiante 
en una clase de N estudiantes, guárdelos en una lista
anidada e imprima el nombre(s) de cualquier estudiante
que tenga la segunda calificación más baja.
Nota: Si hay varios estudiantes con la segunda 
calificación más baja, ordene sus nombres
alfabéticamente e imprima cada nombre en una nueva línea.
"""
def nested_lists(name, score):
    outlist = list()
    data = sorted(list(zip(name, score)), key=lambda x:x[1])
    min_score = data[0][1]
    olist = [i for i in data if i[1] != min_score]
    first =  olist[0][1]
    
    for j in olist:
        if j[1] == first:
            outlist.append(j)
            
    return sorted(outlist, key=lambda x:x[0])

if __name__ == '__main__':
    name, score = list(), list()
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
    result = nested_lists(name, score)
    for i, _ in result:
        print(i)

#SAMPLE INPUT
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39

#SAMPLE OUTPUT
#Berry
#Harry