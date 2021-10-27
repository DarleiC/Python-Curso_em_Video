''' Refaça o DESAFIO 9, mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando um laço "for" '''
n = int(input('Qual número: '))
#cont = 0
for t in range(1,11):
    #cont += 1
    total = t * n 
    print(f'{n} x {(t):2} = {total}')

#como o professor fez
num = int(input('Qual número: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(num, c, num*c))

