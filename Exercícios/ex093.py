# Programa que gerencia o aproveitamento de um jogador de futebol.
# O programa deve ler o nome do jogador e quantas partidas ele jogou.
# Depois ele vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Importação do módulo para temporização
from time import sleep

# Dicionário de cores
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m'}

# Inicialização de variáveis
jogador = dict()
gols = list()

# Apresentação
print(f'{"Análise de jogador":^60}')
print('-=' * 30)

# Recebe os dados do usuário
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} disputou? '))
print('-' * 60)

# Laço de repetição para receber os gols por partida e inserir na lista de gols
for cont in range(0, jogador['partidas']):
    gols.append((int(input(f'Gols na {cont + 1}ª partida: '))))

# Insere a cópia da lista de gols no dicionário
jogador['gols'] = gols.copy()

# Realiza o somatório dos gols
jogador['total'] = sum(gols)

# Retorno de informações
print('-=' * 30)
print('Analisando os dados', end='')
for cont in range(0, 3):
    sleep(0.5)
    print('.', end='')
print()
sleep(1)

# Laço para exibir as chaves e valores do dicionário
print('-' * 60)
for chave, valor in jogador.items():
    print(f'O campo {cores["vermelho"]}{chave}{cores["limpa"]} tem o valor {cores["vermelho"]}{valor}{cores["limpa"]}.')
print('-' * 60)

# Retorno de estatísticas detalhadas de gols por jogo
print(f'Análise de gols do {jogador["nome"]} nas {jogador["partidas"]} partidas disputadas.')

# Laço para exibir a quantidade de gols em cada partida
for partida, gol in enumerate(jogador['gols']):
    print(f'  -> Gols na {partida + 1:>2}ª partida: {cores["azul"]}{gol}{cores["limpa"]}.')

print(f'Total de {cores["azul"]}{jogador["total"]}{cores["limpa"]} gols')
print('-=' * 30)

print(f'{"Fim da execução":^60}')