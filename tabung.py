# Dibuat Oleh : Adiftya Rahmad
# Tanggal Pengerjaan : 22 Oktober 2024
# Program Menghitung Rumus Tabung

print("="*40)
print("PROGRAM TABUNG")
print("="*40)

r = int(input("Jari jari\t: "))
t = int(input("Tinggi\t\t: "))

lp = 2 * 3.14 * r * (r + t)
ls = 2 * 3.14 * r * t
v = 3.14 * r * r * t

print(f"Luas Permukaan\t: {lp}")
print(f"Luas Selimut\t: {ls}")
print(f"Volume\t\t: {v}")