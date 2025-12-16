import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_excel("X:\Code\Tubes_Phyton_Kel4\Dataset\cars.xlsx")

median_mpg = df['MPG_City'].median()
df['Irit_Boros_Binary'] = np.where(df['MPG_City'] >= median_mpg, 1, 0)

features_X = ['Horsepower', 'Weight', 'Cylinders']
target_Y = 'Irit_Boros_Binary'

df.dropna(subset=features_X + [target_Y], inplace=True)

class CustomDataset:
    def __init__(self, mobil, features, target_name):

        self.data = mobil
        self.target = mobil[target_name]
        self.feature_names = features
        self.target_name = target_name
        self.features = mobil[features] 

dataset = CustomDataset(
    mobil=df,
    features=features_X,
    target_name=target_Y
)

X = dataset.features  
Y = dataset.target    

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size= 0.2, random_state= 42
)

model = LogisticRegression(solver='liblinear') 
model.fit(X_train, Y_train)


Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)

print(f"Features (X):\n{X.head()}")
print(f"Target (Y):\n{Y.head()}")
print(f"\nModel Accuracy: {accuracy:.2f}")


databaru=[[300,250,6.0]]
preds=model.predict(databaru)

pred_irit_boros= preds.tolist()
print(f"Hasil Prediksi : {pred_irit_boros}")

joblib.dump(model, "Prediksi irit atau boros.joblib")
