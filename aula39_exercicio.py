"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio' # Iteráveis
#     -1110987654321
print(nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    novo_nome += f'*{nome[indice]}'
    # novo_nome += '*'+nome[indice]
    indice += 1

novo_nome += '*'
print(novo_nome)

