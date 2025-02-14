# Lê vários numeros e coloca em uma lista.
# Crie duas listas extras que vão conter apenas os valores pares e ímpares respectivamente.
# Ao final, mostre o conteúdo das 3 listas geradas

# Inicialização das variáveis
numeros = list()
pares = list()
impares = list()

# Laço de repetição para cadastro dos números
while True:

    # Recebe e adiciona os números
    numeros.append(int(input('Digite um número: ')))

    # Laço de repetição para validar continuação
    while True:
        continuar = str(input('Continuar: [S/N] ')).strip().upper()[0]

        if continuar not in 'SN':
            print('Opção inválida!')
        else:
            break

    # Interrompe o laço de cadastro dos números
    if continuar == 'N':
        break

# Verifica se o número é ímpar ou par e o adiciona o número em sua respectiva lista
for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# Organiza as listas em ordem crescente
numeros.sort()
pares.sort()
impares.sort()

# Retorna as respostas formatadas
print('-=' * 30)

print(f'A lista completa é: {numeros}.')

if len(pares) > 0:
    print(f'A lista dos pares é: {pares}.')
else:
    print('Você não digitou número par!')

if len(impares) > 0:
    print(f'A lista dos ímpares é: {impares}.')
else:
    print('Você não digitou número ímpar!')

print('-=' * 30)
