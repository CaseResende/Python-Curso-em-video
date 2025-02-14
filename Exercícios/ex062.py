# Realiza a PA de 10 termos de um número
# Pregunta ao usuário se quer continuar exibindo mais termos
# Só encerra quando o usuário digitar 0

# Inicialização das variáveis
cont = total = 0
mais = 10

# Recebe os valores
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro

# Repetição do cálculo até o usuário selecionar 0
while mais != 0:
    total += mais
# Realiza o cálculo dos 10 primeiros termos da PA e da quantidade desejada pelo usuário
    while cont < total:
        print(termo, end=' ➝ ')
        termo += razao
        cont += 1
    print('Fim!')
    mais = int(input('Quer que eu calcule quantos termos a mais? '))
print('Progressão finalizada com {} termos calculados.'.format(total))
