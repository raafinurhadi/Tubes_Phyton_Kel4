import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

plt.scatter(df['Horsepower'], df['Miles_per_Gallon'])
plt.xlabel("Horsepower")
plt.ylabel("Miles Per Gallon")
plt.title("Hubungan antara kekuatan mesin dengan Miles per gallon")
plt.show()