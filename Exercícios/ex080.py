# Lê 5 valores e cadastra em uma lista e exibe já a sua posição na lista
# No final mostra a lista ordenada na tela
# Não pode usar o sort()

# Inicialização da variável
numeros = list()

# Estrutura para entrada dos 5 valores
for cont in range(0, 5):
    num = int(input('Digite um valor: '))

    # Condição para verificar se é o primeiro número ou maior que o último número e o adicionar ao final da lista
    if cont == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista...')

    # Caso o número não seja o primeiro ou maior que o último, verifica sua posição
    else:

        # Inicialização da variável
        # (Deve ser feita dentro do for para zerar sempre que um novo número for adicionado)
        posicao = 0

        # Enquanto a posição for inferior à quantidade da lista
        while posicao < len(numeros):

            # Verifica se o número é menor ou igual ao número que está naquela posição
            if num <= numeros[posicao]:

                # Insere naquela posição o número lido
                numeros.insert(posicao, num)
                print(f'Adicionado na posição {posicao} da lista...')

                # Finaliza a repetição
                break

            # Pula para a próxima posição
            posicao += 1

# Exibe os resultados
print('-=' * 30)
print(f'Os valores digitados em ordem foram {numeros}')
print('-=' * 30)
