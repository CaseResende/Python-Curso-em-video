# Recebe peso e altura, calcula o IMC e retorna seu estado

# Recebe peso, altura e calcula o IMC
peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em m? '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))

# Condições de estado
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está com o peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida!')
