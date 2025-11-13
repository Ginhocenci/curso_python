# Try, except, else e finally

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b #ZeroDivisionError
    print('Linha 2')

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu por zero.')
except NameError:
    print('Nome de variável não encontrado')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('Nome:', error.__class__.__name__)
except Exception: # Qualquer erro
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')