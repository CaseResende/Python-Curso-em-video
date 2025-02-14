# Lê números inteiros digitados pelo usuário e para apenas quando digitar 999
# Ao finalizar, exibe quantos números foram digitados e qual a soma entre eles (exceto o finalizador)

# Importação do módulo temporizador
from time import sleep

# Inicialização das variáveis
num = cont = soma = 0

# Inicia a repetição para coleta, contagem e soma dos números
while num != 999:
    num = int(input('Digite um número inteiro qualquer ou 999 para finalizar: '))

    # Condição para não contar o flag
    if num != 999:
        soma += num
        cont += 1

# Retorna o cálculo somente se não parar o programa na primeira execução
if cont != 0:
    print('Calculando', end='')
    for c in range(0, 3):
        sleep(0.5)
        print('.', end='')
    print('')

# Retorna respostas ao usuário de quantos números e soma
if cont > 1:
    print('Você digitou {} números.'.format(cont))
elif cont == 1:
    print('Você digitou {} número.'.format(cont))

if cont >= 1:
    print('A soma entre os números é {}.'.format(soma))
else:
    print('Você finalizou sem digitar nenhum número válido.')
