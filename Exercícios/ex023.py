# Lê um número de 0 a 9999 e retorna sua unidade, dezena, centena e milhar

# Lê o número
num = int(input('Digite um número de 0 a 9999: '))

# Separa a unidade, dezena, centena e milhar e retorna os valores
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Vamos desmembrar o {}?'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
