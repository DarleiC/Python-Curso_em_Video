print('===== EXERCÍCIO 021 ====')
print('21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. ')
print('=' * 24)

import pygame
pygame.mixer.init()
pygame.mixer.music.load('Sorriso.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
