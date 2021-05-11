""" Bob se está preparando para aprobar la prueba de coeficiente intelectual.
La tarea más frecuente en esta prueba es averiguar cuál de los números 
dados difiere de los demás. Bob observó que un número generalmente difiere 
de los demás en la uniformidad. Ayude a Bob: para verificar sus respuestas, 
necesita un programa que entre los números dados encuentre uno que sea diferente
en uniformidad y devuelva una posición de este número. 
! Tenga en cuenta que su tarea es ayudar a Bob a resolver una prueba de 
coeficiente intelectual real, 
lo que significa que los índices de los elementos comienzan desde 1 (no 0) """
from loguru import logger
@logger.catch
def iq_test(numbers):
    num_par, num_impar, cont_impar, cont_par = 0, 0, 0, 0
    int_list = [int(i) for i in list((numbers.split(" ")))]
    for i in int_list:
        if i % 2 != 0:
            cont_impar += 1
            num_impar = int_list.index(i)
        else:
            cont_par += 1
            num_par = int_list.index(i)

    return (num_impar + 1) if cont_impar < cont_par else (num_par + 1)

print(iq_test("1 1 1 2"))
