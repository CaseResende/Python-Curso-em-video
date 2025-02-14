# Realiza a PA de 10 termos de um número

# Recebe os valores
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = termo

# Realiza o cálculo dos 10 termos da PA
for c in range(0, 10):
    print(pa, end=' ➝ ')
    pa = termo + razao
    termo = pa
print('Fim!')
