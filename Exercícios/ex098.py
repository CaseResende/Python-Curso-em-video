# Programa que tenha uma função chamada contador().
# Que recebe 3 parâmetros: início, fim e passo e realize a contagem.
# O programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1.
# b) De 10 até 0, de 2 em 2.
# c) Uma contagem personalizada.

# Importa a função de temporização
from time import sleep


# Função contador
# Recebe início, fim e passo
def contador(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela
    :param inicio: início da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    """

    # Verifica se o passo é igual a 0, se for, conta de 1 em 1
    if passo == 0:
        passo = 1

    # Verifica se o passo é negativo para realizar a contagem de trás pra frente
    if passo < 0:
        passo *= -1

    # Retorna a contagem para o usuário
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(0.5)

    # Verifica se o início é menor que o fim e realiza a contagem normal
    if inicio < fim:
        # Realiza a contagem
        cont = inicio
        while cont <= fim:
            sleep(0.5)
            print(cont, end=' ')
            cont += passo
        print('Fim!')

    # Se o início for maior que o fim, realiza a contagem inversa
    else:
        # Realiza a contagem
        cont = inicio
        while cont >= fim:
            sleep(0.5)
            print(cont, end=' ')
            cont -= passo
        print('Fim!')
    print('-' * 60)

# Programa principal
"""
print('a)')
contador(1, 10, 1)

print('b)')
contador(10, 0, 2)

# Recebe os valores do usuário
print('c)')
print('Agora é sua vez!')
i = int(input('Início: '))
f = int(input('Fim: '))
p= int(input('Passo: '))
contador(i, f, p)
"""
help(contador)

