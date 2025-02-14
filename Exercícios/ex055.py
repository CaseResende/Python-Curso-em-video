# Lê o peso de cinco pessoas. No final, mostra qual foi o maior e o menor peso lidos.

# Inicialização das variáveis
maior = menor = 0

print('Informe o peso de 5 pessoas e direi qual é o maior e o menor peso.')

# Realiza a coleta dos 5 pesos
for cont in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(cont)))

    # Atribui o primeiro peso como maior e menor
    if cont == 1:
        maior = peso
        menor = peso

    # Realiza as atribuições de acordo com a comparação
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

# Retorno de informações
print('O maior peso é: {}.'.format(maior))
print('O menor peso é: {}.'.format(menor))