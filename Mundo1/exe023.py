print('===== EXERCÍCIO 023 ====')
print("""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
      EX: 1834
      UNIDADE: 4
      DEZENA: 3
      CENTENA: 8
      MILHAR: 1""")
print('=' * 24)
print('')
num = int(input('Informe um número inteiro entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f' UNIDADE: {u}')
print(f' DEZENA:  {d}')
print(f' CENTEZA: {c}')
print(f' MILHAR:  {m}')
          