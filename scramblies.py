""" Complete la función scramble (str1, str2) 
que devuelve verdadero si una parte de los
caracteres str1 se puede reorganizar para 
que coincida con str2; de lo contrario, devuelve falso. 
Notas: Solo se utilizarán letras minúsculas (a-z). 
No se incluirán signos de puntuación ni dígitos.
El rendimiento debe considerarse. Las cadenas de entrada
s1 y s2 tienen terminación nula. """
def scramble(s1,s2):
    for i in set(s2):                                                  
        if s1.count(i) < s2.count(i):
            return False                       
    return True

print(scramble('cedewaraaossoqqyt', 'codewars'))