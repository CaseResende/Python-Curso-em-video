# Lê nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da média.

# Importação do módulo temporizador
from time import sleep

# Inicialização de variáveis
pessoa = dict()
pessoas = list()
somaIdade = mediaIdade = 0

# Laço de repetição para cadastro de pessoas
while True:
    pessoa['nome'] = str(input('Nome: '))

    # Laço de repetição para receber e validar sexo
    while True:
        pessoa['sexo'] = str(input(f'Sexo de {pessoa["nome"]}: [M/F] ')).strip().upper()[0]

        if pessoa['sexo'] not in 'MF':
            print('Opção inválida!')

        else:
            break

    # Recebe a idade
    pessoa['idade'] = int(input(f'Idade de {pessoa["nome"]}: '))

    # Laço de repetição para receber e validar a continuação do cadastro
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

        if continuar not in 'SN':
            print('Opção inválida!')
        else:
            break

    # Incrementa a soma da idade
    somaIdade += pessoa['idade']

    # Insere a cópia do dicionário pessoa dentro da lista de pessoas
    pessoas.append(pessoa.copy())

    # Limpa o dicionário pessoa para a próxima execução
    pessoa.clear()

    if continuar == 'N':
        break

# Calcula a média de idade
mediaIdade = somaIdade / len(pessoas)

# Retorno de informações para o usuário
print('-=' * 30)
print('Analisando', end='')
for cont in range(0, 3):
    sleep(0.5)
    print('.', end='')
print()
sleep(1)
print('-=' * 30)

print(f' a) O grupo tem {len(pessoas)} pessoas cadastradas.')
sleep(0.5)
print(f' b) A média de idade é {mediaIdade:.1f} anos.')
sleep(0.5)
print(' c) As mulheres cadastradas foram: ', end='')
# Laço para ler cada dicionário na lista e verifica se o valor para sexo é feminino
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=', ')
print()
sleep(0.5)
print(' d) Lista de pessoas com idade acima da média:')
# Laço para percorrer todos os dicionários dentro da lista
for cadastro in pessoas:
    # Verifica se o valor para a idade é maior que a média de idade
    if cadastro['idade'] > mediaIdade:
        print('   -> ', end='')
        # Laço para coletar todas as chaves e valores do dicionário
        for chave, valor in cadastro.items():
            if chave != 'idade':
                print(f'{chave.capitalize()} = {valor}', end='; ')
            else:
                print(f'{chave.capitalize()} = {valor}.')
print('-=' * 30)
