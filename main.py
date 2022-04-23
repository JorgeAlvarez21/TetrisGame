import pygame, sys
import random
from constructor import Builder

pygame.init()
bdr = Builder()
display = Builder.Display()
Builder.all_figures(bdr.xgridB, bdr.ygridB)
frameSurf = pygame.Surface(bdr.frameSize)
upc_Blocks_Surf = pygame.Surface((160, 520))
tetrisLogo = pygame.image.load('Nintendo_Tetris_logo.png')
tetrisLogo = pygame.transform.scale(tetrisLogo, (290, 85))



# Global variables
color_ind = 0
block_color = bdr.fig_colors[color_ind]
font = pygame.font.SysFont('halkduster.ttf', 48)

figures = [Builder.ele, Builder.eleInv, Builder.te, Builder.square, Builder.zed, Builder.zedInv, Builder.line]
upc_shapes = []
upc_shapes_rev = []
upc_shapes_rots = []

# Initializing figures
def gen_upc_shapes():
    global upc_shapes, rot_choices, figures, upc_shapes_rots
    while len(upc_shapes) < 4:
        choice = random.choice(range(len(figures)))
        fig_choice = figures[choice]
        rotation = random.choice([*fig_choice])
        fig_shape = fig_choice[rotation]
        upc_shapes.insert(0, [rotation, fig_shape])
        upc_shapes_rev.append([rotation, fig_shape])
        upc_shapes_rots.append(fig_choice)

def select_from_upc(upc_shapes):
    global figure
    figure = {}
    if upc_shapes:
        next_fig = upc_shapes.pop()
        rotation = next_fig[0]
        shape = next_fig[1]
        figure[rotation] = shape
        gen_upc_shapes()
        return rotation, shape
    else:
        gen_upc_shapes()
        return select_from_upc(upc_shapes)




rotation, shape = select_from_upc(upc_shapes)
fig_choice = upc_shapes_rots.pop(0)

# figure = figures[1]
# rotation = 'eleInvRot0'
# print(rotation)
# shape = figure[rotation]

def rotations(fig_choice, rotation):
    index = int(rotation[-1])
    if fig_choice.keys() in [Builder.zed.keys(), Builder.zedInv.keys(), Builder.line.keys()]:
        if index == 0:
            new_index = index + 1
        else:
            new_index = 0
    else:
        if index < 3:
            new_index = index + 1
        else:
            new_index = 0
    new_rotation = rotation[:-1] + str(new_index)
    new_shape = fig_choice[new_rotation]
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
strikeLineTimer = 0
# Starting main game loop _______________________________________

