# This is to calculate the avarage of 	petal_length.

import numpy as np 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data.csv',header=None)

#this is to print average of petal_length.
print((np.mean(df.iloc[:150,2])),'average of petal_length') 

# these to pring min and max of petal_length.
print(min(df.iloc[:150,2]),'minimum of petal_length')
print(max(df.iloc[:150,2]),'maximum of petal_length')