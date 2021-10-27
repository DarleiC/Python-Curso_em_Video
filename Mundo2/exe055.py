''' Faça um programa que leia o PESO de  CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR peso lidos.'''

lista = []
for c in range(1,6):
    peso = float(input(f'Informe o peso da {c}° pessoa: '))
    lista.append(peso)
menor = min(lista)
maior = max(lista)
print(f'O Menor peso foi de {(menor) :.2f}Kg e o maior foi de {(maior) :.2f}Kg')

#Como o professor fez ==========================================
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa'))
    if p == 1:
        maio = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de  {menor}Kg')


