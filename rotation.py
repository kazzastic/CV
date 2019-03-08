import imutils as im
import numpy as np
import argparse 
import cv2

#fetching the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#from imutils calling the rotation function
rotated = im.rotate(image, 180)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
