""" Escriba una función llamada repeatStr 
que repita la cadena dada exactamente n veces. """
repeat_str=lambda repeat,string:string*repeat

# TEST
print(repeat_str(6, "I"))#Output "IIIIII"
print(repeat_str(5, "Hello"))#Output "HelloHelloHelloHelloHello"