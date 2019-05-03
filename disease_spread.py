from util import *
import random
import numpy as np
from matplotlib import pyplot as plt


class DiseaseSpread(object):

    def __init__(self, m, n):

        self.row = m
        self.col = n
        self.grid = initialize_grid(self, m,n)

    def evolve(self):
        # TODO at every timestep updates the new state of each block (then after double for loop - update old grid)
        # go through each neighbor
        # updates based on rules
        # - if cell dead & has 3 live neighbors it lives in the next timeself
        # - if cell is alive and has 3+ live neighbors dies next
        # - 0/1 
        pass

    def main(self):
        # TODO: for however 'generations' while gen < 1000
        # updates until 'done'
        # output animation that shows each updated plot at each timestep
        pass