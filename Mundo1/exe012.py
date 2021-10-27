print('===== EXERCÍCIO 012 ====')
print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')
print('=' * 24)

preco = float(input('Qual o preço do produto: R$ '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f} na promoção com 5% de desconto é R${:.2f}'.format(preco, novo))



# PREÇO*PORCENTAGEM/100