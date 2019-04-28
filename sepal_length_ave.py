# This is to calculate the avarage of sepal_length.

import numpy as np 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data.csv',header=None)

#this is to print average of sepal length.
print((np.mean(df.iloc[:150,0])),'average of sepal_length') 

# these to pring min and max of sepal_length.
print(min(df.iloc[:150,0]),'minimum of sepal_length')
print(max(df.iloc[:150,0]),'maximum of sepal_length')