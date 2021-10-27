print('===== EXERCÍCIO 007 ====')
print('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.')
print('========================')

n1 = float(input('Primeira nota: '))
n2 = float(input('segunda nota: '))
m = (n1 + n2) / 2
print('A média entre {} e {} é igual a {:.2f}'.format(n1, n2, m))