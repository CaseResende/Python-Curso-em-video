# Faz o computador pensar em um número inteiro entre 0 e 5 e pede para o usuário descobrir qual o número

# Importa as funções de sorteio e de temporizar
from random import randint
from time import sleep

# Recebe o número
print('Estou pensando em um número de 0 a 5, consegue adivinhar qual é?')
num = int(input('Em qual número estou pensando? '))
print('Processando...')

# Temporiza e sorteia o número
sleep(1)
sorteado = randint(0, 5)

# Retorna qual número o usuário escolheu
print('{}?'.format(num))
sleep(0.5)

# Retorna a resposta
if num == sorteado:
    print('Você venceu! Não é possível!!')
else:
    print('Você perdeu! Hahahaha')
    print('Eu pensei no número {} e não no {}.'.format(sorteado, num))
