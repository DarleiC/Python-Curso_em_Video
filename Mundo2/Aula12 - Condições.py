#Condições aninhadas
nome = str(input('Qual seu nome? '))
if nome == 'Darlei':
    print('Belo nome!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Nome Popular!')
else:
    print('Nome normal!')
print('Tenha um bom dia, {}!'.format(nome))


