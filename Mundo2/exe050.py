''' Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES. Se o valor digitado for ÍMPAR, desconsidere-o. '''
soma = 0
count = 0
lista = []
for c in range(1,7):
    num = int(input(f'Número {c}: '))
    lista.append(num)
for p in lista:
    if p %2 == 0: #ele é PAR
        soma += num
    if p %2 != 0:
        count += 1
print(f'A soma dos PARES é de {soma}')
print(f'{count} números foram descartados por ser IMPAR')

#Como o professor fez:

soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Número {c}: '))
    if num %2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
