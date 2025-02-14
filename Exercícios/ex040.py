# Lê duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

# Cria um banco de cores
cores = {'verde': '\033[30;32m',
         'branco': '\033[7m',
        'vermelho': '\033[30;31m',
         'azul': '\033[30;34m',
        'limpa': '\033[m'}

# Recebe as notas
print('Informe as duas notas do aluno e direi sua média e sua condição.')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

# Calcula a média e a retorna
media = (nota1 + nota2) / 2
print('O aluno tem média {}{}{}.'.format(cores['branco'], media, cores['limpa']))

# Retorna as respostas de acordo com a média do aluno
if media < 5:
    print('Aluno {}REPROVADO!{}'.format(cores['vermelho'], cores['limpa']))
elif media <= 6.9:
    print('Aluno em {}RECUPERAÇÃO!{}'.format(cores['azul'], cores['limpa']))
else:
    print('Aluno {}APROVADO!{}'.format(cores['verde'], cores['limpa']))
