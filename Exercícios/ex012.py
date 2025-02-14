# Recebe o preço do produto e retorna seu valor com desconto de 5%

# Recebe o valor do produto
preco = float(input('Digite o preço do produto: '))

# Calcula o preço com desconto e retorna
desc = preco - (preco * 0.05)
print('O produto que custava {:.2f}, agora, com 5% de desconto, custa {:.2f}.'.format(preco, desc))
