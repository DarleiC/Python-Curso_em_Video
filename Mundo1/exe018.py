print('===== EXERCÍCIO 018 ====')
print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. ')
print('=' * 24)

from math import radians, sin, cos , tan
an = float(input('Digite o Angulo: '))
seno = sin(radians(an))
print('O Angulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O angulo de  {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))
