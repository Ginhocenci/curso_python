"""
args- Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(soma(1, 2, 3, 4, 5, 6))

print(sum((1, 2, 3, 4, 5, 6))) # comando de soma pronto no Python

numeros = 1, 2, 3, 4, 5, 6
print(soma(*numeros))