print('===== EXERCÍCIO 011 ====')
print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.')
print('=' * 24)

larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
area = larg * alt
print(' Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(larg, alt, area))
tinta = area / 2
print(' Para pintar a parede vai precisar de {:.2f}l de tinta'.format(tinta))
print('=' * 24)
