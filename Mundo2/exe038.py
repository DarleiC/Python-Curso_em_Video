'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é MAIOR
- O segundo valor é MAIOR
- Não existe valor maior, os dois são iguais.
'''
num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe um número inteiro: '))

if num1 > num2:
    print(f'o número {num1} foi o primeiro digitado e é o maior')
elif num1 < num2:
    print(f'o número {num2} foi o segundo digitado e é o maior')
else:
    print('Os dois números são iguais')
