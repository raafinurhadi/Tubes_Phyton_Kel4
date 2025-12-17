import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars2_processed.csv")

plt.scatter(df['Cylinders'], df['Miles_per_Gallon'])
plt.xlabel("Cylinders")
plt.ylabel("Miles Per Gallon")
plt.title("Hubungan antara banyaknya piston dengan MPG City pada dataset 2")
plt.show()