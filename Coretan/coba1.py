import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_json("X:\Code\Tubes_Phyton_Kel4\Dataset\Raw\cars.json")

median_mpg = df['Miles_per_Gallon'].median()
df['Irit_Boros'] = np.where(df['Miles_per_Gallon'] >= median_mpg, 1, 0)

X = df[['Horsepower', 'Weight_in_lbs', 'Cylinders']]
Y = df['Irit_Boros']

data = pd.concat([X, Y], axis=1).dropna()
X = data[['Horsepower', 'Weight_in_lbs', 'Cylinders']]
Y = data['Irit_Boros']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=1
)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)

print(f"Akurasi Model : {accuracy:.2f}")

data_baru = [[160, 2456, 6]]
hasil = model.predict(data_baru)
preds=[df.Irit_Boros[p] for p in hasil]
print("Hasil Prediksi (1=Irit, 0=Boros):", hasil[0])
print(f"Hasil akurasi data baru : {preds}")
joblib.dump(model, "logistic_irit_boros.joblib")
