# Lê quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9;
# b) Em que posição foi digitado o primeiro valor 3;
# c) Quais foram os números pares.

# Recebe os valores dentro de uma tupla através de uma estrutura de repetição
numeros = tuple(int(input(f'Digite o {i + 1}° número: ')) for i in range(0, 4))

# Inicialização de variáveis
contPar = 0

# Exibe os números digitados
print('Você digitou os números: ', end='')
for pos, num in enumerate(numeros):
    if pos == 3:
        print(f'{num}.')
    else:
        print(f'{num}', end=', ')

# Verificação de quantas vezes o 9 foi digitado
if numeros.count(9) > 0:
    print(f'O número 9 apareceu {numeros.count(9)} vezes.')
else:
    print('O número 9 não foi digitado.')

# Verificação em qual posição o 3 foi digitado pela primeira vez
if numeros.count(3) > 0:
    print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')

# Conta quantos números pares foram digitados
for numero in numeros:
    if numero % 2 == 0:
        contPar += 1

# Retorna quais foram os números pares, se foi mais de um
if contPar > 1:
    print(f'Os números pares são:', end='')
    for numero in numeros:
        if numero % 2 == 0:
            print(f' {numero}', end='')
    print('.')

# Retorna qual foi o número par, se foi apenas um
elif contPar > 0:
    for numero in numeros:
        if numero % 2 == 0:
            print(f'O único número par é o {numero}.')

# Retorna que não foi digitado número par
else:
    print('Você não digitou número par.')
