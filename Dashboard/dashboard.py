import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
data = pd.read_csv('./main_data.csv')

# Title dashboard
st.title("Dashboard Penyewaan Sepeda")


# RATA-RATA PENYEWAAN HARIAN BERDASARKAN MUSIM 
# Pemberian label
season_labels = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
data['season_label'] = data['season'].map(season_labels)

# Visualisasi rata-rata penyewaan sepeda berdasarkan musim
st.header("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
season_avg = data.groupby('season_label')['cnt'].mean().reset_index()

# Mengurutkan data berdasarkan rata-rata penyewaan (descending)
season_avg = season_avg.sort_values('cnt', ascending=False)

# Membuat bar chart rata-rata penyewaan sepeda per musim
plt.figure(figsize=(8, 6))
sns.barplot(x='cnt', y='season_label', data=season_avg, palette='Blues_d')

# Menambahkan judul dan label
plt.title('Musim')
plt.xlabel('Rata-rata Penyewaan Sepeda Perhari Berdasarkan Musim')
plt.ylabel('Rata-rata Penyewaan Sepeda')
plt.xticks(rotation=0)
st.pyplot(plt)

# LINE CHART TREN PENYEWAAN
# Menambahkan multiselect untuk memilih tahun (bisa memilih 2011, 2012, atau keduanya)
st.sidebar.header("Pilih Tahun")
year_option = st.sidebar.multiselect("Pilih Tahun", options=[2011, 2012], default=[2011, 2012])

# Menambahkan slider untuk memilih rentang bulan
month_range = st.sidebar.slider('Pilih Rentang Bulan', 1, 12, (1, 12))

# Filter data berdasarkan pilihan tahun dan rentang bulan
filtered_data = data[(data['yr'].isin([year - 2011 for year in year_option])) & 
                     (data['mnth'] >= month_range[0]) & (data['mnth'] <= month_range[1])]

# Line chart untuk tren penyewaan sepeda berdasarkan bulan dan tahun
st.header(f"Tren Penyewaan Sepeda Tahun {', '.join(map(str, year_option))}")
monthly_avg = filtered_data.groupby(['yr', 'mnth'])['cnt'].mean().reset_index()

# Menambahkan label tahun dan bulan 
year_labels = {0: '2011', 1: '2012'}
month_labels = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'Mei', 6: 'Jun', 7: 'Jul', 8: 'Agu', 9: 'Sep', 10: 'Okt', 11: 'Nov', 12: 'Des'}
monthly_avg['yr'] = monthly_avg['yr'].map(year_labels)
monthly_avg['mnth'] = monthly_avg['mnth'].map(month_labels)

# Membuat line chart untuk membandingkan tren penyewaan sepeda berdasarkan bulan dan tahun
plt.figure(figsize=(10, 6))
sns.lineplot(x='mnth', y='cnt', hue='yr', data=monthly_avg, marker='o')

# Menambahkan judul dan label
plt.title(f'Tren Penyewaan Sepeda Berdasarkan Bulan untuk Tahun {", ".join(map(str, year_option))}')
plt.xlabel('Bulan')
plt.ylabel('Rata-rata Penyewaan Sepeda')
plt.xticks(rotation=45)
st.pyplot(plt)



