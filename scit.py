#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:54:55 2019

@author: kazzastic
"""
import numpy as np
import os
import tarfile
import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = os.path.join("datasets", "housing")


def load_housing_data(data_path = DATA_PATH):
    csv_path = os.path.join(data_path, "SCIT dataset.csv")
    return pd.read_csv(csv_path, index_col = 0)
