import argparse
import cv2

#fetching image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path")
args = vars(ap.parse_args())

#loading the image and making it a numpy array
image = cv2.imread(args["image"])
cv2.imshow("original", image)
cv2.waitKey(0)

#start x = 150 end x = 300
#start y = 15 end y = 222
cropped = image[15:222, 150:400]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
