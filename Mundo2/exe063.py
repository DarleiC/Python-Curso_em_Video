'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma SEQUÊNCIA FIBONACCI;
Ex.: 0-1-1-2-3-5-8
'''
print('SEQUÊNCIA DE FIBONACCI')
quantos = int(input('Quantos termos quer ver? '))
n1 = 0
n2 = 1
cont = 0
while cont < quantos:
    print(f'{n1} => ', end='')
    n = n1 + n2
    n1 = n2
    n2 = n
    #print(n)
    cont += 1
print('FIM')

# ====== Como o professor fez
print('-' * 30)
print('Sequencia de FIBONACCI')
print('-' * 30)
n = int(input('Quantos termos voê quer mostrar? '))
t1 = 0 
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')




