""" Haga que la función tome un parámetro que se está pasando
y devuelva la palabra más larga de la cadena.
Si hay dos o más palabras que tienen la misma longitud,
devuelva la primera palabra de la cadena con esa longitud.
Ignore la puntuación y asuma que sen no estará vacío.
Las palabras también pueden contener números,
por ejemplo, "Hola mundo123 567". """


def LongestWord(sen):
    st = ''
    for x in sen:
        if x.isalnum() or x == ' ':
            st += x
    longitud = len(list(st.split())[0])
    palabra = list(st.split())[0]
    for p in list(st.split()):
        if len(p) > longitud:
            palabra = p
            longitud = len(p)
    return palabra


print(LongestWord("foundation keywods in panamanian pythonn nonlocal globals continue"))
