import pygame
from time import sleep

print('\033[1;32mTOCANDO MÚSICA EM:\033[m ')

for i in range(10, -1, -1):
    print(i)
    sleep(1)
pygame.init()
pygame.mixer.music.load('ex046.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
