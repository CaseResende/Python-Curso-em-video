# Dentro do pacote utilidadesCeV que criamos no Ex 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input()
# Mas com uma validação de dados para aceitar apenas valores que sejam monetários.

# Programa principal
# Importações dos módulos
from utilidadesCeV import dado
from utilidadesCeV import moeda

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 10, 25)