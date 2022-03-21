'''Melhore o jogo do DESAFIO 28, onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer
'''
import random
from time import sleep
computador = random.randint(0,10)
contador = 1
#print(computador)
print('Vou escolher um número entre 0 e 10')
print(' estou pensando.. ')
sleep(1)
print(' Já sei!')
humano = int(input('Tente adivinhar: '))
while humano != computador:
    contador += 1
    if humano < computador:
        print('Mais..')
    else:
        print('Menos..')
    humano = int(input('Tente de novo: '))
print(f'Acertou! Você precisou de {contador} tentativas.')

# ==== COMO O PROFESSOR FEZ
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos.. Tente mais uma vez.')
print('Acertou com {} palpites!'.format(palpites))




















