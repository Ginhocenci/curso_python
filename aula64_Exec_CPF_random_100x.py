import random
import sys


for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    # print(nove_digitos)

    contador_regressivo_1 = 10
    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    # print('O primeiro dígito do CPF é',digito_1)

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    # print('O segundo dígito do CPF é',digito_2)

    # if digito_1 == int(cpf_str[-2]) and digito_2 == int(cpf_str[-1]):
    #     print('Este CPF é valido.')
    # else:
    #     print('Este CPF é NÃO é valido.')
    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    cpf_gerado_pelo_calculo_str = ''
    i = 0
    for letra in cpf_gerado_pelo_calculo:
        if i==3 or i==6:
            cpf_gerado_pelo_calculo_str += f'.{letra}'
        elif i==9:
            cpf_gerado_pelo_calculo_str += f'-{letra}'
        else:
            cpf_gerado_pelo_calculo_str += f'{letra}'
        i+=1

    print('CPF gerado:',cpf_gerado_pelo_calculo_str)
