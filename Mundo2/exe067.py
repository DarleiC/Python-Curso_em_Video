'''
Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for NEGATIVO.
'''
n = 0
while True:
    print('-'*30)
    n = int(input('Qual numero quer saber a Tabuada? '))
    print('-'*30)
    if n < 0:
        break
    for x in range(10):
        x += 1
        t = x * n
        print(f'{n} X {x} = {t}')
print('O PROGRAMA FOI ENCERRADO')

################ COMO O PPROFESSOR FEZ ##################

while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)



