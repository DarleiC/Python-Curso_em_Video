print('===== EXERCÍCIO 016 ====')
print('Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. ')
print('=' * 24)

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

print('ALTERNATIVA SEM PRECISAR DE BIBLIOTECA')

num - float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))

