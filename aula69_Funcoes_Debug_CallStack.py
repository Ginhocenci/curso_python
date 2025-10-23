"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo glogal e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavras global faz uma variável do escopo externo
ser a mesma no escopo interno.
"""
x = 1

def escopo():
    # global x
    x = 10

    def outra_funcao():
        # global x
        x = 11 # De dentro para fora temos acesso
        y = 2
        print(x,y)

    outra_funcao()
    # print(x)

# print(y) # De fora para dentro NÃO temos acesso
# print(x)
escopo()
# print(x)