"""
Fatiamento de strings
 012345678 (índice)
 Olá mundo (len = 9)
-987654321 (indice invertido)
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de carecteres da str
"""
variavel = 'Olá mundo'
print(variavel[5])  #u
print(variavel[-4]) #u
print(variavel[4:])
print(variavel[-8:-2])

print(len(variavel)) 

print(variavel[-1:-10:-1])
print(variavel[::-1])
print(variavel[0:9:2])