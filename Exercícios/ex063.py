# Exibe a quantidade de termos da sequência de fibonacci que o usuário pedir

# Solicita a entrada do valor
print('Sequência de Fibonacci')
num = int(input('Quantos termos você quer mostrar? '))

# Inicialização das variáveis
termo1 = 0
termo2 = 1
cont = 3 # Começa em 3 pois já irá exibir os dois primeiros termos

# Exibe os dois primeiros termos
print('{} ➝ {}'.format(termo1, termo2), end='')

# Realiza a repetição para exibir os termos conforme o selecionado
while cont <= num:
    termo3 = termo1 + termo2
    print(' ➝ {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' ➝ FIM')
