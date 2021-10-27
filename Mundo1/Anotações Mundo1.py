"""

!  Tipos Primitivos

"""
int()   #Somente Números Inteiros           EXEMPLO(1, -4, 0, 9875)
float() #Números Reais com Ponto Flutuante  EXEMPLO(4.5, 0.076, -15.223, 7.0)
bool()  #Valores Lógicos                    EXEMPLO(True , False)
str()   #Letras, Números e Caracteres       EXEMPLO('Olá', '7.5', '')
#? .format para formatar uma variável dentro de uma String
    print('A soma entre {} e {} vale {}'.format(n1,n2,s))
para objetos STRING é possível usar os métodos "IS"
print(n.isnumeric()) #Avalia se a string informada é numérico
print(n.isalpha())   #Avalia se a string que foi digitado é Letra
.istitle() #Avalia se a string tem Letras Maiusculas e Minusculas

"""
! operações Aritméticas 
"""
Operadores Binários que precisam de duas ou mais variáveis
+   ADIÇÃO'
-   SUBTRAÇÃO'
*   MULTIPLICAÇÃO'
/   DIVISÃO'
**  POTENCIAÇÃO' ('elevar um número 5²==25, por exemplo')
//  DIVISÃO INTEIRA' ('Divisão sem usar a vírgula')
%   RESTO DA DIVISÃO' ('O que sobrou da Divisão Inteira')
== ('Para quando for igual')

Todo operador precisa de um operando, um números ou variáveis que contém números

Ordem de Precedência
1 - ()
2 - **
3 - *, /, //, %
4 - +, -

> Primeiro vai ser executado os Parênteses, despois potências seguidos de Multiplicação, Divisões(Inteiras e Resto) e por ultimo Soma e Subtração

print('texto', end='') Antes de fechar o print o end não vai deixar quebrar a linha
\n #Para quebrar a linha

"""
? Módulos no Pyton 
"""
Fase 8-
    Bibliotecas 
    import biblioteca # importa todas as funcionalidades
    from biblioteca import # importa as funcionalidades que especificar

exemplos de Bibliotecas:

import math 
    ceil    arredondar para cima
    floor   arredondar para baixo
    trunc   retorna as partes inteiras de um float
    pow     potencia
    sqrt    Raiz quadrada
    factorial

quando importar somente uma funcionalidade use: Assim não é necessário colocar "math." para definir a funcionalidade, já que esta especificando quando importa a biblioteca
    from math import sqrt, floor

No site pyton.org é possível ver quais as bibliotecas existentes ou 
Lybrary Reference
    Bibliotecas do Pyton
PyPI
    Bibliotecas criadas pela comunidade    
====================================================
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de  {} é igual a {}.'.format(num, math.ceil(raiz)))
print('='*40)
# math.ceil arredonda pra cima
# math.floor arredonda pra baixo
#ABAIXO É IMPORTANDO ALGUMAS FUNCIONALIDADE DA BIBLIOTECA PARA NÃO PESAR O CÓDIGO
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de  {} é igual a {}.'.format(num, floor(raiz)))
print('='*40)
print('='*40)
print('Abaixo para gerar um número aleatório ou Sorteio')
import random
"""
? n = random.randint(1 , 10) # vai randomizar um numero inteiro
! random.shuffle(lista) #embaralhar uma lista
"""
import emoji
print(emoji.emojize('Oi pra ti :sunglasses:', use_aliases=True))
print('=' * 24)
==============
import pygame 
pygame.mixer.init()
pygame.mixer.music.load("Sorriso.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

"""
? Manipulando Cadeia de textos
"""
Uma string possui indices(cada letra se chama)
[] Colchetes se usa em LISTAS

a frase tem '20' indices "Curso em Vídeo Python"
frase = "Curso em Vídeo Python"
Fatiamento
    frase[9] - Vai selecionar somente um indice da frase
    frase[9:13] - Vai fatiar entre do 9 indice e o 12ª caractere(o ultimo valor não entra)
    frase[9:21:2] - Tras do 9º até o ultimo caractere pulando de DOIS EM DOIS, ou seja == Indices(9,11,13,15,17,19)
    frase[:5] - Assim tras todos os carcteres para tras do 5º indice
    frase[15:] - Assim tras todos os caracteres do 15º até o final
    frase[9::3] - Assim começa no 9º tras todos até o final pulando de 3 em 3

Analise
    len(frase) - mostra o comprimento da string
    frase.count('o') - Vai contas quantas vezes a letra o (Python é case sensitive)
    frase.count('o',0,13) - Assim aplicando o Fatiamento junto na Análise
    frase.find('deo') - Vai procurar na string e mostrar a posição que inicia
    frase.find('Android') - Quando não encontra a string o Python retorna -1
    'Curso' in frase - Se verdadeiro vai mostrar True

Transformação
        Através dos Métodos:
    frase.replace('Python','Android') - Assim ele vai buscar a Primeira string e substituir pela segunda string na string da variável
    frase.upper() - Assim vai deixar a string em Maísculo
    frase.lower() - Assim é o contrário de upper
    frase.capitalize() - Assim fica os indices lower e somente o primeiro indice Upper
    frase.title() - Vai analisar as palavras da string e deixar upper cada uma
    frase.strip() - Remove os espaços inúteis no começo e no fim da string
    frase.rstrip() - Remove somente os ultimos espaços
    frase.lstrip() - Remove somente os primeiros espaços

Divisão
    frase.split() - Vai dividir a string em uma lista através do seu limitador que por padrão é o Espaço, reorganizando os indices de cada string
    '-'.join(frase) -Vai juntar os elementos de uma string
=====
frase = 'Curso em Vídeo Python'
frase[::-1]
print(frase)
FRASE = frase.count('o',13,0)

dividido = frase.split()
print(dividido[2] [3]) #Assim vai trazer elemento 2 da string e o 3 indice do elemento
#print(frase.upper().count('O'))

"""
Aula 10 - CONDIÇÕES
"""
Em uma condição ou executa o bloco verdadeiro ou Falso, os dois ao mesmo tempo não.
Condição SImples só tem um IF
SE/ if
    BLOCO VERDADEIRO True
SENÃO/ else 
    BLOCO FALSO False

if condição():
    bloco True
else:
    bloco False
    
=EXEMPLO=
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('--FIM-- ')

#PARA RODAR UM DADO
import random
while True:
    print(''' 1. Roll the Dice \n 2. exit        ''')
    user = int(input('What you want to do\n'))
    if user == 1:
        number = random.randint(1, 6)
        print(number)
    else:
        break
        
CORES NO TERMINAL
    Padrão ANSI = Escape sequence
    Sempre que quiser usar COR:
        \033[ m = entre o ('[ e o m, vai o código')
            Style; Texte; Backgroud
        \033[0;33;44m
    PARA FUNDO BRANCO E LETRA PRETA USE: \033[7;30m
>>>>Style:
    0 = Nada
    1 = Negrito
    4 = Underline
    7 = Negativo
>>>>Texto:
    30 = BRANCO
    31 = VERMELHO
    32 = VERDE
    33 = AMARELO
    34 = AZUL
    35 = MAGENTA
    36 = CIANO
    37 = CINZA
>>>>Backgroud
    40 = BRANCO
    41 = VERMELHO
    42 = VERDE
    43 = AMARELO
    44 = AZUL
    45 = MAGENTA
    46 = CIANO
    47 = CINZA

nome = 'DARLEI'
cores = {'limpa':'\033[m','azul':'\033[34m'}
print('Olá, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))

    
    
    
    
    
    
    
    
    
    