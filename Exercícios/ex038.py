# Lê dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

# Recebe os valores
print('Digite dois números e irei te falar qual é o maior.')
numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))

# Realiza a comparação e retorna a resposta
if numero1 > numero2:
    print('O primeiro valor é maior.')
elif numero1 < numero2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
