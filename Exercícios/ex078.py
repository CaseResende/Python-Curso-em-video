# Lê 5 números e os armazena em uma lista
# Ao final, mostra qual o maior e o menor e suas posições na lista

# Inicialização das variáveis
numeros = list()
maior = menor = 0

# Estrutura de repetição para adicionar os 5 elementos à lista
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {cont}: ')))

    # Atribui ao primeiro valor, os atributos de maior e menor
    if cont == 0:
        maior = menor = numeros[cont]

    # Verifica o maior valor
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]

        # Verifica o menor valor
        if numeros[cont] < menor:
            menor = numeros[cont]

# Retorna as respostas
print('-=' * 30)

# Retorna os valores digitados
print('Você digitou os valores: ', end='')
for posicao, numero in enumerate(numeros):
    if posicao != 4:
        print(f'{numero}', end=', ')
    else:
        print(f'{numero}', end='.')
print()

# Indica o maior valor e as posições em que foi digitado
print(f'O maior valor digitado foi {maior} nas posições', end='')
for posicao, valor in enumerate(numeros):
    if valor == maior:
        print(f' {posicao}...', end='')
print()

# Indica o menor valor e as posições em que foi digitado
print(f'O menor valor digitado foi {menor} nas posições', end='')
for posicao, valor in enumerate(numeros):
    if valor == menor:
        print(f' {posicao}...', end='')
print()

print('-=' * 30)