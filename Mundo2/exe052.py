''' Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO. '''
lista = []
n1 = int(input('Informe um número: '))
for c in range(1, n1 + 1):
    r = n1 % c
    lista.append(r)
    total = lista.count(0)
if total == 2:
    print(f'o n° {n1} é primo porque ele foi dividido {total}x')
else:
    print(f'o n° {n1} Não é primo porque ele foi divisivel {total}x!')


# Como o professor fez
print('================= PROFESSOR =================')
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO n° {num} foi divisivel {tot}x')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
