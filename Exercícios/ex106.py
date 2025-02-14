# Faça um mini-sistema que utilize o interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Com cores!

def cores(cor):
    if cor == 'verde':
        return '\033[32m'
    elif cor == 'vermelho':
        return '\033[31m'
    elif cor == 'azul':
        return '\033[34m'
    elif cor == 'inverte':
        return '\033[7m'
    elif cor == 'limpa':
        return '\033[m'


def mensagem(msg):

    print(f'{cores("inverte")}')
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))
    print(f'{cores("limpa")}')


while True:
    mensagem('Sistema de ajuda PyHELP')

    print(cores('azul'))
    ajuda = str(input('Função ou Biblioteca > '))

    if ajuda == 'FIM':
        print(f'{cores("vermelho")} -=- Programa encerrado! -=-{cores("limpa")}')
        break

    print(cores('verde'))
    help(ajuda)
    print(cores('limpa'))



