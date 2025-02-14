# Lê dois números e retorna a soma entre eles

# Cria uma base de cores
cores = {'limpa' : '\033[m',
        'verde' : '\033[32m',
        'vermelho' : '\033[31m',
        'azul' : '\033[34m',
        'inverte' : '\033[7m'}

# Recebe dois números e realiza a soma
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2

# Retorna os valores
print('A {}soma{} entre {}{}{} e {}{}{} vale {}{}{}'.format(cores['inverte'], cores['limpa'], cores['verde'], n1, cores['limpa'], cores['vermelho'], n2, cores['limpa'], cores['azul'], s, cores['limpa']))
