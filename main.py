import streamlit as st

st.title("👋 Xin chào!")
name = st.text_input("Nhập tên của bạn:")
if name:
    st.success(f"Chào {name}, chúc bạn một ngày tốt lành!")
