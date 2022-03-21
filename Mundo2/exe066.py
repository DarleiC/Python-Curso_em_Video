'''
Crie um programa que leia VARIOS NUMEROS INTEIROS pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA. 
No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles (Desconsidere o flag)
'''
s = t = 0
while True:
    n = int(input('Informe um numero (999 para parar): '))
    if n == 999:
        break
    t += 1
    s += n
print(f'>> Foram digitados {t} numeros, totalizando {s}')

########### Como o Professor fez ###############

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}')












