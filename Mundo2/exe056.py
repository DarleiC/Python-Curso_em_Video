''' Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa mostre:
- A MÉDIA DE IDADE DO GRUPO;
- QUAL O NOME DO HOMEM MAIS VELHO;
- QUANTAS MULHERS TEM MENOS DE 20 ANOS  '''
velho = 0
nome1 = ''
Idade = int(0)
mulhernova = 0
for c in range(1,5):
    nome = str(input(f'Nome do {c}ª: '))
    idade = int(input(f'Idade do {c}ª: '))
    sexo = str(input(f'''Sexo do {c}ª: 
( F ) FEMININO
( M ) MASCULINO
    : ''').upper())
    print(25*'+=')
    if idade > velho and sexo == 'M':
        velho = idade
        nome1 = nome
    if sexo == 'F' and idade < 20:
        mulhernova += 1
    Idade += idade
medias = Idade/4
if velho > 0:
    print(f'a média de idade do grupo é de : {medias} anos')
    print(f'o nome do homem mais velho é: {nome1} com idade de {velho} anos.')
    print(f'Tem {mulhernova} menor de 20 anos')
else:
    print('Não há homens na lista')
    print(f'a média de idade do grupo é de : {medias} anos')
    print(f'Tem {mulhernova} mulheres menor de 20 anos')

# COMO O PROFESSOR FEZ: ============================================
somaidade = 0 
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('-----{}ª PESSOA -----'. format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velhor tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulhers com menos de 20 anos'.format(totmulher20))


