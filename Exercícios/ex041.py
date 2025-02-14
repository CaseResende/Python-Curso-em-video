# Recebe o ano de nascimento e retorna qual a categoria conforme a idade
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

# Importa função que recebe o ano do sistema
from datetime import date

# Calcula a idade
nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento

# Retorna a idade e a categoria
print('Você tem {} anos.'.format(idade))
print('Categoria ', end='')
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JUNIOR.')
elif idade <= 25:
    print('SÊNIOR.')
else:
    print('MASTER.')
