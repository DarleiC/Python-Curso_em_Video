print('===== EXERCÍCIO 026 ====')
print("""Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A":
> Em que posição ela aparece pela primeira vez:
> Em que posição ela aparece pela última vez:""")
print('=' * 24)
print('')
frase = str(input('Escreva uma frase aleatória: ')).strip().upper()
print('A letra A aparece {}x na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))



#COMO FIZ
#print('A letra A(Maiúscula) aparece {}x'.format(frase.count('A')))
#primeiro = frase.find('A')+1
#print('A primeira esta localizada na posição: {}'.format(primeiro))
#ultimo = frase.rfind('A')+1
#print('A ultima esta localizada na posição: {}'.format(ultimo))
