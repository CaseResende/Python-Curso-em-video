# Gera 5 números aleatórios e coloca em uma tupla
# Exibe a listagem dos números gerados e indica o menor e maior valor na tupla

# Importa o método de randomizar números inteiros
from random import randint

# Cria a lista com 5 números aleatórios de 0 a 9
numeros = tuple(randint(0, 9) for i in range(5))

# Retorna os valores gerados
print('A tupla gerada foi: ', end='')
for num in numeros:
    print(num, end=' ')
print()

# Utiliza o método max para exibir o maior valor
print(f'O maior valor é {max(numeros)}')

# Utiliza o min para exibir o menor valor
print(f'O menor valor é {min(numeros)}')
