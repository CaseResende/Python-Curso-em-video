# Deve ter uma tupla com nomes de produtos e seus respectivos preços na sequência
# Exibir uma listagem de preços, organizando os dados de forma tabular

# Tupla com os ítens e valores
lista = ('Hambúrguer', 10, 'X-burguer', 12, 'X-bacon', 13, 'X-salada', 13, 'X-tudo', 18, 'Batata simples', 10, 'Batata completa', 15)

# Topo da tabela
print('-'*45)
print(f'{"Hamburgueria":^45}')
print('-'*45)

# Estrutura para desmembrar os ítens da tupla
for posicao in range(0, len(lista)):

    # Inserção do ítens e os traços
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<35}', end='')

    # Inserção dos valores
    else:
        print(f' R${lista[posicao]:>7.2f}')

# Fim da tabela
print('-'*45)
