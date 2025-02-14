# Verificar se uma frase é palíndromo sem uma estrutura de repetição

# ignora os espaços sobrando e joga tudo para maiúsculas
frase = str(input('Digite uma frase e irei analisar se ela é um palíndromo: ')).strip().upper()

# Separa a frase em palavras
palavras = frase.split()

# Junta as palavras sem separação
junto = ''.join(palavras)

# Inicia a variável que vai receber a frase ao contrário
inverso = ''

# Começa do início, vai até o fim, percorrendo ao contrário
inverso = junto[::-1]

print('O inverso de {} é {}.'.format(junto, inverso))

# Condições para ser um palíndromo ou não
if junto == inverso:
    print('Temos um palíndromo.')
else:
    print('Não temos um palíndromo.')
