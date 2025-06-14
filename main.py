import streamlit as st

st.title("🎨 Đổi màu nền trang")
r = st.slider("Red", 0, 255, 128)
g = st.slider("Green", 0, 255, 128)
b = st.slider("Blue", 0, 255, 128)

st.markdown(
    f"<div style='background-color: rgb({r},{g},{b}); height: 100px;'></div>",
    unsafe_allow_html=True
)
