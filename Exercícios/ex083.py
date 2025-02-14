# Analise uma expressão matemática digitada pelo usuário, que contenha parênteses
# Verifique se está com os parênteses abertos e fechados na ordem correta

# Inicialização das variáveis
sobra = list()

# Recebe a expressão
expressao = str(input('Digite a expressão para validar: '))

# Repetição para verificar se possui parênteses abertos e fechados
for simbolo in expressao:

    # Possuindo um aberto, adiciona um à lista de sobra
    if simbolo == '(':
        sobra.append('(')

    # Possuindo um fechado, precisa verificar se existe um aberto ou não
    elif simbolo == ')':

        # Existindo um aberto, fecha a dupla e remove da lista de sobra
        if len(sobra) > 0:
            sobra.pop()

        # Não existindo um aberto, adiciona o fechado à lista de sobra
        else:
            sobra.append(')')
            break

# Retorna as respostas ao usuário
# Se a lista de sobra está vazia, é porque está correta
if len(sobra) == 0:
    print('Sua expressão está correta!')

# Com a lista de sobra contendo algum ítem, é porque está incorreta
else:
    print('Sua expressão está incorreta!')
