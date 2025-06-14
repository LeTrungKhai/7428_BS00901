import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image
from io import BytesIO

# Cấu hình giao diện trang
st.set_page_config(page_title="Trang Web Cá Nhân", layout="centered")

# -------------------- TRANG GIỚI THIỆU --------------------
st.title("👨‍💻 Xin chào, tôi là Khải Lê!")
st.subheader("📍 Vị trí: TP.HCM, Việt Nam")
st.write("Tôi là một nhà phát triển phần mềm đam mê công nghệ, thích học hỏi và chia sẻ.")

col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://avatars.githubusercontent.com/u/9919?s=200", width=100, caption="Ảnh đại diện")  # ảnh mẫu
with col2:
    st.write("""
        💼 Vai trò: Backend Developer  
        🎯 Sở thích: Lập trình, Bảo mật, IoT  
        📧 Email: khaile@example.com
    """)

st.markdown("---")

# -------------------- FORM LIÊN HỆ --------------------
st.header("📩 Liên hệ với tôi")
with st.form("contact_form"):
    email = st.text_input("Email của bạn")
    message = st.text_area("Nội dung phản hồi")
    submitted = st.form_submit_button("Gửi")
    if submitted:
        st.success("✅ Cảm ơn bạn đã liên hệ!")

st.markdown("---")

# -------------------- BIỂU ĐỒ DỮ LIỆU --------------------
st.header("📊 Dữ liệu thống kê mẫu")
data = pd.DataFrame(np.random.randn(20, 3), columns=["Doanh thu", "Chi phí", "Lợi nhuận"])
st.line_chart(data)

st.markdown("---")

# -------------------- ĐỔI MÀU GIAO DIỆN --------------------
st.header("🎨 Tùy chỉnh màu nền")
r = st.slider("🔴 Red", 0, 255, 120)
g = st.slider("🟢 Green", 0, 255, 200)
b = st.slider("🔵 Blue", 0, 255, 255)

st.markdown(
    f"<div style='background-color: rgb({r},{g},{b}); height: 60px; border-radius: 10px;'></div>",
    unsafe_allow_html=True
)

st.markdown("---")

# -------------------- GHI CHÚ --------------------
st.header("📝 Ghi chú cá nhân")
note = st.text_area("Hôm nay bạn học được gì?")
if st.button("💾 Lưu ghi chú"):
    if note.strip():
        st.success("Ghi chú đã lưu tạm thời!")
        st.info(note)
    else:
        st.warning("Bạn chưa nhập gì cả!")

st.markdown("---")

# -------------------- HIỂN THỊ ẢNH --------------------
st.header("🖼️ Xem ảnh từ liên kết")
url = st.text_input("🔗 Dán URL ảnh vào đây:")
if url:
    try:
        img = Image.open(BytesIO(requests.get(url).content))
        st.image(img, caption="Ảnh bạn vừa nhập", use_column_width=True)
    except:
        st.error("URL không hợp lệ hoặc không phải là ảnh.")

st.markdown("---")

# -------------------- KHẢO SÁT --------------------
st.header("🗳️ Khảo sát nhanh")
language = st.radio("Bạn thích ngôn ngữ lập trình nào nhất?", ["Python", "Java", "C++", "JavaScript"])
if st.button("📤 Gửi khảo sát"):
    st.success(f"👍 Bạn đã chọn: {language}")

# -------------------- CHÂN TRANG --------------------
st.markdown("---")
st.caption("© 2025 - Thiết kế bởi Khải Lê. Ứng dụng demo bằng Streamlit.")
