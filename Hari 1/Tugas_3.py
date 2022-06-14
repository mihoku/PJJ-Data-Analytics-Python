#Latihan 3
#Banyaknya hari dalam satu bulan bervariasi dari 28 hingga 31. 
#Buatlah program yang memasukkan nama bulan dari user (string). 
#Kemudian program harus melakukan perhitungan jumlah hari dalam bulan tersebut. 
#Untuk bulan februari keluaran berupa string “28 atau 29 hari” for agar berlaku juga untuk bulan kabisat.

bulan = input("Masukkan nama bulan: ")

ganjil = ["Jan", "January", "Januari","Mar","March","Maret","May","Mei","Jul","July","Juli","Aug","Agu","August","Agustus","Oct","Okt","October","Oktober","Dec","Des","December","Desember"]
genap = ["Apr","April","Jun","June","Juni","Sep","September","Nov","November"]
gajelas = ["Feb","February","Februari"]

if(bulan.capitalize() in ganjil):
  print("Pada bulan %s terdapat 31 hari"%bulan)
elif(bulan.capitalize() in genap):
  print("Pada bulan %s terdapat 30 hari"%bulan)
elif(bulan.capitalize() in gajelas):
  print("Pada bulan %s terdapat 28 atau 29 hari"%bulan)
else:
  print("Nama bulan yang Anda berikan invalid")
