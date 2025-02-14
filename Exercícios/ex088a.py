# Ajuda o jogador da mega sena a criar palpites, 6 números de 1 a 60.
# O jogador deverá informar quantos palpites ele quer e o programa irá sortear 6 numeros entre 1 e 60
# Cadastrando tudo em uma lista composta

# Importação dos métodos
from random import sample
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
for cont in range(quantidade):

    # sorted() já ordena os números gerados em ordem crescente e o retorna em uma nova lista
    # sample() seleciona os elementos de 1 a 60 em 6 unidades sem os repetir
    jogo = sorted(sample(range(1, 61), 6))
    jogos.append(jogo)

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

print('BOA SORTE!')
