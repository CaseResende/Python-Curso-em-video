# Lê o ano de nascimento de 7 pessoas.
# No final, mostra quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considerar 21 anos.

# Importação do módulo para puxar o ano atual
from datetime import date

# Inicialização de variáveis
maior = menor = 0

print('Informe o ano de nascimento das 7 pessoas e eu irei dizer quantas atingiram a maioridade.')

# Coleta dos 7 anos de nascimento
for cont in range(1, 8):
    nascimento = int(input(f'Ano de nascimento da {cont}ª pessoa: '))

    # Realiza a verificação se a idade é maior ou igual a 21 anos e adiciona ao contador maior
    if date.today().year - nascimento >= 21:
        maior += 1
    else:
        menor += 1

# Retorna a resposta ao usuário com condições para exibição
if maior == 1:
    print('Tem uma pessoa maior.')
elif maior > 1:
    print('Ao todo, tivemos {} pessoas maiores.'.format(maior))

if menor == 1:
    print('Tem uma pessoa menor.')
elif menor > 1:
    print('Ao todo, tivemos {} pessoas menores.'.format(menor))