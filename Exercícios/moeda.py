# Utilizada nos Ex 107 a 110

def aumentar(preco=0, aumento=0, formatar=False):
    """
    -> Função que calcula aumento percentual de um preço
    :param preco: Preço do produto (opcional)
    :param aumento: Porcentagem de aumento (opcional)
    :param formatar: Formatação do preço (opcional) # Ex 109
    :return: Preço com o aumento aplicado
    -> Criada no Ex107
    """

    total = preco + ((preco * aumento) / 100)

    # Ex 109
    return total if formatar is False else moeda(total) # Condição simplificada


def diminuir(preco=0, desconto=0, formatar=False):
    """
    -> Função que calcula o desconto percentual de um preço
    :param preco: Preço do produto (opcional)
    :param desconto: Porcentagem de desconto (opcional)
    :param formatar: Formatação do preço (opcional) # Ex 109
    :return: Preço com o desconto aplicado
    -> Criada no Ex107
    """

    total = preco - ((preco * desconto) / 100)

    # Ex 109
    if formatar:
        return moeda(total)
    else:
        return total


def dobro(preco=0, formatar=False):
    """
    -> Função que dobra um preço
    :param preco: Preço do produto (opcional)
    :param formatar: Formatação do preço (opcional) # Ex 109
    :return: Dobro do preço
    -> Criada no Ex107
    """

    total = preco * 2

    # Ex 109
    if formatar:
        return moeda(total)
    else:
        return total


def metade(preco=0, formatar=False):
    """
    -> Função que diminui o preço pela metade
    :param preco: Preço do produto (opcional)
    :param formatar: Formatação do preço (opcional) # Ex 109
    :return: Metade do preço
    -> Criada no Ex107
    """

    total = preco / 2

    # Ex 109
    if formatar:
        return moeda(total)
    else:
        return total


def moeda(preco):
    """
    -> Função para formatar o preço no padrão de reais
    :param preco: Preço do produto
    :return: Preço formatado em reais
    -> Criada no Ex108
    """

    # Adiciona R$ no início, fixa duas casas decimais e substitui o . por ,
    return f'R${preco:.2f}'.replace('.', ',')


def resumo(preco, mais, menos):
    """
    -> Função para exibir o resumo do valor em formato de tabela
    :param preco: Preço do produto
    :param mais: Quantidade de aumento percentual
    :param menos: Quantidade de desconto percentual
    :return: Sem retorno
    -> Criada no Ex110
    """

    # Cabeçalho da tabela
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)

    # Conteúdo da tabela
    print(f'{"Preço analisado:":<20}', end='')
    print(f'{moeda(preco):>20}')
    print(f'{"Dobro do preço:":<20}', end='')
    print(f'{dobro(preco, True):>20}')
    print(f'{"Metade do preço:":<20}', end='')
    print(f'{metade(preco, True):>20}')
    print(f'{mais}{"% de aumento:":<18}', end='')
    print(f'{aumentar(preco, mais, True):>20}')
    print(f'{menos}{"% de desconto:":<18}', end='')
    print(f'{diminuir(preco, menos, True):>20}')

    # Fim da tabela
    print('-' * 40)