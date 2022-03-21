''' https://prnt.sc/227y5x9
Crie um programa que leia o NOME e o PREÇO de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam MAIS de R$ 1000
C) Qual é o NOME do produto mais barato
'''
total = qtdmais = valor = i = 0
nomemenos = ' ' 

while True:
    nomeProd = str(input('Nome: '))
    preco = float(input('Preco: '))
    if preco > 1000:
        qtdmais += 1
    if i == 0:
        valor = preco
    elif preco < valor:
        valor = preco
        nomemenos = nomeProd
    total += preco
    i += 1
    mais = ' ' 
    while mais not in 'SN':
        mais = str(input('Mais? [S/N]')).upper()
    if mais == 'N':
        break
print(f'''  Total:{total} \n  QTD ACIMA DE 1000: {qtdmais}\n  Nome do Mais barato: {nomemenos}
''')

############# COMO O PROFESSOR FEZ ####################
total = totmil = menor = cont =0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto       
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato}, custa R$ {menor:.2f}')












