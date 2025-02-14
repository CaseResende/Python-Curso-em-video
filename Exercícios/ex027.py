# Lê o nome completo e retorna o primeiro e o último nome separadamente

# Recebe o nome eliminando os espaços inúteis
nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')

# Divide o nome com base nos espaços
div = nome.split()

# Retorna o primeiro nome indicando o primeiro bloco
print('Seu primeiro nome é {}.'.format(div[0]))

# Retorna o último bloco indicando qual o total de blocos resultantes do split -1 (pois começa no 0)
print('Seu último nome é {}.'.format(div[len(div) - 1]))
