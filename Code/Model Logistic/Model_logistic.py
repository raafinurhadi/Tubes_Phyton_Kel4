import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

X = df[['Tenaga Mesin', 'Berat Dalam LBS', 'Kapasitas Mesin']]
y = df['Irit atau Boros']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Akurasi Model: {accuracy:.2f}")

joblib.dump(model, "model_logistic.joblib")
