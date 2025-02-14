# Tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte
# Ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

# Inicialização da variável tupla
extenso = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
    'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# Recebe o valor e realiza a validação
while True:
    num = int(input('Digite um número entre 0 e 20: '))

    if num < 0 or num > 20:
        print('Opção inválida!')
    else:
        break

# Retorna o valor por extenso para o usuário
print(f'Você digitou o número {extenso[num]}')
