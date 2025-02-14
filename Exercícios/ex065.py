# Lê vários números inteiros.
# Ao final da execução, exibe a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele deseja ou não continuar a digitar valores.

# Importa o módulo temporizador
from time import sleep

# Inicialização das variáveis
cont = soma = media = maior = menor = 0
escolha = ''

# Inicia a repetição e leitura dos números
while escolha != 'n':
    num = int(input('Digite um número: '))

    # Adiciona um ao contador, calcula a soma
    cont += 1
    soma += num

    # Atribui ao maior e menor o primeiro número
    if cont == 1:
        maior = menor = num

    # Faz as atribuições de maior e menor conforme os números
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    # Pergunta se o usuário deseja continuar a repetição
    escolha = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

    # Realiza uma validação de entrada de valor na respostas
    while escolha not in 'sn':
        escolha = str(input('Escolha inválida! Digite novamente [S/N] ')).strip().lower()[0]

# Calcula a média
media = soma / cont

# Retorna as respostas ao usuário
print('Calculando', end='')
for c in range (0, 3):
    sleep(0.5)
    print('.', end='')
print('')

if cont == 1:
    print('Você digitou apenas 1 valor, portanto {} é o maior e menor valor.'.format(num))
else:
    print('A média entre os números é de {:.2f}.'.format(media))
    print('{} é o maior valor.'.format(maior))
    print('{} é o menor valor.'.format(menor))
