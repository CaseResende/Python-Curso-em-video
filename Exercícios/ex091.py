# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

# Importações de módulos
from random import randint
from time import sleep
from operator import itemgetter # Pega um item dentro do dicionário

# Inicialização das variáveis
jogo = dict()
ranking = list()

# Preenchimento de 4 chaves jogador com valores randomizados
for cont in range(1, 5):
    jogo[f'jogador {cont}'] = randint(1, 6)

# Cópia do dicionário jogo, ordenado por valor e de ordem decrescente
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Exibição das jogadas
print('JOGANDO', end="")
sleep(0.5)
for cont in range(0, 3):
    print('.', end="")
    sleep(0.5)
print()

for jogador, jogada in jogo.items():
    print(f'O {jogador.capitalize()} tirou {jogada} no dado.')
    sleep(0.5)

# Exibição da classificação
print('-=' * 30)
print()
print(f'{"=| Classificação |=":^60}')
print('-' * 60)
sleep(0.5)

for cont, valor in enumerate(ranking):
    print(f' * {cont + 1}º lugar: {valor[0].capitalize()} tirou {valor[1]}.')
    sleep(0.5)
print()
print('-=' * 30)
print(f'{"Fim do jogo!":^60}')
