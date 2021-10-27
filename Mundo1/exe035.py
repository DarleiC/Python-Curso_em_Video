print('===== EXERCÍCIO 035 ====')
print(' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo')
print('=' * 24)
r1 = float(input('Primeiro: '))
r2 = float(input('Segundo: '))
r3 = float(input('Terceiro: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO!')
