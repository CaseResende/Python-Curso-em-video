# Realiza um sorteio entre quatro alunos

# Importa a função de escolha
from random import choice

# Recebe os 4 valores
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

# Cria uma lista com os 4 valores
lista = [n1, n2, n3, n4]

# Realiza a escolha e retorna o resultado
r = choice(lista)
print('O aluno a limpar o quadro é {}'. format(r))
