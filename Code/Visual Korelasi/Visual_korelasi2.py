import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars2_processed.csv")

features = [
    'Miles_per_Gallon',
    'Horsepower',
    'Weight_in_lbs',
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
