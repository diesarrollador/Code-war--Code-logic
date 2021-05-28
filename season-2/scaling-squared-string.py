"""
Escribe una función que devuelva la escala de una cadena 
La función scale (strng, k, v) realizará una escala k-horizontal y una escala v-vertical.
Ejemplo:
s = "abcd\nefgh\nijkl\nmnop"
Estudiaremos la escala "horizontal" y "vertical" de este cuadrado de cuerdas.
Una escala k-horizontal de una cadena consiste en replicar k veces 
cada carácter de la cadena (excepto '\ n').
Ejemplo: escala 2-horizontal de s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
Una escala v-vertical de una cadena consiste en replicar v veces cada parte de la cadena al cuadrado.
Ejemplo: escala de 2 verticales de s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
"""
def scale(string,k,n):
    if not string:return ""
    else:
        out,lst_out=str(),list()
        for caracter in string.replace('\n',' '):
            if caracter!=' ':
                out+=caracter*k
            else:
                out+=caracter
        for elemento in out.split(" "):
            for _ in range(n):
                lst_out.append(elemento)
        return "\n".join(lst_out)

print(scale("", 1, 2))#Output->""
print(scale("Kj\nSH", 1, 2))#Output->"Kj\nKj\nSH\nSH"
print(scale("abcd\nefgh\nijkl\nmnop", 2, 3))#Output->"aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"