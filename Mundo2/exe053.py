''' Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO(que pode ler ao contrário e é a mesma), desconsiderando os espaços.
EX: "APOS A SOPA" / "A SACADA DA CASA" / "A TORRE DA DERROTA" / "O LOBO AMA O BOLO" / "ANOTARAM A DATA DA MARATONA" '''

frase = str(input('Escreva uma frase: ')).upper()
frase1 = frase.strip().replace(' ','')
frase2 = frase1[::-1]
if frase1 == frase2:
    print(f'O INVERSO DE "{frase}" é "{frase2}"\nÉ UM PALÍNDROMO')
else:
    print(f'O INVERSO DE "{frase}" e "{frase2}"\nNÃO É UM PALÍNDROMO')

# Como o professor fez:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O INVERSO DE {} É {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('A frase digitada não é um PALÍNDROMO')