import cv2
import argparse

#fetching the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter the image path")
args = vars(ap.parse_args())

#engaging the pixel at the vars i & j
image = cv2.imread(args["image"])
i = 0
j = 0
(b,g,r) = image[i,j]
print("Pixel at "+str((i,j))+" are Red:{}, Green:{}, Blue:{}".format(r,g,b))

#changed the color of a very particular pixel in the image
image[0,0] = (0,0,225)
(b,g,r) = image[0,0]
print("Pixel at"+str((i,j))+"are Red:{}, Green:{}, Blue:{}".format(r,g,b))

#now going to slice the image using corner shit
corner = image[0:100, 0:100]
cv2.imshow("Cropped", corner)
cv2.waitKey(100)

#change color of the particular area
image[40:100, 40:100] = (0, 255, 0)
cv2.imshow("color change", image)
cv2.waitKey(0)

