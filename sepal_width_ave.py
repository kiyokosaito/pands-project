# This is to calculate the avarage of sepal_width.

import numpy as np 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data.csv',header=None)

print((np.mean(df.iloc[:150,1])),'average of sepal_width') 

print(min(df.iloc[:150,1]),'minimum of sepal_width')