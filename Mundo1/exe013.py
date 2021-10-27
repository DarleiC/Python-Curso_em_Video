print('===== EXERCÍCIO 013 ====')
print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')
print('=' * 24)

s=float(input('Qual o salário: R$ '))
novo = s+(s*15/100)
print('O novo salário é {}'.format(novo))