import pygame, sys
from pygame.locals import *
import random
import figures
from constructor import Builder
import time

pygame.init()
bdr = Builder()
display = bdr.Display()
frameSurf = pygame.Surface(bdr.frameSize)
figure = figures.make_figure()
middle_x = 3
#Function to reset vars for each new fig
def figBlockPrep():
    global middle_x
    global choice, rotation_options, shape
    global rot_y
    #Generate new random fig and rotation
    rot_y = 0
    choice, rotation_options, shape = figure.gen_shape()
    find_blocks = figure.find_active_blocks(shape, 6, choice, rotation_options, False) # will return a dict -> {blockId : coords, ...}
    active_blocks = []
    xpos = []
    ypos = []
    for blockId, coords in find_blocks.items():
        xpos.append(coords[0])
        ypos.append(coords[1])
        active_blocks.append('block'+str(blockId))

    return active_blocks, xpos, ypos
active_blocks, xpos, ypos = figBlockPrep()
rot = 0
def rotated(xpos, ypos, choice, rotation_options):
    global clock
    global time
    global currenttime
    global rot
    clock = pygame.time.Clock()
    time = 0
    shape = figure.figures[choice['choice']][rotation_options[rot]]

    rot += 1
    if rot == 4:
        rot = 0

    find_blocks = figure.find_active_blocks(shape, middle_x, choice, rotation_options[rot], True, fix_xpos=xpos, fix_ypos=min(ypos))
    rotated_blocks = []
    xpos = []
    ypos = []
    for blockId, coords in find_blocks.items():
        xpos.append(coords[0])
        ypos.append(coords[1])
        rotated_blocks.append('block' + str(blockId))
    currenttime = 1
    return rotated_blocks, xpos, ypos


floor = {0:20, 1:20, 2:20, 3:20, 4:20, 5:20, 6:20, 7:20, 8:20, 9:20}
clock = pygame.time.Clock()
currenttime = 1
xaxis = bdr.xaxisB
display.blit(frameSurf, (170, 100))
run = True
time = 0
rot_y = 0
block_is_active = False
on_stash = False

minvals = {}
while run == True:
    def main_game_logic(active_blocks, xpos, ypos, **kwargs):
        global time
        global currenttime
        global middle_x
        global floor
        global minvals
        global on_stash
        global choice, rotation_options, shape
        vel = .3
        move_right = 0
        move_left = 0
        bubble_down = 0
        new_block = True
        while new_block:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    run = False
                # Single Key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and min(xpos) >= 1:
                        bdr.pressed_keys["left"] = True
                        xpos = [x - 1 for x in xpos]
                        middle_x -= 1
                    elif event.key == pygame.K_RIGHT and max(xpos) <= 8:
                        bdr.pressed_keys["right"] = True
                        middle_x +=1
                        xpos = [x + 1 for x in xpos]
                    elif event.key == pygame.K_UP:
                        rotated_blocks, xpos, ypos = rotated(xpos, ypos, choice, rotation_options)
                    elif event.key == pygame.K_DOWN:
                        bdr.pressed_keys["down"] = True
                else:
                    bdr.pressed_keys["left"] = False
                    bdr.pressed_keys["right"] = False
                    bdr.pressed_keys["down"] = False
                    bdr.pressed_keys["up"] = False

            if bdr.pressed_keys["right"] and max(xpos) <= 8:
                move_right += vel
                if move_right >= 4:
                    middle_x += 1
                    xpos = [x + 1 for x in xpos]
                    move_right = 0
            if bdr.pressed_keys["left"] and min(xpos) >= 1:
                print('s')
                move_left += vel
                if move_left >= 4:
                    middle_x -= 1
                    xpos = [x - 1 for x in xpos]
                    move_left = 0
            # Display refesh
            display.blit(frameSurf, (170, 100))
            frameSurf.fill(bdr.main_color)

            # Timer
            milli = clock.tick()
            seconds = milli / 1000.
            time += seconds

            #Checking blocks on stash

            if on_stash:
                for savedBlock, coords in bdr.settled_blocks.items():
                    savedx = coords[0]
                    savedy = coords[1]
                    display.blit(bdr.saved_settled_blocks[savedBlock], [bdr.xgridB[savedx], bdr.ygridB[savedy]])
                    bdr.saved_settled_blocks[savedBlock].fill(bdr.blue)
        #Plotting
            for blockId, x, y in zip(active_blocks, xpos, ypos):
                block = getattr(figure, blockId)
                display.blit(block, [bdr.xgridB[x], bdr.ygridB[y]])
                block.fill(bdr.blue)
        #Saving set figures
            max_y = []
            max_x = []
            minvals_y = {}
            for x, y in zip(xpos, ypos):
                if y == max(ypos):
                    max_y.append(y)
                    max_x.append(x)
                if x not in minvals_y.keys():
                    minvals_y[x] = y
                else:
                    if minvals_y.get(x) > y:
                        minvals_y[x] = y
            for x, y in zip(max_x, max_y):
                if bdr.pressed_keys["down"] and y <= floor[x] - 1:
                    print('t')
                    bubble_down += vel
                    if bubble_down >= 5:
                        ypos = [y + 1 for y in ypos]
                        bubble_down = 0

                if y == floor[x]-1:
                    on_stash = True
                    for k, v in minvals_y.items():
                        floor[k] = v
                    bdr.fig_toSave(xpos, ypos)
                    active_blocks, xpos, ypos = figBlockPrep()
                    middle_x = 3
                    main_game_logic(active_blocks, xpos, ypos)
                    new_block = False
                else:
                    # Bubble Y Down
                    if currenttime <= time:
                        currenttime += .5
                        ypos = [y + 1 for y in ypos]
                        rot_y = [y + 1 for y in ypos]

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


    main_game_logic(active_blocks, xpos, ypos)