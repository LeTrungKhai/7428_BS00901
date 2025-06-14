import streamlit as st
import chess
import chess.svg
import random
import time
from io import StringIO
import base64

st.set_page_config(page_title="♟️ Cờ vua với AI", layout="centered")

# Khởi tạo bàn cờ
if 'board' not in st.session_state:
    st.session_state.board = chess.Board()

# Hàm render bàn cờ dưới dạng ảnh SVG
def render_board(board):
    svg_board = chess.svg.board(board=board)
    b64 = base64.b64encode(svg_board.encode('utf-8')).decode('utf-8')
    return f"<img src='data:image/svg+xml;base64,{b64}'/>"

# Hàm đơn giản cho AI chọn nước đi ngẫu nhiên (hoặc bạn có thể dùng Stockfish)
def ai_move(board):
    legal_moves = list(board.legal_moves)
    if legal_moves:
        move = random.choice(legal_moves)
        board.push(move)

st.title("♟️ Chơi Cờ Vua với AI")
st.markdown("Bạn chơi **Trắng**, AI sẽ chơi **Đen**.")

# Hiển thị bàn cờ
st.markdown(render_board(st.session_state.board), unsafe_allow_html=True)

# Nếu chưa kết thúc
if not st.session_state.board.is_game_over():
    move_input = st.text_input("Nhập nước đi (theo dạng UCI, ví dụ: `e2e4`):")

    if st.button("🚀 Thực hiện nước đi"):
        try:
            move = chess.Move.from_uci(move_input)
            if move in st.session_state.board.legal_moves:
                st.session_state.board.push(move)
                if not st.session_state.board.is_game_over():
                    with st.spinner("🤖 AI đang suy nghĩ..."):
                        time.sleep(1)
                        ai_move(st.session_state.board)
            else:
                st.error("❌ Nước đi không hợp lệ.")
        except:
            st.error("⚠️ Hãy nhập nước đi đúng định dạng (vd: `e2e4`)")

else:
    result = st.session_state.board.result()
    if result == '1-0':
        st.success("🎉 Bạn thắng!")
    elif result == '0-1':
        st.error("🤖 AI thắng!")
    else:
        st.info("😐 Hòa cờ!")
    if st.button("🔁 Chơi lại"):
        st.session_state.board = chess.Board()
