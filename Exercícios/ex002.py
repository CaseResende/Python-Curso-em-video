# Lê o nome da pessoa e mostra uma mensagem de boas-vindas

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, \033[4;34m{}\033[m!'.format(nome))
