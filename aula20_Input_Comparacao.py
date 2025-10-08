primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor == segundo_valor:
    print(f'Os valores {primeiro_valor=} e {segundo_valor=} são iguais.')
elif primeiro_valor > segundo_valor:
    print(
        f'O {primeiro_valor=} é maior '
        f'que o {segundo_valor=}'
        )
else:
    print(
        f'O {segundo_valor=} é maior '
        f'que o {primeiro_valor=}'
        )