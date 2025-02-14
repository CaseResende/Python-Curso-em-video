# Refazer o desafio 009, mostrando a tabuada de um número que o usuário escolher, utilizando o for.

num = int(input('Digite um número para ver sua tabuada: '))
print('-=' * 6)

for cont in range (1, 11):
    print('{} x {:2} = {:2}'.format(num, cont, num * cont))
print('-=' * 6)
