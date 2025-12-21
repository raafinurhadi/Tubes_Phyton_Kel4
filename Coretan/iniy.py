from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score
import joblib
import matplotlib as plt
import pandas as pd
iris = load_iris(as_frame=True)
# print(iris)
# print(iris.keys())

# print(iris.keys())
# print(iris.DESCR)

X=iris.data
# print(X)
# print(X.shape)
y=iris.target
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = KNeighborsClassifier(n_neighbors=4)
model.fit (X_train, y_train)

y_pred = model.predict(X_test)
acc=accuracy_score(y_test,y_pred)
print(f"Akurasi : {acc:.2f}")