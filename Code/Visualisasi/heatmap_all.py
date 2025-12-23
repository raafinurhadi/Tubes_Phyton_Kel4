import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_json('X:\Code\Tubes_Phyton_Kel4\Dataset\Raw\cars2.json')

df_numeric = df.select_dtypes(include=['int64', 'float64'])

corr_matrix = df_numeric.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Heatmap Korelasi Antar Fitur Numerik")
plt.tight_layout()
plt.show()