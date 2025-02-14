# Lê nome e duas notas de vários alunos e guarda tudo em uma lista composta (lista nome e lista notas)
# Ao final, exibe um boletim com a média de cada um
# E permite que o usuário possa mostrar as notas de cada aluno individualmente

# Inicialização da lista
ficha = list()

# Laço de repetição para cadastro
while True:

    # Recebe nome e notas
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    # Continuação do cadastro
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

        if continuar not in 'SN':
            print('Opção inválida!')
        else:
            break
    if continuar == 'N':
        break

# Retorna o cabeçalho
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

# Retorna os cadastros com a média
for posicao, aluno in enumerate(ficha):
    print(f'{posicao:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

# Laço para ver detalhes de aluno
while True:
    print('-=' * 30)
    nota = int(input('Mostrar notas de qual aluno? (999 para cancelar): '))
    if nota == 999:
        print('Finalizando...')
        break

    # Retorna os dados detalhados na tela
    if nota <= len(ficha) - 1:
        print(f'As notas de {ficha[nota][0]} são {ficha[nota][1]}')
    else:
        print('Escolha uma opção válida!')
print('<<< Volte Sempre! >>>')
