# Modifique as funções que foram criadas no Ex 107
# Para que elas aceitem um parâmetro a mais
# Informando s eo valor retornado por elas vai ser ou não formatado pela função moeda(), do Ex 108

# Programa principal
# Importação do módulo moeda.py
import moeda

# Recebe o preço
p = float(input('Digite o preço: R$ '))

# Chama as funções dentro do módulo moeda e exibe suas respostas
print(f'Aumentando {moeda.moeda(p)} em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo {moeda.moeda(p)} em 15%, temos {moeda.diminuir(p, 15, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')