import pygame


class Builder():
    def __init__(self):

        #Dimensions
        self.disp_width = 700
        self.disp_height = 850
        self.objSize = width, height = (30, 40)
        self.blockSize = width, height = (34, 35)
        self.frameSize = width, height = (340, 700)
        self.saved_settled_blocks = {}
        self.settled_blocks = {}

        #Grid
        self.wideGrid = [170, 204, 238, 272, 306, 340, 374, 408, 442, 476, 510]
        self.tallGrid = [100, 135, 170, 205, 240, 275, 310, 345, 380, 415, 450,
                         485, 520, 555, 590, 625, 660, 695, 730, 765, 800]
        self.xgridB = {0: 170, 1: 204, 2: 238, 3: 272, 4: 306, 5: 340, 6: 374, 7: 408,
                       8: 442, 9: 476, 10: 510}
        self.ygridB = {0: 100, 1: 135, 2: 170, 3: 205, 4: 240, 5: 275, 6: 310,
                       7: 345, 8: 380, 9: 415, 10: 450, 11: 485, 12: 520, 13: 555,
                       14: 590, 15: 625, 16: 660, 17: 695, 18: 730, 19: 765, 20: 800}

        #Levels
        self.level1time = 2

        #Grid Axis
        self.xaxisB = [x for x in range(11)]
        self.yaxisB = [y for y in range(21)]

        #Colors
        self.grey = (61,61,66)
        self.light_grey = (20,20,60)
        self.main_color = (0,0,20)
        self.white = (255, 255, 255)
        self.blue = (102,102,255)
        self.gridc = (45,45,45)

        #Font
        # self.smallfont = pygame.font.SysFont('Corbel',35)

        #Motion
        self.velocity = .8
        # self.x = 200
        # self.y = 180
        self.pressed_keys = {"left": False, "right": False, "up": False, "down": False}

        #Timer and FPS
        self.FPS = 60
        self.FramePerSec = pygame.time.Clock()
        self.whiteblocks = {'row0' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row7': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row8': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row9': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row10': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row11': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row12': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row13': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row14': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row15': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row16': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row17': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row18': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row19': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'row20': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

    def Display(self):
        self.display = pygame.display.set_mode((self.disp_width, self.disp_height))
        pygame.display.set_caption("Tetris Game")
        return self.display


    def fig_toSave(self, xls, yls):
        import string
        import random
        def gen_code():
            letters = string.ascii_lowercase
            letters = [x for x in letters]
            numbers = [str(n) for n in range(9)]
            lets = random.choices(letters, k=3)
            nums = random.choices(numbers, k=2)
            code = [lets[0]] + [nums[0]] + [lets[1]] + [nums[1]] + [lets[2]]
            code = ''.join(code)
            return code

        for x, y in zip(xls, yls):
            code = gen_code()
            figId = f'figure{code}'
            self.saved_settled_blocks[figId] = pygame.Surface(self.blockSize)
            self.settled_blocks[figId] = [x, y]


rc = Builder().grey
