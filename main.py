import streamlit as st
import requests

# URL tới file raw trên GitHub
github_url = "https://raw.githubusercontent.com/username/repo/main/filename.py"

# Gửi request và hiển thị nội dung
response = requests.get(github_url)
if response.status_code == 200:
    code = response.text
    st.code(code, language='python')
else:
    st.error("Không thể tải nội dung từ GitHub.")
