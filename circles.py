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

'''
#Book code 
canvas = np.zeros((500, 500, 3), dtype="uint8")
for i in range(0,500):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size=(3,)).tolist()
    point = np.random.randint(0, high = 300, size = (2,))
    cv2.circle(canvas, tuple(point), radius, color, -1)
cv2.imshow("beauty", canvas)
cv2.waitKey(0)
'''

#my code simple shiz
canvas = np.zeros((500, 500, 3), dtype = "uint8")
for i in range(0, 100):
    radius = np.random.randint(5, high = 250)
    first = np.random.randint(0, high = 256)
    second = np.random.randint(0, high = 256)
    third = np.random.randint(0, high = 256)
    color = (first, second, third)
    first_pt = np.random.randint(0, high = 300)
    second_pt = np.random.randint(0, high = 300)
    cv2.circle(canvas, (first_pt, second_pt), radius, color, -1)
cv2.imshow("beauty", canvas)
cv2.waitKey(0)

