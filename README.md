# Analisis Efisiensi Penggunaan Bahan Bakar Pada Mobil Menggunakan Machine Learning 

## Deskripsi
Proyek ini bertujuan untuk menganalisis dan memprediksi efisiensi bahan bakar mobil berdasarkan karakteristik kendaraan menggunakan machine learning. Efisiensi bahan bakar diklasifikasikan menjadi dua kategori, yaitu irit dan boros.

## Tujuan
1. Menganalisis pola penggunaan bahan bakar pada mobil.
2. Mengidentifikasi karakteristik kendaraan yang mempengaruhi efisiensi bahan bakar.
3. Membangun model machine learning untuk memprediksi kategori mobil irit atau boros bahan bakar.
4. Memberikan rekomendasi kendaraan yang lebih efisien dan ramah lingkungan.

## Dataset
Dataset yang digunakan berasal dari https://github.com/hananlu/basicPython/blob/master/Dataset/cars2.json

yang berisi spesifikasi mobil seperti : 
1. Jumlah silinder (`Cylinders`)
2. Kapasitas mesin (`Displacement`)
3. Tenaga mesin (`Horsepower`)
4. Berat kendaraan (`Weight_in_lbs`)
5. Akselerasi (`Acceleration`)
6. Tahun produksi (`Year`)
7. Asal kendaraan (`Origin`)
8. Konsumsi bahan bakar dalam Miles Per Gallon (MPG) (`Miles_per_Gallon`)

## Machine Learning
Model utama yang digunakan pada proyek ini adalah Logistic Regression dengan pembagian data menggunakan train-test split dan evaluasi model menggunakan akurasi yang berdasarkan confusion matrix.

## Fitur Yang Digunakan
Berdasarkan scatter plot dan heatmap, korelasi terbanyak antara masing masing label dengan Miles Per Gallon adalah berat kendaraan, besar horsepower, dan jumlah silindernya dan ketiga label inilah yang akan dijadikan sebagai fitur.

## Visualisasi
Visualisasi yang ditampilkan pada proyek ini adalah:
1. Perbandingan antara berat kendaraan dengan MPG
2. Perbandingan antara kekuatan mesin dengan MPG
3. Perbandingan antara banyak piston dengan MPG
4. Distribusi kendaraan irit dan boros
5. Confusion matrix

## Hasil Dan Kesimpulan
1. Berat kendaraan dan jumlah piston memiliki pengaruh signifikan terhadap efisiensi bahan bakar.
2. Model Logistic Regression mampu mengklasifikasikan mobil irit dan boros dengan performa yang baik.
3. Berdasarkan hasil tersebut, kendaraan dengan berat yang ringan dan jumlah silinder lebih sedikit direkomendasikan sebagai pilihan yang lebih hemat bahan bakar dan ramah lingkungan.

## Coretan
https://www.canva.com/design/DAG7mBzojS8/lrzYnMPsFRdp7nWtoJKuUQ/edit?utm_content=DAG7mBzojS8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
