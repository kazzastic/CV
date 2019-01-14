from mazelib import *
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from copy import deepcopy


def showPNG(maze):
    """Generate a simple image of the maze."""
    gridCopy = deepcopy(maze.grid)

    start_row , start_col = m.start
    end_row, end_col = m.end

    gridCopy[start_row][start_col]=2.5 #random values to change colormap
    gridCopy[end_row][end_col]=3.5

    solution = maze.solutions[0]        #what does this line mean, is this is
                                        #array where the (0,1)'s are saved of the solved path?
    if solution:                        

        for r,c in solution:
            gridCopy[r][c]=5.0          #added a new color for the solved path

        start_patch = mpatches.Patch(color='tab:blue', label='Start')
        end_patch = mpatches.Patch(color='turquoise', label='End')
               
            
    
    plt.figure(figsize=(10, 5))         #The size of the window assigned here

    if solution:
        plt.legend(handles = [start_patch,end_patch], \
               loc='center left', bbox_to_anchor=(1, 0.5))
    
    plt.imshow(gridCopy, cmap=plt.cm.ocean,interpolation = "nearest")
    plt.xticks([]), plt.yticks([])      #disables the x and y axis values
    plt.show()



if __name__ == '__main__':
    
    m = Maze()

    m.generator = BacktrackingGenerator(25, 35)
    m.generate()
    m.generate_entrances()
    m.solver = WallFollower()

    m.solve()
    showPNG(m)

    




