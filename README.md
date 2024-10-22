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
    Variabel Max diinisialisasi dengan nilai 0. Variabel ini akan menyimpan angka terbesar yang dimasukkan
2. Perulangan while True:
    loop while yang berjalan tanpa henti, Perulangan ini akan terus berjalan sampai memasukkan angka 0, yang berfungsi sebagai tanda untuk menghentikan program.
3. Input:
    - Program meminta untuk memasukkan sebuah angka. Input tersebut kemudian dikonversi menjadi tipe integer dan disimpan dalam variabel N
    - Setelah mencetak hasilnya, program akan menghentikan eksekusi loop menggunakan break.
4. Memeriksa Angka 0:
    - Jika memasukkan angka 0, program akan menampilkan angka terbesar yang ditemukan (variabel Max). Setelah itu, program keluar dari loop menggunakan break.
    - Proses ini memastikan bahwa setiap kali ada angka yang lebih besar dari nilai maksimum sebelumnya, program akan menyimpannya sebagai angka terbesar yang baru.
6. Memperbarui Nilai Max:
    Jika angka yang dimasukkan lebih besar daripada nilai saat ini dari Max, nilai Max diperbarui menjadi angka tersebut.
7. Selesai
    Setelah loop berakhir (ketika pengguna memasukkan angka 0), program akan mencetak "Selesai" untuk menandakan akhir dari program.

# Foto Flowchart sebelumnya yang diubah 
![Foto](https://github.com/Manueljds2311105/foto/blob/5cb587465c0b8e98db2e38c46ae51c6d7063ffd6/Flowchart%202%20Baru.png)

# Foto Hasil Eksekusi Kode Python
![Foto](https://github.com/Manueljds2311105/foto/blob/e36a440372e16e0111e6cf32069eeefdb5bd07e7/Hasil%20eksekusi%20kode%20python.png)
