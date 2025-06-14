import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# ----------------------------
st.set_page_config(page_title="Ứng dụng Streamlit Demo", layout="centered")
st.title("💻 Ứng dụng Streamlit Đa năng")

# ----------------------------
st.header("👋 Xin chào!")
name = st.text_input("Nhập tên của bạn:")
if name:
    st.success(f"Chào {name}, chúc bạn một ngày tốt lành!")

# ----------------------------
st.header("🎨 Tùy chỉnh màu nền")
r = st.slider("🔴 Red", 0, 255, 128)
g = st.slider("🟢 Green", 0, 255, 128)
b = st.slider("🔵 Blue", 0, 255, 128)

st.markdown(
    f"<div style='background-color: rgb({r},{g},{b}); height: 100px; border-radius: 10px;'></div>",
    unsafe_allow_html=True
)

# ----------------------------
st.header("📊 Biểu đồ dữ liệu ngẫu nhiên")
data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(data)

# ----------------------------
st.header("🖼️ Hiển thị ảnh từ Internet")
url = st.text_input("📷 Nhập URL ảnh:")
if url:
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="Ảnh bạn vừa nhập", use_column_width=True)
    except:
        st.error("⚠️ URL không hợp lệ hoặc không phải ảnh.")

# ----------------------------
st.header("🗳️ Khảo sát nhanh")
st.subheader("Bạn thích ngôn ngữ lập trình nào nhất?")
option = st.radio(
    "Chọn một:",
    ("Python", "Java", "C++", "JavaScript")
)

if st.button("📤 Gửi khảo sát"):
    st.success(f"👍 Bạn đã chọn: {option}")

# ----------------------------
st.header("📝 Ghi chú cá nhân")
note = st.text_area("Ghi chú lại điều gì đó hôm nay...")
if st.button("💾 Lưu ghi chú"):
    if note.strip() != "":
        st.success("✅ Ghi chú đã được lưu tạm!")
        st.info(f"Ghi chú của bạn:\n\n{note}")
    else:
        st.warning("⚠️ Bạn chưa nhập ghi chú.")

# ----------------------------
st.markdown("---")
st.caption("🚀 Được xây dựng bằng Streamlit | © 2025 by Khải Lê")
