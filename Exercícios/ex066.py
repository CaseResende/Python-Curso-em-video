# Lê números inteiros e para quando digitar 999
# Ao final exibe quantos números foram digitados e a soma entre eles

# Inicialização das variáveis
cont = soma = 0

# Estrutura de repetição infinita
while True:
    num = int(input('Digite um valor ou 999 para encerrar: '))

    # Condição para parar a repetição
    if num == 999:
        break

    # O contador e a soma devem ser realizadas após a condição de parada
    cont += 1
    soma += num

# Retorna as informações para o usuário
if cont == 0:
    print('Você finalizou sem digitar nenhum número.')
else:
    print(f'A soma dos {cont} números foi {soma}')
