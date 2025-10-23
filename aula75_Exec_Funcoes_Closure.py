# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

def criar_mutiplicador(mutiplicador):
    def multriplicar(numero):
        return numero * mutiplicador
    return multriplicar

duplicar = criar_mutiplicador(2)
triplicar = criar_mutiplicador(3)
quaduplicar = criar_mutiplicador(4)
print(duplicar(3))
print(triplicar(3))
print(quaduplicar(3))