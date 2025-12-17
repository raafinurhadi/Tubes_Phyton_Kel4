import pandas as pd
import numpy as np

df_raw = pd.read_excel("X:\Code\Tubes_Phyton_Kel4\Dataset\Raw\cars.xlsx")
df = df_raw.copy()

df = df[['MPG_City', 'Horsepower', 'Weight', 'Cylinders']]
df.dropna(inplace=True)

median_mpg = df['MPG_City'].median()
df['Irit_Boros'] = np.where(df['MPG_City'] >= median_mpg, 1, 0)

df.to_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv", index=False)
