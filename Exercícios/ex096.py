# Faça um programa que tenha uma função chamada área().
# Que receba as dimensões de um terreno retangular (largura e comprimento),
# E mostre a área do terreno

# Função area
# Recebe dois valores e retorna o seu produto
def area(larg, comp):
    print('-' * 60)
    print(f'O terreno tem largura de {larg}m e comprimento de {comp}m.')
    print(f'Sua área é de {larg * comp}m².')


# Programa principal
print('Cálculo de área')
print('-' * 60)

# Recebe os valores
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

# Chama a função com seus argumentos
area(largura, comprimento)
