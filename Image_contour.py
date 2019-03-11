import numpy as np
import argparse
import cv2

#fetching the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path")
args = vars(ap.parse_args())

#loading the image as numpy array
image = cv2.imread(args["image"])

#converting the image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#implement guassian blurr
blurr = cv2.GaussianBlur(image, (5,5), 1)

cv2.imshow("Gaussain Blur", blurr)

canny = cv2.Canny(blurr, 30, 150)
cv2.imshow("Canny Edge Detection", canny)
cv2.waitKey(0)
