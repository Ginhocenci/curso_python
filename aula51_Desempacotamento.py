"""
Introdução ao desempacotamento = tuples (tuplas)
"""

# nomes = ['Maria', 'Helena', 'Luiz']
# nomes1, nomes2, nomes3 = ['Maria', 'Helena', 'Luiz']
# print(nomes2)
# nome, *resto = ['Maria', 'Helena', 'Luiz']
# print(nome, resto)
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)
