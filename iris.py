from sklearn import datasets
data = datasets.load_iris()
print("data shape:",data.data.shape)
print("feature name:",data.feature_names)
print("target class", data.target)
print("class name:",data.target_names)

from sklearn.utils import shuffle
X, y = shuffle(data.data,data.target, random_state=0)
print("target class", y)