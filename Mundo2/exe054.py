''' Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS. No final, mostre quantas pessoas ainda não atingiram a maioridade(21 anos) e quantas já são maiores. '''
from datetime import date
atual = date.today().year
lista = []
maior = 0 
menor = 0
for c in range(1,8):
    ano = int(input(f'Em que ano nasceu a {c}° pessoa? '))
    idade = atual - ano
    lista.append(idade)
print(lista)
for i in lista:
    if i >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} São maiores de idade')
print(f'{menor} são menores de idade')

#Como o professor fez================================================
from datetime import date
atual = date.today().year
maior = 0 
menor = 0
for c in range(1,8):
    ano = int(input(f'Em que ano nasceu a {c}° pessoa? '))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} São maiores de idade')
print(f'{menor} são menores de idade')










