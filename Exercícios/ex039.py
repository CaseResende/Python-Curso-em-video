# Lê o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Importa o módulo para ler o ano atual
from datetime import date

# Recebe o ano de nascimento
print('Informe seu ano de nascimento e eu irei te falar sobre seu alistamento militar.')
nascimento = int(input('Ano de nascimento: '))

# Calcula a idade
idade = date.today().year - nascimento

# Retorna as informações de acordo com a idade
print('Você tem {} anos.'.format(idade))
if idade == 18:
    print('Está na hora de se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você deveria ter se alistado há {} anos, em {}!'.format(idade - 18, 18 + nascimento))
else:
    print('Você deve se alistar em {} anos, em {}'.format(18 - idade, 18 + nascimento))
