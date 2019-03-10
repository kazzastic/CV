import numpy as np
import argparse
import cv2

#fetching the image
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path here...')
args = vars(ap.parse_args())

#loading the image here
image = cv2.imread(args["image"])
cv2.imshow("OG", image)
cv2.waitKey(0)

#splitting the blue green red
'''
B = cv2.split(image)
G = cv2.split(image)
R = cv2.split(image)
'''
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.waitKey(0)

#alterante method
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

#merge back the channels
merged = cv2.merge([B, G, R])
cv2.imshow("merged", merged)
cv2.waitKey(0)
