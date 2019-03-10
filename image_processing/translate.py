import argparse
import imutils as im
import cv2

#fetching the image 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Img Path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#from imutils calling translate first arg is image
#second arg is x
#third is y pretty obvious 
shifted = im.translate(image, 100, 0)
cv2.imshow("shift down", shifted)
cv2.waitKey(0)
