#Latihan 7 

# Konversi derajat celcius ke fahrenheit diatur oleh persamaan berikut :  
# F=(9/5)∗C+32  
# Gunakan fungsi ini untuk memprint suatu daftar konversi temperatur dari celcius untuk range 0–100. 
# Gunakan presisi 1 digit.

def CelciusToFahrenheit(celcius):
  Fahrenheit = (9/5)*celcius+32
  return Fahrenheit

for i in range(101):
  print("%.1f° C = %.1f° F"%(i, CelciusToFahrenheit(i)))
