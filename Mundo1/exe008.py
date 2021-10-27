print('===== EXERCÍCIO 008 ====')
print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.')
print('========================')

n = float(input('Informe um valor Metros para converter: '))
cm = n * 100 
mm = n * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(n, cm, mm))