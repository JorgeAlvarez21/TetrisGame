import pygame


class Builder():
    def __init__(self):

        #Dimensions
        self.disp_width = 700
        self.disp_height = 850
        self.blockSize = width, height = (34, 35)
        self.frameSize = width, height = (340, 700)

        #Grid
        self.wideGrid = [170, 204, 238, 272, 306, 340, 374, 408, 442, 476, 510]
        self.tallGrid = [100, 135, 170, 205, 240, 275, 310, 345, 380, 415, 450,
                         485, 520, 555, 590, 625, 660, 695, 730, 765, 800]
        self.xgridB = {0: 170, 1: 204, 2: 238, 3: 272, 4: 306, 5: 340, 6: 374, 7: 408,
                       8: 442, 9: 476, 10: 510}
        self.ygridB = {0: 100, 1: 135, 2: 170, 3: 205, 4: 240, 5: 275, 6: 310,
                       7: 345, 8: 380, 9: 415, 10: 450, 11: 485, 12: 520, 13: 555,
                       14: 590, 15: 625, 16: 660, 17: 695, 18: 730, 19: 765, 20: 800}

        self.invxgrid = {170: 0, 204: 1, 238: 2, 272: 3, 306: 4, 340: 5, 374: 6, 408: 7, 442: 8, 476: 9, 510: 10}

        self.invygrid = {100: 0, 135: 1, 170: 2, 205: 3, 240: 4, 275: 5, 310: 6, 345: 7, 380: 8, 415: 9, 450: 10,
                         485: 11, 520: 12, 555: 13, 590: 14, 625: 15, 660: 16, 695: 17, 730: 18, 765: 19, 800: 20}
        #Colors
        self.grey = (61,61,66)
        self.light_grey = (20,20,60)
        self.main_color = (0,0,20)
        self.white = (255, 255, 255)
        self.blue = (102,102,255)
        self.gridc = (45,45,45)

        self.block_count = 0

        #Motion
        self.pressed_keys = {"left": False, "right": False, "up": False, "down": False}

        #Timer and FPS
        self.main_shape = {   '0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '7': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '8': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '9': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '10':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '11': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '12': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '13': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '14': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '15': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '16': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '17': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '18': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '19': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              '20': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                              '21': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

        self.floor_bounds = {'0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             '1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             '2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             '3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             '4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             '5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             '6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             '7': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             '8': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             '9': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            '10': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] }

        self.settled_blocks = {}



    def Display(self):
        self.display = pygame.display.set_mode((self.disp_width, self.disp_height))
        pygame.display.set_caption("Tetris Game")
        return self.display

    def gen_FigID(self):
        self.block_count += 1
        code = str(self.block_count)+'block'
        return code


    def blocks_meta(self, xpos, ypos):
        #Saving corresponding coords and ID
        for x, y in zip(xpos, ypos):
            blockID = str(x) + 'x' + str(y) + 'y'
            blockID = pygame.Surface(self.blockSize)
            self.settled_blocks[blockID] = [self.xgridB[x], self.ygridB[y]]

        #Update main_shape
        for k in self.main_shape.keys():
            for x, y in zip(xpos, ypos):
                if k == str(y):
                    self.main_shape[k][x] = 1


        pass

    def debug(self, *args):
        print(args)




rc = Builder().grey
