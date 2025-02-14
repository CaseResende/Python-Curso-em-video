# Aprimore o desafio 093 para que funcione com vários jogadores.
# Incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# Programa que gerencia o aproveitamento de um jogador de futebol.
# O programa deve ter o nome do jogador e quantas partidas ele jogou.
# Depois ele vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Importação do módulo temporizador
from time import sleep

# Dicionário de cores
cores = {'limpa' : '\033[m',
        'azul' : '\033[34m',
       'vermelho' : '\033[31m'}

# Inicialização da lista
jogadores = list()

# Apresentação
print(f'{"Análise de jogador":^60}')
print('-=' * 30)

# Laço para cadastrar jogadores
while True:

    # Inicialização de variáveis dentro do laço (não precisa limpar cada variável após o uso)
    jogador = dict()
    gols = list()

    # Recebe nome e quantidade de partidas do jogador
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} disputou? '))
    print('-' * 60)

    # Laço para receber os gols por partida
    for cont in range(0, partidas):
        gols.append((int(input(f'Gols na {cont + 1}ª partida: '))))

    # Insere a lista de gols no dicionário jogador
    jogador['gols'] = gols

    # Realiza o cálculo do total de gols e adiciona ao dicionário jogador
    jogador['total'] = sum(gols)

    # Adiciona o dicionário jogador à lista de jogadores
    jogadores.append(jogador)

    print('-' * 60)

    # Recebe e valida a opção de continuação
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar not in 'SN':
            print(f'{cores["vermelho"]}Opção inválida!{cores["limpa"]}')
        else:
            break

    # Interrompe o laço de cadastro
    if continuar == 'N':
        break
    print('-' * 60)

# Apresentação
print('-=' * 30)
print('Analisando os dados', end='')
for cont in range(0, 3):
    sleep(0.5)
    print('.', end='')
print()
sleep(1)

# Tabela de informações
print()
print('-' * 60)
print(f'{"Nº":<2} | {"Jogador":<18} | {"Gols":<25} | {"Total":<5}')
print('-' * 60)

# Laço para exibir os valores de cada dicionário de jogador
for posicao, jogador in enumerate(jogadores):
    print(f'{posicao:<2} | {jogador["nome"]:<18} | {str(jogador["gols"]):<25} | {jogador["total"]:<5}')
print('-' * 60)
print()

# Laço para escolher um jogador e exibir os detalhes
while True:
    escolha = int(input('Escolha um jogador para ver suas estatísticas detalhadas: (999 para sair) '))
    if escolha == 999:
        break

    # Validação para a escolha ser referente a um jogador na lista
    elif escolha < 0 or escolha >= len(jogadores):
        print(f'{cores["vermelho"]}Opção inválida!{cores["limpa"]}')

    # Exibição dos detalhes do jogador
    else:
        print('-=' * 30)
        print(f'Análise de gols do {jogadores[escolha]["nome"]} nas {len(jogadores[escolha]["gols"])} partidas disputadas.')

        # Laço para exibir cada gol presente na lista de gols do dicionário do jogador escolhido
        for partida, gol in enumerate(jogadores[escolha]['gols']):
            sleep(0.5)
            print(f'  -> Gols na {partida + 1:>2}ª partida: {cores["azul"]}{gol}{cores["limpa"]}.')
        sleep(0.5)

        # Exibe o total de gols do jogador escolhido
        print(f'Total de {cores["azul"]}{jogadores[escolha]["total"]}{cores["limpa"]} gols')
        print('-=' * 30)

print('-=' * 30)
print(f'{"Fim da execução":^60}')

