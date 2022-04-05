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
    #Generate new random fig and rotation
    choice, rotation_options, shape = figure.gen_shape()
    find_blocks = figure.find_active_blocks(shape, middle_x) # will return a dict -> {blockId : coords, ...}
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
  #  print(choice['choice'][rotation_options[rot]])


    rot += 1
    if rot == 4:
        rot = 0

    find_blocks = figure.find_active_blocks(shape,middle_x, fix_xpos=xpos, fix_ypos=min(ypos))
    rotated_blocks = []
    xpos = []
    ypos = []
    for blockId, coords in find_blocks.items():
        xpos.append(coords[0])
        ypos.append(coords[1])
        rotated_blocks.append('block' + str(blockId))
    currenttime = 1
    return main_game_logic(rotated_blocks, xpos, ypos)



x_block = {
           0 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           1 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           2 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           3 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           4 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           5 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           6 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           7 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           8 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           9 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           10 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           11 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           12 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           13 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           14 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           15 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           16 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           17 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           18 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           19 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           20 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] }
flor_iterator = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
floor = 19
clock = pygame.time.Clock()
currenttime = 1
xaxis = bdr.xaxisB
display.blit(frameSurf, (170, 100))
run = True
time = 0
rot_y = 0

block_is_active = False
on_stash = False
while run == True:



    def main_game_logic(active_blocks, xpos, ypos, **kwargs):
        global time
        global currenttime
        global x_block
        global middle_x
        global choice, rotation_options, shape
        new_block = True
        while new_block:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    run = False
                # Single Key
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and min(xpos) >= 1:
                        bdr.pressed_keys["left"] = False
                        xpos = [x - 1 for x in xpos]
                        middle_x -= 1
                    if event.key == pygame.K_RIGHT and max(xpos) <= 8:
                        bdr.pressed_keys["right"] = False
                        print(xpos)
                        middle_x +=1
                        xpos = [x + 1 for x in xpos]

                    if event.key == pygame.K_UP:
                        rotated(xpos, ypos, choice, rotation_options)
                        # for blockId, x, y in zip(active_blocks, xpos, ypos):
                        #     block = getattr(figure, blockId)
                        #     display.blit(block, [bdr.xgridB[x], bdr.ygridB[y]])
                        #     block.fill(bdr.main_color)
                        break
                    # Holding key
                    if event.key == pygame.K_RIGHT:
                        if bdr.pressed_keys["down"]:
                            time += .4
                            print('hi')

            # Display refesh
            display.blit(frameSurf, (170, 100))
            frameSurf.fill(bdr.main_color)
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

            # Timer
            milli = clock.tick()
            seconds = milli / 1000.
            time += seconds

            #Checking blocks on stash

            if 'on_stash' in kwargs.keys() and 'True' in kwargs.values():
                on_stash = True
            else:
                on_stash = False

            if on_stash:
                for savedBlock, coords in bdr.settled_blocks.items():
                    savedx = coords[0]
                    savedy = coords[1]
                    display.blit(bdr.saved_settled_blocks[savedBlock], [bdr.xgridB[savedx], bdr.ygridB[savedy]])
                    bdr.saved_settled_blocks[savedBlock].fill(bdr.white)
        #Plotting
            for blockId, x, y in zip(active_blocks, xpos, ypos):
                # print(xpos, ypos)
                block = getattr(figure, blockId)
                display.blit(block, [bdr.xgridB[x], bdr.ygridB[y]])
                block.fill(bdr.white)
            #Bubble Y Down
            if currenttime <= time:
                currenttime += .5
                ypos = [y+1 for y in ypos]
                rot_y = [y+1 for y in ypos]
            if max(ypos) == floor:
                curr_xpos = xpos
                curr_ypos =  ypos

                for x, y in zip(curr_xpos, curr_ypos):
                    x_block[y][x] = 1
                #To get the floor of each x, get the max(ylist) and find its corresponding x
                bdr.fig_toSave(curr_xpos, curr_ypos)
                active_blocks, xpos, ypos = figBlockPrep()
                main_game_logic(active_blocks, xpos, ypos,  on_stash = 'True')

                new_block = False
            pygame.display.update()


    main_game_logic(active_blocks, xpos, ypos)
    # clock.tick(60)