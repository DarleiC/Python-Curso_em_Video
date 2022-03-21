''' https://prnt.sc/227xq0g
Crie um programa que leia a IDADE e o SEXO de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou nao continuar.
No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''
mais18 = homem = mulher20 = 0
while True:
    idade = int(input('Idade: ')) 
    sexo = ' '
    while sexo not in 'MF': 
        sexo = str(input('Sexo? [M/F]')).upper()
    if sexo == 'M':
        homem += 1
        if idade > 18:
            mais18 += 1
    if sexo == 'F':
        if idade > 19:
            mais18 += 1
        elif idade <= 19 :
            mulher20 += 1
            if idade == 19:
                mais18 += 1
    mais = ' '
    while mais not in 'SN':    
        mais = str(input('Cadastrar mais? ')).upper()
    if mais == 'N':
        break
print(f'=== Acabou ===  \n +18 = {mais18} \n HOMEM = {homem} \n -20 MULHER  = {mulher20}')

########### COMO O PROFESSOR FEZ #################

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')








