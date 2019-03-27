import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

pic = Image.open('00-puppy.jpg')
print(pic)
type(pic)

pic_arr = np.asarray(pic)

pic_red = pic_arr.copy()

