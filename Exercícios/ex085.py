# Lê 7 números e os cadastre em uma lista única que mantenha separados os valores pares dos ímpares
# Exibe os valores pares e ímpares em ordem crescente

# Inicialização da variável. [0] para pares, [1] para ímpares
numeros = [[], []]

# Estrutura de repetição para receber os valores
for cont in range(1, 8):
    num = int(input(f'Digite o {cont}º valor: '))

    # Verifica se é par ou ímpar e o insere no respectivo índice
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

# Organiza em ordem crescente
numeros[0].sort()
numeros[1].sort()

# Retorna as respostas
print('-=' * 30)
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números ímpares digitados foram: {numeros[1]}')
print('-=' * 30)
