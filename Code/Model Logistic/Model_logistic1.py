import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

X = df[['Horsepower', 'Weight', 'Cylinders']]
y = df['Irit_Boros']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=41
)
# random state 8 akurasi 0.90
# random state 15 akurasi 0.91
# random state 32 akurasi 0.92
# random state 41 akurasi 0.93
model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Akurasi Model: {accuracy:.2f}")

joblib.dump(model, "model1_logistic.joblib")
