'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento;
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
* BONUS, SABER O SEXO DA PESSOA E DIZER SE DEVE SE ALISTAR
'''
from datetime import date
atual = date.today().year
s = str(input(''''Informe seu sexo: 
[M] MASCULINO
[F] FEMININO
''')).upper()
if s == 'M':
    nasc = int(input('Em que ano nasceu? '))
    idade = atual - nasc
    print(f'Voce tem {idade} anos')
    if idade < 18:
        falta = 18 - idade
        print(f'Ainda faltam {falta} anos para se alistar')
        ano = atual + falta
        print(f'Seu alistamento será em {ano}')
    elif idade == 18:
        print('Você deve se alistar agora!')
    else:
        falta = idade - 18
        print(f'Você deveria se alistar ha {falta} anos atras')
        ano = atual - falta
        print(f'Seu alistamento foi em {ano}')
else:
    print('Você não precisa se alistar')