""" La raíz digital es la suma recursiva de todos los 
dígitos de un número.

Dado n, tome la suma de los dígitos de n. Si ese valor tiene 
más de un dígito, continúe reduciendo de esta manera hasta 
que se produzca un número de un solo dígito. La entrada será 
un número entero no negativo. """
def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum(map(int, str(n))))
            
print(digital_root(7639))
