''' Faça um programa que calcule a SOMA entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE 3 e que se encontram no intervalo de 1 ATÉ 500 '''

lista = []
for i in range(1, 501):
    if i %2 != 0 and i %3 == 0:
        lista.append(i)
        tamanho = len(lista)
        soma = sum(lista)
print(f'A soma de todos os {tamanho} números encontrados é de {soma}')


#Como o professor fez
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} é de {soma}')
