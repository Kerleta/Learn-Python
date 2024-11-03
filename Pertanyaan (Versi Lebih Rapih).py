import random

# Data tekanan darah berdasarkan kategori usia
data_tekanan_darah = {
    "Bayi <1 Bulan": {"Sistolik": (45, 80), "Diastolik": (30, 55)},
    "Bayi <1 Tahun": {"Sistolik": (65, 100), "Diastolik": (35, 65)},
    "Anak 1-5 Tahun": {"Sistolik": (80, 115), "Diastolik": (55, 80)},
    "Anak 6-13 Tahun": {"Sistolik": (80, 120), "Diastolik": (45, 80)},
    "Remaja 14-18 Tahun": {"Sistolik": (90, 120), "Diastolik": (50, 80)},
    "Dewasa 19-40 Tahun": {"Sistolik": (93, 135), "Diastolik": (60, 80)},
    "Dewasa 41-60 Tahun": {"Sistolik": (110, 145), "Diastolik": (70, 90)},
    "Lansia >60 Tahun": {"Sistolik": (95, 145), "Diastolik": (70, 90)},
}

def tanya_tekanan_darah():
    kategori = random.choice(list(data_tekanan_darah.keys()))
    jenis_tekanan = random.choice(["Sistolik", "Diastolik"])
    nilai_tekanan = data_tekanan_darah[kategori][jenis_tekanan]
    
    print(f"Berapakah rentang {jenis_tekanan} untuk kategori {kategori}?")
    jawaban = input("Masukkan jawaban Anda (misalnya 45-80): ")

    try:
        jawaban_min, jawaban_max = map(int, jawaban.split('-'))
        if jawaban_min == nilai_tekanan[0] and jawaban_max == nilai_tekanan[1]:
            print("Jawaban Anda benar!")
        else:
            print(f"Jawaban Anda salah. Rentang yang benar adalah {nilai_tekanan[0]}-{nilai_tekanan[1]}.")
    except ValueError:
        print("Format jawaban Anda salah. Silakan masukkan dalam format 'min-max'.")

# Menanyakan 5 pertanyaan
for _ in range(5):
    tanya_tekanan_darah()
    print()
