'''  https://prnt.sc/227ym4u
Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO.
No inicio, pergunte ao usuário qual será o VALOR A SER SACADO(numero inteiro) e o programa vai informar quantas CÉDULAS de cada valor serão entregues.
OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''

cont = 0
saque = int(input('Qual valor quer sacar? R$ '))
while True:
    if saque >= 50:
        saque -= 50
        cont += 1 # aqui vai somara qtd de cédulas de 50
    else:
        vinte = saque // 20
        saque -= (vinte * 20)
        dez = saque // 10
        saque -= (dez * 10)
        um = saque // 1
        saque -= (um * 1)
        break
print(f'{cont} cédulas de R$ 50,00')
print(f'{vinte} cédulas de R$ 20,00')
print(f'{dez} cédulas de R$ 10,00')
print(f'{um} cédulas de R$ 1,00')

########## COMO O PROFESSOR FEZ ##########

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor voce quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

