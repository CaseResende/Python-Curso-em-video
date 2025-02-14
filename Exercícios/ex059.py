# Lê dois números e exibe um menu na tela e executa o que o ítem sugere
# 1 - Somar
# 2 - Multiplicar
# 3 - Maior
# 4 - Novos números
# 5 - Sair

# Cria um banco de cores
cores = {'branco': '\033[7m',
         'verde': '\033[30;42m',
         'vermelho': '\033[30;41m',
         'limpa': '\033[m'}

# Inicialização de variáveis
escolha = 0

# Boas vindas e leitura dos números
print('Olá! Sou o {}Math Machine{}. Estou aqui para te ajudar com problemas matemáticos.'.format(cores['vermelho'], cores['limpa']))
print('Para começar, digite dois números.')
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

# Início da estrutura de repetição com encerramento quando a escolha for 5
while escolha != 5:

    # Condição especial de novos números caso a escolha seja 4
    if escolha == 4:
        print('Você optou por escolher novos números.')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))

    # Menu para selecionar as escolhas
    print('')
    print('{}                           {}'.format(cores['branco'], cores['limpa']))
    print('*********** MENU **********'.format(cores['limpa']))
    print('[1] → Soma')
    print('[2] → Multiplicação')
    print('[3] → Maior')
    print('[4] → Novos números')
    print('[5] → Sair')
    escolha = int(input('Digite sua escolha: '))
    print('')

    # Respostas para cada escolha
    if escolha == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    if escolha == 2:
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
    if escolha == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num2 > num1:
            print('{} é maior que {}'.format(num2, num1))
        else:
            print('{} e {} são iguais'.format(num1, num2))

    # Condição para manter o usuário entre as escolhas do menu
    if escolha < 1 or escolha > 5:
        print('Essa escolha não existe!')

# Mensagem final de encerramento
print('Programa finalizado pelo usuário.')
