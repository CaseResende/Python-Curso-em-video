# Recebe a largura e altura de uma parede e calcula quantos litros de tinta são necessários para pintá-la

# Recebe os valores
larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

# Calcula e retorna a área
area = larg * alt
print('A sua parede tem a dimensão de {}x{} e a sua área é de {:.2f}m².'.format(larg, alt, area))

# Calcula e retorna a quantidade de tinta
tinta = area / 2
print('São necessários {:.2f} litros de tinta para pintá-la.'.format(tinta))
