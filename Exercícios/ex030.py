# Verifica se o número é par ou ímpar

# Recebe o número
num = int(input('Digite um número: '))
print('Vamos analisar se {} é par ou ímpar...'.format(num))

# Realiza o módulo do número por 2. Se restar 1, é ímpar. Senão, é par. Se o número for 0, retorna que é neutro
if num % 2 == 1:
    print('O número {} é ímpar!'.format(num))
else:
    if num == 0:
        print('0 é neutro!')
    else:
        print('O número {} é par!'.format(num))
