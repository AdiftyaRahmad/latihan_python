# Dibuat Oleh : Adiftya Rahmad
# Tanggal Pengerjaan : 08 November 2024
# Program Bulan

bulan = ['januari','februari','maret','april','mei','juni','july','agustus','september','oktober','november','desember']
print(bulan[2], bulan[9])
bulan.append('muharram')
index = 1
for data in bulan:
    print(f'bulan ke -{index} : {data}')
    index = index+1