import numpy as np

def initialize_grid(m,n):

    grid = np.random.randint(2, size=[m, n])
    grid2 = np.zeros([3, 3])
    print(grid)
    print(grid2)



initialize_grid(3,4)