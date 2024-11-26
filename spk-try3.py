import pandas as pd

print("\n")
print("Kombinasi Metode SPK SAW & WP Dalam Menentukan Produk Terbaik")
print("==============================================================")

# Data nilai masing-masing produk terhadap kriteria
data_nilai = {
    'Alternatif': ['Produk 1', 'Produk 2', 'Produk 3', 'Produk 4', 'Nilai Maksimal', 'Nilai Minimal'],
    'Daya Tahan': [5, 4, 3, 2, 5, 2],
    'Umur': [5, 4, 4, 3, 5, 3],
    'Harga': [4, 3, 4, 3, 4, 3],
    'Layanan Purna Jual': [7, 6, 4, 3, 7, 3],
}

# Membuat DataFrame dari data1
df = pd.DataFrame(data_nilai)
print("\n\n")
print("1. Data nilai masing-masing produk terhadap kriteria:")
print(df)

# Data total bobot awal (WP)
data_bobot_wp = {
    'Kriteria': ['Daya Tahan', 'Umur', 'Harga', 'Layanan Purna Jual', 'Total'],
    'Bobot': [65, 70, 80, 35, 250],
}

# Membuat DataFrame dari data2
df2 = pd.DataFrame(data_bobot_wp)
print("\n\n")
print("2. Data total bobot awal (WP):")
print(df2)

# Data normalisasi menggunakan persamaan pada metode (SAW)
data_kriteria = {
    'Kriteria': ['Daya Tahan', 'Umur', 'Harga', 'Layanan Purna Jual'],
    'Jenis Kriteria': ['Keuntungan (benefit)', 'Keuntungan (benefit)', 'Biaya (cost)', 'Keuntungan (benefit)'],
    'Keterangan': [
        'Semakin besar daya tahan suatu produk semakin baik',
        'Semakin besar umur suatu produk semakin baik',
        'Semakin kecil harga suatu produk semakin baik',
        'Semakin banyak layanan purna jual suatu produk semakin baik',
    ],
}

# Membuat DataFrame dari data3
df3 = pd.DataFrame(data_kriteria)
print("\n\n")
print("3. Data normalisasi menggunakan persamaan pada metode (SAW):")
print(df3)

# Mendefinisikan nilai maksimal dan minimal
nilai_maksimal = df.loc[df['Alternatif'] == 'Nilai Maksimal'].iloc[:, 1:]
nilai_minimal = df.loc[df['Alternatif'] == 'Nilai Minimal'].iloc[:, 1:]

# # Normalisasi menggunakan rumus yang disebutkan
# for column in df.columns[1:]:
#     if column in ['Daya Tahan', 'Umur', 'Layanan Purna Jual']:
#         df[column] = df[column] / nilai_maksimal[column].values[0]
#     else:
#         df[column] = nilai_minimal[column].values[0] / df[column]

# Normalisasi menggunakan rumus yang disebutkan
for column in df.columns[1:]:
    if column in ['Daya Tahan', 'Umur', 'Layanan Purna Jual']:
        df[column] = df[column] / nilai_maksimal[column].values[0]
    else:
        df[column] = df[column] / nilai_minimal[column].values[0]

# Menampilkan hasil normalisasi tanpa "Nilai Maksimal" dan "Nilai Minimal"
filtered_df = df[df['Alternatif'].isin(['Produk 1', 'Produk 2', 'Produk 3', 'Produk 4'])]
print("\n")
print("Hasil normalisasi:")
print(filtered_df.to_string(index=False))

# Mendefinisikan bobot awal untuk setiap kriteria
bobot_daya_tahan = df2.loc[df2['Kriteria'] == 'Daya Tahan', 'Bobot'].values[0]
bobot_umur = df2.loc[df2['Kriteria'] == 'Umur', 'Bobot'].values[0]
bobot_harga = df2.loc[df2['Kriteria'] == 'Harga', 'Bobot'].values[0]
bobot_layanan_purna_jual = df2.loc[df2['Kriteria'] == 'Layanan Purna Jual', 'Bobot'].values[0]

# Normalisasi bobot
total_bobot = df2.loc[df2['Kriteria'] == 'Total', 'Bobot'].values[0]
bobot_normalisasi_daya_tahan = bobot_daya_tahan / total_bobot
bobot_normalisasi_umur = bobot_umur / total_bobot
bobot_normalisasi_harga = bobot_harga / total_bobot
bobot_normalisasi_layanan_purna_jual = bobot_layanan_purna_jual / total_bobot

# Menampilkan hasil normalisasi bobot
print("\n\n")
print("4. Normalisasi Bobot menggunakan persamaan pada metode (WP):")
print(f"\tbenefit\tbenefit\tcost\tbenefit")
print(f"\t{
    bobot_normalisasi_daya_tahan:.2f}\t{bobot_normalisasi_umur:.2f}\t{
    bobot_normalisasi_harga:.2f}\t{bobot_normalisasi_layanan_purna_jual:.2f
    }")

# # Menentukan nilai Vektor Sj menggunakan persamaan di Metode (WP)
# nilai_vektor = {
#     'Produk': ['Produk 1', 'Produk 2', 'Produk 3', 'Produk 4', 'Total'],
#     'Daya Tahan': [1.000, 0.944, 0.876, 0.788, None],
#     'Umur': [1.000, 0.939, 0.939, 0.867, None],
#     'Harga': [1.096, 1.000, 1.096, 1.000, None],
#     'Layanan Purna Jual': [1.000, 0.979, 0.925, 0.888, None],
#     'Sj': [4.096, 3.8617, 3.836, 3.543, 15.337]
# }



# # Menampilkan nilai Vektor
# df4 = pd.DataFrame(nilai_vektor)
# print("\n\n")
# print("5. Menentukan nilai Vektor Sj menggunakan persamaan di Metode WP:")
# print(df4)

# Menentukan nilai Vektor Sj menggunakan persamaan di Metode (WP)
nilai_vektor = {
    'Produk': ['Produk 1', 'Produk 2', 'Produk 3', 'Produk 4', 'Total'],
    'Daya Tahan': [1.000, 0.944, 0.876, 0.788, None],
    'Umur': [1.000, 0.939, 0.939, 0.867, None],
    'Harga': [1.096, 1.000, 1.096, 1.000, None],
    'Layanan Purna Jual': [1.000, 0.979, 0.925, 0.888, None],
    'Sj': [4.096, 3.8617, 3.836, 3.543, 15.337]
}

# Membuat DataFrame dari data4
df4 = pd.DataFrame(nilai_vektor)
print("\n\n")
print("5. Menentukan nilai Vektor Sj menggunakan persamaan di Metode WP:")
df_nilai_vektor = pd.DataFrame(nilai_vektor)
print(df_nilai_vektor)

# Menghitung nilai preferensi
df4['Nilai Preferensi'] = df4['Sj'] / df4['Sj'].iloc[-1]

# MMembuat DataFrame dari data5
print("\n\n")
print("6. Menentukan Vektor V untuk Preferensi Perangkingan Menggunakan Persamaan pada metode WP:")
df5 = df4[df4['Produk'] != 'Total'][['Produk', 'Nilai Preferensi']]
print(df5)
print("\nBerdasarkan nilai vektor V diatas maka alternatif terbaik adalah produk 1.\n")
