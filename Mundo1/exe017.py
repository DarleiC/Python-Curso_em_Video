print('===== EXERCÍCIO 017 ====')
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa: ')
print('=' * 24)

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)


print('VARIAÇÃO SEM BIBLIOTECA')

co1 = float(input('Comprimento do Cateto Oposto: '))
ca1 = float(input('Comprimento do Cateto Adjacente: '))
hi = (co1 ** 2 + ca1 **2) ** (1/2)
