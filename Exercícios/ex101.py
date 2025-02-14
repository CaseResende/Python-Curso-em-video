# Programa que tenha uma função chamada voto()
# Esta função vai receber o ano de nascimento de uma pessoa como parâmetro
# Vai retornar um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
# Voto opcional -> entre 16 e 18 e maior de 65 anos.


# Função voto()
def voto(nascimento):
    """
    -> Função para verificar a obrigatoriedade de voto
    :param nascimento: Ano de nascimento
    :return: Strings com condições para votar
    """
    # Importação da função para coletar a data
    from datetime import date

    # Calcula a idade
    idade = date.today().year - nascimento

    # Realiza a validação das idades e retorna as condições para votar
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


# Programa principal
# Recebe o ano de nascimento e já imprime o retorno da função voto()
print(voto(int(input('Ano de nascimento: '))))
