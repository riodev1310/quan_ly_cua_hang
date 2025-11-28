import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dataset từ URL trực tuyến
@st.cache_data
def load_data():
    url = "https://gist.githubusercontent.com/nnbphuong/38db511db14542f3ba9ef16e69d3814c/raw/Superstore.csv"
    return pd.read_csv(url)

df = load_data()

st.title("Quản lý Khách hàng (Customer Management)")

# Danh sách khách hàng
st.subheader("Danh sách Khách hàng")
customers = df[['Customer ID', 'Customer Name', 'Segment', 'City', 'State']].drop_duplicates()
st.dataframe(customers)

# Phân khúc khách hàng
st.subheader("Phân bổ theo Phân khúc")
segment_count = df['Segment'].value_counts().reset_index()
fig, ax = plt.subplots()
ax.pie(segment_count['count'], labels=segment_count['Segment'], autopct='%1.1f%%')
ax.set_title('Phân khúc Khách hàng')
st.pyplot(fig)

# Khách hàng hàng đầu theo doanh thu
st.subheader("Top 10 Khách hàng theo Doanh thu")
top_customers = df.groupby('Customer Name')['Sales'].sum().nlargest(10).reset_index()
fig, ax = plt.subplots()
ax.bar(top_customers['Customer Name'], top_customers['Sales'])
ax.set_title('Top 10 Khách hàng')
ax.set_xlabel('Customer Name')
ax.set_ylabel('Sales')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Tìm kiếm khách hàng
search_name = st.text_input("Tìm kiếm Khách hàng theo Tên")
if search_name:
    filtered = customers[customers['Customer Name'].str.contains(search_name, case=False)]
    st.dataframe(filtered)