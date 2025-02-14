# Criado no Ex 112

def leiaDinheiro(mensagem):
    """
    -> Função para validar a entrada do preço no formato correto
    :param mensagem: Recebe uma mensagem e lê seus dados
    :return: Preço validado no tipo float
    -> Criado no Ex 112
    """

    # Inicialização da variável de controle
    valido = False

    # Laço para ler e validar a entrada
    while not valido:

        # Recebe a entrada de dados substituindo a , por . e eliminando os espaços
        dado = str(input(mensagem)).replace(',', '.').strip()

        # Verifica se o valor é alfa numérico ou se está vazio
        if dado.isalpha() or dado == '':
            # Caso sejam, retorna erro
            print(f'\033[31mERRO! "{dado}" é um preço inválido!\033[m')
        else:
            # Caso não sejam, encerra o laço e retorna o preço como float
            valido = True
            return float(dado)