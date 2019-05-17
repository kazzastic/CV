#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 05:59:08 2019

@author: kazzastic
"""
#from mazelib import *
import numpy as np
import cv2
from random import randrange
from random import choice, shuffle
import cython
if not cython.compiled:
    from mazelib.solve.MazeSolveAlgo import MazeSolveAlgo

class Maze(object):
    def __init__(self):
        self.generator = None
        self.grid = arr
        self.start = None
        self.end = None
        self.solver = None
        self.solutions = None
        
    def generate_entrances(self, start_outer=True, end_outer=True):
        """ Generate maze entrances.
            Entrances can be on the walls, or inside the maze.
        """
        if start_outer and end_outer:
            self._generate_outer_entrances()
        elif not start_outer and not end_outer:
            self._generate_inner_entrances()
        elif start_outer:
            self.start, self.end = self._generate_opposite_entrances()
        else:
            self.end, self.start = self._generate_opposite_entrances()

        # the start and end shouldn't be right next to each other
        if abs(self.start[0] - self.end[0]) + abs(self.start[1] - self.end[1]) < 2:
            self.generate_entrances(start_outer, end_outer)    
    
    def _generate_outer_entrances(self):
        """ Generate maze entrances, along the outer walls. """
        H = self.grid.shape[0]
        W = self.grid.shape[1]

        start_side = randrange(4)

        # maze entrances will be on opposite sides of the maze.
        if start_side == 0:
            self.start = (0, randrange(1, W, 2))  # North
            self.end = (H - 1, randrange(1, W, 2))
        elif start_side == 1:
            self.start = (H - 1, randrange(1, W, 2))  # South
            self.end = (0, randrange(1, W, 2))
        elif start_side == 2:
            self.start = (randrange(1, H, 2), 0)  # West
            self.end = (randrange(1, H, 2), W - 1)
        else:
            self.start = (randrange(1, H, 2), W - 1)  # East
            self.end = (randrange(1, H, 2), 0)

    def _generate_inner_entrances(self):
        """ Generate maze entrances, randomly within the maze. """
        H, W = self.grid.shape

        self.start = (randrange(1, H, 2), randrange(1, W, 2))
        end = (randrange(1, H, 2), randrange(1, W, 2))

        # make certain the start and end points aren't the same
        while end == self.start:
            end = (randrange(1, H, 2), randrange(1, W, 2))

        self.end = end

    def solve(self):
        """ public method to solve a new maze, if possible """
        #if self.generator is None:
            #raise UnboundLocalError('No maze-solving algorithm has been set.')
        if self.start is None or self.end is None:
            raise UnboundLocalError('Start and end times must be set first.')
        else:
            self.solutions = self.solver.solve(self.grid, self.start, self.end)

    def tostring(self, entrances=False, solutions=False):
        """ Return a string representation of the maze. """
        if self.grid is None:
            return ''

        # build the walls of the grid
        txt = []
        for row in self.grid:
            txt.append(''.join(['#' if cell else ' ' for cell in row]))

        # insert the start and end points
        if entrances and self.start and self.end:
            r, c = self.start
            txt[r] = txt[r][:c] + 'S' + txt[r][c+1:]
            r, c = self.end
            txt[r] = txt[r][:c] + 'E' + txt[r][c+1:]

        # if extant, insert the solution path
        if solutions and self.solutions:
            for r, c in self.solutions[0]:
                txt[r] = txt[r][:c] + '+' + txt[r][c+1:]

        return '\n'.join(txt)

    def __str__(self):
        """ display maze walls, entrances, and solutions, if available """
        return self.tostring(True, True)

    def __repr__(self):
        return self.__str__()


class WallFollower(MazeSolveAlgo):
    """
    The Algorithm

    Follow the right wall and you will eventually end up at the end.

    details:

    1. Choose a random starting direction.
    2. At each intersection, take the rightmost turn. At dead-ends, turn around.
    3. If you have gone more than (H * W) + 2 cells, stop; the maze will not be solved.
    4. Terminate when you reach the end cell.
    5. Prune the extraneous branches from the solution before returning it.

    Optional Parameters

    Turn: String ['left', 'right']
        Do you want to follow the right wall or the left wall? (default 'right')
    """

    def __init__(self, turn='right', prune=True):
        # turn can take on values 'left' or 'right'
        if turn == 'left':
            self.directions = [(-2, 0), (0, -2), (2, 0), (0, 2)]
        else:  # default to right turns
            self.directions = [(-2, 0), (0, 2), (2, 0), (0, -2)]

        self.prune = prune

    def _solve(self):
        solution = []
        current = self.start

        # a first move has to be made
        if self._on_edge(self.start):
            current = self._push_edge(self.start)
            solution.append(current)

        # pick a random direction and move
        last = current
        current = choice(self._find_neighbors(last, False))
        last_diff = (current[0] - last[0], current[1] - last[1])
        last_dir = self.directions.index(last_diff)

        # add first move to solution
        solution.append(self._midpoint(last, current))
        solution.append(current)

        # now that you have set up the situation, follow the walls
        solution = self._follow_walls(last_dir, current, solution)

        if self.prune:
            solution = self._prune_solution(solution)

        solution = self._fix_entrances(solution)

        return [solution]

    def _follow_walls(self, last_dir, current, solution):
        """Perform the wall following logic.
        Loop until you have found the end,
        or prove you won't solve the maze.
        """
        limit = self.grid.shape[0] * self.grid.shape[1] + 2

        while len(solution) < limit:
            last_dir, temp = self._follow_one_step(last_dir, current)
            # the solution should not include the end point
            if temp == self.end:
                midpoint = self._midpoint(temp, current)
                if midpoint != self.end:
                    solution.append(midpoint)
                break
            solution.append(self._midpoint(temp, current))
            solution.append(temp)
            current = temp

        if len(solution) >= limit:
            raise RuntimeError('This algorithm was not able to converge on a solution.')

        return solution

    def _follow_one_step(self, last_dir, current):
        """At each new cell you reach, take the rightmost turn.
        Turn around if you reach a dead end.
        if right is not available, then straight, if not straight, left, etc...
        """
        for d in range(4):
            next_dir = (last_dir - 1 + d) % 4
            next_cell = self._move(current, self.directions[next_dir])
            r, c= self._midpoint(next_cell, current)

            if self.grid[r, c] == 0 and (r, c) != self.start:
                return (next_dir, next_cell)
            elif (r, c) == self.end:
                return (next_dir, self.end)

        return (last_dir, current)

    def _fix_entrances(self, solution):
        """Ensure the start and end are appropriately placed in the solution."""
        # prune if start is found in solution
        if self.start in solution:
            i = solution.index(self.start)
            solution = solution[i+1:]

        # prune if first position is repeated
        if solution[0] in solution[1:]:
            i = solution[1:].index(solution[0])
            solution = solution[i+1:]

        # prune duplicate end points
        if len(solution) > 1 and solution[-2] == solution[-1]:
            solution = solution[:-1]

        return solution


file = 'mazegreen.jpg'
img = cv2.imread(file)
cv2.imshow('The Initial', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
blurred = cv2.GaussianBlur(gray_img, (5,5), 0)
cv2.imshow('Blur', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
(t, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

arr = np.array(thresh)

for i in range(0, 300):
    for j in range(0, 264):    
        if(arr[i][j] == 255):        
            arr[i][j] = 1

for i in range(0, 300):
    for j in range(0, 264):    
        if(arr[i][j] == 1):        
            arr[i][j] = 170

cv2.cvtColor(arr, cv2.COLOR_GRAY2BGR)
cv2.imshow('Result', arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
            
            
     
my_maze = Maze()
my_maze.generate_entrances(start_outer=True, end_outer=True)
my_maze.solver = WallFollower()
my_maze.solve()

