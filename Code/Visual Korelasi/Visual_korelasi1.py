import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

features = [
    'MPG_City',
    'Horsepower',
    'Weight',
    'Cylinders'
]
corr_matrix = df[features].corr()
print(corr_matrix)

plt.figure(figsize=(8,6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt=".2f"
)
plt.title("Heatmap Korelasi Fitur terhadap Efisiensi Bahan Bakar")
plt.show()
