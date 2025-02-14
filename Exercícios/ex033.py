# Recebe 3 valores e retorna qual o maior e qual o menor

# Recebe os 3 valores
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

# Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# Retorna as respostas
print('O maior número é o {}.'.format(maior))
print('O menor número é o {}.'.format(menor))
