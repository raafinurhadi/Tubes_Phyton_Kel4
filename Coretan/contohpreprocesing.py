import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# membaca dan menampilkan 5 data awal
df = pd.read_csv('data_car_2025(in).csv')
df.head(5)

# memunculkan tipe data dan header data
df.dtypes

# merename header data 
df = df.rename(columns = {"Make":"Merk", "Engine HP":"Tenaga Mesin", "MSRP":"Harga"})
df.head(5)

#menghapus header data spesifik
df = df.drop({"Number of Doors"}, axis=1)
df.head(5)

# melihat banyaknya data dan berapa banyak kolom yang dimiliki
df.shape

# mencari berapa banyak data yang terduplikat
baris_duplikat = df[df.duplicated()]
print("jumlah data duplikat adalah", baris_duplikat.shape)

# menghitung berapa banyak data dari setiap kolom header
df.count()

# menghapus data yang terduplikat
df = df.drop_duplicates()
df.head(5)

# menghitung kembali berapa banyak data setelah dihapus
df.count()

# melihat berapa banyak data yang kosong pada setiap header
print(df.isnull().sum())

# menghapus data yang kosong
df = df.dropna()
df.count()

# melihat ulang data yang kosong setelah dihapus
print(df.isnull().sum())

# membuat boxplot untuk melihat outlier
f = plt.figure(figsize=(12,4))
f.add_subplot(1,2,1)
df["Tenaga Mesin"].plot(kind="kde")
f.add_subplot(1,2,2)
plt.boxplot(df["Tenaga Mesin"])
plt.show()