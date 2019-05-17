#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 01:29:59 2019

@author: kazzastic
"""

import numpy as np
import cv2

def working(file):
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
      for j in range(i, 264):
          if(arr[i][j] == 255):
              arr[i][j] = 1
    print(arr)
if __name__ == "__main__": 
    file = 'mazegreen.jpg' 
    working(file)