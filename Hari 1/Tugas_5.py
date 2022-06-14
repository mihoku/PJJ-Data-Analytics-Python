#Latihan 5

#Buatlah script yang menerima input berupa lima digit angka dari user.
#Pisahkan angka menjadi digit indivual. Print secara terpisah dengan separator berupa tiga spasi
#Contoh: Jika user memasukkan 42339, maka hasil print adalah 4 2 3 3 9
#Asumsikan bahwa user selalu menginput angka dalam panjang yang tepat.

digit = input("Input 5 digit angka") #lebih atau kurang juga boleh sih, wkwk

result = ''
separated_digit = []

for urutan_digit in range(len(digit)):
  sep = digit[urutan_digit:urutan_digit+1]
  separated_digit.append(int(sep))
  result = result+sep+'   '

print(result)
