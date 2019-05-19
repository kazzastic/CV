#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:05:29 2019

@author: kazzastic
"""
import cv2
import numpy as np
import threading 
#import colorsys

class Point(object):
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
rw = 2
p = 0 
start = Point()
end = Point()

dir4 = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]

#def mouse_mov(event, pX, pY, flags, params):
    #global 
    
    
    
    
if __name__ == "__main__":
    
    img = cv2.imread('mazegreen.jpg', cv2.IMREAD_GRAYSCALE)
    t, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    h, w= img.shape[:2]
    
        