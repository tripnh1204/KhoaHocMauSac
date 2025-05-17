import streamlit as st
import base64

# Cấu hình trang
st.set_page_config(
    page_title="Khoa học Màu sắc",
    layout="wide"
)

# Hàm chèn background với overlay mờ để dễ nhìn chữ
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
        .stApp {{
            background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.75)), 
                              url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Gọi hàm đặt nền
set_background("background.jpg")

# Layout chính
col1, col2 = st.columns([4, 1])

with col1:
    st.markdown("<h1 style='color:#003366;'>Chào mừng bạn đến với project <i>Khoa học Màu sắc</i>!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px;color:#222;'>Dự án này được thực hiện bởi nhóm sinh viên HCMUTE.</p>", unsafe_allow_html=True)

    st.markdown("""
        <div style='background-color:rgba(255, 255
