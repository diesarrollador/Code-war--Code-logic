""" Los cajeros automáticos permiten códigos PIN de 4 o 6 
dígitos y los códigos PIN no pueden contener nada más 
que exactamente 4 dígitos o exactamente 6 dígitos.

y que no tenga letras
verificar longitud
que no sea negativo

Si a la función se le pasa una cadena de PIN válida, 
devuelve verdadero, de lo contrario devuelve falso. """
def validate_pin(pin):
    if not pin.isnumeric():
        return False
    if len(pin) <= 3 or len(pin) == 5 or len(pin) > 6:
        return False
    return True
    
print(validate_pin("11111"))
