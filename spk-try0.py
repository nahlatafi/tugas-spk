import pandas as pd

# Fungsi untuk normalisasi nilai kriteria (SAW)
def normalize_criteria(criteria_data):
    normalized_data = criteria_data.copy()
    for column in criteria_data.columns[1:]:
        max_value = criteria_data[column].max()
        min_value = criteria_data[column].min()
        normalized_data[column] = (criteria_data[column] - min_value) / (max_value - min_value)
    return normalized_data

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

# Contoh data kriteria dan bobot
data = {
    'Alternatif': ['A1', 'A2', 'A3', 'A4'],
    'Kriteria1': [3, 4, 5, 2],
    'Kriteria2': [5, 3, 4, 2],
    'Kriteria3': [2, 5, 4, 3],
}

criteria_weights = [0.4, 0.3, 0.3]  # Bobot untuk SAW dan WP

# Membuat DataFrame dari data
criteria_data = pd.DataFrame(data)

# Menghitung nilai SAW
saw_result = saw(criteria_data, criteria_weights)
print("Hasil SAW:")
print(saw_result[['Alternatif', 'SAW']])

# Menghitung nilai WP
wp_result = wp(criteria_data, criteria_weights)
print("\nHasil WP:")
print(wp_result[['Alternatif', 'WP']])
