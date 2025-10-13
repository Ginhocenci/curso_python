""" Calculadora com while """
while True:
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break
    
    numero_1 = input('Digite o primeiro numero: ')
    numero_2 = input('Digite o segundo numero: ')
    operacao = input('Qual a operação +, -, * ou /: ')

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        resultado = 0.0
        if len(operacao) == 1:
            if operacao == '+':
                resultado = numero_1_float + numero_2_float
            elif operacao == '-':
                resultado = numero_1_float - numero_2_float
            elif operacao == '*':
                resultado = numero_1_float * numero_2_float
            elif operacao == '/':
                resultado = numero_1_float / numero_2_float
            else:
                print('Favor digitar um operador valido.')

            if resultado > 0:
                imprimir = f'Resultado = {resultado:.2f}'
                print(imprimir)
        else:
            print('Favor digitar um operador valido.')

    except:
        print('Favor inserir apenas números.')