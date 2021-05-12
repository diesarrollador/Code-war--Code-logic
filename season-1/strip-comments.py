""" Complete la solución de modo que elimine 
todo el texto que sigue a cualquiera de un 
conjunto de marcadores de comentarios pasados.
Cualquier espacio en blanco al final de la
línea también debe eliminarse. """


def solution(string, markers):
    div = string.split('\n')
    for i, words in enumerate(div):
        for mark in markers:
            i_mark = words.find(mark)
            if i_mark != -1:
                words = words[:i_mark]
        div[i] = words.rstrip(' ')
    return '\n'.join(div)


print(
    solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
