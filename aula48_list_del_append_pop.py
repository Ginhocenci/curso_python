"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
# lista[2] = 3000
# del lista[2]
# print(lista[2])
lista.append(50)
lista.pop() # Apaga o último adicionado
lista.append(60)
lista.append(70)
# ultimo_valor = lista.pop() # Apaga o último adicionado e retorna o conteudo que apagou.
ultimo_valor = lista.pop(3) # Apaga o item da lista do indice e retorna o conteudo que apagou.
print(lista, 'Removido,', ultimo_valor)

