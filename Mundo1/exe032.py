print('===== EXERCÍCIO 032 ====')
print(' Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO')
print('=' * 24)
from datetime import date
ano = int(input(' Informe um ano e eu vou dizer se ele é Bissexto: (Digite 0 para analisar o ano atual) : '))
print(' ')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(' O Ano {} é BISSEXTO'.format(ano))
else:
    print(' O Ano {} NÃO é BISSEXTO'.format(ano))
