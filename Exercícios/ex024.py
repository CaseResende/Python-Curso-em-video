# Lê o nome de uma cidade e retorna se ela começa com "santo"

# Recebe o nome da cidade e elimina os espaços no início e fim
cidade = input('Digite o nome da sua cidade: ').strip()

# Imprime os 5 primeiros caracteres em maiúsculo se forem 'SANTO'
print(cidade[:5].upper() == 'SANTO')
