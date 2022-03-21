'''Refaça o DESAFIO 51, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA(Progressão Arítimética), mostrando os 10 primeiros termos de uma progressão usando a estrutura WHILE
'''
a1 = int(input('Primeiro Termo: ')) #10
razao = int(input('Razão: '))       #2
decimo = a1 + (10 - 1) * razao      #28
c = 0
while c < 10:
    if c == 0:
        a1 = a1
    else:
        a1 = a1 + razao
    print(a1, '=>', end=' ')
    c += 1
print('ACABOU')

# ========== Como o professor fez

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('primeiro termo: '))
raz = int(input('Razáo PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += raz
    cont += 1
print('FIM!')