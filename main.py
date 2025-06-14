import streamlit as st
import chess
import chess.svg
import random
import time
import base64

st.set_page_config(page_title="♟️ Cờ vua AI", layout="centered")

# Khởi tạo bàn cờ và trạng thái
if 'board' not in st.session_state:
    st.session_state.board = chess.Board()
    st.session_state.game_over = False

def render_board(board):
    svg = chess.svg.board(board=board, size=400)
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    return f"<img src='data:image/svg+xml;base64,{b64}'/>"

def ai_move(board):
    move = random.choice(list(board.legal_moves))
    board.push(move)

st.title("♟️ Game Đánh Cờ vs AI (Ngẫu nhiên)")
st.markdown("Bạn chơi **Trắng**, AI chơi **Đen**.")

# Hiển thị bàn cờ
st.markdown(render_board(st.session_state.board), unsafe_allow_html=True)

if not st.session_state.game_over:
    user_move = st.text_input("Nhập nước đi (UCI, ví dụ e2e4):")
    if st.button("Đánh!"):
        try:
            move = chess.Move.from_uci(user_move)
            if move in st.session_state.board.legal_moves:
                st.session_state.board.push(move)
                if not st.session_state.board.is_game_over():
                    with st.spinner("AI đang suy nghĩ..."):
                        time.sleep(1)
                        ai_move(st.session_state.board)
                else:
                    st.success("🎉 Kết thúc ván cờ!")
                    st.session_state.game_over = True
            else:
                st.error("Nước đi không hợp lệ.")
        except:
            st.error("Định dạng UCI sai!")
else:
    res = st.session_state.board.result()
    if res == '1-0': st.success("🎉 Bạn thắng!")
    elif res == '0-1': st.error("🤖 AI thắng!")
    else: st.info("🤝 Hòa!")

    if st.button("🔁 Chơi lại"):
        st.session_state.board = chess.Board()
        st.session_state.game_over = False
        st.experimental_rerun()
