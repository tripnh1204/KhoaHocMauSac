import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from colour import SpectralShape, MSDS_CMFS, SDS_ILLUMINANTS
from colour.colorimetry import sd_to_XYZ, wavelength_to_XYZ
from colour.plotting import XYZ_to_plotting_RGB
from matplotlib.patches import Rectangle

st.set_page_config(page_title="Biểu đồ CIE Band 400–700 nm", layout="wide")
st.title("Biểu đồ CIE Band ")
st.write("Biểu đồ mô tả màu sắc khả kiến trong dải bước sóng từ 400 đến 700 nm.")

# Thiết lập dải bước sóng
wavelengths = np.arange(400, 701, 1)  # từ 400 đến 700 nm

# Sử dụng hệ màu tiêu chuẩn CIE 1931 2-deg
cmfs = MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]
cmfs = cmfs.copy().trim(400, 700)

# Chuyển đổi mỗi bước sóng thành màu RGB để vẽ band
fig, ax = plt.subplots(figsize=(10, 2))
for wavelength in wavelengths:
    XYZ = wavelength_to_XYZ(wavelength, cmfs)
    RGB = XYZ_to_plotting_RGB(XYZ / np.max(XYZ))

    # Giới hạn RGB trong khoảng hợp lệ
    RGB = np.clip(RGB, 0, 1)
    
    ax.add_patch(Rectangle((wavelength, 0), 1, 1, color=RGB))

ax.set_xlim(400, 700)
ax.set_ylim(0, 1)
ax.set_xlabel("Bước sóng (nm)")
ax.set_yticks([])
ax.set_title("CIE Band từ 400–700 nm")
st.pyplot(fig)
