# Programa com função chamada ficha(), que receba dois parâmetros opcionais:
# O nome de um jogador.
# Quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# Função ficha()
def ficha(nome='<desconhecido>', gols=0):
    """
    -> Exibe quantos gols o jogador fez no campeonato
    :param nome: String com nome do jogador (opcional)
    :param gols: Inteiro com número de gols (opcional)
    :return: Sem retorno
    """
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


# Programa principal
# Recebe os valores
jogador = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))

# Verifica se o valor digitado para gols é numérico ou não
if gol.isnumeric():
    # Transforma o valor em numérico
    gol = int(gol)
else:
    # Entende como 0 gols
    gol = 0

# Verifica se o valor digitado para jogador está vazio ou não
if jogador.strip() == '':
    # Envia apenas o parâmetro gols
    ficha(gols=gol)
else:
    # Envia os dois parâmetros
    ficha(jogador, gol)





