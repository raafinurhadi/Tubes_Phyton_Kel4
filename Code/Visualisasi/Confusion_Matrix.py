import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

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
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
xticklabels=['BOROS', 'IRIT'], yticklabels=['BOROS', 'IRIT'])
plt.xlabel('Prediksi Model')
plt.ylabel('Ground Truth')
plt.title('Confusion Matrix Logistic Regression')
plt.tight_layout()
plt.show()