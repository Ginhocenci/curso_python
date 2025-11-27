# Exercício - Unir listas
# Crie uma função zipper (como o ziper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores de menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
# def zipper(l1, l2):
#     intervalo_maximo = min(len(l1), len(l2))
#     return [
#         (l1[i], l2[i]) for i in range(intervalo_maximo)
#     ]
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
# print(zipper (l1, l2))
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))