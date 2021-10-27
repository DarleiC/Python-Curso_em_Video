'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa. calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: PESO IDEAL
- 25 Até 30: SOBREPESO
- 30 até 40: OBESIDADE
- Acima de 40: OBESIDADE MÓRBIDA
'''
p = float(input('Seu peso: '))
a = float(input('Sua altura: '))
imc = p / (a*a)
print('SEU IMC É: {:.2f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')