print('===== EXERCÍCIO 022 ====')
print("""Crie um programa que leia o nome completo de uma pessoa e mostre:
    > O nome com todas as letras maiúsculas:
    > O nome com todas as letras minúsculas:
    > Quantas letras ao todo(Sem considerar espaços)
    > Quantas letras tem o primero nome:""")
print('=' * 24)
print('')
nome = str(input('Qual o seu nome completo? ')).strip()
print(f'= COM TODAS AS LETRAS MAIÚSCULAS FICA ASSIM: {nome.upper()}')
print(f'= com todas as letras minúsculas fica assim: {nome.lower()}')
strip = nome.replace(' ', '')
print('= O nome possui {} letras ao todo'.format(len(strip)))
primeiro=nome.split()
quanto=len(primeiro[0])
first = primeiro[0]
print('= O primeiro nome é "{}" possui {} letras '.format(first,quanto))
print('=' * 24)
