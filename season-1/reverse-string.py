""" Escriba una función que tome una cadena de una o más palabras y
devuelva la misma cadena, pero con las cinco o más palabras 
invertidas (como el nombre de este kata).

Las cadenas pasadas constarán solo de letras y espacios.
Los espacios se incluirán solo cuando haya más de una palabra. """
def spin_words(sentence):
    r = []
    s = sentence.split()
    for i in range(len(s)):
        if len(s[i]) < 5: r.append(s[i])
        if len(s[i]) > 4: r.append(s[i][::-1])
    return ' '.join(r)

print(spin_words("This is another test"))
