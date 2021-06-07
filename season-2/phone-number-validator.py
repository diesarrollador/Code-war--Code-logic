""" Se le proporciona una entrada de número y debe
verificar si es un número de teléfono válido.
Un número de teléfono válido tiene exactamente 8
dígitos y comienza con 1, 8 o 9.
Salida "Válido" si el número es válido y "Inválido" si no lo es. """
import re
phone_number_validator = lambda num : 'Valid' if len(num) == 8 and re.match(r'^(1|8|9)[0-9]', num) else 'Invalid'

if __name__ == '__main__':
    print(phone_number_validator(num := input()))

#TEST Input
# 81234567 -> Valid
# 57345672 -> Invalid