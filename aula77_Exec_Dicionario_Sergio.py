# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    try:
        escolha = int(input('Escolha uma opção: '))
        if pergunta['Opções'][escolha] == pergunta['Resposta']:
            qtd_acertos += 1
            print('Acertou 👍')
        else:
            print('Errou ❌')
    except ValueError:
        print('Errou ❌')

    print()
print('Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')





