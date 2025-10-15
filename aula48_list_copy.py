"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor da memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a # aponta para o mesmo endereço de memória

lista_a[0] = 'Qualquer coisa'
print(lista_b)

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # copia os valores imutáveis da lista

lista_a[0] = 'Qualquer coisa'
print(lista_b)