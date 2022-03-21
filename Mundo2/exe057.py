'''Fça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Qual o sexo [M/F]? ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informou sexo inválido, tente de novo: ')).upper()
print(f'Informou {sexo}')

# ====== Como o professor fez:

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


