"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}','|','x + y =',x + y + z)

# print(soma)
# print(soma(1, 2))
soma(1, 2, 3)
soma(y=2, z=3, x=1)
soma(1, y=2, z=5) # depois do primeiro nomeado todos precisam ser nomeados