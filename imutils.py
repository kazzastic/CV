import numpy as np
import cv2

#M is a matrix here such that [1, 0 , tx]
# and second for [0, 1, ty]
def translate(image , x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image ,M, (image.shape[1], image.shape[0]))
    return shifted 

def rotate(image, angle, center = None, scale = 1.0):
    h = image.shape[0]
    w = image.shape[1]

    if center is None:
        center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w,h))
    return rotated
