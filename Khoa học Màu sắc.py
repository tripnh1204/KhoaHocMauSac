import streamlit as st
st.set_page_config(
    page_title="Khoa học Màu sắc", layout="wide"
)

col1, col2 = st.columns([4, 1])
with col1:
    st.write("### Chào mừng bạn đến với project Khoa học Màu sắc của tụi mình!")
    st.write("# Nhóm tụi mình gồm:")
    st.write("- Phạm Nguyễn Hữu Trí, MaSV 22158100")
    st.write("- Đào Nguyễn Ngọc Linh, MaSV 22158064")

with col2:
    st.image("logo-hcmute.jpg", width=120)
