""" se pasa el parámetro str y determina 
si la cadena es un nombre de usuario válido
de acuerdo con las siguientes reglas:
1. El nombre de usuario tiene entre 4 y 25 caracteres.
2. Debe comenzar con una letra.
3. Solo puede contener letras, números y el carácter de subrayado.
4. No puede terminar con un carácter de subrayado.
Si el nombre de usuario es válido, 
entonces su programa debe devolver la cadena verdadera,
de lo contrario devolver la cadena falsa. """


def CodelandUsernameValidation(strParam):
    cont = 0
    if (len(strParam) > 3) and (len(strParam) < 27) and (strParam[0].isalpha()) and (strParam[-1] != '_'):
        for i in strParam:
            if i.isalpha() or i.isnumeric() or i == '_':
                cont += 1
    return cont == len(strParam)


print(CodelandUsernameValidation('5dh8ej8'))
