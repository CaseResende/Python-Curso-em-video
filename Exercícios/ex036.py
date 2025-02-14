# Programa que irá aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Importa módulo de temporização
from time import sleep

# Cria um banco de cores
cores = {'verde': '\033[30;42m',
        'vermelho': '\033[30;41m',
        'limpa': '\033[m'}

# Recebe os valores
print('Olá! Por favor, me informe o valor da casa, o seu salário e em quantos anos deseja pagar o seu empréstimo.')
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Com quantos anos deseja pagar? '))

# Converte anos em meses
meses = anos * 12

# Calcula o valor da prestação
prestacao = casa / meses

# Simulação de computador calculando
print('Calculando.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('')

# Realiza a condição e retorna as respostas
if prestacao <= salario * 0.3:
    print('Empréstimo {}APROVADO!{}'.format(cores['verde'], cores['limpa']))
    print('Você irá pagar {} prestações de R${:.2f} para quitar sua casa de R${:.2f}.'.format(meses, prestacao, casa))
else:
    print('Empréstimo {}NEGADO!{}'.format(cores['vermelho'], cores['limpa']))
    print('Você teria que pagar {} prestações de R${:.2f}, ultrapassando 30% do seu salário de R${:.2f}.'.format(meses, prestacao, salario))
