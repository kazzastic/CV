import argparse
import numpy as np
import cv2

#creating a rectangle
rectangle = np.zeros((300,300), dtype = 'uint8')
cv2.rectangle(rectangle, (25,25), (275,275), 255, -1)
cv2.imshow("rectangle", rectangle)

#creating a circle
circle = np.zeros((300,300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("circle", circle)

#performing the bitwise operation
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOR)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

