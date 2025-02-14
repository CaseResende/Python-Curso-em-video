# Lê o ano e verifica se ele é bissexto ou não

# Importa a função de puxar a data do sistema
from datetime import date

# Recebe o ano
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))

# Condições e retornos
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
