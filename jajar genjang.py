# Dibuat Oleh : Adiftya Rahmad
# Tanggal Pengerjaan : 22 Oktober 2024
# Program Menghitung Rumus Jajar Genjang

print("="*40)
print("PROGRAM JAJAR GENJANG")
print("="*40)

a = int(input("Alas\t\t: "))
t = int(input("Tinggi\t\t: "))
sm = int(input("Sisi Miring\t: "))

l = a * t
k = 2 * (a + sm)

print(f"Luas\t\t: {l}")
print(f"Keliling\t: {k}")