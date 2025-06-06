import streamlit as st
import base64

# Cấu hình trang
st.set_page_config(
    page_title="Khoa học Màu sắc",
    layout="wide"
)

# Hàm chèn background với overlay mờ
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
        .stApp {{
            background-image: linear-gradient(rgba(255,255,255,0.8), rgba(255,255,255,0.8)), 
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
        <div style='background-color:rgba(255, 255, 255, 0.95);
                    padding:20px;
                    border-radius:12px;
                    box-shadow:0 0 10px rgba(0,0,0,0.1);
                    margin-top:20px;
                    color:#000000;'>
            <h4>Thành viên nhóm:</h4>
            <ul>
                <li><b>Phạm Nguyễn Hữu Trí</b> - MSSV: 22158100</li>
                <li><b>Đào Nguyễn Ngọc Linh</b> - MSSV: 22158064</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Logo HCMUTE và GAM xếp ngang
    col_logo1, col_logo2 = st.columns(2)
    with col_logo1:
        st.image("logo-hcmute.jpg", width=100)
    with col_logo2:
        st.image("gam-logo.png", width=100) 
  
    st.markdown("<hr>", unsafe_allow_html=True) 
    
    # CSS để làm ảnh avatar tròn
    st.markdown("""
        <style>
        .avatar img {
            border-radius: 50%;
            width: 100px;
            height: 100px;
            object-fit: cover;
            margin-bottom: 5px;
        }
        .avatar-name {
            text-align: center;
            font-size: 14px;
            color: #444;
        }
        </style>
    """, unsafe_allow_html=True)

    # Hiển thị 2 ảnh thành viên theo chiều ngang
    member_col1, member_col2 = st.columns(2)

    with member_col1:
        st.markdown("<div class='avatar'>", unsafe_allow_html=True)
        st.image("tri_img.jpg")
        st.markdown("<div class='avatar-name'>Phạm Nguyễn Hữu Trí</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with member_col2:
        st.markdown("<div class='avatar'>", unsafe_allow_html=True)
        st.image("linh_img.jpg")
        st.markdown("<div class='avatar-name'>Đào Nguyễn Ngọc Linh</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
