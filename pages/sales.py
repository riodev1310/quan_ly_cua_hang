import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dataset
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/Sample-Superstore.csv")  # Đường dẫn tương đối

df = load_data()

st.title("Phân tích Bán hàng (Sales Analysis)")

# Chuyển đổi ngày tháng
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Biểu đồ doanh thu theo thời gian
st.subheader("Doanh thu theo Năm")
df['Year'] = df['Order Date'].dt.year
sales_by_year = df.groupby('Year')['Sales'].sum().reset_index()
fig, ax = plt.subplots()
sns.lineplot(data=sales_by_year, x='Year', y='Sales', ax=ax)
ax.set_title('Doanh thu theo Năm')
st.pyplot(fig)

# Biểu đồ doanh thu theo khu vực
st.subheader("Doanh thu theo Khu vực")
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
fig, ax = plt.subplots()
ax.pie(sales_by_region['Sales'], labels=sales_by_region['Region'], autopct='%1.1f%%')
ax.set_title('Phân bổ Doanh thu theo Khu vực')
st.pyplot(fig)

# Biểu đồ lợi nhuận theo danh mục
st.subheader("Lợi nhuận theo Danh mục Sản phẩm")
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(data=profit_by_category, x='Category', y='Profit', ax=ax)
ax.set_title('Lợi nhuận theo Danh mục')
st.pyplot(fig)