import random

# Data tekanan darah
data_tekanan_darah = {
    "bayi <1 Bulan": {"sistolik": "45-80", "diastolik": "30-55"},
    "bayi <1 tahun": {"sistolik": "65-100", "diastolik": "35-65"},
    "Anak 1-5 tahun": {"sistolik": "80-115", "diastolik": "55-80"},
    "Anak 6-13 tahun": {"sistolik": "80-120", "diastolik": "45-80"},
    "Remaja 14-18 tahun": {"sistolik": "90-120", "diastolik": "50-80"},
    "Dewasa 19-40 tahun": {"sistolik": "93-135", "diastolik": "60-80"},
    "Dewasa 41-60 tahun": {"sistolik": "110-145", "diastolik": "70-90"},
    "Lansia >60 tahun": {"sistolik": "95-145", "diastolik": "70-90"}
}

def tanya_tekanan_darah():
    # Pilih kategori usia secara acak
    kategori = random.choice(list(data_tekanan_darah.keys()))
    
    # Pilih jenis tekanan darah secara acak (sistolik atau diastolik)
    jenis_tekanan = random.choice(["sistolik", "diastolik"])
    
    # Ambil rentang tekanan darah yang sesuai
    rentang_tekanan = data_tekanan_darah[kategori][jenis_tekanan]
    
    # Tanyakan pertanyaan kepada pengguna
    print(f"Berapakah rentang tekanan darah {jenis_tekanan} untuk {kategori}?")
    
    # Tunggu jawaban pengguna
    jawaban = input("Jawaban Anda: ")
    
    # Cek jawaban pengguna
    if jawaban.strip() == rentang_tekanan:
        print("Jawaban Anda benar!")
    else:
        print(f"Jawaban Anda salah. Jawaban yang benar adalah {rentang_tekanan}.")

# Loop untuk terus menanyakan pertanyaan
while True:
    tanya_tekanan_darah()
    lagi = input("Apakah Anda ingin mencoba lagi? (ya/tidak): ").strip().lower()
    if lagi != 'ya':
        break
