#buat aplikasi untuk menghitung luas permukaan tabung
# v * r * r + 2 * 3.14 * r * t

r = int(input("Jari Jari: "))
t = int(input("Tinggi: "))
v = int(input("Volume: "))

lp = 3.14 * r * r + 2 * 3.14 * r * t

print(f"Luas Permukaan: {lp}")
