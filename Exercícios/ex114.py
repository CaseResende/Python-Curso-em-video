# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado
import urllib.request


def testeSite(url):
    """
    -> Função que testa se o site está acessível
    :param url: Site a ser testado
    :return: Sem retorno
    """

    # Importação de biblioteca para teste de url
    from urllib import request

    try:
        # Tenta abrir o site
        site = urllib.request.urlopen(url)

    except urllib.error.URLError:
        # Caso não consiga, exibe mensagem de erro
        print(f'\033[31mO site {url} não está acessível.\033[m')

    else:
        # Caso consiga, exibe que está acessível
        print(f'\033[32m O site {url} está acessível.\033[m')


# Programa principal
# Chama a função testeSite
testeSite('https://www.pudim.com.br')
