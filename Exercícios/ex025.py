# Lê e verifica se o nome possui "Silva"

# Recebe o nome eliminando os espaços no início e fim
nome = str(input('Digite seu nome: ')).strip()

# Retorna True ou False se o nome possui 'SILVA'
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
