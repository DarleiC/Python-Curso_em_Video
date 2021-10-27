print('===== EXERCÍCIO 033 ====')
print(' Faça um programa que leia três números e mostre qual é o MAIOR e qual é o Menor.')
print('=' * 24)

a = int(input('O primeiro: '))
b = int(input('O segundo: '))
c = int(input('O terceiro: '))
menor = a
if b < a  and b < c:
    menor = b
if c < a and c < b:
    menor = c        
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor é: {}'.format(menor))
print('O maior é: {}'.format(maior))
