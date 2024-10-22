# Input 3 bilangan 
A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))
C = int(input("Masukkan nilai C: "))

# Mengecek bilangan terbesar
if A > B and A > C:
    print("A adalah bilangan terbesar")
elif B > A and B > C:
    print("B adalah bilangan terbesar")
else:
    print("C adalah bilangan terbesar")