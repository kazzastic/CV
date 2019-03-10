import argparse
import cv2
import numpy as np

#created a canvas
canvas = np.zeros((300,300,3), dtype="uint8")

#draws a green colored line on the canvas
green = (0, 255, 0)
line = cv2.line(canvas,(0,0), (100,100), green,20) #the last arg is the width of the line
cv2.imshow("Canvas", line)
cv2.waitKey(0)

#draws a line with some width

#draws a rectangle
blue = (0, 255, 0)
rectangle = cv2.rectangle(canvas, (10,10), (60,60), blue,-1)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

#draw a rectangle
red = (0, 0, 255)
rectangle = cv2.rectangle(canvas, (20, 20), (80, 80), green, 2)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

#draw a line wihtout any width
line = cv2.line(canvas, (300, 300), (50,50), red)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)
