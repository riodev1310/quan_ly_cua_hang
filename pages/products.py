import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dataset
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/Sample-Superstore.csv")

df = load_data()

st.title("Quản lý Sản phẩm (Product Inventory)")

# Danh sách sản phẩm
st.subheader("Danh sách Sản phẩm")
products = df[['Product ID', 'Product Name', 'Category', 'Sub-Category', 'Sales', 'Quantity']].drop_duplicates(subset=['Product ID'])
st.dataframe(products)

# Doanh thu theo Danh mục
st.subheader("Doanh thu theo Danh mục và Phân danh mục")
sales_by_cat = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(data=sales_by_cat, x='Category', y='Sales', hue='Sub-Category', ax=ax)
ax.set_title('Doanh thu theo Danh mục')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Top sản phẩm bán chạy
st.subheader("Top 10 Sản phẩm theo Số lượng Bán")
top_products = df.groupby('Product Name')['Quantity'].sum().nlargest(10).reset_index()
fig, ax = plt.subplots()
sns.barplot(data=top_products, x='Product Name', y='Quantity', ax=ax)
ax.set_title('Top 10 Sản phẩm Bán chạy')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Tìm kiếm sản phẩm
search_product = st.text_input("Tìm kiếm Sản phẩm theo Tên")
if search_product:
    filtered = products[products['Product Name'].str.contains(search_product, case=False)]
    st.dataframe(filtered)