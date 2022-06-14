#Latihan 8

#Pak Joni memiliki rencana untuk membeli sebuah rumah, tetapi sayangnya dia tidak punya banyak uang. 
#Dia berencana untuk membeli tetapi dengan cicilan ke bank saja. 
#Namun, sayangnya lagi-lagi untuk membayar DP pinjaman bankpun ia tidak punya. 
#Oleh karena itu, dia berencana untuk menabung setiap bulan agar bisa membayar DP. 

#Tugas anda : tentukan berapa lama dia harus menabung agar dia bisa membayar cicilan rumah tersebut.

# 1. Mintalah pak joni untuk membuat harga perkiraan rumah yang dia inginkan simpan pada variable, total_cost.

total_cost = float(input("Harga perkiraan rumah yang Anda inginkan: "))

# 2. Biasanya untuk DP rumah, bank akan mensyaratkan pembayaran DP sebesar 25%, simpan pada variabel portion_down_payment = 0.25.

portion_down_payment = 0.25

# 3. Tanyakan pak joni berapa uang yang sudah dia punya selama ini yang dicadangkan untuk membayar DP, simpan pada variable current_savings nilai defaultnya boleh anda set 0.

current_savings = float(input("Tabungan yang Anda miliki saat ini: ") or "0") 

# 4. Asumsikan bahwa pak joni menginvestasikan tabungan dengan bijak, sehingga memperoleh imbal hasil 5 % per tahun.

investment_return = 0.05

# 5. Simpan gaji tahunan pak joni dalam variabel annual_salary.

annual_salary = float(input("Berapa gaji tahunan Anda: "))

# 6. Tanyakan pak Joni persen dari gaji pak joni yang dia sisishkan untuk menabung simpan pada variable portion_saved. Variabel ini berbentuk decimal (contoh 0.1 untuk persentase 10%).

portion_saved = float(input("Berapa porsi yang Anda sisihkan dari gaji untuk diinvestasikan/ditabung: "))

# 7. Pada akhir tiap bulan bulan, tabungan anda akan meningkat sesuai dengan besarnya investasi ditambah dengan porsi gaji yang ditabungkan (gaji tahunan/ 12).

investment_period = 0
while(current_savings<portion_down_payment*total_cost):
  investment_period+=1
  current_savings = current_savings*(investment_return/12)+portion_saved*annual_salary/12

print("Jangka waktu investasi yang diperlukan adalah: %d bulan" %investment_period)
