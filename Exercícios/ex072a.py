# Tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte
# Ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
# Perguntar se o usuário quer continuar ou não

# Inicialização da variável tupla
extenso = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
    'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# Inicia a repetição e encerra quando o usuário responder que não deseja continuar
while True:

    # Recebe o valor e realiza a validação
    while True:
        num = int(input('Digite um número entre 0 e 20: '))

        if num < 0 or num > 20:
            print('Opção inválida!')
        else:
            break

    # Retorna o valor por extenso para o usuário
    print(f'Você digitou o número {extenso[num]}')

    # Recebe a resposta de continuidade e realiza a validação
    while True:
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]

        if continuar not in 'SN':
            print('Opção inválida!')

        else:
            break

    # Encerra quando a resposta for Não
    if continuar == 'N':
        break

# Saudações finais
print('Obrigado e volte sempre!')
