''' Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa mostre:
- A MÉDIA DE IDADE DO GRUPO;
- QUAL O NOME DO HOMEM MAIS VELHO;
- QUANTAS MULHERS TEM MENOS DE 20 ANOS  '''
lista = []
Idade1 = 0
velho = 0
for c in range(1,5):
    Nome = str(input(f'Nome da {c}ª: ')).upper()
    Idade = int(input(f'Idade da {c}ª: '))
    Sexo = str(input(f'Sexo da {c}ª: ')).upper()
    print(5*'==')
    Idade1 = Idade1 + Idade
    lista.append(Nome, Idade, Sexo)
    if c == 1:
        velho = Idade
    else:
        if Idade > velho:
            velho = Idade
            nome = Nome
Idade = Idade1/4
print(Idade)








