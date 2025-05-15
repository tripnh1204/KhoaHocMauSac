import streamlit as st

st.set_page_config(page_title="Khoa học Màu sắc", layout="wide")

page_bg_img = """
<style>
/* Đặt nền cho toàn bộ app */
.stApp {
  background: none !important;
}

.block-container {
  background: none !important;
}

/* Tạo div background nằm cố định toàn màn hình */
.bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-image: url("background.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  z-index: -1;
  opacity: 0.4;
}
</style>

<div class="bg"></div>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2 = st.columns([4,1])
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
