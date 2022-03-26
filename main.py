import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Screen information
disp_width = 700
disp_height = 850
#Font
smallfont = pygame.font.SysFont('Corbel',35)
#Colors
grey = (61,61,66)
light_grey = (170,170,170)
#Display
display = pygame.display.set_mode((disp_width, disp_height))

pygame.display.set_caption("Tetris Game")
display.fill(grey)
pygame.display.flip()
pygame.display.update()

#Surfaces
left_surf = pygame.Rect(20, 170, 150, 200)
left_surf_buttom = pygame.Rect(20, 490, 150, 250)
right_surf = pygame.Rect(560, 210, 120, 480)
game_surf = pygame.Rect(190, 150, 350, 650)
pygame.draw.rect(display, light_grey,game_surf)
pygame.draw.rect(display, light_grey,left_surf_buttom)
pygame.draw.rect(display, light_grey,left_surf)
pygame.draw.rect(display, light_grey,right_surf)
pygame.display.flip()



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

