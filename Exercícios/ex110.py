# Adicione ao módulo moeda.py, uma função chamada resumo()
# Que irá mostrar na tela algumas iformações geradas pelas funções que já temos no módulo criado até aqui

# Programa principal
# Importação do módulo moeda.py
import moeda

# Recebe o preço
p = float(input('Digite o preço: R$ '))

# Chama a função resumo
moeda.resumo(p, 30, 10)