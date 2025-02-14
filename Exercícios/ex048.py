# Este programa calcula a soma entre todos os números ímpares múltiplos de 3 no intervalo de 1 a 500

# Inicialização de variáveis
soma = 0
contador = 0

print('')
print('Este programa calcula a soma entre todos os números ímpares múltiplos de 3 no intervalo de 1 a 500.')
print('')

# Contador de 1 a 500 pulando de 2 em 2.
# Pega somente os múltiplos de 3 e realiza a contagem
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        soma += cont
        contador += 1

# Retorna as informações
print('A soma de todos os {} valores solicitados é {}.'.format(contador, soma))
