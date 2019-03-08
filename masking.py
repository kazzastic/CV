import argparse
import numpy as np
import cv2

#fetching the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter the path")
args = vars(ap.parse_args())

#loading the image as a numpy array
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = "uint8")
cX = image.shape[1] // 2
cY = image.shape[0] // 2
cv2.rectangle(mask, (cX - 75, cY -75),(cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked Image", masked)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = "uint8")
#cX = image.shape[1] // 2
#cY = image.shape[0] // 2
cv2.circle(mask, (cX, cY), 100, 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked Image", masked)
cv2.waitKey(0)
