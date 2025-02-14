# Adapte o código do Ex 107
# Criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

# Programa principal
# Importação do módulo moeda.py
import moeda

# Recebe o preço
p = float(input('Digite o preço: R$ '))

# Chama as funções dentro do módulo moeda e exibe suas respostas
print(f'Aumentando {moeda.moeda(p)} em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo {moeda.moeda(p)} em 15%, temos {moeda.moeda(moeda.diminuir(p, 15))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')