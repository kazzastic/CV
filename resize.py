import numpy as np
import imutils as im
import argparse
import cv2

#fetching image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Load Image")
args = vars(ap.parse_args())

#original image
image = cv2.imread(args["image"])
cv2.imshow("original", image)
cv2.waitKey(0)

#chaning the height
resized = im.resize(image, height = 1000)
cv2.imshow("Height", resized)
cv2.waitKey(0)

#changing the width
resized = im.resize(image, width = 100)
cv2.imshow("Resizing", resized)
cv2.waitKey(0)
