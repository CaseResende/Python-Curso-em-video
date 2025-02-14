# Programa que lê o sexo da pessoa, mas aceita valores 'M' ou 'F'
# Caso esteja errado, peça a digitação novamente até ter um valor correto

# Recebe o sexo e coloca em maiúsculas, elimina os espaços no início e fim e considera apenas o primeiro caractere
sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]

# Realiza a análise do sexo e pede sua entrada novamente, se estiver incorreto
while sexo not in 'MF':
    sexo = str(input('Esse sexo não existe, por favor digite novamente: [M/F] ')).strip().upper()[0]

# Retorna as respostas para o usuário
if sexo == 'M':
    print('É meninoooo!')
else:
    print('É meninaaaa!')
