import pygame, sys
from pygame.locals import *
import random
import figures
from constructor import Builder
import time as timer

pygame.init()
bdr = Builder()
display = bdr.Display()
frameSurf = pygame.Surface(bdr.frameSize)
running = True


eleInv = {
'eleInvRot0' : [ [bdr.xgridB[5], bdr.ygridB[0]], [bdr.xgridB[5], bdr.ygridB[1]], [bdr.xgridB[5], bdr.ygridB[2]], [bdr.xgridB[4], bdr.ygridB[2]] ],
'eleInvRot1'  : [ [bdr.xgridB[4], bdr.ygridB[0]], [bdr.xgridB[4], bdr.ygridB[1]], [bdr.xgridB[5], bdr.ygridB[1]], [bdr.xgridB[6], bdr.ygridB[1]] ],
'eleInvRot2' : [ [bdr.xgridB[4], bdr.ygridB[0]], [bdr.xgridB[5], bdr.ygridB[0]], [bdr.xgridB[4], bdr.ygridB[1]], [bdr.xgridB[4], bdr.ygridB[2]] ],
'eleInvRot3' : [ [bdr.xgridB[4], bdr.ygridB[0]], [bdr.xgridB[5], bdr.ygridB[0]], [bdr.xgridB[6], bdr.ygridB[0]], [bdr.xgridB[6], bdr.ygridB[1]] ]
}
te = {
'teRot0' :  [[bdr.xgridB[5], bdr.ygridB[0]], [bdr.xgridB[4], bdr.ygridB[1]], [bdr.xgridB[5], bdr.ygridB[1]], [bdr.xgridB[6], bdr.ygridB[1]]],
'teRot1'  : [[bdr.xgridB[4], bdr.ygridB[0]], [bdr.xgridB[5], bdr.ygridB[1]], [bdr.xgridB[4], bdr.ygridB[1]], [bdr.xgridB[4], bdr.ygridB[2]]],
'teRot2' : [[bdr.xgridB[4], bdr.ygridB[0]], [bdr.xgridB[5], bdr.ygridB[1]], [bdr.xgridB[5], bdr.ygridB[0]], [bdr.xgridB[6], bdr.ygridB[0]]],
'teRot3' : [[bdr.xgridB[5], bdr.ygridB[0]], [bdr.xgridB[4], bdr.ygridB[1]], [bdr.xgridB[5], bdr.ygridB[1]], [bdr.xgridB[5], bdr.ygridB[2]]]
}


shape = eleInv['eleInvRot0']
figure = eleInv
rotation = 'eleInvRot0'

def rotations(figure, rotation):
    index = int(rotation[-1])
    if index < 3:
        new_index = index + 1
    else:
        new_index = 0
    new_rotation = rotation[:-1] + str(new_index)
    new_shape = figure[new_rotation]
    return new_shape, new_rotation

def blocks_plot(shape):
    xpos = []
    ypos = []
    figBlocks = []
    for coords in shape:
        blockID = bdr.gen_FigID()
        blockID = pygame.Surface(bdr.blockSize)
        xpos.append(bdr.invxgrid[coords[0]])
        ypos.append(bdr.invygrid[coords[1]])
        figBlocks.append(blockID)
    bdr.block_count = 0
    return figBlocks, xpos, ypos

def find_bounds():
    bounds = {}
    for k, v in bdr.main_shape.items():
        bounds[k] = []
        for i in range(len(v)):
            if v[i] == 1:
                bounds[k] += [i]
    return bounds


figBlocks, xpos, ypos = blocks_plot(shape)
clock = pygame.time.Clock()
blocksCount, bubbleDown, speedDown, holdKeyLeft, holdKeyRight, time, currenttime = 0, 0, .96, 0, 0, 0, 2
xspan = 0
running = True
bubble = True

