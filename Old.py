# import pygame, sys
# from pygame.locals import *
# import random
# from constructor import Builder
#
# pygame.init()
#
# bdr = Builder()
# display = bdr.Display()
#
# obj = pygame.Surface(bdr.objSize)
# frameSurf = pygame.Surface(bdr.frameSize)
# display.fill(bdr.grey)
# pygame.display.flip()
#
# # BOUNDARIES
# upper = (170, 100), (510, 100)
# bottom = (170, 800), (510, 800)
# left = (170, 100), (170, 800)
# right = (510, 100), (510, 800)
# sidebounds = (175, 400)
# altbounds = (100, 810)
#
# # FIGURES
#
#
# x1 = (bdr.xGridLoc[5], bdr.yGridLoc[1])
# x2 = (bdr.xGridLoc[5], bdr.yGridLoc[2])
# x3 = (bdr.xGridLoc[5], bdr.yGridLoc[3])
# x4 = (bdr.xGridLoc[5], bdr.yGridLoc[4])
# y1 = (bdr.xGridLoc[6], bdr.yGridLoc[1])
# y2 = (bdr.xGridLoc[6], bdr.yGridLoc[2])
# y3 = (bdr.xGridLoc[6], bdr.yGridLoc[3])
# y4 = (bdr.xGridLoc[6], bdr.yGridLoc[4])
#
# blockX1 = pygame.Surface(bdr.blockSize)
# blockX2 = pygame.Surface(bdr.blockSize)
# blockX3 = pygame.Surface(bdr.blockSize)
# blockX4 = pygame.Surface(bdr.blockSize)
# blockY1 = pygame.Surface(bdr.blockSize)
# blockY2 = pygame.Surface(bdr.blockSize)
# blockY3 = pygame.Surface(bdr.blockSize)
#
#
# blocks_cords = []
# cord = [(1, 1),
#         (1, 1),
#         (0, 0)]
# x1On, x2On, x3On, x4On, y1On, y2On,y3On = False, False, False, False, False, False, False
#
# shape = [(0, 0, 0, 0),
#          (0, 0, 0, 0),
#          (0, 0, 0, 0),
#          (0, 0, 0, 0)]
#
#
#
#
#
#
#
# if cord[0][0] == 1:
#     x1On = True
#     x1 = [bdr.xGridLoc[5], bdr.yGridLoc[1]]
#     blockX1 = pygame.Surface(bdr.blockSize)
#     blocks_cords.append(x1)
# else:
#     blocks_cords.append((0,0))
# if cord[1][0] == 1:
#     x2On = True
#     x2 = [bdr.xGridLoc[5], bdr.yGridLoc[2]]
#     blockX2 = pygame.Surface(bdr.blockSize)
#     blocks_cords.append(x2)
# else:
#     blocks_cords.append((0,0))
# if cord[2][0] == 1:
#     x3On = True
#     x3 = [bdr.xGridLoc[5], bdr.yGridLoc[3]]
#     blockX3 = pygame.Surface(bdr.blockSize)
#     blocks_cords.append(x3)
# else:
#     blocks_cords.append((0,0))
# if cord[0][1] == 1:
#     y1On = True
#     y1 = [bdr.xGridLoc[6], bdr.yGridLoc[1]]
#     blockY1 = pygame.Surface(bdr.blockSize)
#     blocks_cords.append(y1)
# else:
#     blocks_cords.append((0,0))
# if cord[1][1] == 1:
#     y2 = [bdr.xGridLoc[6], bdr.yGridLoc[2]]
#     blockY2 = pygame.Surface(bdr.blockSize)
#     blocks_cords.append(y2)
#     y2On = True
# else:
#     blocks_cords.append((0,0))
# if cord[2][1] == 1:
#     y3 = [bdr.xGridLoc[6], bdr.yGridLoc[3]]
#     blockY3 = pygame.Surface(bdr.blockSize)
#     blocks_cords.append(y3)
#     y3On = True
# else:
#     blocks_cords.append((0,0))
#
# print(blocks_cords)
# tempX = bdr.x
# tempY = bdr.y
# idleObjs = {}
# idleObjsCoors = {}
# activeObj = obj
# numObjs = 0
# bubbleDown = .2
# sidemov = 34
#
# sdb = 240
# run = True
# while run == True:
#
#     for event in pygame.event.get():
#
#         if event.type == pygame.QUIT:
#             sys.exit()
#             run = False
#
#         # Single Key
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT: # and 135 < sdb
#                 bdr.pressed_keys["left"] = True
#                 if x1On == True:
#                     sdb -=sidemov
#                     blocks_cords[0][0] -= sidemov
#                 if x2On == True:
#                     sdb -= sidemov
#                     blocks_cords[1][0] -= sidemov
#                 if x3On == True:
#                     sdb -= sidemov
#                     blocks_cords[2][0] -= sidemov
#                 if y1On == True:
#                     sdb -= sidemov
#                     blocks_cords[3][0] -= sidemov
#                 if y2On == True:
#                     sdb -= sidemov
#                     blocks_cords[4][0] -= sidemov
#                 if y3On == True:
#                     sdb -= sidemov
#                     blocks_cords[5][0] -= sidemov
#             if event.key == pygame.K_RIGHT: # and sdb < 400
#                 bdr.pressed_keys["right"] = True
#
#                 if x1On == True:
#                     blocks_cords[0][0] += sidemov
#                 if x2On == True:
#                     sdb += sidemov
#                     blocks_cords[1][0] += sidemov
#                 if x3On == True:
#                     sdb += sidemov
#                     blocks_cords[2][0] += sidemov
#                 if y1On == True:
#                     sdb += sidemov
#                     blocks_cords[3][0] += sidemov
#                 if y2On == True:
#                     sdb += sidemov
#                     blocks_cords[4][0] += sidemov
#                 if y3On == True:
#                     sdb += sidemov
#                     blocks_cords[5][0] += sidemov
#
#         else:
#             bdr.pressed_keys["left"] = False
#             bdr.pressed_keys["right"] = False
#     # Holding key
#     # if bdr.pressed_keys["left"] and tempX >= sidebounds[0]:
#     #     if x1On == True:
#     #         blocks_cords[0][0] += sidemov
#     #     if x2On == True:
#     #         blocks_cords[1][0] += sidemov
#     #     if x3On == True:
#     #         blocks_cords[2][0] += sidemov
#     #     if y1On == True:
#     #         blocks_cords[3][0] += sidemov
#     #     if y2On == True:
#     #         blocks_cords[4][0] += sidemov
#     #     if y3On == True:
#     #         blocks_cords[5][0] += sidemov
#     # elif bdr.pressed_keys["right"] and tempX <= sidebounds[1] - 25:
#     #     if x1On == True:
#     #         blocks_cords[0][0] += bubbleDown
#     #     if x2On == True:
#     #         blocks_cords[1][0] += bubbleDown
#     #     if x3On == True:
#     #         blocks_cords[2][0] += bubbleDown
#     #     if y1On == True:
#     #         blocks_cords[3][0] += bubbleDown
#     #     if y2On == True:
#     #         blocks_cords[4][0] += bubbleDown
#     #     if y3On == True:
#     #         blocks_cords[5][0] += bubbleDown
#
#
#
#
#
#
#         # if x >= 500
#
#     # display.fill(bdr.main_color)
#     # tempY += .2
#     display.blit(frameSurf, (170, 100))
#     # display.blit(activeObj, (tempX, tempY))
#     # activeObj.fill(bdr.white)
#
#     if numObjs > 0:
#         print('ssss')
#         for i in range(1, numObjs + 1):
#             idleObjs["Obj" + str(i)].fill(bdr.white)
#             display.blit(idleObjs["Obj" + str(i)], idleObjsCoors["ObjCoords" + str(i)])
#
#     frameSurf.fill(bdr.main_color)
#
#     pygame.draw.line(display, bdr.blue, (170, 100), (510, 100), 2)
#     pygame.draw.line(display, bdr.blue, (170, 800), (510, 800), 2)
#     pygame.draw.line(display, bdr.blue, (170, 100), (170, 800), 2)
#     pygame.draw.line(display, bdr.blue, (510, 100), (510, 800), 2)
#
#
#     if x1On == True:
#         blocks_cords[0][1] += bubbleDown
#         display.blit(blockX1, (blocks_cords[0][0], blocks_cords[0][1]))
#         blockX1.fill(bdr.white)
#     if x2On == True:
#         blocks_cords[1][1] += bubbleDown
#         display.blit(blockX2, (blocks_cords[1][0], blocks_cords[1][1]))
#         blockX2.fill(bdr.white)
#     if x3On == True:
#         blocks_cords[2][1] += bubbleDown
#         display.blit(blockX3, (blocks_cords[2][0], blocks_cords[2][1]))
#         blockX3.fill(bdr.white)
#     if y1On == True:
#         blocks_cords[3][1] += bubbleDown
#         display.blit(blockY1, (blocks_cords[3][0], blocks_cords[3][1]))
#         blockY1.fill(bdr.white)
#     if y2On == True:
#         blocks_cords[4][1] += bubbleDown
#         display.blit(blockY2, (blocks_cords[4][0], blocks_cords[4][1]))
#         blockY2.fill(bdr.white)
#     if y3On == True:
#         blocks_cords[5][1] += bubbleDown
#         display.blit(blockY3, (blocks_cords[5][0], blocks_cords[5][1]))
#         blockY3.fill(bdr.white)
#
#     for i in range(20):
#         hline = i
#         if i <= 10:
#             vline = i
#             pygame.draw.line(display, bdr.gridc, (bdr.wideGrid[vline], 100), (bdr.wideGrid[vline], 800), 2)
#         pygame.draw.line(display, bdr.gridc, (170, bdr.tallGrid[hline]), (510, bdr.tallGrid[hline]), 2)
#     pygame.draw.line(display, bdr.blue, (170, 100), (510, 100), 3)
#     pygame.draw.line(display, bdr.blue, (170, 800), (510, 800), 3)
#     pygame.draw.line(display, bdr.blue, (170, 100), (170, 800), 3)
#     pygame.draw.line(display, bdr.blue, (510, 100), (510, 800), 3)
#
#     if tempY >= altbounds[1] - 50:
#         print('enter')
#         numObjs += 1
#         idleObjs["Obj" + str(numObjs)] = activeObj
#         idleObjsCoors["ObjCoords" + str(numObjs)] = (tempX, tempY)
#         activeObj = obj = pygame.Surface(bdr.objSize)
#         tempX = bdr.x
#         tempY = bdr.y
#     pygame.display.flip()
#     # clock.tick(60)
# x1On ,x2On ,x3On ,y1On ,y2On ,y3On = False, False, False, False, False, False
# sidebounds = (175, 500)