# Recebe 3 retas e retorna se é possível formar um triângulo
# Condição de formação: Um lado não pode ser maior que a soma dos outros dois

# Recebe as 3 retas
r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

# Faz a verificação e retorna as respostas
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Podem formar um triângulo.')
else:
    print('Não podem formar um triângulo.')
