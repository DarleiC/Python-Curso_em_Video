'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5: REPROVADO
- Média entre 5 e 6.9: RECUPERAÇÃO
- Média 7 ou superior: APROVADO
'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print(f'Sua média é: {media}')
if media < 5:
    print('REPROVADO!')
elif media >= 5 and media <=6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')