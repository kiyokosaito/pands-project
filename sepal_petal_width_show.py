
# This is to visualise sepal and petal width of three irises.
# In order to create 2D chart, I chose sepal and petal width.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('iris.data.csv',header=None)
X = df.iloc[:,[1,3]].values
plt.scatter(X[:50,0],X[:50,1],color='red',marker='o',label='setosa')
plt.scatter(X[50:100,0],X[50:100,1],color='blue',marker='x',label='versicolor')
plt.scatter(X[101:150,0],X[101:150,1],color='green',marker='s',label='virginica')
plt.xlabel('Sepal width')
plt.ylabel('Petal width')
plt.legend(loc='upper left')
plt.show()
plt.quit()