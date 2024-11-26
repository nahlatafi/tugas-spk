import pandas as pd

# Data nilai masing-masing produk terhadap kriteria
data_nilai = {
    'Alternatif': ['Produk 1', 'Produk 2', 'Produk 3', 'Produk 4'],
    'Daya Tahan': [5, 4, 3, 2],
    'Umur': [5, 4, 4, 3],
    'Harga': [4, 3, 4, 3],
    'Layanan Purna Jual': [7, 6, 4, 3],
}
print("Data nilai masing-masing produk terhadap kriteria:")
print(data_nilai)

# Data total bobot awal (WP)
data_bobot_wp = {
    'Kriteria': ['Daya Tahan', 'Umur', 'Harga', 'Layanan Purna Jual'],
    'Total': [65, 70, 80, 35],
}
print("Data total bobot awal (WP):")
print(data_bobot_wp)

# Fungsi untuk normalisasi nilai kriteria (SAW)
def normalize_criteria(criteria_data):
    normalized_data = criteria_data.copy()
    for column in criteria_data.columns[1:]:
        max_value = criteria_data.loc['Nilai Maksimal', column]
        min_value = criteria_data.loc['Nilai Minimal', column]
        normalized_data[column] = (criteria_data[column] - min_value) / (max_value - min_value)
    return normalized_data

# Fungsi untuk normalisasi bobot (WP)
def normalize_weights(weights_data):
    total_weight = weights_data['Total'].sum()
    weights_data['Normalized'] = weights_data['Total'] / total_weight
    return weights_data['Normalized']

# Fungsi untuk menghitung nilai SAW
def saw(data, weights):
    normalized_data = normalize_criteria(data)
    scores = normalized_data.iloc[:, 1:].sum(axis=1)
    final_scores = scores / len(weights)
    data['SAW'] = final_scores
    return data

# Fungsi untuk menghitung nilai WP
def wp(data, weights):
    normalized_data = normalize_criteria(data)
    product = 1
    for column, weight in zip(normalized_data.columns[1:], weights):
        product *= normalized_data[column] ** weight
    final_scores = product.pow(1 / len(weights))
    data['WP'] = final_scores
    return data

# Data bobot awal (WP)
weights_data = pd.DataFrame(data_bobot_wp)

# Normalisasi bobot (WP)
normalized_weights = normalize_weights(weights_data)

# Data nilai masing-masing produk terhadap kriteria
criteria_data = pd.DataFrame(data_nilai)

# Menghitung nilai SAW
saw_result = saw(criteria_data, normalized_weights)
print("Hasil SAW:")
print(saw_result[['Alternatif', 'SAW']])

# Menghitung nilai WP
wp_result = wp(criteria_data, normalized_weights)
print("\nHasil WP:")
print(wp_result[['Alternatif', 'WP']])

# Menentukan Vektor V untuk Preferensi Perangkingan menggunakan metode WP
vectors = pd.DataFrame({
    'Alternatif': criteria_data['Alternatif'],
    'Nilai Preferensi': wp_result['WP']
})

# Menampilkan hasil perangkingan
sorted_result = vectors.sort_values(by='Nilai Preferensi', ascending=False)
print("\nHasil Perangkingan:")
print(sorted_result)