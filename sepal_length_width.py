# This is to visualise sepal length and width of three irises.
# In order to create 2D chart, I chose sepal lrngth and width.


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('iris.data.csv',header=None)
X = df.iloc[:,[0,1]].values
plt.scatter(X[:50,0],X[:50,1],color='red',marker='o',label='setosa')
plt.scatter(X[50:100,0],X[50:100,1],color='blue',marker='x',label='versicolor')
plt.scatter(X[101:150,0],X[101:150,1],color='green',marker='s',label='virginica')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.legend(loc='upper left')
plt.show()
plt.quit()