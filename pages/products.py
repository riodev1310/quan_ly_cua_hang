import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dataset từ URL trực tuyến
@st.cache_data
def load_data():
    url = "https://gist.githubusercontent.com/nnbphuong/38db511db14542f3ba9ef16e69d3814c/raw/Superstore.csv"
    return pd.read_csv(url)

df = load_data()

st.title("Quản lý Sản phẩm (Product Inventory)")

# Danh sách sản phẩm
st.subheader("Danh sách Sản phẩm")
products = df[['Product ID', 'Product Name', 'Category', 'Sub-Category', 'Sales', 'Quantity']].drop_duplicates(subset=['Product ID'])
st.dataframe(products)

# Doanh thu theo Danh mục
st.subheader("Doanh thu theo Danh mục và Phân danh mục")
sales_by_cat = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
categories = sales_by_cat['Category'].unique()
sub_categories = sales_by_cat['Sub-Category'].unique()
fig, ax = plt.subplots()
width = 0.35 / len(sub_categories)  # Điều chỉnh width nếu cần
x = np.arange(len(categories))
for i, sub in enumerate(sub_categories):
    sub_data = sales_by_cat[sales_by_cat['Sub-Category'] == sub]
    ax.bar(x + i * width, sub_data['Sales'], width, label=sub)
ax.set_title('Doanh thu theo Danh mục')
ax.set_xlabel('Category')
ax.set_ylabel('Sales')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Top sản phẩm bán chạy
st.subheader("Top 10 Sản phẩm theo Số lượng Bán")
top_products = df.groupby('Product Name')['Quantity'].sum().nlargest(10).reset_index()
fig, ax = plt.subplots()
ax.bar(top_products['Product Name'], top_products['Quantity'])
ax.set_title('Top 10 Sản phẩm Bán chạy')
ax.set_xlabel('Product Name')
ax.set_ylabel('Quantity')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Tìm kiếm sản phẩm
search_product = st.text_input("Tìm kiếm Sản phẩm theo Tên")
if search_product:
    filtered = products[products['Product Name'].str.contains(search_product, case=False)]
    st.dataframe(filtered)