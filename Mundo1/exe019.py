print('===== EXERCÍCIO 019 ====')
print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido. ')
print('=' * 24)
from random import choice
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))