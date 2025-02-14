# Verificar se uma frase é palíndromo

# ignora os espaços sobrando e joga tudo para maiúsculas
frase = str(input('Digite uma frase e irei analisar se ela é um palíndromo: ')).strip().upper()

# Separa a frase em palavras
palavras = frase.split()

# Junta as palavras sem separação
junto = ''.join(palavras)

# Inicia a variável que vai receber a frase ao contrário
inverso = ''

# Pega a última letra (len(junto) -1), até a primeira (-1), voltando de 1 em 1
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}.'.format(junto, inverso))

# Condições para ser um palíndromo ou não
if junto == inverso:
    print('Temos um palíndromo.')
else:
    print('Não temos um palíndromo.')
