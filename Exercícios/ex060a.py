# Lê um número qualquer e mostre seu fatorial
# Ex: 5! = 5x4x3x2x1 = 120

# Recebe o número
num = int(input('Número: '))

# Inicialização das variáveis
fat = 1

# Retorna resposta ao usuário
print('Calculando {}! = '.format(num), end='')

# Inicia a repetição para subtrair 1 ao número e calcular o fatorial
while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    fat *= num
    num -= 1
print('{}'.format(fat))
