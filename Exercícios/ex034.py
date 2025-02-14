# Lê o salário e calcula o seguinte aumento
# Para salários superiores a 1250, 10% de aumento
# Para inferiores e iguais, 15%

# Recebe o salário
sal = float(input('Informe seu salário: R$'))

# Realiza as verificações, cálculos e retorna as respostas
if sal > 1250:
    print('Seu salário de R${:.2f} sofreu um reajuste de 10%.'.format(sal))
    print('Seu novo salário é R${:.2f}.'.format(sal + (sal * 0.1)))
else:
    print('Seu salário de R${:.2f} sofreu um reajuste de 15%.'.format(sal))
    print('Seu novo salário é R${:.2f}.'.format(sal + (sal * 0.15)))
