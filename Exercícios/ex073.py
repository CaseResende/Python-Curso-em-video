# Criar uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato inglês, em sua ordem de colocação
# Exibir:
# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados
# Uma lista com os times em ordem alfabética
# Em que posição se encontra o Chelsea

# Inicialização da tabela
tabela = (
    'Arsenal', 'Manchester City', 'Newcastle', 'Manchester United', 'Tottenham', 'Brighton', 'Fulham', 'Brentford',
    'Liverpool', 'Chelsea', 'Aston Villa', 'Crystal Palace', 'Nottingham Forest', 'Leicester City', 'Leeds United',
    'West Ham', 'Wolverhampton', 'Bournemouth', 'Everton', 'Southampton')

# Identificando os 5 primeiros e imprimindo lado a lado
print('-=' * 30)
print('Os 5 primeiros colocados são:')
for posicao, cinco in enumerate(tabela[:5]):
    if posicao == 4:
        print(cinco)
    else:
        print(cinco, end=', ')

# Identificando os 4 últimos
print('-=' * 30)
print('Os 4 últimos são:')
for quatro in tabela[-4:]:
    print(quatro)

# Utilizando o sorted para ordenar alfabeticamente
print('-=' * 30)
print('A tabela em ordem alfabética fica:')
for alfabetica in sorted(tabela):
    print(alfabetica)

# Usando o index para encontrar a posição do Chelsea
print('-=' * 30)
print(f'O Chelsea está na {tabela.index('Chelsea') + 1}ª posição.')
print('-=' * 30)

