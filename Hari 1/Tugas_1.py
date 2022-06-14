#Tugas 1
#Buatlah sebuah program dengan masukan berupa tiga bilangan bulat dari user. 
#Kemudian program akan melakukan perhitungan dan menghasilkan keluaran berupa jam dan menit sisanya bila ada.

#Contoh keluaran bila input dari user 121:
#Hours
#2
#Minutes
#1

minutes = int(input("Masukkan angka menit untuk dikonversi ke jam: "))
hour_converter= minutes//60
print('Hours\n%d'%hour_converter)
minute_converter = minutes%60
print('Minutes\n%d'%minute_converter)
