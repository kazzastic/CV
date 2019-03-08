import argparse
import cv2

#fetching the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter the fucking path")
args = vars(ap.parse_args())

#loading and converting the image into numpy array
image = cv2.imread(args["image"])

flipped = cv2.flip(image, 0)
cv2.imshow("Horizontally flipped image", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, 1)
cv2.imshow("Horizontally flipped image", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, -1)
cv2.imshow("Horizontally flipped image", flipped)
cv2.waitKey(0)
