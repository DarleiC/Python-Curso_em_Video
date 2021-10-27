print('===== EXERCÍCIO 024 ====')
print('Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO" ')
print('=' * 24)
print('')
cidade = str(input('Qual o nome da sua cidade? ')).strip()
print(cidade[:5].upper() == 'SANTO')


# ASSIM QUE EU FIZ:
#cidade = cidade.upper()
#cidade = cidade.split()
#tem = 'SANTO' in cidade[0]
#print(tem)