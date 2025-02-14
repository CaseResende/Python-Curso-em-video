# Cria uma matriz 3x3 e a preencha com valores lidos pelo teclado
# # Ao final, mostre a matriz na tela com a formatação correta
# Exibe a soma de todos os valores pares digitados
# A soma dos valores da terceira coluna
# O maior valor da segunda linha

# Inicialização da variável composta
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceira = maiorSegunda = cont = 0

# Repetição para alimentar a matriz, 3 linhas e 3 colunas
for linha in range(0, 3):
    for coluna in range(0, 3):

        # Inserção dos dados na matriz em suas respectivas posições
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

        # Condição para somar os números pares
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]

        # Condição para somar os valores da terceira coluna
        if coluna == 2:
            somaTerceira += matriz[linha][coluna]

        # Condição para verificar o maior valor da segunda linha
        if linha == 1:

            # Se for o primeiro valor ou maior que o maior valor, o atribui como maior
            if cont == 0 or matriz[linha][coluna] > maiorSegunda:
                maiorSegunda = matriz[linha][coluna]

        # Adiciona o contador para a segunda linha
        cont += 1

# Retorno das respostas
print('-=' * 30)
print(f'{"MATRIZ":^22}')

# Repetição para ler os valores da matriz (linha x coluna)
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print()

# Retorna os resultados
print()
print('-' * 60)
print(f'A soma dos valores pares é igual a {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerceira}.')
print(f'O maior valor da segunda linha é {maiorSegunda}.')
print('-=' * 30)
