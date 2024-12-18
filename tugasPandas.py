import pandas as pd 
from collections import defaultdict 

# no 1 buat data frame 
dataframe_sampah = pd.read_csv("data sampah jawa barat.csv", 
usecols=['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']) 
dataframe_sampah.dropna(inplace=True) 
print(dataframe_sampah) 
 
print("="*50)

# no 2 hitunglah total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun tertentu. Tampilkan hasilnya
jumlahsampah_2019 = [] 
for index, row in dataframe_sampah.iterrows(): 
    if row['tahun'] == 2019: 
        jumlahsampah_2019.append(row['jumlah_produksi_sampah']) 
print(f"{sum(jumlahsampah_2019)} Ton") 
 
print("="*50)

# no 3 Jumlahkan Data Pertahun
totalsampah_pertahun = defaultdict(int)  
for index, row in dataframe_sampah.iterrows(): 
    totalsampah_pertahun[row['tahun']] += row['jumlah_produksi_sampah'] 
 
totalsampah_pertahun = dict(totalsampah_pertahun)  
for index, row in totalsampah_pertahun.items(): 
    print(f"Data sampah tahun {index}: {round(row, 2)} Ton")
    
print("="*50)


#no 4 Jumlahkan data per Kota/Kabupaten per tahun
totalsampah_perkota = defaultdict(int) 
 
for index, row in dataframe_sampah.iterrows(): 
    totalsampah_perkota[row['nama_kabupaten_kota']] += row['jumlah_produksi_sampah']  
    
totalsampah_perkota = dict(totalsampah_perkota) 
for index, row in totalsampah_perkota.items(): 
    print(f"Jumlah sampah di {index} dari tahun 2015-2021: {round(row, 2)} Ton") 

#Export hasil akhir menjadi CSV dan Excel
df_sampah = pd.DataFrame(list(totalsampah_perkota.items()), 
columns=['tahun', 'total_sampah']) 
df_sampah.to_csv('sampahkota_pertahun.csv', index=False) 
df_sampah.to_excel('sampahkota_pertahun.xlsx', index=False) 