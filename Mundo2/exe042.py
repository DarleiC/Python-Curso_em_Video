'''
Refaça o Desafio 35, dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: Todos os lados iguais;
- ISÓSCELES: Dois lados iguais;
- ESCALENO: Todos os lados diferentes;
'''
r1 = float(input('Primeiro: '))
r2 = float(input('Segundo: '))
r3 = float(input('Terceiro: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO!')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO!')