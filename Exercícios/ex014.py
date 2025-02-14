# Recebe a temperatura em C e retora em F

# Recebe a temperatura em C
c = float(input('Informe a temperatura em ºC: '))

# Calcula e retorna a temperatura em F
f = ((9 * c) / 5) + 32
print('A temperatura {}ºC corresponde a {}ºF.'.format(c, f))
