# Programa que lê nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela
# Média ≥ 7, aprovado

# Inicialização do dicionário
aluno = dict()

# Recebe os valores nome e média
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

# Cálculo para situação
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

# Retorno das respostas na tela
print('-=' * 30)
for chave, valor in aluno.items():
    print(f'* {chave.capitalize()} é {valor}.')

