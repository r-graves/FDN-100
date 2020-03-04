import pandas as pd

# url to get file from
url = "http://mlr.cs.umass.edu/ml/machine-learning-databases/iris/iris.data"

# create headers
headers = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class']

# read the file into a dataframe
iris = pd.read_csv(url, header=None, names=headers)

print(iris.head())

sepal_lengths = iris[['Sepal Length']]
print(sepal_lengths.head())