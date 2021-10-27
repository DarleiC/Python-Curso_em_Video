a='='*40
print(a*2)
print('>>>>>>>>> Desafio Aula 7 <<<<<<<<<')
print('Peça o nome e dois valores e calcule a SOMA, MULTIPLICAÇÃO, DIVISÃO, DIVISÃO INTEIRA, RESTO e a POTÊNCIA')
print('')
nome = input('Qual o seu nome?: ')
print(' - Prazer em conhecer, {:=^20}!'.format(nome))
n1=int(input(' - {}, informe um valor: '.format(nome)))
n2=int(input(' - {}, informe outro: '.format(nome)))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
r=n1%n2
e=n1**n2
print('  A SOMA vale: > {} <\n  O PRODUTO: > {} <\n  A DIVISÃO: > {:.3F} <'.format(s,m,d))
print('  A DIVISÃO INTEIRA: > {} <\n  o RESTO: > {} <\n  A POTÊNCIA: > {} <'. format(di,r,e))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')
print('>>>>>>>>> Desafio Aula 7 - 1 <<<<<<<<<')
print('')
print('> Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor')
print('>')
n3=int(input(' - {}, informe um valor: '.format(nome)))
print('o número Sucessor é: {}'.format(n3+1))
print('o número Antecessor é {}'.format(n3-1))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')
print('>>>>>>>>> Desafio Aula 7 - 2 <<<<<<<<<')
print('')
print('> Crie um Algoritmo que leia um número e mostre o DOBRO, TRIPLO e a RAIZ QUADRADA')
print('>')
n4=int(input(' - {}, informe um valor: '.format(nome)))
print('o DOBRO é {}'.format(n4*2))
print('o TRIPLO é {}'.format(n4*3))
print('a RAIZ QUADRADA é {}'.format(n4**(1/2))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')
print('>>>>>>>>> Desafio Aula 7 - 3 <<<<<<<<<')
print('')
print('> Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média')
print('>')
nota1 = float(input('Informe a Primeira Nota: '))
nota2 = float(input('Informe a Segunda Nota:'))
media = (nota1 + nota2) / 2
print('> A Média do Aluno é: {}'.format(media))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')
print('>>>>>>>>> Desafio Aula 7 - 4 <<<<<<<<<')
print('')
print('> Escreva um programa que leia um valor em Metros e o exiba convertido em centímetros e milímetros')
print('>')
metro = float(input('- Informe quantos metros quer converter: '))
print('A conversão em centímetros é: {:.2f}cm'.format(metro*100))
print('A conversão em milimetros é: {:.2f}mm'.format(metro*1000))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')
print('>>>>>>>>> Desafio Aula 7 - 5 <<<<<<<<<')
print('')
print('> Faça um programa que leia um número Inteiro qualquer e mostra na tela a sua tabuada')
print('>')
tabua = int(input('Quer saber a Tabuada de qual Número? '))
x1 = tabua*1
x2 = tabua*2
x3 = tabua*3
x4 = tabua*4
x5 = tabua*5
x6 = tabua*6
x7 = tabua*7
x8 = tabua*8
x9 = tabua*9
x10 = tabua*10
print('{} x 01 = {}'.format(tabua,x1))
print('{} x 02 = {}'.format(tabua,x2))
print('{} x 03 = {}'.format(tabua,x3))
print('{} x 04 = {}'.format(tabua,x4))
print('{} x 05 = {}'.format(tabua,x5))
print('{} x 06 = {}'.format(tabua,x6))
print('{} x 07 = {}'.format(tabua,x7))
print('{} x 08 = {}'.format(tabua,x8))
print('{} x 09 = {}'.format(tabua,x9))
print('{} x 10 = {}'.format(tabua,x10))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')
print('>>>>>>>>> Desafio Aula 7 - 6 <<<<<<<<<')
print('')
print('> Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar')
print('>')
d=float(input('Informe a Cotação atual do Dólar: $ '))
c=float(input('Quanto dinheiro você tem na Carteira: R$ '))
print('Você consegue comprar: $ {:.2f}'.format(c/d))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')
print('>>>>>>>>> Desafio Aula 7 - 7 <<<<<<<<<')
print('')
print('> Faça um programa que leia a Largura e a Altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²')
print('>')
h = float(input('Informe a Altura da Parede em Metros: '))
l = float(input('Informe a Largura da Parede em Metros: '))
area =h*l
tinta = area/2
print('> A área da parede é: {} m² e para pintá-la será necessário {} Litros de tinta'.format(area, tinta))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')
print('>>>>>>>>> Desafio Aula 7 - 8 <<<<<<<<<')
print('')
print('> Faça um Algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto')
print('>')
preco = float(input('Qual o preço atual: R$ '))
print('O preço atual do produto com 5% de Desconto é R$ {:.2f}'. format(preco-(5/100*preco))
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
input('Para seguir para o próximo desafio aperte ENTER')
print(a)
print('')
print('>>>>>>>>> Desafio Aula 7 - 9 <<<<<<<<<')
print('')
print('> Faça um Algoritmo que leia o Salário e mostre seu novo Salário com 15% de aumento')
print('>')
salario = float(input('Informe seu salário atual: R$ '))
print('Seu salário recebeu um aumento de 15% e agora é: R$ {:.2f}'.format(salario+(15/100)*salario))









#{:^20} centralizar em 20 espaços
#{:>20} alinhar a direita em 20 espaços
#{:=^20} o caractere entre o ':' e o '>' vai preencher o espaço vazio do limite
#divisão: {:.3F} ASSIM DEFINO QUESERA 3 PONTOS FLUTUANTES OU VAI TER 3 CASAS DECIMAIS




