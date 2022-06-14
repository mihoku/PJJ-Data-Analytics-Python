#Latihan 6

#Sebuah bilangan palindrom adalah angka yang jika dibaca dari depan kebelakang sama. 
#Contoh: 12321, 55555, 45554 and 11611. 
#Tulislah sebuah program yang membaca lima digit bilangan bulat untuk menentukan apakah mereka palindrome atau bukan. 
#[Hint: Use the // and % operators to separate the number into its digits.]

supposedly_palindrome = input("Coba input bilangan palindrome: ")
bilangan_uji = int(supposedly_palindrome)
panjang_input = len(supposedly_palindrome)
result = True

for i in range(panjang_input):
  #apakah floor division dari hasil perpangkatan tertinggi sepuluh sama dengan modula hasil perpangkatan terrendah sepuluh, dst..
  digit_depan = "%s"%(bilangan_uji // 10**(panjang_input-i-1))
  digit_belakang = ("%s"%(bilangan_uji % 10**(i+1)))[::-1]
  test = digit_depan==digit_belakang
  
  #print("digit depan : %s digit belakang: %s" %(digit_depan, digit_belakang))
  result = result and test

if(result):
  print("Bilangan %s merupakan palindrome"%supposedly_palindrome)
else:
  print("Bilangan %s bukan merupakan palindrome"%supposedly_palindrome)
