import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dataset
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/Sample-Superstore.csv")

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
sns.lineplot(data=orders_by_year, x='Year', y='Order ID', ax=ax)
ax.set_title('Số lượng Đơn hàng theo Năm')
st.pyplot(fig)

# Tìm kiếm đơn hàng
search_order = st.text_input("Tìm kiếm Đơn hàng theo ID")
if search_order:
    filtered = orders[orders['Order ID'].str.contains(search_order, case=False)]
    st.dataframe(filtered)