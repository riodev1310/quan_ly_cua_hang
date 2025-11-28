import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dataset
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/Sample-Superstore.csv")

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
sns.barplot(data=top_customers, x='Customer Name', y='Sales', ax=ax)
ax.set_title('Top 10 Khách hàng')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Tìm kiếm khách hàng
search_name = st.text_input("Tìm kiếm Khách hàng theo Tên")
if search_name:
    filtered = customers[customers['Customer Name'].str.contains(search_name, case=False)]
    st.dataframe(filtered)