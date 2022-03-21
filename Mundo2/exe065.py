'''Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual foi o MAIOR e o MENOR valores lidos.
O programa deve perguntar ao usuário se ele que ou continuar A DIGITAR VALORES
'''

cont = 0
r = ''
lista = []
while r != 'N':
    n1 = int(input('Informe número: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    lista.append(n1)
    cont += 1 # Aqui vai contar quantas valores foram lidos
maior = max(lista)
menor = min(lista)
media = sum(lista)/cont
print(f'A media foi de {media} com {cont} numeros digitados.\nSendo o maior = {maior} e o menor = {menor}')

# ============ Como o professor fez

resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} numeros e a media foi {}'.format(quant,media))
print('O maior foi {} e o menor foi {}'.format(maior, menor))

