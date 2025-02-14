# Recebe um número e retorna seu dobro, triplo e raiz quadrada

# Recebe o número e realiza os cálculos
n1 = int(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = pow(n1, (1/2))

# Retorna os valores
print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nE a raiz quadrada de {} é igual a {:.2f}.'.format(n1, d, n1, t, n1, r))
