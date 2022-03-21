'''Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai para quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA.
No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a soma entre eles(desconsiderando o flag[ignorar os número 999])
'''
from time import sleep
n = 0
total = 0
cont = 0
while  n != 999:
    n = int(input('Informe um número (999 sai): '))
    if n != 999:
        total += n
        cont += 1
    else:
        print('Contando...')
        sleep(1)
print(f'Digitou {cont} números e o somatório deles foi {total}')

# =============== Como o professor fez

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))


