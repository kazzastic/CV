#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 01:29:59 2019

@author: kazzastic
"""
from mazelib import *
import numpy as np
import cv2

def working(file):
    '''Here we load our image in the var img'''
    img = cv2.imread(file)
    cv2.imshow('The Initial', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    '''We convert image from colored to grayscale'''
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    '''We put a blur on our picture in order to make thresholding result accurate'''
    blurred = cv2.GaussianBlur(gray_img, (5,5), 0)
    cv2.imshow('Blur', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    '''Thresholding our image to a certain tone of gray'''
    (t, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
    cv2.imshow('Threshold Binary', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    '''Converting our image into a useful numpy array'''
    arr = np.array(thresh)
    
    '''a nested for loop to change every value 255 ->  150 '''
    '''hence, wherever their is 150 it means that this path can be iterated in order to
    solve our maze'''
    for i in range(0, 293):
      for j in range(0, 257):
          if(arr[i][j] == 255):
              arr[i][j] = 150
    cv2.imshow('Result', arr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()         
     
    
if __name__ == "__main__": 
    file = 'mazegreen.jpg' 
    working(file)