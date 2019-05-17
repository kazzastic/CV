#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 01:29:59 2019

@author: kazzastic
"""

import numpy as np
import cv2




def load_img(file): 
    global img
    img = cv2.imread(file, 0)


def display():
    cv2.imshow('The Maze Of Life', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def working():
    global gray_img
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

if __name__ == "__main__": 
    file = 'mazegreen.jpg' 
    load_img(file)
    working()
    display()