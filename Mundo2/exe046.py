'''Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artificio, indo de 10 até 0, com uma pause de 1s entre eles'''
import time
print ('iniciar contagem!')
for i in range(10,-1,-1):
    print(i)
    time.sleep(0.5)
print('KABUM!! \U0001f680 ')