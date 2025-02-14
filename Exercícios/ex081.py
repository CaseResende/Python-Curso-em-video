# Lê vários números e coloca em uma lista, depois disso mostre:
# Quantos números foram digitados
# A lista de valores ordenada de forma decrescente
# Se o valor 5 foi digitado e está ou não na lista

# Inicialização das variáveis
numeros = list()

# Estrutura de repetição para a entrada dos valores
while True:

    # Realiza a leitura dos números já adicionado ao final da lista
    numeros.append(int(input('Digite um valor: ')))

    # Repetição para continuar entrando com os valores com validação
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

        if continuar not in 'SN':
            print('Opção inválida!')

        else:
            break

    # Interrompe o laço caso a resposta seja N
    if continuar == 'N':
        break

# Retorna as respostas
print('-=' * 30)

# Quantos valores foram digitados
print(f'Você digitou {len(numeros)} elementos.')

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são:')
print(f'{numeros}')

# Verifica se o valor 5 faz parte da lista
if numeros.count(5):
    print(f'Encontramos o número 5 nas posições: ', end='')
    for posicao, numero in enumerate(numeros):
        if numero == 5:
            print(f'{posicao},', end=' ')
else:
    print('Você não digitou o número 5!')
