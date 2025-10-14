"""
Iterável -> str, range, etc (__iter__)
Iterador -> quam sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Luiz') # __iter__()

# print(next(texto)) #texto.__next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))
# for letra in texto
texto = 'Luiz'  # iterável
iteratador = iter(texto)    # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)