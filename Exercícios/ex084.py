# Lê o nome e peso de várias pessoas e armazena em uma lista e mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

# Inicialização das variáveis
temp = list()
pessoas = list()
maiorPeso = menorPeso = 0

# Repetição para receber os valores e inserir nas listas
while True:

    # Recebe os nomes e adiciona à lista temporária
    temp.append(str(input('Nome: ')))

    # Recebe os pesos e adiciona à lista temporária
    temp.append(float(input('Peso: ')))

    # Verifica se foi o primeiro nome cadastrado e armazena seu peso nas variáveis maior e menor
    if len(pessoas) == 0:
        maiorPeso = menorPeso = temp[1]

    # Verifica qual peso é maior e menor e o armazena na respectiva variável
    else:
        if temp[1] > maiorPeso:
            maiorPeso = temp[1]
        if temp[1] < menorPeso:
            menorPeso = temp[1]

    # Copia os dados da lista temporária e envia para a lista final
    pessoas.append(temp[:])

    # Limpa a lista temporária
    temp.clear()

    # Repetição para verificar a continuação do laço
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

        if continuar not in 'SN':
            print('Opção inválida!')
        else:
            break

    if continuar == 'N':
        break

    print('-' * 60)

# Retorna as respostas
print('-=' * 30)

# Quantidade de pessoas
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')

# Retorna o maior peso e as pessoas com esse peso
print(f'O maior peso foi de {maiorPeso}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maiorPeso:
        print(f'[{pessoa[0]}] ', end='')
print()

# Retorna o menor peso e as pessoas com esse peso
print(f'O menor peso foi de {menorPeso}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menorPeso:
        print(f'[{pessoa[0]}] ', end='')
print()
print('-=' * 30)
