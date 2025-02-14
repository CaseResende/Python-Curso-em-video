# Verifica se o número é primo ou não.

# Inicialização de variáveis
dividido = 0

# Recebe o número
num = int(input('Digite um número inteiro e iremos analisar se ele é primo: '))

# Pega o número e realiza a divisão dele pelo contador (que vai de 1 até o número)
for c in range(1, num + 1):

    # Exibe os números até o valor do número e colore de azul os divisíveis e vermelho os não divisíveis
    if num % c == 0:
        print('\033[34m', end=' ')
        dividido += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

# Retorna os valores
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, dividido))

# Se possuir apenas 2 divisíveis (1 e ele mesmo) é primo, se possuir mais, não é primo
if dividido == 2:
    print('Por isso ele é primo.')
else:
    print('Por isso ele não é primo.')
