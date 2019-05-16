#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 01:29:59 2019

@author: kazzastic
"""

import numpy as np
import cv2
import threading 
import colorsys



def load_img():
    img = "mazegreen.jpg"  
    cv2.imread(img, 0)


def display():
    cv2.imshow('The Maze Of Life', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    load_img()
    display()

