import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

plt.scatter(df['Tenaga Mesin'], df['MPG'])
plt.xlabel("Tenaga Mesin")
plt.ylabel("Miles Per Gallon")
plt.title("Hubungan antara kekuatan mesin dengan Miles per gallon")
plt.show()