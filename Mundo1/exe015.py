print('===== EXERCÍCIO 015 ====')
print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
print('=' * 24)

km = float(input('Quantos KM o veículo rodou? '))
d = float(input('Quantos dias usou o carro? '))
print(' O custo do aluguel do veículo é R$ {:.2f}'.format((d*60)+(km*0.15)))
print('=' * 24)
