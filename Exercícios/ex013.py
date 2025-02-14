# Recebe o salário e realiza o aumento de 15%

# Recebe o salário
sal = float(input('Digite seu salário: '))

# Calcula e retorna o aumento
aum = sal + (sal * 0.15)
print('Seu salário era {:.2f} reais. Agora com o aumento de 15%, passou para {:.2f} reais.'.format(sal, aum))
