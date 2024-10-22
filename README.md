# PRAKTIKUM 3 CODE PYTHON DARI FLOWCHART

Nama: Manuel johansen Dolok Saribu

Nim: 312410493

Dosen Pengampu: Agung Nugroho, S.Kom., M.Kom.,

Mata Pelajaran: Bahasa Pemograman

# Kode Python

```python
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
```

# Penjelasan Kode:
1. Inisialisasi Max = 0:
Anda menginisialisasi variabel Max dengan nilai 0, yang akan digunakan untuk menyimpan angka terbesar yang dimasukkan oleh pengguna.
2. Perulangan while True:
Perulangan ini akan terus berjalan sampai pengguna memasukkan angka 0, yang berfungsi sebagai tanda untuk menghentikan program.
3. Menerima Input:
Program meminta pengguna memasukkan angka dengan input(). Input tersebut dikonversi ke tipe integer dengan int().
4. Memeriksa Angka 0:
Jika pengguna memasukkan angka 0, program akan mencetak "Selesai" dan menampilkan angka terbesar yang ditemukan sejauh ini (variabel Max). Setelah itu, program keluar dari loop menggunakan break.
5. Memperbarui Nilai Max:
Jika angka yang dimasukkan lebih besar daripada nilai saat ini dari Max, nilai Max diperbarui menjadi angka tersebut.
6. Mencetak Angka Terbesar:
Setelah perulangan selesai (saat n == 0), program mencetak angka terbesar yang dimasukkan oleh pengguna menggunakan print("Angka terbesar adalah: " + str(Max)). Fungsi str() digunakan untuk mengonversi angka (integer) ke string 

# Foto Flowchart sebelumnya yang diubah 
![Foto](https://github.com/Manueljds2311105/foto/blob/5cb587465c0b8e98db2e38c46ae51c6d7063ffd6/Flowchart%202%20Baru.png)

# Foto Hasil Eksekusi Kode Python
![Foto](https://github.com/Manueljds2311105/foto/blob/e36a440372e16e0111e6cf32069eeefdb5bd07e7/Hasil%20eksekusi%20kode%20python.png)
