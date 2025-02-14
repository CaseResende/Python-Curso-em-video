# Lê nome, ano de nascimento e carteira de trabalho.
# Cadastra (com idade) em um dicionário.
# Se, por acaso a CTPS (carteira de trabalho) for diferente de zero
# O dicionário receberá também o ano de contratação e salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Contagem de 35 anos de contribuição!

# Importação do módulo que coleta data e hora
from datetime import datetime

# Inicialização do dicionário
trabalhador = dict()

# Recebe os valores do usuário
trabalhador['nome'] = str(input(f'Nome: '))
anoDeNascimento = int(input(f'Ano de nascimento de {trabalhador["nome"]}: '))

trabalhador['idade'] = datetime.now().year - anoDeNascimento

trabalhador['ctps'] = int(input(f'Carteira de trabalho de {trabalhador["nome"]}(0 caso não possua): '))

# Condição para prosseguir o cadastro
if trabalhador['ctps'] != 0:
    trabalhador['ano de contratação'] = int(input(f'Ano de contratação de {trabalhador["nome"]}: '))
    trabalhador['salario'] = float(input(f'Salário: R$ '))
    trabalhador['aposentadoria'] = (trabalhador['ano de contratação'] + 35) - anoDeNascimento

else:
    print(f'{trabalhador["nome"]} não possui carteira de trabalho, portanto não tenho o que exibir.')

# Exibição das respostas
print('-=' * 30)

for key, value in trabalhador.items():
    print(f' - {key.capitalize()} tem o valor: {value}.')

print('-=' * 30)
