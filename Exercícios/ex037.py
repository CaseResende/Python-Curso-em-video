# Lê um número e retorna o mesmo número na base binária, octal e hexadecimal

# Recebe o número e a base de conversão
num = int(input('Digite um número inteiro qualquer: '))
c = int(input('Escolha a base de conversão:\n [ 1 ] - Binário \n [ 2 ] - Octal \n [ 3 ] - Hexadecimal \nEscolha: '))

# Converte para as bases ou retorna erro na escolha
# O 'bin(num)[2:]' transforma o número em binário e remove os dois primeiros dígitos da resposta
if c == 1:
    print('O número {} na base binária fica: {}'.format(num, bin(num)[2:]))
elif c == 2:
    print('O número {} na base octal fica: {}'.format(num, oct(num)[2:]))
elif c == 3:
    print('O número {} na base hexadecimal fica: {}'.format(num, hex(num)[2:]))
else:
    print('Escolha inválida!')
