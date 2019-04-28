# This is to visualise petal length and petal width of three irises.
# In order to create 2D chart, I chose petal length and petal width.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data.csv',header=None)

# Specify petal length and width values 
X = df.iloc[:,[2,3]].values

# To make the scatter charts, nominate colors to each type of iris in 2 attributes.
# adapted from https://ameblo.jp/cognitive-solution/entry-12265630846.html 

plt.scatter(X[:50,0],X[:50,1],color='red',marker='o',label='setosa')
plt.scatter(X[50:100,0],X[50:100,1],color='blue',marker='x',label='versicolor')
plt.scatter(X[101:150,0],X[101:150,1],color='green',marker='s',label='virginica')
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.legend(loc='upper left')
plt.show()
plt.quit()
