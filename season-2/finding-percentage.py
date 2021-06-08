""" El código auxiliar proporcionado se leerá
en un diccionario que contiene pares clave / valor
de nombre: [marcas] para obtener una lista de estudiantes.
Imprima el promedio de la matriz de calificaciones 
para el nombre del estudiante proporcionado, 
mostrando 2 lugares después del decimal.
La primera línea contiene el número entero N,
el número de registros de los estudiantes.
Las siguientes líneas N contienen los nombres y
las calificaciones obtenidas por un estudiante,
cada valor separado por un espacio. La última 
línea contiene query_name, el nombre de un estudiante a consultar. """
def finding_the_percentage(dic_data, q_name):
    return format([i for x, i in [(n, sum(i)/3) for n, i in dic_data.items()] if x == q_name].pop(), '.2f')

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(finding_the_percentage(student_marks, query_name))

# TEST
# Input:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Output:
# 56.00

# Input:
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
# Output:
# 26.50