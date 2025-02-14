# Recebe um valor em metros e retorna seu valor em outras escalas

# Recebe o valor
m = float(input('Insira o valor em metros: '))

# Converte o valor em suas escalas
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

# Retorna os valores
print('O valor {}m corresponde a: \n * {}km,\n * {}hm,\n * {}dam,\n * {:.0f}dm,\n * {:.0f}cm,\n * {:.0f}mm.'.format(m, km, hm, dam, dm, cm, mm))
