print('===== EXERCÍCIO 031 ====')
print(""" Dsesenvolva um programa que pergunte a distância de uma viagem em Km. 
      Calcule o preço da passagem, cobrando: 
      R$ 0,50 por Km para viagens de até 200Km
      R$ 0,45 para viagens mais longas.""")
print('=' * 24)
print(' ')
dist = float(input(' Qual a distância da viagem? '))
if dist <= 200:
      preco = dist * 0.50
else:
      preco = dist * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))





'''if dist <= 200:
      menos = dist * 0.5
      print('A viagem vai custar R${:.2f}'.format(menos))
elif dist > 200: 
      mais = dist * 0.4
      print('A viagem vai custar R${:.2f}'.format(mais))
else:
      print('Paga nada')
print(' ')
'''

