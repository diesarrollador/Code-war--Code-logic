"""
Cree una función que devuelva la suma de los dos números positivos
más bajos dada una matriz de un mínimo de 4 enteros positivos.
No se pasarán números flotantes o enteros no positivos.
"""
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])
