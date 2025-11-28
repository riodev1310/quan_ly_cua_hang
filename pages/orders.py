import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dataset từ URL trực tuyến
@st.cache_data
def load_data():
    url = "https://gist.githubusercontent.com/nnbphuong/38db511db14542f3ba9ef16e69d3814c/raw/Superstore.csv"
    return pd.read_csv(url)

df = load_data()

st.title("Quản lý Đơn hàng (Order Management)")

# Danh sách đơn hàng
st.subheader("Danh sách Đơn hàng")
orders = df[['Order ID', 'Order Date', 'Customer Name', 'Sales', 'Profit', 'Quantity']]
st.dataframe(orders)

# Đơn hàng theo thời gian
st.subheader("Số lượng Đơn hàng theo Năm")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
orders_by_year = df.groupby('Year')['Order ID'].nunique().reset_index()
fig, ax = plt.subplots()
ax.plot(orders_by_year['Year'], orders_by_year['Order ID'])
ax.set_title('Số lượng Đơn hàng theo Năm')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Orders')
st.pyplot(fig)

# Tìm kiếm đơn hàng
search_order = st.text_input("Tìm kiếm Đơn hàng theo ID")
if search_order:
    filtered = orders[orders['Order ID'].str.contains(search_order, case=False)]
    st.dataframe(filtered)