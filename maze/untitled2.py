#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 05:59:08 2019

@author: kazzastic
"""
import numpy as np
import cv2

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

maze = np.array(thresh)