# Programa que tenha uma função chamada maior().
# Que receba vários parâmetros com valores inteiros.
# O programa tem que analisar todos os valores e dizer qual deles é o maior.

# Importa a função temporizadora
from time import sleep


# Função maior
def maior(*valores):
    maior = 0

    # Retorno para o usuário
    print('-' * 60)
    print('Analisando os valores passados', end='')
    for _ in range(0, 3):
        sleep(0.5)
        print('.', end='')
    print()

    # Loop que percorre toda a lista e verifica qual o maior valor
    for pos, num in enumerate(valores):
        if pos == 0 or num > maior:
            maior = num
        print(f'{num}', end=' ')
    print()

    # Retorno da quantidade de valores e o maior valor da lista
    if len(valores) < 1:
        print('Você não informou nenhum valor.')
    elif len(valores) == 1:
        print('Foi informado apenas um valor.')
    else:
        print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 4, 0, 1, 7)
maior(9, 1, 8, 7)
maior(1)
maior()
