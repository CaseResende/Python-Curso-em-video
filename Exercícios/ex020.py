# Realiza o sorteio da ordem dos alunos

# Importa a função de embaralhar
from random import shuffle

# Recebe os 4 valores
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

# Cria uma lista com os 4 valores
lista = [n1, n2, n3, n4]

# Embaralha a lista e retorna os valores na ordem embaralhada
shuffle(lista)
print('A ordem para apresentar o trabalho é: ')
print(lista)
