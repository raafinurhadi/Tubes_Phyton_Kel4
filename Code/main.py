import joblib

def dataset1():
    model = joblib.load("X:\Code\Tubes_Phyton_Kel4\Model ML\model1_logistic.joblib")

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

def dataset2():
    model = joblib.load("X:\Code\Tubes_Phyton_Kel4\Model ML\model2_logistic.joblib")

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
    print("1. Analisis Menggunakan Model Dataset 1")
    print("2. Analisis Menggunakan Model Dataset 2")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        dataset1()
    elif pilihan == "2":
        dataset2()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
