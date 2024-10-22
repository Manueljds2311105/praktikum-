# PRAKTIKUM 3 KODE PYTHON DARI FLOWCHART

Nama: Manuel Johansen Dolok Saribu

Nim: 312410493

Dosen Pengampu: Agung Nugroho, S.Kom., M.Kom.,

Mata Pelajaran: Bahasa Pemograman

# Menentukan bilangan terbesar dari 3 bilangan yang diinputkan
# Foto flowchart 3 bilangan 
![FOTO](https://github.com/Manueljds2311105/foto/blob/b58f66cd98a9ae7600651efe368eeed0606ac030/flowchart%203%20bilangan.png)

# kode python 3 bilangan
```python
# Input 3 bilangan 
A = float(input("Masukkan nilai A: "))
B = float(input("Masukkan nilai B: "))
C = float(input("Masukkan nilai C: "))

# Mengecek bilangan terbesar
if A > B and A > C:
    print("A adalah bilangan terbesar")
elif B > A and B > C:
    print("B adalah bilangan terbesar")
else:
    print("C adalah bilangan terbesar")
```
Penjelasan:
- Program meminta input tiga bilangan A, B, Dan C
- Setelah itu, program memeriksa apakah A lebih besar dari B dan C, jika benar A adalah bilangan terbesar
- jika tidak, apakah B lebih besar dari A dan C, jika benar B adalah bilangan terbesar
- jika kedua bilangan A dan B tidak terbesar, Maka C adalah bilangan terbesar dari A dan B

# Foto hasil eksekusi kode program 3 bilangan
![FOTO](https://github.com/Manueljds2311105/foto/blob/9362d1918ade56ef42ffa83c5139634f80575731/Hasil%20eksekusi%20kode.png)
  
# Menentukan bilangan terbesar dari N bilangan yang diinputkan, untuk menentukan jumlah N, Masukkan angka 0
# Kode Python input N

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
    - Variabel Max diinisialisasi dengan nilai 0. Variabel ini akan menyimpan angka terbesar yang dimasukkan
2. Perulangan while True:
    - loop while/perulangan yang berjalan tanpa henti ini (hingga menemukan kondisi break). program akan terus berjalan sampai memasukkan angka 0, yang berfungsi sebagai tanda untuk menghentikan program
3. int(Input:
    - Program meminta untuk memasukkan sebuah angka. Input tersebut kemudian dikonversi menjadi tipe integer dan disimpan dalam variabel N
4. Memeriksa Angka 0:
    - Jika memasukkan angka 0, program akan menampilkan angka terbesar yang ada di (variabel Max)
    - Setelah mencetak hasilnya, program akan menghentikan eksekusi loop menggunakan break
6. Memperbarui Nilai Max:
    - Jika angka yang dimasukkan lebih besar daripada nilai saat ini dari Max, nilai Max diperbarui menjadi angka tersebut
    - Proses ini memastikan bahwa setiap kali ada angka yang lebih besar dari nilai maksimum sebelumnya, program akan menyimpannya sebagai angka terbesar yang baru
7. Selesai
    - Setelah loop berakhir (ketika memasukkan angka 0), program akan mencetak "Selesai" untuk menandakan akhir dari program

# Foto Flowchart sebelumnya yang diubah 
![Foto](https://github.com/Manueljds2311105/foto/blob/b58f66cd98a9ae7600651efe368eeed0606ac030/Flowchart%20input%200.png)

# Foto Hasil Eksekusi Kode Python input 0
![Foto](https://github.com/Manueljds2311105/foto/blob/b58f66cd98a9ae7600651efe368eeed0606ac030/Hasil%20eksekusi%20kode%20python.png)
