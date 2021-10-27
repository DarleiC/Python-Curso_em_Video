'''Crie um programa que faça o computador jogar Jokenpô com você:'''
import random
from time import sleep
p2 = int(random.randint(0,2))
if p2 == 0:
    p2 = 'PEDRA'
elif p2 == 1:
    p2 = 'PAPEL'
elif p2 == 2:
    p2 = 'TESOURA'
p1 = int(input('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Escolha: '''))
if p1 == 0:
    p1 = 'PEDRA'
elif p1 == 1:
    p1 = 'PAPEL'
elif p1 == 2:
    p1 = 'TESOURA'
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('=-=' *10)
print(f'Máquina jogou {p2}')
print(f'Humano jogou {p1}')
print('=-=' *10)
if p1 == 'TESOURA' and p2 == 'PAPEL' or p1 == 'PAPEL' and p2 == 'PEDRA' or p1 == 'PEDRA' and p2 == 'TESOURA':  # p1 ganha
    print('Humano ganhou')
elif p1 == 'PAPEL' and p2 == 'TESOURA' or p1 == 'PEDRA' and p2 == 'PAPEL' or p1 == 'TESOURA' and p2 == 'PEDRA': #p2 ganha
    print('Maquina ganhou')
elif p1 == 'PAPEL' and p2 == 'PAPEL' or p1 == 'TESOURA' and p2 == 'TESOURA' or p1 == 'PEDRA' and p2 == 'PEDRA': #empata
    print('EMPATOU')


