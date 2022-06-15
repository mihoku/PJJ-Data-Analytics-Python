original_str = "Pemerintah berencana untuk melarang mobil kubikasi mesin besar alias cc besar untuk membeli Bahan Bakar Minyak (BBM) dengan kadar oktan 90 jenis Pertalite. Saat ini, wacana tersebut masih terus digodok."

# Masukkan string ke dalam list
splitted_text = original_str.split(" ")
print("List Awal: ")
print(splitted_text)

#Membersihkan List dari karakter tanda baca
disallowed_characters = ".(),!?#$%"
cleaned_list = []
for i in splitted_text:
  for x in disallowed_characters:
    i = i.replace(x,"")
  cleaned_list.append(i)

print("List setelah dibersihkan: ")
print(cleaned_list)
splitted_text = cleaned_list

# Ganti 90 menjadi 98
splitted_text[splitted_text.index("90")]="98"
print("Ganti 90 menjadi 98")
print(splitted_text)

# Hapuskan BBM
splitted_text.remove("BBM")
print("Hapuskan BBM")
print(splitted_text)

#Tambahkan jenis pertamax setelah pertalite
splitted_text.insert(splitted_text.index("Pertalite")+1,"Pertamax")
print("Tambah Pertamax setelah Pertalite")
print(splitted_text)

