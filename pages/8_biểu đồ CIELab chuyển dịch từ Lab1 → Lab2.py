import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import colour

st.set_page_config(page_title="Chuyển dịch màu CIELab", layout="centered")

st.title("🔵 Biểu đồ CIELab và chuyển dịch màu từ Lab1 sang Lab2")

st.markdown("### Nhập giá trị CIELab:")

# Nhập giá trị Lab1
col1, col2 = st.columns(2)
with col1:
    L1 = st.number_input("L1*", min_value=0.0, max_value=100.0, value=50.0)
    a1 = st.number_input("a1*", min_value=-128.0, max_value=128.0, value=20.0)
    b1 = st.number_input("b1*", min_value=-128.0, max_value=128.0, value=30.0)

with col2:
    L2 = st.number_input("L2*", min_value=0.0, max_value=100.0, value=50.0)
    a2 = st.number_input("a2*", min_value=-128.0, max_value=128.0, value=-10.0)
    b2 = st.number_input("b2*", min_value=-128.0, max_value=128.0, value=40.0)

Lab1 = np.array([L1, a1, b1])
Lab2 = np.array([L2, a2, b2])

# Vẽ biểu đồ a*-b*
fig, ax = plt.subplots(figsize=(6, 6))
ax.axhline(0, color='gray', linestyle='--')
ax.axvline(0, color='gray', linestyle='--')

ax.scatter(a1, b1, color='blue', label='Lab1', s=100)
ax.scatter(a2, b2, color='red', label='Lab2', s=100)
ax.plot([a1, a2], [b1, b2], 'k--', label='Chuyển dịch màu')

ax.set_xlabel("a*")
ax.set_ylabel("b*")
ax.set_title("Biểu đồ CIELab (a* vs b*)")
ax.legend()
ax.set_xlim(-128, 128)
ax.set_ylim(-128, 128)
ax.grid(True)

st.pyplot(fig)

# Tính khoảng cách màu ΔE
delta_e = colour.delta_E(Lab1, Lab2, method='CIE 1976')
st.markdown(f"### Khoảng cách màu ΔE (CIE76): `{delta_e:.2f}`")

# Nhận xét
st.markdown("###  Nhận xét:")
if delta_e < 1:
    st.success("Sự khác biệt không thể nhận ra bằng mắt người.")
elif delta_e < 2:
    st.info("Sự khác biệt có thể nhận ra nhẹ.")
elif delta_e < 5:
    st.warning("Sự khác biệt màu sắc nhiều.")
else:
    st.error("Sự khác biệt màu sắc rõ ràng.")
