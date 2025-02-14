# Lê o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$1000.
# c) Qual é o nome do produto mais barato.

# Importação o módulo temporizador
from time import sleep

# Inicialização de variáveis
total = produtoMil = cont = precoBarato = 0
produtoBarato = ''

# Apresentação
print('-=' * 30)
print('{:^60}'.format('LOJÃO'))
print('=-' * 30)

# Estrutura de repetição para cadastro
while True:

    # Recebe o nome do produto e seu preço
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))

    # Acrescenta o contador
    cont += 1

    # Somatório de preço
    total += preco

    # Contabilização de produtos acima de 1000
    if preco > 1000:
        produtoMil += 1

    # Registra qual foi o menor preço e o nome do produto
    if cont == 1 or preco < precoBarato:
        precoBarato = preco
        produtoBarato = produto

    # Recebe e valida a continuidade do cadastro
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

        if continuar not in 'SN':
            print('Opção inválida!')
        else:
            break

    # Interrupção do fluxo do cadastro
    if continuar == 'N':
        break
    print('-' * 60)

# Retorno de informações
print('=-' * 30)

print('FINALIZANDO', end='')
for c in range(0, 3):
    sleep(0.5)
    print('.', end='')
print('')
sleep(0.5)

print('-=' * 30)

print(f'O total da compra foi de R${total:.2f}.')

if produtoMil == 1:
    print('Apenas um produto custando mais de R$1000.00.')
elif produtoMil > 1:
    print(f'Temos {produtoMil} produtos custando mais de R$1000.00.')
else:
    print('Nenhum produto custou mais de R$1000.00.')

print(f'O produto mais barato foi {produtoBarato}, custando R${precoBarato:.2f}.')
