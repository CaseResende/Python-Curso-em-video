# Lê seis números inteiros e mostra a soma apenas dos que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Inicialização das variáveis
soma = 0

# Recebe e calcula a soma de 6 números pares
for cont in range(0, 6):
    num = int(input('Digite o {}º número: '.format(cont + 1)))
    if num % 2 == 0:
        soma += num

# Retorna os valores
print('A soma de todos os números pares é {}.'.format(soma))
