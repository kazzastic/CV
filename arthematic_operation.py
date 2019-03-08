import argparse
import numpy as np
import cv2

#fetching the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter the Path")
args = vars(ap.parse_args())

#loading image and conversting it into a numpy array
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

print("max of 255 by openCV: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("max of 255 by openCV: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("wrap of max by np: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap of max by np: {}".format(np.uint8([50]) - np.uint8([100])))

#generating one array(matrix) and multiplying it with 100
#and adding that with original numpy array(image)
M = np.ones(image.shape, dtype = "uint8")*100
added = cv2.add(image, M)
cv2.imshow("added img", added)

#doing the same thing here as well but multiplying it with 50
#and substracting it with array of original image nunpy array(matrix)
M = np.ones(image.shape, dtype = "uint8")*50
subtracted = cv2.subtract(image, M)
cv2.imshow("subtracted Image", subtracted)
cv2.waitKey(0)
