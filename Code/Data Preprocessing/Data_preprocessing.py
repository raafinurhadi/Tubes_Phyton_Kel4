import pandas as pd
import numpy as np

df_raw = pd.read_json("X:\Code\Tubes_Phyton_Kel4\Dataset\Raw\cars2.json")
df = df_raw.copy()

df = df[['Miles_per_Gallon', 'Horsepower', 'Weight_in_lbs', 'Cylinders']]
df.dropna(inplace=True)

median_mpg = df['Miles_per_Gallon'].median()
df['Irit_Boros'] = np.where(df['Miles_per_Gallon'] >= median_mpg, 1, 0)

df.to_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars2_processed.csv", index=False)
