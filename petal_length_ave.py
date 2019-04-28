# This is to calculate the avarage of 	petal_length.

import numpy as np 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data.csv',header=None)

print((np.mean(df.iloc[:149,2])),'average of petal_length') 
