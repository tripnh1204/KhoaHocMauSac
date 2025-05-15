import streamlit as st
import base64

st.set_page_config(page_title="Khoa học Màu sắc", layout="wide")

def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("background.jpg")

# Phần nội dung app
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("<h1 style='color:#0e4d92;'>Chào mừng bạn đến với project <i>Khoa học Màu sắc</i>!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px;color:#444;'>Dự án này được thực hiện bởi nhóm sinh viên HCMUTE.</p>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background-color:rgba(240,242,246,0.8);padding:20px;border-radius:12px;box-shadow:0 0 10px rgba(0,0,0,0.1);'>
            <h4>Thành viên nhóm:</h4>
            <ul>
                <li><b>Phạm Nguyễn Hữu Trí</b> - MSSV: 22158100</li>
                <li><b>Đào Nguyễn Ngọc Linh</b> - MSSV: 22158064</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("logo-hcmute.jpg", width=140)
