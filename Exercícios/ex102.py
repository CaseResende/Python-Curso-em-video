# Programa que tenha uma função fatorial() que receba dois parâmetros:
# O primeiro que indique o número a calcular
# Show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial


# Função fatorial()
def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostra ou não o processo de cálculo.
    :return: O valor do Fatorial de um número numero.
    """
    # Importação da função temporizador
    from time import sleep

    # Inicialização de variáveis
    fat = 1
    cont = numero

    # Laço para calcular o fatorial
    while cont > 0:
        fat *= cont

        # Condição para exibir o cálculo
        if show:

            sleep(0.5)
            # Condições para personalizar o separador
            if cont == 1:
                print(f'{cont} = ', end='')
            else:
                print(f'{cont}', end=' x ')

        # Decrementa o contador
        cont -= 1

    # Exibe o fatorial
    print(fat)


# Programa principal
# Chama a função fatorial com os seus parâmetros
fatorial(5, True)