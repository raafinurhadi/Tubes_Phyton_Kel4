import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

plt.scatter(df['Horsepower'], df['MPG_City'])
plt.xlabel("Horsepower")
plt.ylabel("MPG City")
plt.title("Hubungan antara kekuatan mesin dengan MPG City pada dataset 1")
plt.show()