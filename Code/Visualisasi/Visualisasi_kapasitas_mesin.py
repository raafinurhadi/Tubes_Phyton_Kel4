import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

plt.scatter(df['Kapasitas Mesin'], df['MPG'])
plt.xlabel("Kapasitas Mesin")
plt.ylabel("Miles Per Gallon")
plt.title("Hubungan antara kapasitas mesin dengan Miles per gallon")
plt.show()