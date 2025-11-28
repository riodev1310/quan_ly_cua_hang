import streamlit as st
import pandas as pd

# Đọc dataset (giả sử file CSV ở cùng thư mục)
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/Sample-Superstore.csv")

df = load_data()

st.title("Nền tảng Quản lý Superstore")
st.markdown("""
    Chào mừng đến với ứng dụng quản lý Superstore! 
    Ứng dụng này giúp bạn phân tích và quản lý dữ liệu bán hàng từ dataset Sample-Superstore.
    - Tổng số đơn hàng: **{0}**
    - Tổng doanh thu: **${1:,.2f}**
    - Tổng lợi nhuận: **${2:,.2f}**
""".format(len(df), df['Sales'].sum(), df['Profit'].sum()))

st.subheader("Điều hướng đến các trang")
st.page_link("pages/sales.py", label="Phân tích Bán hàng (Sales Analysis)")
st.page_link("pages/customers.py", label="Quản lý Khách hàng (Customer Management)")
st.page_link("pages/products.py", label="Quản lý Sản phẩm (Product Inventory)")
st.page_link("pages/orders.py", label="Quản lý Đơn hàng (Order Management)")

# Hiển thị dữ liệu mẫu
st.subheader("Dữ liệu mẫu (10 dòng đầu)")
st.dataframe(df.head(10))