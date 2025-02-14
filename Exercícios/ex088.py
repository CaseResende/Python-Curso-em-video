# Ajuda o jogador da mega sena a criar palpites, 6 números de 1 a 60.
# O jogador deverá informar quantos palpites ele quer e o programa irá sortear 6 numeros entre 1 e 60
# Cadastrando tudo em uma lista composta

# Importação dos métodos
from random import randint
from time import sleep

# Inicialização da lista de jogos
jogos = list()

# Exibição para o usuário
print('-=' * 30)
print(f'{"JOGOS DA MEGA SENA":^60}')
print('-=' * 30)

# Entrada de quantos jogos irá gerar
quantidade = int(input('Quantos jogos deseja gerar? '))

# Repetição para criar a quantidade de jogos que o usuário solicitou
for jogo in range(0, quantidade):

    # Inicialização das variáveis
    temporaria = list()
    cont = 0

    # Repetição para randomizar os 6 números e armazenar na lista temporária
    while True:
        num = randint(1, 60)

        # Verificação para não repetir um valor
        if num not in temporaria:

            # Adiciona o número à lista
            temporaria.append(num)

            # Adiciona um ao contador
            cont += 1

        # Finaliza a repetição quando gerar os 6 valores
        if cont >= 6:
            break

    # Classifica os valores em ordem crescente, adiciona à lista final e limpa a temporária
    temporaria.sort()
    jogos.append(temporaria[:])
    temporaria.clear()

# Retorno para o usuário
print(f'SORTEANDO {quantidade} JOGOS', end='')
for cont in range(0, 3):
    sleep(0.5)
    print('.', end='')
sleep(1)
print()


for indice, resultado in enumerate(jogos):
    print(f'Jogo {indice + 1}: {resultado}')
    sleep(0.5)

print('-' * 60)
print(f'{"BOA SORTE!":^60}')
print('-=' * 30)
