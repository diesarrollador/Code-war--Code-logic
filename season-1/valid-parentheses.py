""" Escriba una función que tome una cadena
de paréntesis y determine si el orden de
los paréntesis es válido. La función debe
devolver verdadero si la cadena es válida
y falso si no es válida. """


def valid_parentheses(string):
    cont = 0
    for i in string:
        if i == '(':
            cont += 1
        elif i == ')':
            cont -= 1
        if cont < 0:
            return False
    return cont == 0


print(valid_parentheses("()(()"))
print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses("hi(hi)()"))
print(valid_parentheses("(gg))("))
print(valid_parentheses("(())((()())())"))
