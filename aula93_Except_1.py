# Try, except, else e finally

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b #ZeroDivisionError
    print('Linha 2')

except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome de variável não encontrado')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception: # Qualquer erro
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')