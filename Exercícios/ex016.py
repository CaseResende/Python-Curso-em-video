# Retorna a parte inteira de um número

# Importa a função trunc, que separa apenas a parte inteira de um número
from math import trunc

# Recebe o número
num = float(input('Digite um número: '))

# Retorna apenas sua parte inteira
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