# Starting main game loop
while running == True:
    # Timer
    milli = clock.tick()
    seconds = milli / 1000.
    time += seconds
    yspan = min(ypos)

    # Display refesh
    display.blit(frameSurf, (170, 100))
    frameSurf.fill(bdr.main_color)

    # Plotting active figure
    for block, x, y in zip(figBlocks, xpos, ypos):
        display.blit(block, [bdr.xgridB[x], bdr.ygridB[y]])
        block.fill(bdr.blue)

    # Find all side bounds
    bounds = find_bounds()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False

        # Keystrokes
        if event.type == pygame.KEYDOWN and not any([bdr.pressed_keys["left"], bdr.pressed_keys["right"]]):
            if event.key == pygame.K_LEFT and min(xpos) >= 1:
                bdr.pressed_keys["left"] = True
                move_left = []
                if x + 1 > 0:
                    left_xpos = [x - 1 for x in xpos]
                    for j, x in enumerate(left_xpos):
                        if x in bounds[str(ypos[j])]:
                            move_left.append(False)
                        else:
                            move_left.append(True)
                if all(move_left):
                    xpos = left_xpos
                    xspan -= 1
            if event.key == pygame.K_RIGHT and max(xpos) <= 8:
                move_right = []
                if x + 1 < 9:
                    right_xpos = [x + 1 for x in xpos]
                    for j, x in enumerate(right_xpos):
                        if x in bounds[str(ypos[j])]:
                            move_right.append(False)
                        else:
                            move_right.append(True)
                if all(move_right):
                    xpos = right_xpos
                    xspan += 1
                    bdr.pressed_keys["right"] = True
            if event.key == pygame.K_DOWN:
                bdr.pressed_keys["down"] = True
            if event.key == pygame.K_UP:
                #Rotating the figure
                shape, rotation = rotations(figure, rotation)

                figBlocks, xposTemp, yposTemp = blocks_plot(shape)
                bounds = find_bounds()
                canRotate = []
                new_xpos = [x + xspan for x in xposTemp]
                new_ypos = [y + yspan for y in yposTemp]
                for x, y in zip(new_xpos, new_ypos):
                    if x in bounds[str(y)]:
                        canRotate.append(False)
                    else:
                        canRotate.append(True)
                if all(canRotate):
                    if max(new_xpos) <= 9 and min(new_xpos) >= 1:
                        xpos = new_xpos
                        ypos = new_ypos
                    elif max(new_xpos) > 8:
                        diff = max(new_xpos) - 9
                        xpos = [x - diff for x in new_xpos]
                        ypos = new_ypos
                    elif min(new_xpos) < 1:
                        diff = abs(min(new_xpos))
                        xpos = [x + diff for x in new_xpos]
                        ypos = new_ypos
        else:
            bdr.pressed_keys["right"] = False
            bdr.pressed_keys["left"] = False
            bdr.pressed_keys["down"] = False
            holdKeyRight = -10
            holdKeyLeft = -10

    if bdr.pressed_keys["left"] and min(xpos) >= 1:
        holdKeyLeft += .3
        move_left = []
        if holdKeyLeft >= 5:
            if x + 1 > 0:
                left_xpos = [x - 1 for x in xpos]
                for j, x in enumerate(left_xpos):
                    if x in bounds[str(ypos[j])]:
                        move_left.append(False)
                    else:
                        move_left.append(True)
            if all(move_left):
                xpos = left_xpos
                xspan -= 1
            holdKeyLeft = 0

    if bdr.pressed_keys["right"] and max(xpos) <= 8:
        holdKeyRight += .3
        move_right = []
        if holdKeyRight >= 5:
            if x + 1 < 9:
                right_xpos = [x + 1 for x in xpos]
                for j, x in enumerate(right_xpos):
                    if x in bounds[str(ypos[j])]:
                        move_right.append(False)
                    else:
                        move_right.append(True)
            if all(move_right):
                xpos = right_xpos
                xspan += 1
            holdKeyRight = 0

    if bdr.pressed_keys["down"]:
        bubbleDown += speedDown
        if bubbleDown >= 20:
            ypos = [y + 1 for y in ypos]
            bubbleDown = 0

    #Saved blocks plot
    for blockID, coords in bdr.settled_blocks.items():
        display.blit(blockID, coords)
        blockID.fill(bdr.blue)

    # Stop at Floor
    for x, y in zip(xpos, ypos):
        if bdr.main_shape[str(y+1)][x] == 1:

            bdr.blocks_meta(xpos,ypos)
            figBlocks, xpos, ypos = blocks_plot(shape)
            xspan = 0
            break

        if currenttime <= time:
            on_motion = True
            currenttime += .5
            ypos = [y + 1  for y in ypos]
            bounds = find_bounds()
        else:
            on_motion = False


    # Create Grid
    for i in range(20):
        hline = i
        if i <= 10:
            vline = i
            pygame.draw.line(display, bdr.gridc, (bdr.wideGrid[vline], 100), (bdr.wideGrid[vline], 800), 2)
        pygame.draw.line(display, bdr.gridc, (170, bdr.tallGrid[hline]), (510, bdr.tallGrid[hline]), 2)
    # Bound lines
    pygame.draw.line(display, bdr.blue, (170, 100), (510, 100), 3)
    pygame.draw.line(display, bdr.blue, (170, 800), (510, 800), 3)
    pygame.draw.line(display, bdr.blue, (170, 100), (170, 800), 3)
    pygame.draw.line(display, bdr.blue, (510, 100), (510, 800), 3)

    pygame.display.update()
