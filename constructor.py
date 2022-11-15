import pygame
import numpy as np


class Builder():
    def __init__(self):
        self.lines = 0
        self.blockSize = width, height = (34, 35)
        self.frameSize = width, height = (340, 700)

        # Grid
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
        # Colors
        self.grey = (61, 61, 66)
        self.cyan = (76, 160, 160)
        self.disp_color = '#5C6591'
        self.main_color = '#0F193D'
        self.light_green = '#46E1B7'
        self.light_blue = '#7FD9FF'
        self.white = (255, 255, 255)
        self.blue = (95, 8, 255)
        self.surf_outline = '#8A7C7C'
        self.upc_shapes_color = '#5E668F'
        self.gridc = '#4B538F'
        self.orange = '#ee964b'

        self.block_count = 0
        self.settled_blocks = {}
        self.strike = []

        # self.fig_colors = [[37, 162, 68], [118, 120, 237],  [ 247, 184, 1], [241, 135, 1], [243, 91, 4]]
        self.fig_colors = [[166, 160, 0], [168, 8, 82], [247, 57, 20], [118, 120, 237], [111, 163, 112]]
        self.fig_colors_dic = {'yellow': [166, 160, 0], 'red': [168, 8, 82], 'orange': [247, 57, 20],
                               'blue': [118, 120, 237],
                               'green': [111, 163, 112]}
        self.pressed_keys = {"left": False, "right": False, "up": False, "down": False}

        # Creating main_shape to update active blocks
        self.main_shape = {}
        self.colored_blocks = {}
        for y in range(22):
            if y not in [20, 21]:
                self.main_shape[str(y)] = np.zeros(10, dtype=int).tolist()
                self.colored_blocks[str(y)] = np.zeros(10, dtype=int).tolist()

            else:
                self.main_shape[str(y)] = np.ones(10, dtype=int).tolist()
                self.colored_blocks[str(y)] = np.ones(10, dtype=int).tolist()

        comp_ = ['10000'] * 9
        self.comp = [10000]
        for i, num in enumerate(comp_):
            self.comp.append(self.comp[i] + int(num))

    @staticmethod
    def Display():
        # Dimensions
        width = 700
        height = 850
        display = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Tetris Game")
        return display

    def gen_FigID(self):
        self.block_count += 1
        code = str(self.block_count) + 'block'
        return code

    def trickle_down(self, grid, colors_grid):
        full_line = [False if 0 in line else True for line in grid.values()]
        if True in full_line[:-2]:
            for i in range(20):
                if 0 not in grid[str(i)]:
                    self.strike.append(i)
                    self.lines += 1
                    ls = [l for l in range(i)]
                    print('Something wrong with Rec')
                    ls.reverse()
                    for j in ls:
                        grid[str(j + 1)] = grid[str(j)]
                        colors_grid[str(j + 1)] = colors_grid[str(j)]
            return self.trickle_down(grid, colors_grid)
        else:
            return grid, colors_grid

    def blocks_meta(self, xpos, ypos, color):

        # Update main shape and colored blocks
        for k in self.main_shape.keys():
            for x, y in zip(xpos, ypos):
                if k == str(y):
                    self.main_shape[k][x] = 1
                    self.colored_blocks[k][x] = color
        full_line = [False if 0 in line else True for line in self.main_shape.values()]
        if True in full_line[:-2]:
            self.main_shape, self.colored_blocks = self.trickle_down(self.main_shape, self.colored_blocks)

    @staticmethod
    def all_figures(xgridB, ygridB):
        Builder.ele = {
            'eleRot0': [[xgridB[4], ygridB[0]], [xgridB[4], ygridB[1]], [xgridB[4], ygridB[2]], [xgridB[5], ygridB[2]]],
            'eleRot1': [[xgridB[6], ygridB[0]], [xgridB[4], ygridB[1]], [xgridB[5], ygridB[1]], [xgridB[6], ygridB[1]]],
            'eleRot2': [[xgridB[4], ygridB[0]], [xgridB[5], ygridB[0]], [xgridB[5], ygridB[1]], [xgridB[5], ygridB[2]]],
            'eleRot3': [[xgridB[4], ygridB[0]], [xgridB[5], ygridB[0]], [xgridB[6], ygridB[0]], [xgridB[4], ygridB[1]]]
        }

        Builder.eleInv = {
            'eleInvRot0': [[xgridB[5], ygridB[0]], [xgridB[5], ygridB[1]], [xgridB[5], ygridB[2]],
                           [xgridB[4], ygridB[2]]],
            'eleInvRot1': [[xgridB[4], ygridB[0]], [xgridB[4], ygridB[1]], [xgridB[5], ygridB[1]],
                           [xgridB[6], ygridB[1]]],
            'eleInvRot2': [[xgridB[4], ygridB[0]], [xgridB[5], ygridB[0]], [xgridB[4], ygridB[1]],
                           [xgridB[4], ygridB[2]]],
            'eleInvRot3': [[xgridB[4], ygridB[0]], [xgridB[5], ygridB[0]], [xgridB[6], ygridB[0]],
                           [xgridB[6], ygridB[1]]]
        }

        Builder.te = {
            'teRot0': [[xgridB[5], ygridB[0]], [xgridB[4], ygridB[1]], [xgridB[5], ygridB[1]], [xgridB[6], ygridB[1]]],
            'teRot1': [[xgridB[4], ygridB[0]], [xgridB[5], ygridB[1]], [xgridB[4], ygridB[1]], [xgridB[4], ygridB[2]]],
            'teRot2': [[xgridB[4], ygridB[0]], [xgridB[5], ygridB[1]], [xgridB[5], ygridB[0]], [xgridB[6], ygridB[0]]],
            'teRot3': [[xgridB[5], ygridB[0]], [xgridB[4], ygridB[1]], [xgridB[5], ygridB[1]], [xgridB[5], ygridB[2]]]
        }

        Builder.square = {
            'squareRot0': [[xgridB[4], ygridB[0]], [xgridB[5], ygridB[0]], [xgridB[5], ygridB[1]],
                           [xgridB[4], ygridB[1]]]
        }

        Builder.zed = {
            'zedRot0': [[xgridB[4], ygridB[0]], [xgridB[5], ygridB[0]], [xgridB[6], ygridB[1]], [xgridB[5], ygridB[1]]],
            'zedRot1': [[xgridB[5], ygridB[0]], [xgridB[4], ygridB[1]], [xgridB[4], ygridB[2]], [xgridB[5], ygridB[1]]],
        }

        Builder.zedInv = {
            'zedInvRot0': [[xgridB[6], ygridB[0]], [xgridB[5], ygridB[0]], [xgridB[4], ygridB[1]],
                           [xgridB[5], ygridB[1]]],
            'zedInvRot1': [[xgridB[5], ygridB[1]], [xgridB[4], ygridB[0]], [xgridB[4], ygridB[1]],
                           [xgridB[5], ygridB[2]]],
        }
        Builder.line = {
            'lineRot0': [[xgridB[5], ygridB[2]], [xgridB[5], ygridB[0]], [xgridB[5], ygridB[3]],
                         [xgridB[5], ygridB[1]]],
            'lineRot1': [[xgridB[6], ygridB[1]], [xgridB[4], ygridB[1]], [xgridB[3], ygridB[1]],
                         [xgridB[5], ygridB[1]]],
        }
