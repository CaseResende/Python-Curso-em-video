# Programa que tenha uma função chamada escreva().
# Que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Função escreva
def escreva(txt):
    print('-' * (len(txt) + 4))
    print(f'  {txt}')
    print('-' * (len(txt) + 4))


# Programa principal
# Recebe os valores
texto = str(input('Digite o texto a ser exibido: '))

# Chama função escreva
escreva(texto)
