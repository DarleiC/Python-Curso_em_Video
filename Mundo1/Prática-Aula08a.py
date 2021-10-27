a='='*40
print(a*2)
print('>>>>>>>> Desafios Aula 8 - 1 <<<<<<<<<')
print('Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. ')
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
#Dica, explorar "import math"
from math import trunc
n = float(input('Informe um número Real: '))
print(' A parte inteira do número {} é {}'.format(n, trunc(n)))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
print('>>>>>>>> Desafios Aula 8 - 2 <<<<<<<<<')
print('Faça um programa que leia o comprimenTo do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa:')
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
from math import hypot
oposto = float(input('Informe o Cateto Oposto: '))
adjacente = float(input('Informe o Cateto Adjacente: '))
print(' A Hipotenusa do Triangulo Retângulo é {:.5f}'.format(hypot(oposto, adjacente)))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
print('>>>>>>>> Desafios Aula 8 - 3 <<<<<<<<<')
print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do Seno, Cosseno e Tangente desse ângulo: ')
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
from math import sin, cos, tan, radians
angulo=float(input('Informe um ângulo: '))
print(' Do ângulo {} º o Seno é {:.2f} Cosseno {:.2f} e a Tangente {:.2f}'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
print('>>>>>>>> Desafios Aula 8 - 4 <<<<<<<<<')
print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido ')
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
from random import choice, shuffle 
al1 = input('Informe o nome do 1ª: ')
al2 = input('Informe o nome do 2ª: ')
al3 = input('Informe o nome do 3ª: ')
al4 = input('Informe o nome do 4ª: ')
lista=[al1, al2, al3, al4]
print(' O aluno escolhido foi >>> {}'.format(choice(lista)))
print(('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'))
input('Para seguir para o próximo desafio aperte ENTER')
#print(a)
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
print('>>>>>>>> Desafios Aula 8 - 5 <<<<<<<<<')
print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. ')
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
input('Para realizar o sorteio aperte ENTER')
shuffle(lista)
print('A ordem de apresentação dos trabalhos será: {}'.format(lista))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
print('>>>>>>>> Desafios Aula 8 - 6 <<<<<<<<<')
print(' Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3 ')
print('')#ESPAÇO EM BRANO PARAPULAR A LINHA
import pygame

