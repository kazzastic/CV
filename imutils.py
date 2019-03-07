import numpy as np
import cv2

#M is a matrix here such that [1, 0 , tx]
# and second for [0, 1, ty]
def translate(image , x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image ,M, (image.shape[1], image.shape[0]))
    return shifted 
