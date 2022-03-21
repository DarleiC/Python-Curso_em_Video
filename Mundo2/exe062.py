'''Melhore o desafio 61:
Perguntando para o usuário se ele quer mostrar mais alguns termos.(do ultimo termo até o número que o usuário informou)
O programa encerra quando ele disse que quer mostrar 0 termos.
'''
print('Gerador de PA')
print('-=' * 10)
quanto = int(input('Quantos termos quer ver? '))
primeiro = int(input('Inicia em qual: '))  
raz = int(input('Qual Razão : '))           
termo = primeiro                            
cont = 1
quer = 1
while quer > 0:
    while cont <= quanto:
        print('{} -> '.format(termo), end='')
        termo += raz
        cont += 1
    print('Aguardando...')
    quer = int(input('\n Quer ver mais quantos termos?: [0 para sair] '))
    quanto += quer
print(f'FIM! com {cont - 1} termos exibidos')

# ========= Como o professor fez:

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('primeiro termo: '))
raz = int(input('Razáo PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += raz
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos vocë quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))









