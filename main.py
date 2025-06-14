import streamlit as st
import chess
from stchess import board

import random

st.set_page_config(page_title="♟️ Cờ vua AI", layout="centered")
st.title("♟️ Chơi cờ vua AI với giao diện click")

# Khởi tạo bàn cờ và trạng thái game
if "board" not in st.session_state:
    st.session_state.board = chess.Board()

# Hiển thị bàn cờ và lấy nước đi người chơi
move = board(fen=st.session_state.board.fen(), key="chessboard")

if move:
    st.session_state.board.push(chess.Move.from_uci(move))
    # Nếu chưa kết thúc lượt người, AI phản công
    if not st.session_state.board.is_game_over():
        ai_move = random.choice(list(st.session_state.board.legal_moves))
        st.session_state.board.push(ai_move)

# Thông báo kết quả nếu game đã kết thúc
if st.session_state.board.is_game_over():
    st.markdown("### 🏁 Ván cờ đã kết thúc!")
    st.write("Kết quả:", st.session_state.board.result())
    if st.button("🔁 Chơi lại"):
        st.session_state.board = chess.Board()
        st.experimental_rerun()
