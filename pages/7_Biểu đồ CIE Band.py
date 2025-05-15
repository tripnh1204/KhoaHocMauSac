import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from colour import MSDS_CMFS
from colour.colorimetry import wavelength_to_XYZ
from matplotlib.patches import Rectangle

# Hàm chuyển XYZ sang RGB (chuẩn sRGB)
def xyz_to_srgb(XYZ):
    # Ma trận chuyển từ XYZ sang sRGB (D65)
    M = np.array([[ 3.2406, -1.5372, -0.4986],
                  [-0.9689,  1.8758,  0.0415],
                  [ 0.0557, -0.2040,  1.0570]])
    RGB = np.dot(M, XYZ)
    return np.clip(RGB, 0, 1)

# Cấu hình giao diện Streamlit
st.set_page_config(page_title="Biểu đồ CIE Band 400–700 nm", layout="wide")
st.title("Biểu đồ CIE Band ")
st.write("Biểu đồ mô tả màu sắc khả kiến trong dải bước sóng từ 400 đến 700 nm.")

# Chuẩn bị dữ liệu
wavelengths = np.arange(400, 701, 1)
cmfs = MSDS_CMFS["CIE 1931 2 Degree Standard Observer"].copy().trim(400, 700)

fig, ax = plt.subplots(figsize=(10, 2))
for wl in wavelengths:
    XYZ = wavelength_to_XYZ(wl, cmfs)
    RGB = xyz_to_srgb(XYZ / np.max(XYZ))  # chuẩn hóa
    ax.add_patch(Rectangle((wl, 0), 1, 1, color=RGB))

ax.set_xlim(400, 700)
ax.set_ylim(0, 1)
ax.set_xlabel("Bước sóng (nm)")
ax.set_yticks([])
ax.set_title("CIE Band từ 400–700 nm")
st.pyplot(fig)
