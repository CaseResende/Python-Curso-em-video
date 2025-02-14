# Analisa sua quantia em reais e mostra quantos dólares pode comprar

# Recebe o valor em real
rs = float(input('Quanto dinheiro você tem na sua carteira? R$'))

# Calcula quantos dólares vale um real
us = rs / 3.27

# Retorna os valores
print('Você possui R${:.2f} e pode comprar US${:.2f}.'.format(rs, us))
