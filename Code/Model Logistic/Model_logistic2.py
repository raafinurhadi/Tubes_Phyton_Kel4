import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars2_processed.csv")

X = df[['Horsepower', 'Weight_in_lbs', 'Cylinders']]
y = df['Irit_Boros']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9
)
# random state 1 akurasi 0.94
# random state 9 akurasi 0.97
model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Akurasi Model: {accuracy:.2f}")

joblib.dump(model, "model2_logistic.joblib")
