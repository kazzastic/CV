from mazelib import *
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
from copy import deepcopy

def showPNG(maze):
    """Generate a simple image of the maze."""
    gridCopy = deepcopy(maze.grid)
    start_row , start_col = m.start
    end_row, end_col = m.end
    gridCopy[start_row][start_col]=5
    gridCopy[end_row][end_col]=10
    
    plt.figure(figsize=(10, 5), facecolor=("pink"), edgecolor=("red"))
    plt.imshow(gridCopy, cmap=plt.cm.binary)
    #plt.xticks([]), plt.yticks([])
    plt.show()

    
m = Maze()
m.generator = BacktrackingGenerator(25, 35)
m.generate()

print(m)

m.solver = WallFollower()

m.generate_entrances()

print(m.start,m.end)

showPNG(m)

m.solve()

print(m)
