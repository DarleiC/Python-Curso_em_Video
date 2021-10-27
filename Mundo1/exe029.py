print('===== EXERCÍCIO 029 ====')
print(""" Escreva um programa que leia a velocidade de um carro. 
      Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
      A multa vai custar R$7,00 por cada Km acima do limite""")
print('=' * 24)
from time import sleep
print(' ')
velocidade = float(input('Qual a velocidade do veículo: '))
print('CALCULANDO ...')
sleep(2)
if velocidade > 80:
      acima = velocidade - 80
      quanto = acima * 7
      print(' ')
      print('Você será multado em R$ {:.2f} por ter ultrapassado {} km/h acima da velocidade permitida'.format(quanto, acima))
print('Velocidade permitida')
print(' ')
