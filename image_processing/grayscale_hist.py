import numpy as np
import matplotlib.pyplot as plt
import argparse
import cv2

#fetching the data
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

#load the image as a numpy array
image = cv2.imread(args["image"])
cv2.imshow("OG", image)
cv2.waitKey(0)

#from colored to grayscape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

#histogram hahah
# calcHist(array of imahe, color mode, mask, dont konw this, color range)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

#graph
plt.figure()
plt.title("Grayscale Histogram")
plt.ylabel("No of Pixels")
plt.xlabel("bins")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
