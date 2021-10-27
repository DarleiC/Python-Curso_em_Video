print('===== EXERCÍCIO 014 ====')
print('Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.')
print('=' * 24)

t = float(input('Informe a Temperatura em ºC: '))
f = (t*1.8)+32
print(' {:.2f}ºC em Fahrenheit é {:.2f}ºF'.format(t, f))
print('=' * 24)