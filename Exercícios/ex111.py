# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos, chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107 a 110 para o primeiro pacote e faça tudo funcionar

# Programa principal
# Importação do módulo moeda.py
from utilidadesCeV import moeda

# Recebe o preço
p = float(input('Digite o preço: R$ '))

# Chama a função resumo
moeda.resumo(p, 30, 10)