print('===== EXERCÍCIO 006 ====')
print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')
print('========================')

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} vale {}'.format(n,d))
print('O triplo de {} vale {}. \nA raiz quadrad de {} é igual a {:.2f}'.format(n,t,n,r))