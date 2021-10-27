'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
Calcule o valor da prestação mensal, 
sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
''' 
vcasa = float(input("Quanto custa a casa? R$ "))
vsalario = float(input("Informe seu salário? R$ "))
anos = int(input("em quantos anos quer pagar? "))* 12

tetomensal = (vsalario * 30) / 100
vprestacao = vcasa/anos

if tetomensal >= vprestacao:
    print("Empréstimo APROVADO. pois o valor da prestação R$ {:.2f}!".format(vprestacao))
else:
    print("Empréstimo NEGADO, pois o valor da prestação é R$ {:.2f}".format(vprestacao))
