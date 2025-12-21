import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

plt.scatter(df['Weight_in_lbs'], df['Miles_per_Gallon'])
plt.xlabel("Weight")
plt.ylabel("Miles Per Gallon")
plt.title("Hubungan antara berat kendaraan dengan Miles per gallon")
plt.show()