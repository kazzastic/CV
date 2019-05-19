#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:29:59 2019

@author: kazzastic
"""
from PIL import Image
import pytesseract as ts
import cv2
import os

ocr = cv2.imread('ocr.jpeg')
ocr_gray = cv2.cvtColor(ocr, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(ocr_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

file = "{}.png".format(os.getpid())
cv2.imwrite(file, gray)

txt = ts.image_to_string(Image.open(file))
os.remove(file)
print(txt)

cv2.imshow("Image", ocr_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()