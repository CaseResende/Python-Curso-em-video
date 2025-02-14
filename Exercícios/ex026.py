# Lê uma frase e mostra:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

# Recebe a frase e elimina os espaços no início e fim e, também, muda as letras para maiúsculas
frase = str(input('Digite uma frase: ')).strip().upper()

# Conta quantas vezes aparece a letra A com a função .count()
print('A sua frase possui {} letras "A".'.format(frase.count('A')))

# Mostra a primeira vez que encontrou a letra 'A' com a função .find()
# O +1 é para indicar corretamente qual a posição (pois sempre começa no 0)
print('A primeira letra "A" apareceu na posição {}.'.format(frase.find('A') + 1))

# Mesma coisa do anterior, porém buscando da direita para a esquerda
print('A última letra "A" apareceu na posição {}.'.format(frase.rfind('A') + 1))
