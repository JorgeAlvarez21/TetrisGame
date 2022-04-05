# import pygame, sys
# from pygame.locals import *
# import random
#
# pygame.init()
#
# FPS = 60
# FramePerSec = pygame.time.Clock()
#
# # Screen information
# disp_width = 700
# disp_height = 850
# #Font
# smallfont = pygame.font.SysFont('Corbel',35)
# #Colors
# grey = (61,61,66)
# light_grey = (20,20,60)
# main_color = (0,0,20)
# #Display
# display = pygame.display.set_mode((disp_width, disp_height))
#
# pygame.display.set_caption("Tetris Game")
# display.fill(light_grey)
# pygame.display.flip()
# pygame.display.update()
#
#
#
#
#
# #Images
# logoimg = pygame.image.load('tetris-logo.png')
# logoimg = pygame.transform.scale(logoimg, (470, 190))
# display.blit(logoimg, (130, 20))
#
#
# pygame.display.update()
#
# #MOVEMENT
# velocity = 12
# x = 400
# y = 20
#Add surface to move
# run = True
# # while run == True:
# #     display.fill(grey)
# #     display.blit(gr, (x, y))
# #     for event in pygame.event.get():
# #         if event.type == QUIT:
# #             run = False
# #             pygame.quit()
# #             sys.exit()
# #
# #         if event.type == pygame.KEYDOWN:
# #             if event.key == pygame.K_LEFT:
# #                 x -= velocity
# #             if event.key == pygame.K_RIGHT:
# #                 x += velocity
# #             key_pressed_is = pygame.key.get_pressed()
#
# pressed_keys = {"left": False, "right": False, "up": False, "down": False}
#
# while run ==  True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 pressed_keys["left"] = True
#             if event.key == pygame.K_RIGHT:
#                 pressed_keys["right"] = True
#         else:
#             pressed_keys["left"] = False
#             pressed_keys["right"] = False
#
#     if pressed_keys["left"]:  # == True is implied here
#         x -= velocity/3
#     if pressed_keys["right"]:
#         x += velocity/3
#     pygame.display.update()
#     # clock.tick(60)
#
# #Surfaces
# main_frame = pygame.Rect(10, 10, 680, 830)
# left_surf = pygame.Rect(20, 220, 150, 120)
# left_surf_buttom = pygame.Rect(20, 380, 150, 170)
# left_surf_buttom1 = pygame.Rect(20, 600, 150, 40)
# left_surf_buttom2 = pygame.Rect(20, 670, 150, 40)
# left_surf_buttom3 = pygame.Rect(20, 740, 150, 40)
# right_surf = pygame.Rect(560, 270, 120, 500)
# pygame.draw.rect(display, light_grey, main_frame)
# pygame.draw.rect(display, light_grey, left_surf_buttom)
# pygame.draw.rect(display, light_grey, left_surf)
# pygame.draw.rect(display, light_grey, right_surf)
# pygame.draw.rect(display, light_grey, left_surf_buttom1)
# pygame.draw.rect(display, light_grey, left_surf_buttom2)
# pygame.draw.rect(display, light_grey, left_surf_buttom3)
# pygame.display.flip()
# pygame.display.update()
# thisvar = 'Esta'