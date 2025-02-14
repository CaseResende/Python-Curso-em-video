# Lê a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário deseja continuar.
# No final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

# Importação de módulo temporizador
from time import sleep

# Inicialização de variáveis
maior = homem = mulher = 0

# Estrutura de repetição de cadastro
while True:
    # Apresentação
    print('-' * 60)
    print('Cadastre uma pessoa')
    print('-' * 60)

    # Recebe a idade
    idade = int(input('Idade: '))

    # Recebe e valida o sexo
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

        if sexo not in 'MF':
            print('Sexo inválido!')
        else:
            break

    print('-' * 60)

    # Verifica e conta se o cadastrado tem mais de 18 anos
    if idade >= 18:
        maior += 1

    # Verfica e conta se o cadastrado é homem
    if sexo == 'M':
        homem += 1

    else:
        # Verifica e conta se o cadastrado não é homem e tem menos de 20 anos
        if idade < 20:
            mulher += 1

    # Recebe e valida a opção de continuar
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if continuar not in 'SN':
            print('Escolha inválida!')
        else:
            break

    # Interrompe o fluxo de cadastro
    if continuar == 'N':
        break

# Temporizador
sleep(0.5)
print('Pensando', end='')
for cont in range(0, 3):
    sleep(0.5)
    print('.', end='')
sleep(0.5)
print()

# Retorna as respostas personalizadas
print('-=' * 30)

if maior == 1:
    print(f'Ao todo, você cadastrou apenas uma pessoa com mais de 18 anos.')
elif maior > 1:
    print(f'Ao todo, você cadastrou {maior} pessoas com mais de 18 anos.')
else:
    print('Nenhuma pessoa com mais de 18 anos cadastrada.')

if homem == 1:
    print(f'Temos apenas {homem} homem cadastrado.')
elif homem > 1:
    print(f'Temos {homem} homens cadastrados.')
else:
    print('Nenhum homem cadastrado.')

if mulher == 1:
    print(f'E temos apenas {mulher} mulher com menos de 20 anos.')
elif mulher > 1:
    print(f'E temos {mulher} mulheres com menos de 20 anos.')
else:
    print('Nenhhuma mulher com menos de 20 anos cadastrada.')
