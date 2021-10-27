''' Crie um programa que mostre na tela TODOS OS NÚMEROS pares que estão no intervalo entre 1 e 50 '''

for i in range(1,51):
    if i % 2 == 0:
        print(i, end=' ')
print('\n')

#como o professor fez. o ultimo 2 é para pular de dois em dois
for n in range(2, 51, 2):
    print(n, end=' ')