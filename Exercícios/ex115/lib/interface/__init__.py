def leiaInt(mensagem):
    """
    -> Função que valida a leitura de, apenas, números inteiros
    :param mensagem: Mensagem a ser exibida no input
    :return: Retorna o número inteiro ou 0 caso o usuário não digite
    """

    # Laço para realizar a leitura
    while True:

        # Captura a exceção e recebe o valor
        try:
            entrada = int(input(mensagem))

        # Trata a exceção de interromper a execução, retornando 0
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0

        # Trata as exceções de valor ou tipo incorretos e continua o laço
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue

        # Retorna o número inteiro
        else:
            return entrada


def linha(tam=60):
    """
    -> Função para imprimir uma linha horizontal
    :param tam: Tamanho da linha (opcional)
    :return: Uma linha horizontal do tamanho selecionado
    """
    return '-' * tam


def cabecalho(txt, animar=False):
    """
    -> Função que cria um cabeçalho
    :param txt: Mensagem a ser exibida
    :param animar: Criar uma animação com reticências
    :return: Sem retorno
    """

    print(linha())

    # Cria uma animação com reticências temporizadas
    if animar:
        from time import sleep
        print(f'{txt:>37}', end='')
        for cont in range(0, 3):
            sleep(0.5)
            print('.', end='')
        print()

    # Cabeçalho padrão
    else:
        print(txt.center(60))

    # Chama a função linha()
    print(linha())


def menu(lista):
    """
    -> Função para criar um menu
    :param lista: Valores a serem exibidos no menu
    :return: Retorna uma opção de valor inteiro
    """

    # Chama a função cabeçalho()
    cabecalho('MENU PRINCIPAL')

    # Percorre a lista e exibe cada item formatado
    for cont, item in enumerate(lista):
        print(f'{cont + 1} - {item}')

    # Chama a função linha()
    print(linha())

    # Chama a função leiaInt() e retorna seu valor
    opcao = leiaInt('Sua opção: ')

    # Retorna a opção selecionada
    return opcao