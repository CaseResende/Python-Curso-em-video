# Lê o nome completo da pessoa e retorna:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras tem sem considerar os espaços
# Quantas letras tem o primeiro nome

# Recebe o nome e utiliza o strip para remover os espaços que sobram antes e depois
nome = input('Digite seu nome completo: ').strip()

# Retorna o nome
print('Olá, {}'.format(nome))

# Converte e retorna o nome com letras maiúsculas (upper converte para todas maiúsculas)
print('Aqui está o seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))

# Converte e retorna o nome com letras minúsculas (lower converte para todas minúsculas)
print('Aqui está o seu nome com todas as letras minúsculas: {}'.format(nome.lower()))

# Conta os caracteres com o len(nome) e subtrai os espaços com o - nome.count(' ')
print('O seu nome possui {} letras, sem considerar os espaços.'.format(len(nome) - nome.count(' ')))

# Utiliza o split para dividir o nome com base nos espaços e calcula o len da primeira divisão
dividido = nome.split()
print('O seu primeiro nome {}, possui {} letras.'.format(dividido[0], len(dividido[0])))
