# Receba vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Cria um banco de cores
cores = {'azul': '\033[34m',
        'vermelho': '\033[31m',
        'limpa': '\033[m'}

# Inicialização da lista
numeros = list()

# Repetição para realizar o cadastro
while True:

    # Realiza a leitura do número a se cadastrar
    num = int(input('Digite um número: '))

    print('-' * 60)

    # Verifica se o número está ou não na lista
    # Se não estiver, o adiciona e informa ao usuário. Se estiver, não adiciona e pede outro valor
    if num not in numeros:
        numeros.append(num)
        print(f'{cores["azul"]}O valor {num} foi adicionado à lista.{cores["limpa"]}')
    else:
        print(f'{cores["vermelho"]}O valor {num} já existe, não vou adicionar...{cores["limpa"]}')

    print('-' * 60)
    # Questiona se deseja continuar cadastrando
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

        if continuar not in 'SN':
            print('Opção inválida!')
        else:
            break

    if continuar == 'N':
        break

# Classifica os valores por ordem crescente
numeros.sort()

# Retorna os números ordenados e formatados
print('-=' * 30)

print('Você digitou os números: ', end='')
for posicao, numero in enumerate(numeros):
    if posicao != (len(numeros) - 1):
        print(f'{numero}', end=', ')
    else:
        print(f'{numero}', end='.')
print()
print('-=' * 30)