while running:
    # Timer
    milli = clock.tick()
    seconds = milli / 1000.
    time += seconds
    yspan = min(ypos)

    # Display refesh
    display.fill(bdr.disp_color)
    display.blit(frameSurf, (170, 100))
    display.blit(tetrisLogo, (190, 10))
    frameSurf.fill(bdr.main_color)
    display.blit(upc_Blocks_Surf, (520, 200))
    upc_Blocks_Surf.fill(bdr.main_color)

    # Plotting upcoming shapes
    upc_xgrid = {272: 540, 306: 570, 340: 600, 374: 625, 408: 670}
    upc_ygrid = {100: 210, 135: 240, 170: 270, 205: 300}
    y_increment = 0
    count = 0
    for i in range(len(upc_shapes)):
        ind = len(upc_shapes) - 1
        ind -= i
        ls = upc_shapes[ind]
        for coords in ls[1:]:
            if count >= 1:
                y_increment += len(coords) * (30)
            count += 1
            for x, y in coords:
                y = upc_ygrid[y] + y_increment
                x = upc_xgrid[x]
                upcShape = pygame.Surface((30, 30))
                upcShape.fill(bdr.orange)
                display.blit(upcShape, [x, y])
                img = font.render("y :  " + 'YY', True, bdr.white)
            y_increment += 10

    # Colors for saved blocks
    saved_blocks_coors = {}
    for key, values in bdr.main_shape.items():
        if int(key) <= 19:
            for i in range(len(values)):
                if bdr.colored_blocks[key][i] != 0:
                    color = bdr.fig_colors_dic[bdr.colored_blocks[key][i]]
                    x_color = bdr.xgridB[i]
                    y_color = bdr.ygridB[int(key)]
                    saved_blocks_coors[x_color, y_color] = color
            for item, color in saved_blocks_coors.items():
                x_color = item[0]
                y_color = item[1]
                active_block = pygame.Surface(bdr.blockSize)
                active_block.fill(color)
                display.blit(active_block, [x_color, y_color])
        # print(saved_blocks_coors.values())

    display.blit(img, (550, 90))

    # Plotting active figure
    for block, x, y in zip(figBlocks, xpos, ypos):
        display.blit(block, [bdr.xgridB[x], bdr.ygridB[y]])
        display.blit(block, [bdr.xgridB[x], bdr.ygridB[y]])
        block_color = bdr.fig_colors[color_ind]
        block.fill(block_color)

    # Find all side bounds
    bounds = find_bounds()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


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
                if x + 1 <= 9:
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
                if 'squareRot0' not in figure.keys():
                    #Rotating the figure
                    shape, rotation = rotations(fig_choice, rotation)
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
                        elif max(new_xpos) >= 9:
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
            # Timer in between side move keystroke and holding key
            holdKeyRight = -5
            holdKeyLeft = -5

    # Holding key
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
            if x + 1 <= 9:
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

    # Adding flash color to filled line strike
    # if len(bdr.strike) > 0:®
    #     ('ACTIVE')
    #     strikeLineTimer = 0
    #     for i, num in enumerate(bdr.comp):
    #         while strikeLineTimer < num:
    #             for line_strike in bdr.strike:
    #                 strike_block = pygame.Surface(bdr.blockSize)
    #                 strike_block.fill(bdr.white)
    #                 for x in range(10):
    #                     display.blit(strike_block, [bdr.xgridB[x], bdr.ygridB[line_strike]])
    #             strikeLineTimer += 1
    #         bdr.strike = []

    for x, y in zip(xpos, ypos):
        if bdr.main_shape[str(y+1)][x] == 1:
            #Saving current color and its coords
            curr_color = [color for color, color_code in bdr.fig_colors_dic.items() if color_code == block_color]
            curr_color = '.'.join(map(str, curr_color))
            bdr.blocks_meta(xpos,ypos, curr_color)

            rotation, shape = select_from_upc(upc_shapes)
            fig_choice = upc_shapes_rots.pop(0)
            if color_ind < len(bdr.fig_colors)-1:
                color_ind += 1
                block_color = bdr.fig_colors[color_ind]
            else:
                color_ind = 0
            figBlocks, xpos, ypos = blocks_plot(shape)
            xspan = 0
            break

        if currenttime <= time:
            # print(bdr.settled_blocks)
            currenttime += .5
            ypos = [y + 1  for y in ypos]
            bounds = find_bounds()


    # Create Grid
    for i in range(20):
        hline = i
        if i <= 10:
            vline = i
            pygame.draw.line(display, bdr.gridc, (bdr.wideGrid[vline], 100), (bdr.wideGrid[vline], 800), 2)
        pygame.draw.line(display, bdr.gridc, (170, bdr.tallGrid[hline]), (510, bdr.tallGrid[hline]), 2)

    # Bound lines for game play
    pygame.draw.line(display, bdr.surf_outline, (170, 100 ), (510, 100), 3)
    pygame.draw.line(display, bdr.surf_outline, (170, 800), (510, 800), 3)
    pygame.draw.line(display, bdr.surf_outline, (170, 100), (170, 800), 3)
    pygame.draw.line(display, bdr.surf_outline, (510, 100), (510, 800), 3)
    # Bound lines for upc_shapes
    pygame.draw.line(display, bdr.surf_outline, (520, 200), (520, 720), 3)
    pygame.draw.line(display, bdr.surf_outline, (680, 200), (680, 720), 3)
    pygame.draw.line(display, bdr.surf_outline, (520, 200), (680, 200), 3)
    pygame.draw.line(display, bdr.surf_outline, (520, 720), (680, 720), 3)


    pygame.display.update()
