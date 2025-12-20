import joblib

def dataset():
    model = joblib.load("X:\Code\Tubes_Phyton_Kel4\Model ML\model_logistic.joblib")

    a = int(input("Masukkan horsepower kendaraan: "))
    b = int(input("Masukkan berat kendaraan: "))
    c = int(input("Masukkan jumlah silinder: "))

    analisis = [[a, b, c]]
    preds = model.predict(analisis)

    if preds[0] == 1:
        hasil = "IRIT"
    else:
        hasil = "BOROS"

    print(f"Hasil prediksi kendaraan: {hasil}")
    return hasil

while True:
    print("=== MENU ===")
    print("1. Analisis Menggunakan Model Dataset")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    
    if pilihan == "1":
        dataset()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
