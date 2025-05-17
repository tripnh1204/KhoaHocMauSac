import streamlit as st
import base64

# Cấu hình trang
st.set_page_config(
    page_title="Khoa học Màu sắc",
    layout="wide"
)

# Hàm chèn background từ ảnh nội bộ
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        /* Tăng độ sáng cho chữ trong dark mode */
        .css-10trblm, .css-1v3fvcr, .css-qbe2hs {{
            color: #000000 !important;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Gọi hàm đặt background
set_background("background.jpg")

# Layout chính
col1, col2 = st.columns([4, 1])

with col1:
    st.markdown("<h1 style='color:#0e4d92;'>Chào mừng bạn đến với project <i>Khoa học Màu sắc</i>!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px;color:#444;'>Dự án này được thực hiện bởi nhóm sinh viên HCMUTE.</p>", unsafe_allow_html=True)

    st.markdown("""
        <div style='background-color:rgba(255, 255, 255, 0.85);
                    padding:20px;
                    border-radius:12px;
                    box-shadow:0 0 10px rgba(0,0,0,0.1);
                    margin-top:20px;'>
            <h4>Thành viên nhóm:</h4>
            <ul>
                <li><b>Phạm Nguyễn Hữu Trí</b> - MSSV: 22158100</li>
                <li><b>Đào Nguyễn Ngọc Linh</b> - MSSV: 22158064</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("logo-hcmute.jpg", width=140)
