# Programa que tenha uma tupla com várias palavras (sem acentos).
# Deve mostrar para cada palavra, quais são as suas vogais.

from time import sleep

palavras = ('Carlos', 'Caroline', 'Jacqueline', 'Daniela', 'Raphael', 'Tobias', 'Bonnie', 'Andre')

print('-=' * 30)
print(f'{"Dissecador de vogais":^60}')
print('-=' * 30)
sleep(0.5)

for palavra in palavras:
    print(f'A palavra {palavra.upper()} tem as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
    print()

sleep(0.5)
print('-=' * 30)
print(f'{"FIM":^60}')
print('-=' * 30)
