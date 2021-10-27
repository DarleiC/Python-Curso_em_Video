print('===== EXERCÍCIO 030 ====')
print(' Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR')
print('=' * 24)
num = int(input('Me diga um número: '))
print(' ')
x = num % 2
if x == 1:
    print('IMPAR')
else:
    print('PAR')
print(' ')