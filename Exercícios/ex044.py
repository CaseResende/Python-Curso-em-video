# Calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# À vista dinheiro ou cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros

print('Informe o valor do produto e a forma de pagamento que irei calcular o valor final.')

produto = float(input('Valor do produto: R$'))
pagamento = int(input('Forma de pagamento:\n 1 - À vista no dinheiro\n 2 - À vista no cheque\n 3 - À vista no cartão\n 4 - 2x no cartão\n 5 - 3x no cartão\n 6 - 4x no cartão\n >'))

if pagamento == 1 or pagamento == 2:
    print('10% de desconto, valor final: R${}'.format(produto - (produto * 0.1)))
elif pagamento == 3:
    print('5% de desconto, valor final: R${}'.format(produto - (produto * 0.05)))
elif pagamento == 4:
    print('Valor final R${}'.format(produto))
elif pagamento == 5 or pagamento == 6:
    print('20% de juros, valor final: R${}'.format(produto + (produto * 0.2)))
else:
    print('Opção inválida!')