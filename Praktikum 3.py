# Inisialisasi angka maksimal ke 0  
Max = 0

while True:
    N = int(input("Masukkan angka: "))

    if N == 0:
        print("Angka terbesar adalah: " + str(Max))
        break
    if N > Max:  # Memperbarui nilai Max jika n lebih besar
        Max = N
print("Selesai")