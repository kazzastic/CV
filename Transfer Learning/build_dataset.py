#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:22:02 2019

@author: kazzastic
"""

from pyimagesearch import config
from imutils import paths
import shutil
import os

for split in (config.TRAIN, config.TEST, config.VAL):
	# grab all image paths in the current split
	print("[INFO] processing '{} split'...".format(split))
	p = os.path.sep.join([config.ORIG_INPUT_DATASET, split])
	imagePaths = list(paths.list_images(p))
    
	for imagePath in imagePaths:
		# extract class label from the filename
		filename = imagePath.split(os.path.sep)[-1]
		label = config.CLASSES[int(filename.split("_")[0])]
 
		# construct the path to the output directory
		dirPath = os.path.sep.join([config.BASE_PATH, split, label])
 
		# if the output directory does not exist, create it
		if not os.path.exists(dirPath):
			os.makedirs(dirPath)
 
		# construct the path to the output image file and copy it
		p = os.path.sep.join([dirPath, filename])
		shutil.copy2(imagePath, p)