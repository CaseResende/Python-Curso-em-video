# Programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# E a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

# Importação da função de sorteio e temporizador
from random import randint
from time import sleep

# Inicialização da variável
valores = list()


# Função sorteia
def sorteia():

    # Apresentação
    print(f'Sorteando 5 valores da lista: ', end='')

    # Loop para sortear os 5 números
    for cont in range(0, 5):
        sleep(0.3)
        numero = int(randint(0, 10))

        # Condições para apresentação na tela
        if cont < 4:
            print(f'{numero}', end=', ')
        else:
            print(f'{numero}', end='.')

        # Adiciona os números sorteados na lista
        valores.append(numero)
    print()


# Função somaPar
def somaPar(lista):

    # Inicialização da variável
    soma = 0

    # Apresentação
    print(f'Os valores pares são: ', end='')

    # Loop para percorrer cada valor na lista e verificar se é par
    for valor in lista:
        if valor % 2 == 0:

            # Exibe o valor par
            print(f'{valor}', end=' ')

            # Realiza a soma dos valores pares
            soma += valor
    print()
    sleep(0.5)

    # Exibição da soma
    print(f'Sua soma é {soma}.')


# Programa principal
sorteia()
sleep(0.5)
somaPar(valores)
