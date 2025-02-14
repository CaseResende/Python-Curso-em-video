# Jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER.
# Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Importação dos módulos para randomizar e temporizar
from random import randint
from time import sleep

# Inicialização de variáveis
soma = vitoria = 0
resultado = ''

# Apresentação
print('-=' * 30)
print('Vamos jogar PAR ou ÍMPAR')

# Estrutura de repetição que controla o jogo
while True:
    print('-=' * 30)

    # Leitura e validação do número do jogador
    while True:
        numJogador = int(input('Diga um valor: '))

        if numJogador < 0 or numJogador > 10:
            print('Você tem mais que 5 dedos em cada mão? Jogue de 0 a 10 igual todo ser humano...')
        else:
            break

    # Leitura e validação da jogada do jogador
    while True:
        jogadaJogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

        if jogadaJogador in 'PI':
            break
        else:
            print('Jogada inválida!')

    print('-' * 60)

    # Randomização do número para o computador
    numComputador = randint(0, 10)

    # Soma os dois números
    soma = numJogador + numComputador

    # Conversão da jogada do jogador
    if jogadaJogador == 'I':
        jogadaJogador = 'Ímpar'
    else:
        jogadaJogador = 'Par'

    # Verifica se a soma foi par ou ímpar
    if soma % 2 == 1:
        resultado = 'Ímpar'
    else:
        resultado = 'Par'

    # Retorna o resultado da partida
    sleep(0.5)
    print(f'Você jogou {numJogador} e eu {numComputador}. Total de {soma}, deu {resultado}.')
    print('-' * 60)

    # Calcula se o jogador foi vencedor e incrementa uma vitória
    if jogadaJogador == resultado:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        vitoria += 1

    # Encerra o laço caso seja uma derrota
    else:
        break

# Retorno do placar
if vitoria < 1:
    print('Poxa... Logo de cara?')
elif vitoria >= 1:
    print('Perdeu!')
    print(f'Você venceu {vitoria} partidas hein...')

print('** GAME OVER **')
print('-=' * 30)