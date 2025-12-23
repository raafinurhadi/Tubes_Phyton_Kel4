import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

plt.scatter(df['Berat Dalam LBS'], df['MPG'])
plt.xlabel("Berat")
plt.ylabel("Miles Per Gallon")
plt.title("Hubungan antara berat kendaraan dengan Miles per gallon")
plt.show()