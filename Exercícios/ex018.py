# Lê um ânguo e retorna seu seno, cosseno e tangente

# Importa as funções seno, cosseno, tangente e radiano (para converter para graus)
from math import sin, cos, tan, radians

# Recebe o ângulo
a = float(input('Digite o ângulo desejado: '))

# Calcula as variáveis e retorna os valores
ar = radians(a)
s = sin(ar)
c = cos(ar)
t = tan(ar)
print('O ângulo de {}º possui:\n * Seno {:.2f},\n * Cosseno {:.2f}, \n * Tangente {:.2f}.'. format(a, s, c, t))
