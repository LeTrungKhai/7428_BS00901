import streamlit as st
st.title("👋 Xin chào!")
name = st.text_input("Nhập tên của bạn:")
if name:
    st.success(f"Chào {name}, chúc bạn một ngày tốt lành!")
st.title("🎨 Edit color")
r = st.slider("Red", 0, 255, 128)
g = st.slider("Green", 0, 255, 128)
b = st.slider("Blue", 0, 255, 128)

st.markdown(
    f"<div style='background-color: rgb({r},{g},{b}); height: 100px;'></div>",
    unsafe_allow_html=True
)
import pandas as pd
import numpy as np

st.title("📊 Random data chart")
data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(data)

from PIL import Image
import requests
from io import BytesIO

st.title("🖼️ Show picture from Internet")

url = st.text_input("Enter image URL:")
if url:
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="Ảnh bạn vừa nhập", use_column_width=True)
    except:
        st.error("URL không hợp lệ hoặc không phải ảnh.")

st.title("🗳️ Khảo sát nhỏ")
st.subheader("Bạn thích ngôn ngữ lập trình nào nhất?")

option = st.radio(
    "Chọn một:",
    ("Python", "Java", "C++", "JavaScript")
)

if st.button("Gửi"):
    st.success(f"Bạn đã chọn: {option}")
