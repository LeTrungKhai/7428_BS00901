import streamlit as st
import chess
from stchess import st_chess

st.set_page_config(page_title="♟️ Cờ vua AI", layout="centered")
st.title("♟️ Chơi cờ vua với AI")

# Khởi tạo bàn cờ
if "board" not in st.session_state:
    st.session_state.board = chess.Board()
    st.session_state.game_over = False

# Xử lý lượt đi của người chơi
last_move = st_chess(st.session_state.board.fen(), key="chessboard")

if last_move:
    move = chess.Move.from_uci(last_move)
    if move in st.session_state.board.legal_moves:
        st.session_state.board.push(move)

        # Kiểm tra kết thúc game
        if st.session_state.board.is_game_over():
            st.session_state.game_over = True
        else:
            # AI đánh ngẫu nhiên
            import random
            ai_move = random.choice(list(st.session_state.board.legal_moves))
            st.session_state.board.push(ai_move)

# Hiển thị kết quả
if st.session_state.board.is_game_over():
    st.markdown("### 🏁 Ván cờ đã kết thúc!")
    st.write("Kết quả:", st.session_state.board.result())
    if st.button("🔁 Chơi lại"):
        st.session_state.board = chess.Board()
        st.session_state.game_over = False
        st.experimental_rerun()
