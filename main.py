import pygame
import random
import sys
import os
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,30'

pygame.init()
FPS = 60
clock = pygame.time.Clock()

Info = pygame.display.Info()
W, H = Info.current_w, Info.current_h

MAX_SNOW = 150
SNOW_SIZE = 64
BG_COLOR = (25, 25, 25)


def check_for_exit():
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit(0)

'_______________________MAIN______________________'

pygame.display.set_icon(pygame.image.load('snow.ico'))
pygame.display.set_caption('Snow')
screen = pygame.display.set_mode((W, H))

while True:
    check_for_exit()
    pygame.display.update()
    clock.tick(FPS)
