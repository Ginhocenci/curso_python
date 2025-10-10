"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>100,.1f
Conversion flags - !r !s !a __repr__ __str__
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #Completa a esquerda
print(f'{variavel:-<10}') #Completa a direita
print(f'{variavel:$^10}') #Centraliza
print(f'{1000.12423412431243:0>+10,.1f}')
print(f'{1000.12423412431243:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
# print(f'{variavel!a}')