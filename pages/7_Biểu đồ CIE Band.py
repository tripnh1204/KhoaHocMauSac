import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from colour import MSDS_CMFS, SpectralShape, wavelength_to_XYZ, XYZ_to_sRGB
from matplotlib.patches import Rectangle

st.set_page_config(page_title="Biểu đồ CIE Band 400–700 nm", layout="wide")
st.title("Biểu đồ CIE Band ")
st.write("Biểu đồ mô tả màu sắc khả kiến trong dải bước sóng từ 400 đến 700 nm.")

# Lấy CMFs với bước sóng từ 400 đến 700 nm
cmfs = MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]
cmfs = cmfs.trim(SpectralShape(400, 700, 1))

wavelengths = np.arange(400, 701, 1)

fig, ax = plt.subplots(figsize=(10, 2))

for wl in wavelengths:
    XYZ = wavelength_to_XYZ(wl, cmfs)
    RGB = XYZ_to_sRGB(XYZ / np.max(XYZ))
    RGB = np.clip(RGB, 0, 1)
    ax.add_patch(Rectangle((wl, 0), 1, 1, color=RGB))

ax.set_xlim(400, 700)
ax.set_ylim(0, 1)
ax.set_xlabel("Bước sóng (nm)")
ax.set_yticks([])
ax.set_title("CIE Band từ 400–700 nm")

st.pyplot(fig)
