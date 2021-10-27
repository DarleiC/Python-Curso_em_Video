print('===== EXERCÍCIO 034 ====')
print(""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
      Para salários acima de R$1.250,00, calcule um aumento de 10%
      Para inferiores ou iguais o aumento é de 15%""")
print('=' * 24)
while True:
      quer = int(input(('Calcular? 1=SIM 2=NÃO: ')))
      if quer == 1:
            print('=' * 40)
            salario = float(input('Qual seu salário: R$'))
            if salario > 1250:
                  novo = salario+(salario*10/100)
            if salario <= 1250:
                  novo = salario+(salario*15/100)
            print('> Seu novo salário é: \n R$ {:.2f}\n'.format(novo))
      elif quer == 2:
            print('====== Cálculos encerrados! ======')
            break