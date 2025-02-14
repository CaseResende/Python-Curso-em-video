# Mostra na tela uma contagem regressiva para o estouro de fogos de artifício.
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# Importa a função de temporizar
from time import sleep

# Indicação da contagem
print('-=-' * 7)
print('Contagem para 2025:')
print('-=-' * 7)

# Contagem regressiva com temporização de 1s entre os contadores
sleep(1)
for cont in range (10, -1, -1):
    print(cont)
    sleep(1)

# Explosão
print('*' * 10)
print(' BOOOM!!!')
print('*' * 10)
