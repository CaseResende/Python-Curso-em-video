# Mostra a tabuada de vários números, um de cada vez, para cada valor digitado
# O programa será interrompido quando o número solicitado for negativo

# Estrutura de repetição infinita
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 60)

    # Condição para parar quando o número for negativo
    if num < 0:
        break

    # Conta até 10 realizando o cálculo do numero vezes o contador
    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num * cont}')

    print('-' * 60)

print('Programa finalizado pelo usuário.')
