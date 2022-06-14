#Tugas Pengayaan
#Write a program that converts a binary (base 2) number to decimal (base 10). 
#Your program should begin by reading the binary number from the user as a string. 
#Then it should compute the equivalent decimal number by processing each digit in the binary number. 
#Finally, your program should display the equivalent decimal number with an appropriate message.

binary_number = input("Bilangan biner yang ingin dikonversi ke decimal: ")
decimal_conversion = 0
for urutan_karakter in range(len(binary_number)):
  karakter = int(binary_number[urutan_karakter:urutan_karakter+1])
  pangkat = len(binary_number) - urutan_karakter - 1
  decimal_conversion = decimal_conversion+karakter*2**pangkat

print("Bilangan biner %s jika dikonversi ke desimal menjadi %d" %(binary_number,decimal_conversion))
