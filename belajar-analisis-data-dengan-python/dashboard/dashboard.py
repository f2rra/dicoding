import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

st.write(
    """
    ## **Dashboard Brazilian E-Commerce | Olist**
    """
)

monthly_orders_df = pd.read_csv('dataframe/monthly_orders.csv')
col1,col2 = st.columns([3,1])

# PERTANYAAN 1
# Buat figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot data untuk 2016
ax.plot(
    monthly_orders_df["order_date"][:5], 
    monthly_orders_df["order_count"][:5], 
    marker='o', linewidth=2, color="#72BCD4", label="2016"
)

# Plot data untuk 2017
ax.plot(
    monthly_orders_df["order_date"][4:17], 
    monthly_orders_df["order_count"][4:17], 
    marker='s', linewidth=2, color="#FF6F61", label="2017"
)

# Plot data untuk 2018
ax.plot(
    monthly_orders_df["order_date"][16:], 
    monthly_orders_df["order_count"][16:], 
    marker='D', linewidth=2, color="#2E8B57", label="2018"
)

# Judul dan label
ax.set_title("Total Penjualan per Bulan (2016-2018)", loc="center", fontsize=20)
ax.set_xlabel("Bulan", fontsize=12)
ax.set_ylabel("Total Penjualan", fontsize=12)

# Rotasi label sumbu X agar mudah dibaca
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# Menampilkan legend
ax.legend()

# Menampilkan grid
ax.grid(True, linestyle="--", alpha=0.7)

# Tampilkan plot di Streamlit
# col2.pyplot(fig)
col1.pyplot(fig)
monthly_orders_df['order_date'] = pd.to_datetime(monthly_orders_df['order_date'])
col2.write(monthly_orders_df.sort_values(by='order_date', ascending=False).reset_index(drop=True))
# month = monthly_orders_df.loc[-1,'order_date'].month_name()
# col2.metric(label=f"Total Orders ({month}):", value="2569", delta=f"{2897-2569}")


col1,col2,col3 = st.columns([1,1,1])
products_counts = pd.read_csv('dataframe/product_counts.csv')
top_products_df = pd.read_csv('dataframe/top_products.csv')






# PERTANYAAN 2
# Warna untuk highlight kategori teratas
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# Buat figure
fig, ax = plt.subplots(figsize=(8, 5))

# Plot data
sns.barplot(
    x="count", 
    y="product_category_name",
    data=products_counts.head(),
    hue="product_category_name",
    palette=colors,
    legend=False,
    ax=ax  # Tambahkan ax agar sesuai dengan figure
)


ax.set_title("5 Kategori Produk dengan Penjualan Tertinggi (2016-2018)", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel("Total Penjualan")

col1.pyplot(fig)

# Warna untuk highlight kategori terendah
colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4"]

# Buat figure
fig, ax = plt.subplots(figsize=(8, 5))

# Plot data
sns.barplot(
    x="count", 
    y="product_category_name",
    data=products_counts.tail(),  # Mengambil kategori dengan penjualan terendah
    hue="product_category_name",
    palette=colors,
    legend=False,
    ax=ax  # Tambahkan ax agar sesuai dengan figure
)

# Judul dan label
ax.set_title("5 Kategori Produk dengan Penjualan Terendah (2016-2018)", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel("Total Penjualan")

# Tampilkan plot di Streamlit
col1.pyplot(fig)

# PERTANYAAN 3
# Warna untuk highlight kategori teratas
colors = ["#72BCD4"] + ["#D3D3D3"] * 19

# Filter hanya produk dengan review score 5, lalu urutkan berdasarkan persentase review
df_filtered = top_products_df[top_products_df.review_score == 5].sort_values(by="reviews_percentage", ascending=False)

# Buat figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data
sns.barplot(
    x=df_filtered.reviews_percentage, 
    y=df_filtered.product_category_name,
    data=df_filtered,
    hue=df_filtered.product_category_name,
    palette=colors,
    legend=False,
    ax=ax  # Pastikan menggunakan ax agar figure sesuai
)

# Judul dan label
ax.set_title("Persentase Kategori Produk dengan Skor Review 5", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel("Total Review (%)")

# Tampilkan plot di Streamlit
col3.pyplot(fig)

# Warna untuk highlight kategori terbawah
colors = ["#D3D3D3"] * 19 + ["#72BCD4"]

# Filter hanya produk dengan review score 1, lalu urutkan berdasarkan persentase review
df_filtered = top_products_df[top_products_df.review_score == 1].sort_values(by="reviews_percentage")

# Buat figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data
sns.barplot(
    x=df_filtered.reviews_percentage, 
    y=df_filtered.product_category_name,
    data=df_filtered,
    hue=df_filtered.product_category_name,
    palette=colors,
    legend=False,
    ax=ax  # Pastikan menggunakan ax agar figure sesuai
)

# Judul dan label
ax.set_title("Persentase Kategori Produk dengan Skor Review 1", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel("Total Review (%)")

# Tampilkan plot di Streamlit
col3.pyplot(fig)