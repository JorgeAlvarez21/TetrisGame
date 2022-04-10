import random
import pygame
class make_figure:
    def __init__(self):
        self.xgridB = {0: 170, 1: 204, 2: 238, 3: 272, 4: 306, 5: 340, 6: 374, 7: 408,
                       8: 442, 9: 476, 10: 510}
        self.ygridB = {0: 100, 1: 135, 2: 170, 3: 205, 4: 240, 5: 275, 6: 310,
                       7: 345, 8: 380, 9: 415, 10: 450, 11: 485, 12: 520, 13: 555,
                       14: 590, 15: 625, 16: 660, 17: 695, 18: 730, 19: 765, 20: 800}

        blockSize = width, height = (34, 35)
        self.blocka0 = pygame.Surface(blockSize)
        self.blockb0 = pygame.Surface(blockSize)
        self.blockc0 = pygame.Surface(blockSize)
        self.blockd0 = pygame.Surface(blockSize)
        self.blocka1 = pygame.Surface(blockSize)
        self.blockb1 = pygame.Surface(blockSize)
        self.blockc1 = pygame.Surface(blockSize)
        self.blockd1 = pygame.Surface(blockSize)
        self.blocka2 = pygame.Surface(blockSize)
        self.blockb2 = pygame.Surface(blockSize)
        self.blockc2 = pygame.Surface(blockSize)
        self.blockd2 = pygame.Surface(blockSize)
        self.blocka3 = pygame.Surface(blockSize)
        self.blockb3 = pygame.Surface(blockSize)
        self.blockc3 = pygame.Surface(blockSize)
        self.blockd3 = pygame.Surface(blockSize)



        self.figures = {
    'square': {'main': [(0, 1, 1, 0),
                        (0, 1, 1, 0),
                        (0, 0, 0, 0),
                        (0, 0, 0, 0)],
               'rotA': [(0, 1, 1, 0),
                        (0, 1, 1, 0),
                        (0, 0, 0, 0),
                        (0, 0, 0, 0)],
               'rotB': [(0, 1, 1, 0),
                        (0, 1, 1, 0),
                        (0, 0, 0, 0),
                        (0, 0, 0, 0)],
               'rotC': [(0, 1, 1, 0),
                        (0, 1, 1, 0),
                        (0, 0, 0, 0),
                        (0, 0, 0, 0)]},
    'ele': {'main': [(1, 1, 0, 0),
                     (1, 0, 0, 0),
                     (1, 0, 0, 0),
                     (0, 0, 0, 0)],
            'rotA': [(1, 1, 1, 0),
                     (0, 0, 1, 0),
                     (0, 0, 0, 0),
                     (0, 0, 0, 0)],
            'rotB': [(0, 1, 0, 0),
                     (0, 1, 0, 0),
                     (1, 1, 0, 0),
                     (0, 0, 0, 0)],
            'rotC': [(1, 0, 0, 0),
                     (1, 1, 1, 0),
                     (0, 0, 0, 0),
                     (0, 0, 0, 0)]},
    'eleInv': {'main': [(1, 1, 0, 0),
                        (0, 1, 0, 0),
                        (0, 1, 0, 0),
                        (0, 0, 0, 0)],

               'rotA': [(0, 0, 1, 0),
                        (1, 1, 1, 0),
                        (0, 0, 0, 0),
                        (0, 0, 0, 0)],

               'rotB': [(1, 0, 0, 0),
                        (1, 0, 0, 0),
                        (1, 1, 0, 0),
                        (0, 0, 0, 0)],

               'rotC': [(1, 1, 1, 0),
                        (1, 0, 0, 0),
                        (0, 0, 0, 0),
                        (0, 0, 0, 0)]},

    'stick': {'main': [(1, 0, 0, 0),
                       (1, 0, 0, 0),
                       (1, 0, 0, 0),
                       (1, 0, 0, 0)],
              'rotA': [(1, 1, 1, 1),
                       (0, 0, 0, 0),
                       (0, 0, 0, 0),
                       (0, 0, 0, 0)],
              'rotB': [(1, 0, 0, 0),
                       (1, 0, 0, 0),
                       (1, 0, 0, 0),
                       (1, 0, 0, 0)],
              'rotC': [(1, 1, 1, 1),
                       (0, 0, 0, 0),
                       (0, 0, 0, 0),
                       (0, 0, 0, 0)]},
    'te': {'main': [(0, 1, 0, 0),
                    (1, 1, 1, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)],
           'rotA': [(1, 0, 0, 0),
                    (1, 1, 0, 0),
                    (1, 0, 0, 0),
                    (0, 0, 0, 0)],
           'rotB': [(1, 1, 1, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)],
           'rotC': [(0, 1, 0, 0),
                    (1, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0)]},
    'zed': {'main': [(1, 1, 0, 0),
                     (0, 1, 1, 0),
                     (0, 0, 0, 0),
                     (0, 0, 0, 0)],
            'rotA': [(0, 1, 0, 0),
                     (1, 1, 0, 0),
                     (1, 0, 0, 0),
                     (0, 0, 0, 0)],
            'rotB': [(1, 1, 0, 0),
                     (0, 1, 1, 0),
                     (0, 0, 0, 0),
                     (0, 0, 0, 0)],
            'rotC': [(0, 1, 0, 0),
                     (1, 1, 0, 0),
                     (1, 0, 0, 0),
                     (0, 0, 0, 0)]},
    'zedInv': {'main': [(0, 1, 1, 0),
                        (1, 1, 0, 0),
                        (0, 0, 0, 0),
                        (0, 0, 0, 0), ],
               'rotA': [(1, 0, 0, 0),
                        (1, 1, 0, 0),
                        (0, 1, 0, 0),
                        (0, 0, 0, 0)],
               'rotB': [(0, 1, 1, 0),
                        (1, 1, 0, 0),
                        (0, 0, 0, 0),
                        (0, 0, 0, 0), ],
               'rotC': [(1, 0, 0, 0),
                        (1, 1, 0, 0),
                        (0, 1, 0, 0),
                        (0, 0, 0, 0)]}}


    def gen_shape(self):
        shapes = {0:'square', 1:'ele', 2:'eleInv', 3:'stick', 4:'te', 5:'zed', 6:'zedInv'}
        rotations = {0:'main', 1: 'rotA', 2:'rotB', 3:'rotC'}
        choice = shapes[random.randint(0,6)]
        rots_int = random.randint(0,3)
        rotationChoice = rotations[rots_int]

        next_rots = []
        for i in range(0, 4):
            if rots_int == i:
                prev_rot = rotations[i]
            else:
                next_rots.append(rotations[i])
        next_rots.append(prev_rot)

        self.shapeChoice = {'choice' : choice, 'rotation' : rotationChoice}
        return self.shapeChoice, next_rots, self.figures[choice][rotationChoice]

    def find_active_blocks(self, shape, x, rot_shape, rotation, rotated, **kwargs):
        startx0 = 3
        startx1 = 4
        startx2 = 5
        startx3 = 6

        starty0 = 0
        starty1 = 1
        starty2 = 2
        starty3 = 3

        if rotated:
            print(rot_shape['choice'], rotation)
            for k, v in kwargs.items():
                if rot_shape['choice'] == 'stick':
                    if rotation == 'rotA' or rotation == 'rotC':
                        if k == "fix_xpos":
                            if x >= 7:
                                x = 6
                            startx0 = x
                            startx1 = x + 1
                            startx2 = x + 2
                            startx3 = x + 3
                        if k == "fix_ypos":
                            starty0 = v
                            starty1 = v + 1
                            starty2 = v + 2
                            starty3 = v + 3
                    else:
                        if k == "fix_xpos":
                                if x >= 7:
                                    x = 6
                                startx0 = x
                                startx1 = x + 1
                                startx2 = x + 2
                                startx3 = x + 3
                        if k == "fix_ypos":
                            starty0 = v
                            starty1 = v + 1
                            starty2 = v + 2
                            starty3 = v + 3
                elif rot_shape['choice'] == 'zed' or rot_shape['choice'] == 'zedInv':
                    if k == "fix_xpos":
                        if x >= 8:
                            x = 7
                        startx0 = x
                        startx1 = x + 1
                        startx2 = x + 2
                        startx3 = x + 3
                    if k == "fix_ypos":
                        starty0 = v
                        starty1 = v + 1
                        starty2 = v + 2
                        starty3 = v + 3
                elif rot_shape['choice'] == 'te':
                    if rotation == 'rotA' or rotation == 'rotC':
                        if k == "fix_xpos":
                                if x >= 7:
                                    x = 7
                                startx0 = x
                                startx1 = x + 1
                                startx2 = x + 2
                                startx3 = x + 3
                        if k == "fix_ypos":
                            starty0 = v
                            starty1 = v + 1
                            starty2 = v + 2
                            starty3 = v + 3
                    else:
                        if k == "fix_xpos":
                                if x >= 7:
                                    x = 7
                                startx0 = x
                                startx1 = x + 1
                                startx2 = x + 2
                                startx3 = x + 3
                        if k == "fix_ypos":
                            starty0 = v
                            starty1 = v + 1
                            starty2 = v + 2
                            starty3 = v + 3

                else:
                    if k == "fix_xpos":
                        if x >= 7:
                            x = 7
                        startx0 = x
                        startx1 = x + 1
                        startx2 = x + 2
                        startx3 = x + 3
                    if k == "fix_ypos":
                        starty0 = v
                        starty1 = v + 1
                        starty2 = v + 2
                        starty3 = v + 3


        # x_ls = [startx0, startx1, startx2, startx3]
        # if max(x_ls) >=8 :
        #     diff = max(x_ls) - 8
        #     startx0 -= diff
        #     startx1 -= diff
        #     startx2 -= diff
        #     startx3 -= diff

        # IF THE MAXIMUM OF X_LS IS PAST 8, FIND DIFFERENCE AND SUBSTRACT FROM X


        active_blocks = {}


        if shape[0][0] == 1:  # a0
            coord = [startx0, starty0]
            active_blocks['a0'] = coord
        if shape[0][1] == 1:  # a1
            coord = [startx1, starty0]
            active_blocks['a1'] = coord
        if shape[0][2] == 1:  # a2
            coord = [startx2, starty0]
            active_blocks['a2'] = coord
        if shape[0][3] == 1:  # a3
            coord = [startx3, starty0]
            active_blocks['a3'] = coord
        if shape[1][0] == 1:  # a3
            coord = [startx0, starty1]
            active_blocks['b0'] = coord
        if shape[1][1] == 1:
            coord = [startx1, starty1]
            active_blocks['b1'] = coord
        if shape[1][2] == 1:
            coord = [startx2, starty1]
            active_blocks['b2'] = coord
        if shape[1][3] == 1:
            coord = [startx3, starty1]
            active_blocks['b3'] = coord
        if shape[2][0] == 1:
            coord = [startx0, starty2]
            active_blocks['c0'] = coord
        if shape[2][1] == 1:
            coord = [startx1, starty2]
            active_blocks['c1'] = coord
        if shape[2][2] == 1:
            coord = [startx2, starty2]
            active_blocks['c2'] = coord
        if shape[2][3] == 1:
            coord = [startx3, starty2]
            active_blocks['c3'] = coord
        if shape[3][0] == 1:
            coord = [startx0, starty3]
            active_blocks['d0'] = coord
        if shape[3][1] == 1:
            coord = [startx1, starty3]
            active_blocks['d1'] = coord
        if shape[3][2] == 1:
            coord = [startx2, starty3]
            active_blocks['d2'] = coord
        if shape[3][3] == 1:
            coord = [startx3, starty3]
            active_blocks['d3'] = coord

        return active_blocks











