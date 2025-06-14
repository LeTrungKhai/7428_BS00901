import streamlit as st
import random
import time

# Cấu hình trang
st.set_page_config(page_title="🎮 Game Đoán Số", layout="centered")

# ------------------ INIT SESSION ------------------
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'high_scores' not in st.session_state:
    st.session_state.high_scores = []

# ------------------ HEADER ------------------
st.title("🎮 Game: Đoán số bí mật từ 1 đến 100")
st.caption("🌟 Bạn có đoán đúng trong ít lượt nhất không?")

player_name = st.text_input("👤 Nhập tên của bạn:", max_chars=20)

# ------------------ GAME PLAY ------------------
if player_name:
    if not st.session_state.game_over:
        guess = st.number_input("🔢 Nhập số bạn đoán (1-100):", min_value=1, max_value=100, step=1)
        if st.button("🎯 Đoán"):
            st.session_state.attempts += 1
            if guess == st.session_state.secret_number:
                st.success(f"🎉 Chính xác! Số bí mật là {st.session_state.secret_number}.")
                duration = round(time.time() - st.session_state.start_time, 2)
                st.info(f"⏱️ Bạn đoán đúng sau {st.session_state.attempts} lần, mất {duration} giây.")
                st.session_state.game_over = True

                # Lưu điểm cao
                st.session_state.high_scores.append({
                    "name": player_name,
                    "attempts": st.session_state.attempts,
                    "time": duration
                })

            elif guess < st.session_state.secret_number:
                st.warning("📉 Số bạn đoán nhỏ hơn số bí mật!")
            else:
                st.warning("📈 Số bạn đoán lớn hơn số bí mật!")

    else:
        if st.button("🔁 Chơi lại"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.start_time = time.time()
            st.session_state.game_over = False

# ------------------ BẢNG XẾP HẠNG ------------------
if st.session_state.high_scores:
    st.markdown("---")
    st.header("🏆 Bảng xếp hạng người chơi")
    sorted_scores = sorted(st.session_state.high_scores, key=lambda x: (x['attempts'], x['time']))
    for idx, score in enumerate(sorted_scores[:5], 1):
        st.write(f"**#{idx}** - 👤 {score['name']} | 🎯 {score['attempts']} lần | ⏱️ {score['time']} giây")

# ------------------ TUỲ CHỈNH GIAO DIỆN ------------------
st.markdown("---")
st.header("🎨 Tuỳ chỉnh giao diện")
bg_color = st.color_picker("Chọn màu nền bạn thích", "#FFFFFF")
st.markdown(
    f"""
    <style>
    div[data-testid="stApp"] {{
        background-color: {bg_color};
        padding: 20px;
        border-radius: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ GHI CHÚ / PHẢN HỒI ------------------
st.markdown("---")
st.header("📝 Góp ý sau khi chơi")
feedback = st.text_area("Bạn nghĩ gì về trò chơi này?")
if st.button("📤 Gửi phản hồi"):
    if feedback.strip():
        st.success("Cảm ơn bạn đã góp ý ❤️")
    else:
        st.warning("Vui lòng nhập nội dung phản hồi.")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("© 2025 | Xây dựng bởi Khải Lê với ❤️ và Streamlit")
