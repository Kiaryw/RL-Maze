import numpy
import random


class Maze:
    def __init__(self):
        self.maze = None
        self.start_point = None
        self.end_point = None
        self.path = None
        self.selected_block = None
        self.block_size = 49
        self.WALL_COLOR = [0, 0, 0]
        self.BACKGROUND_COLOR_INT = 255
        self.BACKGROUND_COLOR = [self.BACKGROUND_COLOR_INT for i in range(0, 3, 1)]
        self.START_COLOR = [255, 0, 0]
        self.GOAL_COLOR = [0, 255, 0]
        self.PATH_COLOR = [0, 0, 255]
        self.SELECTION_COLOR = [232, 244, 66]
