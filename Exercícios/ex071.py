# Simula o funcionamento de um caixa eletrônico. Pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# O programa vai informar quantas cédulas de cada valor serão entregues
# O caixa possui cédulas de 50, 20, 10 e 1

# Saudações
print('=' * 30)
print('{:^30}'.format('Caixa Eletrônico'))
print('=' * 30)

# Lê o valor a ser sacado
valorSaque = int(input('Digite o valor a ser sacado: R$ '))

# Inicialização das variáveis, com um montante e a nota fica atribuída à maior nota disponível
valorTotal = valorSaque
nota = 50
totalNota = 0

# Repetição para subtrair o valor da nota do montante
while True:
    if valorTotal >= nota:
        valorTotal -= nota
        totalNota += 1

    # Se o montante for menor que a nota, troca para a próxima nota
    else:

        # Retorna a quantidade e a nota para o usuário
        if totalNota > 0:
            print(f'Total de {totalNota} cédulas de R${nota}.')

        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1

        # Zera o total de notas após trocar de nota, para começar zerado
        totalNota = 0

        # Condição para parar
        if valorTotal == 0:
            break

# Mensagem de encerramento
print('=' * 30)
print('Volte sempre! Tenha um bom dia!')
