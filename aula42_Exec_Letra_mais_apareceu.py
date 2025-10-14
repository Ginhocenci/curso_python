# frase = 'O Python é uma linguagem de programação '\
#     'multiparadigma. ' \
#     'Python foi criado por Guido van Rossum.'.upper()

# print(frase)

frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'.lower()

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

i = 0
while i < len(frase):
    letra_atual = frase[i]
    i += 1

    if letra_atual == ' ':
        continue

    qtd_atual = frase.count(letra_atual)
    
    if qtd_atual > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

# print(f'A letra mais usada é "{letra_apareceu_mais_vezes}" foi utilizada {qtd_apareceu_mais_vezes}.')

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x.'
)