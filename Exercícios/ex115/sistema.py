# Crie um pequeno sistema modularizado
# Que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
# O sistema só vai ter duas opções:
# 1) Cadastrar uma nova pessoa
# 2) Listar todas as pessoas cadastradas

# Programa principal

# Importação de bibliotecas
from ex115.lib.interface import *
from ex115.lib.arquivo import *

# Declara o arquivo de texto
arq = 'cadastro.txt'

# Verifica se o arquivo de texto existe, caso não exista chama a função criarArquivo()
if not arquivoExiste(arq):
    criarArquivo(arq)

# Laço do programa principal
while True:
    # Chama a função menu() e recebe seu retorno na variável resposta
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])

    # Opção para ler o arquivo
    if resposta == 1:

        # Chama a função lerArquivo()
        lerArquivo(arq)

    # Opção para modificar o arquivo
    elif resposta == 2:

        # Chama a função cabecalho()
        cabecalho('NOVO CADASTRO')

        # Recebe o nome da pessoa
        nome = str(input('Nome: '))

        # Chama a função leiaInt() para receber a idade da pessoa
        idade = leiaInt('Idade: ')

        # Chama a função cadastrar()
        cadastrar(arq, nome, idade)

    # Opção para sair do sistema
    elif resposta == 3:

        # Chama a função cabecalho()
        cabecalho('Saindo do sistema', True)
        break

    # Resposta de opção inválida
    else:
        print('\033[31mERRO! Escolha uma opção válida!\033[m')