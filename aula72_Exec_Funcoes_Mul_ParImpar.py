# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da varável.

# Crie uma função fala se um número é par ou impar.
# Retorne se o número é par ou impar.

def multiplicar(*args):
    total = 1 #args[0]
    for numeros in args:
        total *= numeros
    return total

def par_impar(numero):
    # multiplo_de_dois = numero % 2 ==0

    # if multiplo_de_dois:
    #     return f'{numero} é par'
    # # else:
    # return f'{numero} é impar'

    return f'{numero} é par' if numero % 2 == 0 else f'{numero} é impar'
    # return x % 2 == 0

print(multiplicar(1,2,3,4,5,6))
print(1*2*3*4*5*6)
print(par_impar(8))
print(par_impar(7))