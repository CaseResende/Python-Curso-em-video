# Lê a distância da viagem em km e calcula o valor da passagem
# Calculando 50 centavos por Km até 200 km e 45 centavos para viagens mais longas

# Recebe a distância e retorna para o usuário
d = float(input('Digite a distância a ser percorrida: '))
print('O destino selecionado fica a {}Km.'.format(d))

# Realiza os cálculos de acordo com as duas condições e retorna o valor
if d <= 200.0:
    p = d * 0.5
else:
    p = d * 0.45
print('O valor da sua passagem será R${}.'.format(p))
