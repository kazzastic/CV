import numpy as np
import cv2

#created the canvas to work on
canvas = np.zeros((300,300,3), dtype="uint8")

#selected a color
#the second and thrid args in cv2.cricles are the centre points and radius
green = (0, 255, 0)
circle = cv2.circle(canvas, (100,100), 100, green)
cv2.imshow("first circle", canvas)
cv2.waitKey(0)

#making a concentric circle
#canvas.shape[1] is actually the width
#canvas.shape[0] is actully the height
canvas = np.zeros((300,300,3), dtype="uint8")
white = (255, 255, 255)
centre_x, centre_y = canvas.shape[1]//2 , canvas.shape[0]//2
for radius in range(0, 175, 25):
    cv2.circle(canvas, (centre_x, centre_y), radius, white)
cv2.imshow("concentric circle", canvas)
cv2.waitKey(0)

