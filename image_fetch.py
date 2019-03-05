import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "1.2 cat.jpeg.jpeg")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width :{} pixel".format(image.shape[1]))
print("height :{} pixel".format(image.shape[0]))
print("channels :{} pixel".format(image.shape[2]))

cv2.imshow("A cato", image)
cv2.waitKey(0)
cv2.imwrite("newcato.jpeg", image)
