# Recebe duas notas do aluno e calcula a média

# Recebe as duas notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Calcula a média
media = (n1 + n2)/2

# Retorna os valores
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, media))
