''' Crie um programa que leia dois valores e mostre um MENU na tela:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
Seu programa deverá realizar a operação solicitada em cada caso
'''
n1 = int(input('Informe o 1º: '))
n2 = int(input('Informe o 2º: '))
escolha = 0
while escolha != 5:
    print(' [ 1 ] SOMAR\n   [ 2 ] MULTIPLICAR\n [ 3 ] MAIOR\n   [ 4 ] NOVOS NÚMEROS\n   [ 5 ] SAIR DO PROGRAMA')
    escolha = int(input('Qual opção deseja? '))
    if escolha == 1:
        total = n1 + n2
        print(f'SOMA é {total}')
    elif escolha == 2:
        total1 = n1 * n2
        print(f'MULTIPLICAÇÃO é {total1}')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é o número MAIOR')
        else:
            print(f'{n2} é o número MAIOR')
    elif escolha == 4:
        n1 = int(input('Informe o 1º: '))
        n2 = int(input('Informe o 2º: '))
    elif escolha > 5:
        print('ESCOLHA INVÁLIDA')
print('SAIU')


# ====== Como o professor fez:
from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    print('''   [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    ''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado entre {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=*=' * 10)
    sleep(2)
print('Fim do programa! Volte Sempre!')



