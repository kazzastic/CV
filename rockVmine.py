__author__ = "kazim"
import os
import pandas as pd
#import statsmodels.formula.api as smf
#import statsmodels.stats.multicomp as multi
import scipy.stats
import numpy as np
#import seaborn
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

PATH = os.path.join("datasets", "wine")

def load_wine_data(wine_path=PATH):
    csv_path = os.path.join(wine_path, "winequality-red.csv")
    return pd.read_csv(csv_path)

red = load_wine_data()
#white = pd.read_csv('winequality-white.csv', low_memory=False, sep=';')