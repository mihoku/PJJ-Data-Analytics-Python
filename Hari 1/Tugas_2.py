#Tugas 2
#Berikut adalah suatu string 
# str = ’X-DSPAM-Confidence:0.8475’
#Gunakan 'find' dan 'string slicing' untuk mengekstrak porsi dari karakter setelah tanda kolon, kemudian gunakan ubahlah menjadi data float.

str = 'X-DSPAM-Confidence:0.8475'
processing_result = float(str[str.find(':')+1:])
processing_result
