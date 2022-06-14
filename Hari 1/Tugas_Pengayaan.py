#Tugas Pengayaan

binary_number = input("Bilangan biner yang ingin dikonversi ke decimal: ")

#Teknik 1: string slicing dari kiri
decimal_conversion = 0
secure = True
for urutan_karakter in range(len(binary_number)):
  karakter = int(binary_number[urutan_karakter])
  if(karakter!=0 and karakter!=1):
    secure=False
    break
  pangkat = len(binary_number) - urutan_karakter - 1
  decimal_conversion = decimal_conversion+karakter*2**pangkat

if(secure):
  print("Bilangan biner %s jika dikonversi ke desimal menjadi %d (Teknik 1)" %(binary_number,decimal_conversion))
else:
  print("Bilangan biner %s invalid (Teknik 1)" %(binary_number))

#Teknik 2: string slicing dari kanan
decimal_conversion = 0
for urutan_karakter in range(len(binary_number)):
  karakter = int(binary_number[-urutan_karakter-1])
  pangkat = urutan_karakter
  decimal_conversion = decimal_conversion+karakter*2**pangkat

if(secure):
  print("Bilangan biner %s jika dikonversi ke desimal menjadi %d (Teknik 2)" %(binary_number,decimal_conversion))
else:
  print("Bilangan biner %s invalid (Teknik 2)" %(binary_number))
