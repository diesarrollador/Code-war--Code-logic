""" Escribe una función que encuentre todos
los anagramas de una palabra de una lista.
Se le darán dos entradas, una palabra 
y una matriz con palabras.
Debe devolver una matriz de todos los anagramas 
o una matriz vacía si no hay ninguno """
anagrams=lambda word,words:[elemento for elemento in words if ''.join(sorted(elemento))==''.join(sorted(word))]

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) )
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))