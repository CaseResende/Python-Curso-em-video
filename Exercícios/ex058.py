# Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Importa as funções de sorteio e de temporizar
from random import randint
from time import sleep

# Inicialização de variáveis
computador = randint(0, 10)
jogador = 11
tentativas = 0

# Apresentação
print('Bem vindo humano, sou o COMPUTADOR!')
print('Estou pensando em um número de 0 a 10, consegue adivinhar qual é?')
print('-' * 40)

# Fluxo de repetição para continuar jogando até acertar
while computador != jogador:

    # Recebe a escolha do jogador
    jogador = (int(input('Em que número estou pensando? ')))

    # Valida a escolha somente ao intervalo solicitado
    while jogador < 0 or jogador > 10:
        print('Escolha somente entre 0 e 10!')
        jogador = (int(input('Em que número estou pensando? ')))

    # Contabiliza uma tentativa
    tentativas += 1

    # Retorno com temporização
    print('{}?'.format(jogador))
    sleep(0.5)
    print('Pensando', end='')
    for cont in range(0, 3):
        sleep(0.5)
        print('.', end='')
    print('')

    # Condição caso o jogador erre com auxílios para a próxima escolha
    if computador != jogador:
        print('ERRRRROOOOU!!')

        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')

        print('Tenta de novo!')

# Retorna as respostas finais para o usuário
if tentativas > 5:
    print('Finalmente!!! Depois de {} tentativas! Já estava ficando cansado de tanto rir da sua cara!'.format(tentativas))
elif tentativas > 1:
    print('Você acertou! Mas gastou {} tentativas hein...'.format(tentativas))
else:
    print('Err.... Espere aí, não é possível!! Você acertou!')
