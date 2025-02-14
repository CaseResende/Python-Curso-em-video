# Calcula a hipotenusa de um triângulo

# Importa a função de cálculo de hipotenusa
from math import hypot

# Recebe os dois catetos
a = float(input('Digite o cateto oposto do triângulo: '))
b = float(input('Digite o cateto adjacente do triângulo: '))

# Calcula e retorna a hipotenusa
h = hypot(a, b)
print('A hipotenusa deste triângulo mede {:.2f}.'.format(h))
