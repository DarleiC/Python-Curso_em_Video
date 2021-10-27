print('===== EXERCÍCIO 025 ====')
print('Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome')
print('=' * 24)
print('')
nome = str(input('Qual seu nome? ')).strip()
print('Seu nome tem "Silva"? {}'.format('Silva' in nome.title()))

#COMO FIZ:
#nome = nome.title()
#tem = 'Silva' in nome
#print(tem)