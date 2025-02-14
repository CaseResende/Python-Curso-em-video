# Lê um valor qualquer e retorna seu tipo primitivo e informações sobre ele

# Lê o valor
n = input('Digite algo: ')

# Retorna suas informações
print(n, 'pertence ao tipo primitivo', type(n))
print(n, 'é numérico? - ', n.isnumeric())
print(n, 'é alfabético? - ', n.isalpha())
print(n, 'é somente espaços? - ', n.isspace())
print(n, 'é alfanumérico? - ', n.isalnum())
print(n, 'está em maíusculas? - ', n.isupper())
print(n, 'está em minúsculas? - ', n.islower())
print(n, 'está capitalizada? - ', n.istitle())
