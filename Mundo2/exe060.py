''' Faça um programa que leia um NÚMERO qualquer e o mostre o seu FATORIAL.
Ex: 5! = 5x4x3x2x1=120
'''
# professor fez
'''
from math import factorial
n1 = int(input('Informe um número: '))
f = factorial(n1)
print('O fatorial de {} é {}.'.format(n1, f))'''

n1 = int(input('Informe um número: '))
c = n1
f = 1
print('Calculando {}! '.format(n1), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))


