print(' ')
print('===== EXERCÍCIO 028 ====')
print(' Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. ')
print('O programa deverá escrever na tela se o usuário venceu ou perdeu')
print('=' * 24)

import random
from time import sleep #Biblioteca para dar um cooldow até iniciar o próximo comando
r = str(random.randint(0, 5))
#print(r)
input('Aperte ENTER e eu vou escolher um número entre 0 e 5')
print(' estou pensando.. Já sei!')
sleep(2)
humano = str(input('Qual número eu escolhi entre 0 e 5? ')).strip()
print(' ')
print('Um suspense para dar emoção ...')
sleep(2)
if humano == r:
    print(' ')
    print(' VENCEU, acertou o número que escolhi! Ta de hack!')
else:
    print(' ')
    print(' Há! PERDEU, escolhi o número {}'.format(r))
print(' ')










