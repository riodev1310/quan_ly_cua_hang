import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dataset từ URL trực tuyến
@st.cache_data
def load_data():
    url = "https://gist.githubusercontent.com/nnbphuong/38db511db14542f3ba9ef16e69d3814c/raw/Superstore.csv"
    return pd.read_csv(url)

df = load_data()

st.title("Phân tích Bán hàng (Sales Analysis)")

# Chuyển đổi ngày tháng
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Biểu đồ doanh thu theo thời gian
st.subheader("Doanh thu theo Năm")
df['Year'] = df['Order Date'].dt.year
sales_by_year = df.groupby('Year')['Sales'].sum().reset_index()
fig, ax = plt.subplots()
ax.plot(sales_by_year['Year'], sales_by_year['Sales'])
ax.set_title('Doanh thu theo Năm')
ax.set_xlabel('Year')
ax.set_ylabel('Sales')
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
ax.bar(profit_by_category['Category'], profit_by_category['Profit'])
ax.set_title('Lợi nhuận theo Danh mục')
ax.set_xlabel('Category')
ax.set_ylabel('Profit')
st.pyplot(fig)