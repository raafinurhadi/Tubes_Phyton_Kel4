import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv")

sns.histplot(
    data=df,
    x='MPG',
    hue='Irit atau Boros',
    bins=20,
    kde=True
)

plt.title('Distribusi MPG: Irit vs Boros')
plt.xlabel('Miles per Gallon')
plt.ylabel('Jumlah Kendaraan')
plt.show()
