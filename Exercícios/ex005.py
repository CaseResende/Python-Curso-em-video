# Recebe um número e mostra seu antecessor e seu sucessor

# Recebe o valor
n1 = int(input('Digite um número: '))

# Calcula seu antecessor e seu sucessor
ant = n1 - 1
suc = n1 + 1

# Retorna as informações
print('O número digitado foi {}, seu antecessor é {} e seu sucessor é {}'.format(n1, ant, suc))
