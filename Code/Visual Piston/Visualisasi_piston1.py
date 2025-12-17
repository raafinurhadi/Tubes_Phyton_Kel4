import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

plt.scatter(df['Cylinders'], df['MPG_City'])
plt.xlabel("Cylinders")
plt.ylabel("MPG City")
plt.title("Hubungan antara banyaknya piston dengan MPG City pada dataset 1")
plt.show()