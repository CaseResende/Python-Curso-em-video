# Lê a velocidade de um carro e se ultrapassar 80 km/h, multa. Valor de 7 reais por km excedido

# Recebe a velocidade
velocidade = float(input('Informe a velocidade em Km/h: '))

# Realiza as condições e retorna as respectivas respostas
if velocidade > 80.0:
    print('Calma aí Toretto! Você foi multado!')
    excedente = (velocidade - 80.0)
    valor = (excedente * 7)
    print('Você deve pagar R${:.2f}, pois excedeu em {}Km/h a velocidade permitida.'.format(valor, excedente))
print('Tenha um bom dia! Dirija com segurança.')
