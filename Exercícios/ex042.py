# Refaça o 035 dos triângulos e acrescente o recurso de mostrar que tipo de triângulo será formado
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: todos os lados diferentes

print('Me informe as 3 retas e irei dizer se podem ou não formar um triângulo.')
a = int(input('Reta 1: '))
b = int(input('Reta 2: '))
c = int(input('Reta 3: '))

if a > (b + c) or b > (a + c) or c > (a + b):
    print('As três retas NÃO podem formar um triângulo.')
else:
    print('As três retas formam um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
