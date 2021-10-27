print('===== EXERCÍCIO 027 ====')
print("""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
> Ex: Ana Maria de Souza
 primeiro: Ana
 último: Souza""")
print('=' * 24)

nome = str(input('Informe seu nome completo: ')).strip()
primeiro = nome.split()
print(primeiro)
print ('Seu primeiro nome é: {}'.format(primeiro [0]))
print ('Seu ultimo nome é: {}'.format(primeiro[-1]))
 