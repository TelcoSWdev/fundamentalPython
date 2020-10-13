# Konstruksi Dasar Python
# Sequential: Eksekusi Berurutan

print('Hello World!')
print('by Irfan')
print('tanggal 14 Okt 2020')
print('-' * 10)

# Percabangan: Eksekusi Terpilih

ingin_cepat = True
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('Jalan lain')

# Perulangan
jumlah_anak = 4

for index_anak in range(1,jumlah_anak+1): #jumlah perulangan = 5-1 = 4
    print(f'Halo anak #{index_anak}')