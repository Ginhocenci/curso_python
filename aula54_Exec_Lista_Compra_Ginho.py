"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os
lista = []
indice = 0

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        lista.append(input('Valor: '))
        os.system('cls')
    elif opcao == 'a':
        indice_apagar = input('Escolha o índice para apagar:')
        if not indice_apagar.isdecimal():
            print('O indice precisa ser um número inteiro.')
            continue
        
        indice_apagar_int = int(indice_apagar)
        
        if indice_apagar_int >= len(lista):
            print('O índice não existe.')
            continue
        
        lista.pop(indice_apagar_int)
        os.system('cls')
        
    elif opcao == 'l':
        os.system('cls')
        for indice, nome in enumerate(lista):
            print(indice, nome)
    else:
        print('Opção não encontrada.')