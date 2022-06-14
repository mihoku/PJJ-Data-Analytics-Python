#Latihan 6

#Sebuah bilangan palindrom adalah angka yang jika dibaca dari depan kebelakang sama. 
#Contoh: 12321, 55555, 45554 and 11611. 
#Tulislah sebuah program yang membaca lima digit bilangan bulat untuk menentukan apakah mereka palindrome atau bukan. 
#[Hint: Use the // and % operators to separate the number into its digits.]

supposedly_palindrome = input("Coba input bilangan palindrome: ")
panjang_input = len(supposedly_palindrome)

#Teknik 1: menggunakan operator // dan %
bilangan_uji = int(supposedly_palindrome)
result = True

#selama angkanya belum habis(atau minus jika jumlah angka di bilangan palindrom ganjil, maka iterasi dijalankan terus menerus)
while(bilangan_uji>0):
  jumlah_angka_tersisa = len("%s"%bilangan_uji)
  #apakah floor division dari hasil perpangkatan tertinggi sepuluh sama dengan modula hasil perpangkatan terrendah sepuluh, dst..
  digit_depan = bilangan_uji // 10**(jumlah_angka_tersisa-1)
  digit_belakang = bilangan_uji % 10
  test = digit_depan==digit_belakang
  result = result and test

  #angka yang sudah diuji dihapus dari bilangan awal
  bilangan_uji = int((bilangan_uji-digit_belakang-(digit_depan*10**(jumlah_angka_tersisa-1)))/10)

if(result):
  print("Bilangan %s merupakan palindrome (Teknik 1)"%supposedly_palindrome)
else:
  print("Bilangan %s bukan merupakan palindrome (Teknik 1)"%supposedly_palindrome)

#Teknik 2: menggunakan string slicing
result2 = True

for a in range(panjang_input):
  digit_depan = supposedly_palindrome[a]
  digit_belakang = supposedly_palindrome[-a-1]
  test2 = digit_depan==digit_belakang
  result2 = result2 and test2

if(result2):
  print("Bilangan %s merupakan palindrome (Teknik 2)"%supposedly_palindrome)
else:
  print("Bilangan %s bukan merupakan palindrome (Teknik 2)"%supposedly_palindrome)

#Teknik 3: string inverse
test3 = supposedly_palindrome[::-1]==supposedly_palindrome
if(test3):
  print("Bilangan %s merupakan palindrome (Teknik 3)"%supposedly_palindrome)
else:
  print("Bilangan %s bukan merupakan palindrome (Teknik 3)"%supposedly_palindrome)
