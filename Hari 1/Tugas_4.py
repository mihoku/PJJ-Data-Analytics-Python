#Latihan 4
#Skala Richter Magnitude Descriptor 
#Less than 2.0 Micro 
#2.0 to less than 3.0 Very Minor 
#3.0 to less than 4.0 Minor 
#4.0 to less than 5.0 Light 
#5.0 to less than 6.0 Moderate 
#6.0 to less than 7.0 Strong 
#7.0 to less than 8.0 Major 
#8.0 to less than 10.0 Great 
#10.0 or more Meteoric

#Buatlah program yang membaca besarnya magnitude dari user dan memberikan keluaran terkait grade dari kekuatan gempa.
#Contoh keluaran : 'Gempa berskala 5,5 berkategori Moderat'

magnitude = float(input("Magnitude dari gempa: "))
if(magnitude<2.0):
  kategori = 'Micro'
elif(magnitude<3.0):
  kategori = 'Very Minor'
elif(magnitude<4.0):
  kategori = 'Minor'
elif(magnitude<5.0):
  kategori = 'Light'
elif(magnitude<6.0):
  kategori = 'Moderate'
elif(magnitude<7.0):
  kategori = 'Strong'
elif(magnitude<8.0):
  kategori = 'Major'
elif(magnitude<10.0):
  kategori = 'Great'
else: 
  kategori = 'Meteoric'

print('Gempa berskala %.1f berkategori %s' %(magnitude,kategori))
