# Lê nome, idade e sexo de 4 pessoas.
# No final, mostre:
# a) A média de idade do grupo
# b) O nome do homem mais velho.
# c) Quantas mulheres têm menos de 20 anos.

# Inicialização de variáveis
media = soma = idadeVelho = mulherMenor = 0
nomeVelho = ''

# Realiza a coleta dos dados
for cont in range (0, 4):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(cont + 1))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(cont + 1)))
    sexo = str(input('Digite o sexo da {}ª pessoa: [M/F] '.format(cont + 1))).strip().upper()

    # Atribuição da soma de idade
    soma += idade

    # Testes para a atribuição da idade e nome do homem mais velho
    if sexo == 'M':

        # Atribui a idade e nome assim que o primeiro nome for lido
        if cont == 0:
            idadeVelho = idade
            nomeVelho = nome

        # Realiza a comparação e atribuição se o homem for mais velho
        if idade > idadeVelho:
            idadeVelho = idade
            nomeVelho = nome

    # Testes e atribuição de mulher menor de 20 anos
    if sexo == 'F' and idade < 20:
        mulherMenor += 1

# Realiza o cálculo da média de idade
media = soma / 4

# Retorna as respostas com condições
print('=-' * 20)

print('A média de idade do grupo é de {:.2f} anos.'.format(media))

if len(nomeVelho) >= 1:
    print('O homem mais velho é {}, com {} anos.'.format(nomeVelho, idadeVelho))

if mulherMenor == 0:
    print('Nenhuma mulher menor de 20 anos.')
elif mulherMenor == 1:
    print('Uma mulher menor de 20 anos.')
else:
    print('Tem {} mulheres menores de 20 anos.'.format(mulherMenor))

print('-=' * 20)