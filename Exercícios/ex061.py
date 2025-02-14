# Refaça o desafio 051, lendo o primeiro termo e a razão de um PA.
# Mostrando os 10 primeiros termos da progressão usando a estrutura while

# Recebe os valores
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 0

# Realiza o cálculo dos 10 termos da PA
while cont < 10:
    print(termo, end=' ➝ ')
    termo += razao
    cont += 1
print('Fim!')
