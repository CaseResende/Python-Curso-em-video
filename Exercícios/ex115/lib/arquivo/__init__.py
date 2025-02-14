# Importação da biblioteca interface
from ex115.lib.interface import *


def arquivoExiste(nome):
    """
    -> Função para verificar a existência de um arquivo txt
    :param nome: Nome do arquivo
    :return: Verdadeiro ou Falso
    """
    try:
        # Abre o arquivo com o nome do arquivo e leitura de texto
        # R = Read, T = Text
        a = open(nome, 'rt')

        # Fecha o arquivo
        a.close()

    # Caso não encontre o arquivo
    except FileNotFoundError:
        return False

    # Caso encontre
    else:
        return True


def criarArquivo(nome):
    """
    -> Função para criar um arquivo txt
    :param nome: Nome do arquivo a ser criado
    :return: Sem retorno
    """
    try:
        # Abre o arquivo com o nome e escrita de texto
        # W = Write, T = Text, + = Criar caso não exista
        a = open(nome, 'wt+')

        # Fecha o arquivo
        a.close()

    # Caso não consiga criar o arquivo
    except:
        print(f'\033[31mHouve um erro na criação do arquivo!\033[m')

    # Caso consiga criar o arquivo
    else:
        print(f'\033[34mArquivo "{nome}" criado com sucesso!\033[m')


def lerArquivo(nome):
    """
    -> Função para ler um arquivo de texto
    :param nome: Nome do arquivo a ser lido
    :return: Sem retorno
    """
    global a
    try:
        # Abre o arquivo no modo leitura
        a = open(nome, 'rt')

    # Caso não consiga abrir o arquivo
    except:
        print(f'\033[31mErro ao ler o arquivo!\033[m')

    # Caso consiga abrir o arquivo
    else:
        # Chama a função cabecalho()
        cabecalho('PESSOAS CADASTRADAS')

        # Percorre todas as linhas do arquivo
        for linha in a:

            # Separa cada ítem através do ;
            dado = linha.split(';')

            # Remove a quebra de linha
            dado[1] = dado[1].replace('\n', '')

            # Exibe os dados formatados
            print(f'{dado[0]:<52}{dado[1]:>3} anos')

    # Fecha o arquivo
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    """
    -> Função para cadastrar pessoas no arquivo
    :param arq: Nome do arquivo de texto
    :param nome: Nome da pessoa a ser cadastrada
    :param idade: Idade da pessoa a ser cadastrada
    :return: Sem retorno
    """

    # Abre o arquivo de texto
    # A = Append, T = Text
    try:
        a = open(arq, 'at')

    # Caso não consiga abrir o arquivo
    except:
        print(f'\033[31mHouve um ERRO na abertura do arquivo!\033[m')

    # Caso consiga abrir o arquivo
    else:

        # Escreve o nome;idade e quebra a linha
        try:
            a.write(f'{nome};{idade}\n')

        # Caso não consiga escrever no arquivo
        except:
            print(f'\033[31mHouve um ERRO na escrita dos dados!\033[m')

        # Caso consiga escrever no arquivo
        # Retorna uma mensagem de sucesso e fecha o arquivo
        else:
            print(f'\033[35m * Novo registro de \033[32m<{nome}>\033[35m adicionado.\033[m')
            a.close()

