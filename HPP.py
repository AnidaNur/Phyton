print("Menghitung dana usaha produksi")

bahan = float(input('Masukkan Biaya bahan baku: '))
operasional = float(input('Masukkan overhead produksi: '))
tenaga = float(input('Masukkan biaya tenaga kerja: '))
olahan = float(input('Masukkan jumlah olahan: '))
butir = float(input('Masukkan hasil 1x olahan: '))

#Menghitung HPP keseluruhan (no 1)
total_HPP = bahan + operasional + tenaga

#HPP Perbutir bakso (no 2)
HPP_perbutir = total_HPP/ (olahan * butir)

#Menghitung untung (no 3)
untung = float(input('Masukkan keuntungan(%): '))
untung_desimal = untung / 100

Keuntungan_sekali_olah = untung_desimal * (total_HPP / olahan)
Keuntungan_perbutir = HPP_perbutir * untung_desimal

#Harga jual 
Harga_perbutir = HPP_perbutir + Keuntungan_perbutir
# Menampilkan hasil perhitungan
print ("Hasil perhitungan")
print('HPP Keseluruhan: %0.2f' % total_HPP)
print('HPP Perbutir: %0.2f' % HPP_perbutir)
print('Keuntungan sekali olah:  %0.2f' % Keuntungan_sekali_olah)
print('Keuntungan perbutir: %0.2f' % Keuntungan_perbutir)
print('Harga perbutir: %0.2f' % Harga_perbutir)

