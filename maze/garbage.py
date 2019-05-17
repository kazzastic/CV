#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:05:29 2019

@author: kazzastic
"""

from mazelib import *
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from copy import deepcopy



m = Maze()
m.generator = Prims(27, 34)
m.generate()

m.solver = WallFollower()
m.generate_entrances()
m.solve()
sol = m.solutions
sol = np
maze = m.grid
'''
def showPNG(maze):
    """Generate a simple image of the maze."""
    gridCopy = deepcopy(maze.grid)

    start_row , start_col = m.start
    end_row, end_col = m.end
    
    
    gridCopy[start_row][start_col]=2.5 #random values to change colormap
    gridCopy[end_row][end_col]=3.5

    solution = maze.solutions[0]

    if solution:

        for r,c in solution:
            gridCopy[r][c]=4.0

        start_patch = mpatches.Patch(color='tab:blue', label='Start')
        end_patch = mpatches.Patch(color='turquoise', label='End')



    plt.figure(figsize=(10, 5))

    plt.legend(handles = [start_patch,end_patch], \
               loc='center left', bbox_to_anchor=(1, 0.5))

    plt.imshow(gridCopy, cmap=plt.cm.ocean,interpolation = "nearest")
    plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    
    m = Maze()
    m.generator = BacktrackingGenerator(25, 35)
    m.generate()
    m.generate_entrances()    
    m.solver = WallFollower()
    showPNG(m)
'''
    