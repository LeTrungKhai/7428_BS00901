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

st.title("📊 Biểu đồ dữ liệu ngẫu nhiên")
data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(data)
