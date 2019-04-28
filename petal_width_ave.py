# This is to calculate the avarage of petal_width.

import numpy as np 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data.csv',header=None)

# This is to calculate the avarage of petal_width.
print((np.mean(df.iloc[:150,3])),'average of petal_width') 

# these to pring min and max of petal_width.
print(min(df.iloc[:150,3]),'minimum of petal_width')
print(max(df.iloc[:150,3]),'maximum of petal_width')


