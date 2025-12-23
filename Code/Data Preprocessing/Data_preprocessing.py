import pandas as pd
import numpy as np

df_raw = pd.read_json("X:\Code\Tubes_Phyton_Kel4\Dataset\Raw\cars2.json")
df = df_raw.copy()

baris_duplikat = df[df.duplicated()]
print("jumlah data duplikat adalah", baris_duplikat.shape)

print(df.isnull().sum())

df = df.rename(columns = {"Miles_per_Gallon":"MPG", "Horsepower":"Tenaga Mesin", "Weight_in_lbs":"Berat Dalam LBS", "Displacement":"Kapasitas Mesin"})
df.head(5)

df = df[['MPG', 'Tenaga Mesin', 'Berat Dalam LBS', 'Kapasitas Mesin']]
df.dropna(inplace=True)

median_mpg = df['MPG'].median()
df['Irit atau Boros'] = np.where(df['MPG'] >= median_mpg, 1, 0)

df.to_csv("X:\Code\Tubes_Phyton_Kel4\Dataset\Processed\cars_processed.csv", index=False)
