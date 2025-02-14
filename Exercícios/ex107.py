# Crie um módulo chamado moeda.py que tenha as funções incorporadas:
# -> aumentar() * Aumenta o preço em x% *
# -> diminuir() * Diminui o preço em x% *
# -> dobro()
# -> metade()
# Faça também um programa que importe esse módulo e use algumas dessas funções


# Programa principal
# Importação do módulo moeda.py
import moeda

# Recebe o preço
p = float(input('Digite o preço: R$ '))

# Chama as funções dentro do módulo moeda e exibe suas respostas
print(f'Aumentando {p} em 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo {p} em 15%, temos {moeda.diminuir(p, 15)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')

