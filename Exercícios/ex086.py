# Cria uma matriz 3x3 e a preencha com valores lidos pelo teclado
# Ao final, mostre a matriz na tela com a formatação correta

# Inicialização da variável composta
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Repetição para alimentar a matriz, 3 linhas e 3 colunas
for linha in range(0, 3):
    for coluna in range(0, 3):

        # Inserção dos dados na matriz em suas respectivas posições
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

# Retorno das respostas
print('-=' * 30)

# Repetição para exibir a matriz organizada
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print()
