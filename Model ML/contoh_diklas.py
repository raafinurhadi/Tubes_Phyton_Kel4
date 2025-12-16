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

namafitur= iris.feature_names
# print(namafitur)
namatarget= iris.target_names
# print(namatarget)
# X=X[:,:2]
# x_min, x_max= X[:,0].min()-0.5, X[:,0].max()+0.5
# y_min, y_max= X[:,1].min()-0.5, X[:,1].max()+0.5
# print(x_min)

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=1)

print(f"X train : {X_train.shape}")
print(f"X test: {X_test.shape}")
print(f"y train: {y_train.shape}")
print(f"y test: {y_test.shape}")
# print(X_train)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

y_pred= model.predict(X_test)
acc=accuracy_score(y_test,y_pred)
print(f"Akurasi : {acc}")
# print(model)
# sepallength=int(input("Masukkan Panjang Sepal : "))
# sepalwidth=int(input("Masukkan Lebar Sepal : "))
# petallength=int(input("Masukkan Panjang Petal : "))
# petalwidth=int(input("Masukkan Lebar Petal : "))

databaru=[[4,4,4,4],[4,3,2,1]]
preds=model.predict(databaru)
# print(preds)
predsspecies=[iris.target_names[p] for p in preds]
print(f"Hasil Prediksi : {predsspecies}")

joblib.dump(model, "Prediksi Iris.joblib")