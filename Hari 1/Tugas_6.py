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

for i in range(panjang_input):
  #apakah floor division dari hasil perpangkatan tertinggi sepuluh sama dengan modula hasil perpangkatan terrendah sepuluh, dst..
  digit_depan = "%s"%(bilangan_uji // 10**(panjang_input-i-1))
  digit_belakang = ("%s"%(bilangan_uji % 10**(i+1)))[::-1]
  test = digit_depan==digit_belakang
  
  #print("digit depan : %s digit belakang: %s" %(digit_depan, digit_belakang))
  result = result and test

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
