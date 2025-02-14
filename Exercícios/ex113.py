# Reescreva a função leiaInt() do Ex 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também a função leiaFloat() com a mesma funcionalidade.

# Programa que tenha a função leiaInt()
# Vai funcionar de forma semelhante à função input() do Python.
# Porém fazendo a validação para aceitar apenas um valor numérico.


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

        # Trata as excessões de valor ou tipo incorretos e continua o laço
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue

        # Retorna o número inteiro
        else:
            return entrada



def leiaFloat(mensagem):
    """
    -> Função que valida a leitura de, apenas, números reais
    :param mensagem: Mensagem a ser exibida no input
    :return: Retorna o número real ou 0 caso o usuário não digite
    """

    # Laço para realizar a leitura
    while True:

        # Captura a exceção e recebe o valor
        try:
            entrada = float(input(mensagem))

        # Trata a exceção de interromper a execução, retornando 0
        except KeyboardInterrupt:
            print(f'\n \033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0

        # Trata as excessões de valor ou tipo incorretos e continua o laço
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue

        # Retorna o número inteiro
        else:
            return entrada



# Programa principal
# Chama as funções validadoras e recebe seus retornos
i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')

# Exibe a resposta
print('-' * 60)
print(f'O valor inteiro foi {i} e o real foi {r}')
