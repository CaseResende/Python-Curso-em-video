# Joga JOKENPÔ contra o computador

# Importa a função randômica de sorteio de números inteiros (randint)
from random import randint

# Importa a função de temporização, atrasar um tempo
from time import sleep

# Importa emojis
import emoji

# Cria um banco de cores
cores = {'branco': '\033[7m',
        'verde': '\033[30;42m',
        'vermelho': '\033[30;41m',
        'limpa': '\033[m'}

# Define os ítens e realiza o sorteio
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

# Recebe a escolha do usuário e insere um emoji em cada escolha
print('Quem ousa me desafiar para uma partida de JOKENPO?')
print('')
print('Escolha com sabedoria:')
print(emoji.emojize('[ 0 ] Pedra :facepunch:', language='alias'))
print(emoji.emojize('[ 1 ] Papel :raised_hand:', language='alias'))
print(emoji.emojize('[ 2 ] Tesoura :v:', language='alias'))
print('')
jogador = int(input('Qual é a sua jogada? '))

# Analisa a escolha do usuário e retorna as palavras com um intervalo de 1 segundo e as jogadas
if 0 <= jogador <= 2:
    print('JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)
    print('-=' * 13)
    print('Computador jogou {}'.format(itens[computador]))
    print('Você jogou {}'.format(itens[jogador]))
    print('-=' * 13)

    # Compara as escolhas do computador e do usuário e retorna quem venceu
    if computador == 0 and jogador == 2:
        print('Você {}PERDEU{}!'.format(cores['vermelho'], cores['limpa']))
    elif computador == 0 and jogador == 1:
        print('Você {}VENCEU{}!'.format(cores['verde'], cores['limpa']))
    elif computador == 1 and jogador ==0:
        print('Você {}PERDEU{}!'.format(cores['vermelho'], cores['limpa']))
    elif computador == 1 and jogador == 2:
        print('Você {}VENCEU{}!'.format(cores['verde'], cores['limpa']))
    elif computador == 2 and jogador == 0:
        print('Você {}VENCEU{}!'.format(cores['verde'], cores['limpa']))
    elif computador == 2 and jogador == 1:
        print('Você {}PERDEU{}!'.format(cores['vermelho'], cores['limpa']))
    else:
        print('{}EMPATE!{}'.format(cores['branco'], cores['limpa']))

# Retorna que o usuário digitou um valor inválido
else:
    print('{}JOGADA INVÁLIDA!{}'.format(cores['branco'], cores['limpa']))
