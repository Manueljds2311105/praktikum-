# PRAKTIKUM 3 CODE PYTHON DARI FLOWCHART

Nama: Manuel johansen Dolok Saribu

Nim: 312410493

Dosen Pengampu: Agung Nugroho, S.Kom., M.Kom.,

Mata Pelajaran: Bahasa Pemograman

# Kode Python Flowchart sebelumnya

```python
# Initialize max number to None (to handle the first input)
max_number = None

while True:
    # Ask for user input
    n = int(input("Enter a number (0 to stop): "))
    
    # If the input is 0, exit the loop
    if n == 0:
        break
    
    # If max_number is None or n is greater than max_number, update max_number
    if max_number is None or n > max_number:
        max_number = n

# Output the result
if max_number is not None:
    print("The largest number entered is:", max_number)
else:
    print("No numbers were entered.")
```

