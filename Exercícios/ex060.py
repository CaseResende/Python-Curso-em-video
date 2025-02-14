# Lê um número qualquer e mostre seu fatorial
# Ex: 5! = 5x4x3x2x1 = 120

# Importa a função fatorial da biblioteca math
from math import factorial

# Recebe o número e calcula seu fatorial
num = int(input('Numero: '))
fat = factorial(num)

# Inicialização da variável contador
cont = num - 1

# Exibe o número para iniciar a sequência
print(num, end='')

# Repetição para exibir todos os números do valor de entrada até 1
while 0 < cont < num:
    print(' x {}'.format(cont), end='')
    cont -= 1

# Retorna o valor do fatorial
print(' = {}'.format(fat))
