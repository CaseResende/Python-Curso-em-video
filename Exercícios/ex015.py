# Calcula o valor a pagar no aluguel de um carro de acordo com os dias alugados e km rodados
# Carro custa 60 reais por dia e 15 centavos por km rodado

# Recebe os dias e os km
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

# Calcula e retorna o valor a pagar
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}.'.format(pago))
