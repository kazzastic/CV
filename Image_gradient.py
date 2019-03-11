import numpy as np
import argparse
import cv2

#fetching image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path")
args = vars(ap.parse_args())

#loading the image in numpy array
image = cv2.imread(args["image"])

#converting the image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#laplace gradient detection
lap = cv2.Laplacian(image, cv2.CV_64F)

#convert back to 8 bit unsigned int
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplace Gradient Detection", lap)

#Sobel X and Y
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

#conver it back to 8 bit unsigned image
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)

cv2.waitKey(0)
