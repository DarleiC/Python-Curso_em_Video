''' https://prnt.sc/227x858
Faça um programa que jogue PAR ou ÍMPAR com o Computador. 
O programa só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
import random
venceu = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('PAR ou IMPAR? [P/I]: ')).upper().strip()
    print('-'*30)
    maquina = random.randint(0,10)
    n = jogador + maquina
    r = n % 2
    if r == 0 and escolha == 'P':
        print(f'Você jogou {jogador} e o computador {maquina}. Total de {n} é PAR')
        venceu += 1
    elif r == 1 and escolha == 'I':
        print(f'Você jogou {jogador} e o computador {maquina}. Total de {n} é IMPAR')
        venceu += 1
    elif r == 0 and escolha == 'I':
        print(f'Você jogou {jogador} e o computador {maquina}. Total de {n} é PAR')
        print('=-'*15)
        print('GAME OVER')
        break
    else:
        print(f'Você jogou {jogador} e o computador {maquina}. Total de {n} é IMPAR')
        print('=-'*15)
        print('GAME OVER')
        break
print(f'Ganhou {venceu} vezes!')

'''
0 P = OK
1 I = OK
1 P = NOK
0 I = NOK
'''

######### COMO O PROFESSOR FEZ ################

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' ' 
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print ('Voce VENCEU!')
            v +=1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')        
print(f'GAME OVER! Voce vencer {v} vezes')








