import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_excel("X:/Code/Tubes_Phyton_Kel4/Dataset/cars.xlsx")

median_mpg = df['MPG_City'].median()
df['Irit_Boros_Binary'] = np.where(df['MPG_City'] >= median_mpg, 1, 0)

X = df[['Horsepower', 'Weight', 'Cylinders']]
Y = df['Irit_Boros_Binary']

data = pd.concat([X, Y], axis=1).dropna()
X = data[['Horsepower', 'Weight', 'Cylinders']]
Y = data['Irit_Boros_Binary']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)

print(f"Akurasi Model : {accuracy:.2f}")

data_baru = [[300, 250, 6]]
hasil = model.predict(data_baru)

print("Hasil Prediksi (1=Irit, 0=Boros):", hasil[0])

joblib.dump(model, "logistic_irit_boros.joblib")
