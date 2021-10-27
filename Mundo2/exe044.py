'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
- a vista DINHEIRO/CHEQUE: 10% de desconto;
- a vista no CARTÃO: 5% de desconto;
- em até 2x NO CARTÃO: Preço normal;
- em 3x ou mais NO CARTÃO: 20% de Juros;
'''
pn = float(input('Preço normal: R$ '))
cp = int(input('''Como deseja pagar:
[ 1 ] A VISTA DINHEIRO/CHEQUE(- 10%)
[ 2 ] A VISTA CARTÃO(- 5%)
[ 3 ] 2X NO CARTÃO(S/ DESCONTO OU JUROS)
[ 4 ] 3X OU MAIS NO CARTÃO (20% DE JUROS)
Qual Opção: '''))
if cp == 1:
    v = pn - (pn * 10 /100)
    print(f'Vai custar R$ {v}')
elif cp == 2:
    v = pn - (pn * 5 / 100)
    print(f'Vai custar R$ {v}')
elif cp == 3:
    v = pn / 2
    print(f'Em 2X a parcela vai ser: R$ {v}')
elif cp == 4:
    x = int(input('Quantas Parcelas? '))
    v = pn + (pn * 20 / 100)
    p = v / x
    print('Vai custar R$ {:.2f} e dividido em {}x a parcela vai ser R$ {:.2f}'.format(v,x,p))
else:
    print('Opção inválida!')
