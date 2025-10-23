"""
Retorno de valores das funções (return)
"""
def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

# return [10, 20]
# return (10, 20)

soma1 = soma(11, 6)
soma2 = soma(3, 3)
# print(soma1 + soma2)
print(soma1)
print(soma2)
print(soma(11, 55))
