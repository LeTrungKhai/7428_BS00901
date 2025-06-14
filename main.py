import streamlit as st
import chess
import chess.svg
import random
import base64

st.set_page_config(page_title="♟️ Cờ vua AI", layout="centered")
st.title("♟️ Chơi cờ vua AI — Click + Nhập UCI")

if "board" not in st.session_state:
    st.session_state.board = chess.Board()

def render_board(board):
    svg = chess.svg.board(board=board, size=400)
    b64 = base64.b64encode(svg.encode("utf-8")).decode()
    st.markdown(f"<img src='data:image/svg+xml;base64,{b64}'/>", unsafe_allow_html=True)

render_board(st.session_state.board)

move = st.text_input("Nhập nước đi (UCI, ví dụ e2e4):")
if st.button("Đánh"):
    try:
        m = chess.Move.from_uci(move)
        if m in st.session_state.board.legal_moves:
            st.session_state.board.push(m)
            if not st.session_state.board.is_game_over():
                ai = random.choice(list(st.session_state.board.legal_moves))
                st.session_state.board.push(ai)
        else:
            st.error("❌ Nước đi không hợp lệ!")
    except:
        st.error("⚠️ Sai định dạng UCI")

if st.session_state.board.is_game_over():
    st.success(f"Kết thúc ván cờ: {st.session_state.board.result()}")
    if st.button("🔁 Chơi lại"):
        st.session_state.board = chess.Board()
        st.experimental_rerun()
