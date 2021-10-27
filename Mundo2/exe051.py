''' Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA(Progressão Aritimética). No final, mostre os 10 primeiros termos dessa progressão. '''
a1 = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
for c in range(0,10):
    a1 = a1 + razao
    print(a1, '=>', end=' ')
print('ACABOU')

#Como o professor fez:
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' => ')
print('ACABOU')