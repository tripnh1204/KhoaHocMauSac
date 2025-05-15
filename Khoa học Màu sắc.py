import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Khoa học Màu sắc",
    layout="wide"
)

# CSS để làm đẹp
st.markdown("""
    <style>
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #0e4d92;
        }
        .subtitle {
            font-size: 24px;
            color: #444;
        }
        .info-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Hàm đổi nền bằng ảnh nội bộ
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
        body {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Gọi hàm để đặt nền — đảm bảo file background.png có trong thư mục gốc
set_background("background.png")

# Layout chính
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("<div class='title'>Chào mừng bạn đến với project <i>Khoa học Màu sắc</i>!</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Dự án này được thực hiện bởi nhóm sinh viên HCMUTE.</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        <h4>Thành viên nhóm:</h4>
        <ul>
            <li><b>Phạm Nguyễn Hữu Trí</b> - MSSV: 22158100</li>
            <li><b>Đào Nguyễn Ngọc Linh</b> - MSSV: 22158064</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("logo-hcmute.jpg", width=140)
