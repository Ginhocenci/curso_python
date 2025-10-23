"""
Higher Order Fuctions
Funções de primeira classe
"""
# def saudacao(msg):
#     return msg

# def executa(funcao, texto):
#     return funcao(texto)

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

# saudacao_2 = saudacao

# print(saudacao('Bom dia'))
# print(saudacao_2('Bom dia'))

print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Boa Noite', 'Maria'))